# Durable Objects

Durable Objects provide strongly consistent state and coordination for Cloudflare Workers. Each object instance is globally unique and maintains its state across requests.

## When to Use Durable Objects

| Use Case | Why Durable Objects |
|----------|---------------------|
| **Stateful workflows** | Track multi-step processes |
| **Rate limiting** | Per-user counters with strong consistency |
| **WebSocket servers** | Maintain connection state |
| **Coordination** | Ensure single-writer access to resources |
| **Queues** | Ordered, reliable task processing |

## Setup

### Wrangler Configuration

```toml
# wrangler.toml
[[durable_objects.bindings]]
name = "WORKFLOW"
class_name = "WorkflowObject"

[[durable_objects.bindings]]
name = "RATE_LIMITER"
class_name = "RateLimiter"

# Required migration for new classes
[[migrations]]
tag = "v1"
new_classes = ["WorkflowObject", "RateLimiter"]
```

### TypeScript Types

```typescript
export interface Env {
  WORKFLOW: DurableObjectNamespace;
  RATE_LIMITER: DurableObjectNamespace;
}
```

## Basic Durable Object

```typescript
export class WorkflowObject implements DurableObject {
  private state: DurableObjectState;
  private env: Env;

  constructor(state: DurableObjectState, env: Env) {
    this.state = state;
    this.env = env;
  }

  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    switch (url.pathname) {
      case '/status':
        return this.getStatus();
      case '/start':
        return this.startWorkflow(request);
      case '/advance':
        return this.advanceStep(request);
      default:
        return new Response('Not Found', { status: 404 });
    }
  }

  private async getStatus(): Promise<Response> {
    const status = await this.state.storage.get('status') || 'idle';
    const step = await this.state.storage.get('currentStep') || 0;
    return Response.json({ status, step });
  }

  private async startWorkflow(request: Request): Promise<Response> {
    const data = await request.json();

    await this.state.storage.put({
      status: 'running',
      currentStep: 0,
      data: data,
      startedAt: Date.now()
    });

    return Response.json({ success: true, message: 'Workflow started' });
  }

  private async advanceStep(request: Request): Promise<Response> {
    const currentStep = await this.state.storage.get<number>('currentStep') || 0;
    const nextStep = currentStep + 1;

    await this.state.storage.put('currentStep', nextStep);

    // Check if workflow is complete
    const totalSteps = 5;
    if (nextStep >= totalSteps) {
      await this.state.storage.put('status', 'completed');
      await this.state.storage.put('completedAt', Date.now());
    }

    return Response.json({ step: nextStep, complete: nextStep >= totalSteps });
  }
}

// Export the class
export { WorkflowObject };
```

## Accessing Durable Objects from Workers

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    // Get or create a Durable Object by ID
    const workflowId = url.searchParams.get('id') || 'default';

    // Create a stable ID from a name
    const id = env.WORKFLOW.idFromName(workflowId);

    // Get a stub (proxy) to the Durable Object
    const stub = env.WORKFLOW.get(id);

    // Forward the request to the Durable Object
    return stub.fetch(request);
  }
};
```

## Stateful Workflow Pattern

Track multi-step processes with state persistence:

```typescript
interface WorkflowState {
  id: string;
  status: 'pending' | 'running' | 'paused' | 'completed' | 'failed';
  currentStep: number;
  steps: StepResult[];
  data: Record<string, unknown>;
  createdAt: number;
  updatedAt: number;
  error?: string;
}

interface StepResult {
  step: number;
  name: string;
  status: 'pending' | 'completed' | 'failed';
  result?: unknown;
  error?: string;
  completedAt?: number;
}

export class StatefulWorkflow implements DurableObject {
  private state: DurableObjectState;
  private env: Env;
  private workflow: WorkflowState | null = null;

  constructor(state: DurableObjectState, env: Env) {
    this.state = state;
    this.env = env;

    // Load state on initialization
    this.state.blockConcurrencyWhile(async () => {
      this.workflow = await this.state.storage.get('workflow') || null;
    });
  }

  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const action = url.pathname.slice(1); // Remove leading /

