---
name: cloudflare
description: |
  Cloudflare Workers development patterns including Workers AI, Durable Objects, KV storage, and Hono routing.
  Use when building serverless edge functions, AI-powered services, or stateful workflows on Cloudflare.
---

# cloudflare

Edge computing patterns for Cloudflare Workers, AI, and stateful services.

## Scope

This skill covers **Cloudflare Workers development** - serverless edge functions, AI integration, state management, and modern routing patterns. For general Swift or web development, see related skills.

## Routing

Based on what you're building, load the appropriate reference:

### Workers Fundamentals
**When**: Setting up a Worker, handling requests, environment bindings
**Reference**: `references/workers.md`
- Module export pattern
- Request/Response handling
- Environment bindings (Env type)
- Wrangler configuration
- Multi-environment setup (dev/staging/prod)

### Hono Framework
**When**: Building APIs with clean routing, middleware, type-safe handlers
**Reference**: `references/hono.md`
- App setup and routing
- Middleware patterns
- Request validation
- Error handling
- Cloudflare bindings with Hono

### Workers AI
**When**: Running AI models at the edge, text generation, summarization
**Reference**: `references/workers-ai.md`
- AI binding and model invocation
- Available models (Mistral, Llama, etc.)
- Prompt engineering patterns
- Token management and truncation
- Streaming responses

### Durable Objects
**When**: Stateful workflows, WebSockets, coordination, rate limiting
**Reference**: `references/durable-objects.md`
- Durable Object classes
- State persistence
- Alarm scheduling
- WebSocket handling
- Coordination patterns

### KV Storage
**When**: Caching, key-value data, edge storage
**Reference**: `references/kv.md`
- KV binding and operations
- TTL and expiration
- Caching strategies
- Namespace management

## Quick Reference

### Worker Entry Point (Module)

```typescript
export interface Env {
  AI: Ai;
  FEED_CACHE: KVNamespace;
  MY_DURABLE_OBJECT: DurableObjectNamespace;
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);

    // Route by pathname
    switch (url.pathname) {
      case '/health':
        return new Response('OK');
      case '/api/summarize':
        return handleSummarize(request, env);
      default:
        return new Response('Not Found', { status: 404 });
    }
  }
};
```

### Hono Setup

```typescript
import { Hono } from 'hono';

type Bindings = {
  AI: Ai;
  FEED_CACHE: KVNamespace;
};

const app = new Hono<{ Bindings: Bindings }>();

app.get('/health', (c) => c.text('OK'));
app.post('/summarize', async (c) => {
  const { text } = await c.req.json();
  const result = await c.env.AI.run('@cf/mistralai/mistral-small-3.1-24b-instruct', {
    messages: [{ role: 'user', content: `Summarize: ${text}` }]
  });
  return c.json(result);
});

export default app;
```

### Workers AI Call

```typescript
const result = await env.AI.run(
  '@cf/mistralai/mistral-small-3.1-24b-instruct',
  {
    messages: [
      { role: 'system', content: 'You are a helpful assistant.' },
      { role: 'user', content: prompt }
    ],
    max_tokens: 500
  }
);
```

### KV Operations

```typescript
// Write with TTL (1 hour)
await env.FEED_CACHE.put(key, JSON.stringify(data), { expirationTtl: 3600 });

// Read
const cached = await env.FEED_CACHE.get(key, 'json');

// Delete
await env.FEED_CACHE.delete(key);
```

## Learning Path

```
1. Workers Fundamentals     → Basic request handling
2. Hono Framework          → Clean routing patterns
3. KV Storage              → Caching layer
4. Workers AI              → AI model integration
5. Durable Objects         → Stateful workflows (advanced)
```

## Anti-Patterns

- Blocking the main thread with synchronous operations
- Not using `ctx.waitUntil()` for background tasks
- Hardcoding secrets (use environment variables)
- Ignoring token limits with AI models
- Creating new Durable Object instances unnecessarily

## Related Skills

- **swift-lang** - If building iOS clients for your Workers
- **swift-ui** - SwiftUI apps consuming Worker APIs

## References

- Patterns adapted from [rss-agent](https://github.com/mpazaryna/rss-agent) project
- Cloudflare Workers Documentation
- Hono Framework Documentation