    try {
      switch (action) {
        case 'create':
          return this.createWorkflow(request);
        case 'status':
          return this.getStatus();
        case 'execute':
          return this.executeNextStep();
        case 'pause':
          return this.pauseWorkflow();
        case 'resume':
          return this.resumeWorkflow();
        case 'cancel':
          return this.cancelWorkflow();
        default:
          return Response.json({ error: 'Unknown action' }, { status: 400 });
      }
    } catch (error) {
      return Response.json({
        error: error instanceof Error ? error.message : 'Unknown error'
      }, { status: 500 });
    }
  }

  private async createWorkflow(request: Request): Promise<Response> {
    if (this.workflow) {
      return Response.json({ error: 'Workflow already exists' }, { status: 409 });
    }

    const data = await request.json<{ steps: string[] }>();

    this.workflow = {
      id: this.state.id.toString(),
      status: 'pending',
      currentStep: 0,
      steps: data.steps.map((name, i) => ({
        step: i,
        name,
        status: 'pending'
      })),
      data: {},
      createdAt: Date.now(),
      updatedAt: Date.now()
    };

    await this.saveState();
    return Response.json({ success: true, workflow: this.workflow });
  }

  private async executeNextStep(): Promise<Response> {
    if (!this.workflow) {
      return Response.json({ error: 'No workflow' }, { status: 404 });
    }

    if (this.workflow.status !== 'running' && this.workflow.status !== 'pending') {
      return Response.json({ error: `Cannot execute: ${this.workflow.status}` }, { status: 400 });
    }

    this.workflow.status = 'running';
    const stepIndex = this.workflow.currentStep;
    const step = this.workflow.steps[stepIndex];

    try {
      // Execute the step (implement your logic here)
      const result = await this.runStep(step.name, this.workflow.data);

      // Update step result
      step.status = 'completed';
      step.result = result;
      step.completedAt = Date.now();

      // Advance to next step
      this.workflow.currentStep++;
      this.workflow.updatedAt = Date.now();

      // Check if complete
      if (this.workflow.currentStep >= this.workflow.steps.length) {
        this.workflow.status = 'completed';
      }

      await this.saveState();
      return Response.json({ success: true, step: step, workflow: this.workflow });

    } catch (error) {
      step.status = 'failed';
      step.error = error instanceof Error ? error.message : 'Unknown error';
      this.workflow.status = 'failed';
      this.workflow.error = step.error;
      this.workflow.updatedAt = Date.now();

      await this.saveState();
      return Response.json({ success: false, error: step.error }, { status: 500 });
    }
  }

  private async runStep(name: string, data: Record<string, unknown>): Promise<unknown> {
    // Implement step execution logic
    // Could call external APIs, process data, etc.
    await new Promise(r => setTimeout(r, 100)); // Simulate work
    return { executed: name, timestamp: Date.now() };
  }

  private getStatus(): Response {
    if (!this.workflow) {
      return Response.json({ exists: false });
    }
    return Response.json({ exists: true, workflow: this.workflow });
  }

  private async pauseWorkflow(): Promise<Response> {
    if (!this.workflow || this.workflow.status !== 'running') {
      return Response.json({ error: 'Cannot pause' }, { status: 400 });
    }
    this.workflow.status = 'paused';
    this.workflow.updatedAt = Date.now();
    await this.saveState();
    return Response.json({ success: true });
  }

  private async resumeWorkflow(): Promise<Response> {
    if (!this.workflow || this.workflow.status !== 'paused') {
      return Response.json({ error: 'Cannot resume' }, { status: 400 });
    }
    this.workflow.status = 'running';
    this.workflow.updatedAt = Date.now();
    await this.saveState();
    return Response.json({ success: true });
  }

  private async cancelWorkflow(): Promise<Response> {
    if (!this.workflow) {
      return Response.json({ error: 'No workflow' }, { status: 404 });
    }
    await this.state.storage.deleteAll();
    this.workflow = null;
    return Response.json({ success: true });
  }

  private async saveState(): Promise<void> {
    await this.state.storage.put('workflow', this.workflow);
  }
}
```

## Alarm Scheduling

Schedule future work with alarms:

```typescript
export class ScheduledWorkflow implements DurableObject {
  private state: DurableObjectState;

  constructor(state: DurableObjectState, env: Env) {
    this.state = state;
  }

  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === '/schedule') {
      const { delayMs } = await request.json<{ delayMs: number }>();

      // Schedule alarm
      await this.state.storage.setAlarm(Date.now() + delayMs);

      return Response.json({ scheduled: true, executeAt: Date.now() + delayMs });
    }

    return Response.json({ error: 'Unknown endpoint' }, { status: 404 });
  }

  // Called when alarm fires
  async alarm(): Promise<void> {
    console.log('Alarm fired at', new Date().toISOString());

    // Do scheduled work
    const pendingTasks = await this.state.storage.get<string[]>('pendingTasks') || [];

    for (const task of pendingTasks) {
      await this.processTask(task);
    }

    await this.state.storage.delete('pendingTasks');

    // Optionally reschedule for recurring work
    // await this.state.storage.setAlarm(Date.now() + 60000); // 1 minute
  }

  private async processTask(task: string): Promise<void> {
    // Process the task
  }
}
```

## Rate Limiter Pattern

Per-user rate limiting with strong consistency:

```typescript
export class RateLimiter implements DurableObject {
  private state: DurableObjectState;

  constructor(state: DurableObjectState, env: Env) {
    this.state = state;
  }

  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const limit = parseInt(url.searchParams.get('limit') || '10');
    const windowMs = parseInt(url.searchParams.get('window') || '60000');

    const now = Date.now();
    const windowStart = now - windowMs;

    // Get current request timestamps
    const requests = await this.state.storage.get<number[]>('requests') || [];

    // Filter to current window
    const recentRequests = requests.filter(ts => ts > windowStart);

    if (recentRequests.length >= limit) {
      const oldestInWindow = Math.min(...recentRequests);
      const retryAfter = Math.ceil((oldestInWindow + windowMs - now) / 1000);

      return Response.json(
        { allowed: false, retryAfter },
        {
          status: 429,
          headers: { 'Retry-After': String(retryAfter) }
        }
      );
    }

    // Add current request
    recentRequests.push(now);
    await this.state.storage.put('requests', recentRequests);

    return Response.json({
      allowed: true,
      remaining: limit - recentRequests.length,
      resetAt: windowStart + windowMs
    });
  }
}

// Usage from Worker
async function checkRateLimit(clientId: string, env: Env): Promise<boolean> {
  const id = env.RATE_LIMITER.idFromName(clientId);
  const limiter = env.RATE_LIMITER.get(id);

  const response = await limiter.fetch('http://internal/check?limit=10&window=60000');
  const result = await response.json<{ allowed: boolean }>();

  return !result.allowed;
}
```

## WebSocket with Durable Objects

Real-time communication with state:

```typescript
export class ChatRoom implements DurableObject {
  private state: DurableObjectState;
  private sessions: Map<WebSocket, { name: string }> = new Map();

  constructor(state: DurableObjectState, env: Env) {
    this.state = state;
  }

  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === '/websocket') {
      if (request.headers.get('Upgrade') !== 'websocket') {
        return new Response('Expected WebSocket', { status: 400 });
      }

      const pair = new WebSocketPair();
      const [client, server] = Object.values(pair);

      await this.handleWebSocket(server, url);

      return new Response(null, { status: 101, webSocket: client });
    }

    return new Response('Not Found', { status: 404 });
  }

  private async handleWebSocket(ws: WebSocket, url: URL): Promise<void> {
    ws.accept();

    const name = url.searchParams.get('name') || 'Anonymous';
    this.sessions.set(ws, { name });

    // Send chat history
    const history = await this.state.storage.get<string[]>('history') || [];
    ws.send(JSON.stringify({ type: 'history', messages: history.slice(-50) }));

    // Broadcast join
    this.broadcast({ type: 'join', name });

    ws.addEventListener('message', async (event) => {
      const data = JSON.parse(event.data as string);

      if (data.type === 'message') {
        const message = `${name}: ${data.text}`;

        // Save to history
        history.push(message);
        await this.state.storage.put('history', history.slice(-100));

        // Broadcast to all
        this.broadcast({ type: 'message', text: message });
      }
    });

    ws.addEventListener('close', () => {
      this.sessions.delete(ws);
      this.broadcast({ type: 'leave', name });
    });
  }

  private broadcast(message: object): void {
    const json = JSON.stringify(message);
    for (const ws of this.sessions.keys()) {
      try {
        ws.send(json);
      } catch {
        this.sessions.delete(ws);
      }
    }
  }
}
```

## Anti-Patterns

- **Creating too many objects** - Each object has overhead; batch operations when possible
- **Large storage values** - Keep individual values under 128KB
- **Synchronous blocking** - Use `blockConcurrencyWhile` only during initialization
- **Not handling disconnects** - WebSocket clients can disconnect unexpectedly
- **Forgetting migrations** - New classes need migration tags in wrangler.toml

## References

- Cloudflare Durable Objects Documentation
- Cloudflare Workers Examples
