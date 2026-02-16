# Hono Framework

Hono is a lightweight, fast web framework for Cloudflare Workers with excellent TypeScript support.

## Setup

### Installation

```bash
npm install hono
```

### Basic App

```typescript
import { Hono } from 'hono';

type Bindings = {
  AI: Ai;
  FEED_CACHE: KVNamespace;
  RATE_LIMITER: DurableObjectNamespace;
};

const app = new Hono<{ Bindings: Bindings }>();

app.get('/', (c) => c.text('Hello Hono!'));

export default app;
```

## Routing

### Basic Routes

```typescript
// HTTP methods
app.get('/users', (c) => c.json({ users: [] }));
app.post('/users', (c) => handleCreateUser(c));
app.put('/users/:id', (c) => handleUpdateUser(c));
app.delete('/users/:id', (c) => handleDeleteUser(c));

// All methods
app.all('/webhook', (c) => handleWebhook(c));
```

### Path Parameters

```typescript
app.get('/users/:id', (c) => {
  const id = c.req.param('id');
  return c.json({ id });
});

// Multiple params
app.get('/posts/:postId/comments/:commentId', (c) => {
  const { postId, commentId } = c.req.param();
  return c.json({ postId, commentId });
});

// Optional params
app.get('/files/:path{.+}?', (c) => {
  const path = c.req.param('path') || 'index';
  return c.text(`File: ${path}`);
});
```

### Query Parameters

```typescript
app.get('/search', (c) => {
  const query = c.req.query('q');
  const page = c.req.query('page') || '1';
  const tags = c.req.queries('tag'); // Multiple values: ?tag=a&tag=b

  return c.json({ query, page, tags });
});
```

### Route Groups

```typescript
const api = new Hono<{ Bindings: Bindings }>();

// Group routes under /api
api.get('/feeds', (c) => handleListFeeds(c));
api.post('/feeds', (c) => handleCreateFeed(c));
api.get('/feeds/:id', (c) => handleGetFeed(c));

// Mount on main app
app.route('/api', api);
```

## Request Handling

### Body Parsing

```typescript
// JSON body
app.post('/feeds', async (c) => {
  const body = await c.req.json<{ url: string; name?: string }>();
  return c.json({ received: body });
});

// Form data
app.post('/upload', async (c) => {
  const formData = await c.req.formData();
  const file = formData.get('file') as File;
  return c.json({ filename: file.name, size: file.size });
});

// Text body
app.post('/raw', async (c) => {
  const text = await c.req.text();
  return c.text(`Received: ${text}`);
});

// ArrayBuffer
app.post('/binary', async (c) => {
  const buffer = await c.req.arrayBuffer();
  return c.json({ bytes: buffer.byteLength });
});
```

### Headers

```typescript
app.get('/headers', (c) => {
  const clientId = c.req.header('X-Client-ID');
  const contentType = c.req.header('Content-Type');
  const userAgent = c.req.header('User-Agent');

  // Get client IP (Cloudflare-specific)
  const clientIP = c.req.header('CF-Connecting-IP');

  return c.json({ clientId, contentType, userAgent, clientIP });
});
```

## Response Helpers

### JSON Response

```typescript
app.get('/data', (c) => {
  return c.json({ success: true, data: { id: 1 } });
});

// With status code
app.post('/create', (c) => {
  return c.json({ created: true }, 201);
});

// With headers
app.get('/cached', (c) => {
  return c.json(
    { data: 'cached' },
    200,
    { 'Cache-Control': 'max-age=3600' }
  );
});
```

### Other Response Types

```typescript
// Text
app.get('/text', (c) => c.text('Plain text'));

// HTML
app.get('/page', (c) => c.html('<h1>Hello</h1>'));

// Redirect
app.get('/old', (c) => c.redirect('/new'));
app.get('/external', (c) => c.redirect('https://example.com', 301));

// Not Found
app.get('/missing', (c) => c.notFound());

// Custom status
app.get('/error', (c) => {
  c.status(500);
  return c.json({ error: 'Internal error' });
});
```

## Middleware

### Built-in Middleware

```typescript
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';
import { prettyJSON } from 'hono/pretty-json';
import { secureHeaders } from 'hono/secure-headers';

// Apply globally
app.use('*', logger());
app.use('*', secureHeaders());
app.use('*', cors({
  origin: ['https://example.com'],
  allowMethods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowHeaders: ['Content-Type', 'X-Client-ID'],
  maxAge: 86400
}));

// Pretty JSON in development
app.use('*', prettyJSON());
```

### Custom Middleware

```typescript
// Timing middleware
app.use('*', async (c, next) => {
  const start = Date.now();
  await next();
  const ms = Date.now() - start;
  c.header('X-Response-Time', `${ms}ms`);
});

// Auth middleware
const authMiddleware = async (c: Context, next: Next) => {
  const token = c.req.header('Authorization')?.replace('Bearer ', '');

  if (!token) {
    return c.json({ error: 'Unauthorized' }, 401);
  }

  // Validate token (implement your logic)
  const user = await validateToken(token, c.env);
  if (!user) {
    return c.json({ error: 'Invalid token' }, 401);
  }

  // Store user in context for handlers
  c.set('user', user);
  await next();
};

// Apply to specific routes
app.use('/api/*', authMiddleware);
```

### Rate Limiting Middleware

```typescript
const rateLimitMiddleware = async (c: Context<{ Bindings: Bindings }>, next: Next) => {
  const clientId = c.req.header('X-Client-ID') ||
                   c.req.header('CF-Connecting-IP') ||
                   'anonymous';

  const id = c.env.RATE_LIMITER.idFromName(clientId);
  const limiter = c.env.RATE_LIMITER.get(id);

  const response = await limiter.fetch('http://internal/check?limit=10&window=60000');
  const result = await response.json<{ allowed: boolean; retryAfter?: number }>();

  if (!result.allowed) {
    return c.json(
      { error: 'Rate limited', retryAfter: result.retryAfter },
      429
    );
  }

  await next();
};

app.use('/api/*', rateLimitMiddleware);
```

## Error Handling

### Global Error Handler

```typescript
app.onError((err, c) => {
  console.error('Error:', err.message);

  if (err instanceof HTTPException) {
    return err.getResponse();
  }

  return c.json(
    { error: 'Internal Server Error', message: err.message },
    500
  );
});
```

### Not Found Handler

```typescript
app.notFound((c) => {
  return c.json(
    { error: 'Not Found', path: c.req.path },
    404
  );
});
```

### HTTP Exceptions

```typescript
import { HTTPException } from 'hono/http-exception';

app.get('/protected', (c) => {
  const token = c.req.header('Authorization');

  if (!token) {
    throw new HTTPException(401, { message: 'Authorization required' });
  }

  // Continue...
});
```

## Cloudflare Bindings

### Accessing Environment

```typescript
app.get('/ai', async (c) => {
  // Access bindings via c.env
  const result = await c.env.AI.run(
    '@cf/mistralai/mistral-small-3.1-24b-instruct',
    {
      messages: [{ role: 'user', content: 'Hello!' }]
    }
  );

  return c.json(result);
});

app.get('/cache/:key', async (c) => {
  const key = c.req.param('key');
  const value = await c.env.FEED_CACHE.get(key);

  if (!value) {
    return c.notFound();
  }

  return c.json({ key, value });
});
```

### Durable Objects

```typescript
app.post('/workflow/:id/start', async (c) => {
  const workflowId = c.req.param('id');
  const body = await c.req.json();

  const id = c.env.WORKFLOW.idFromName(workflowId);
  const stub = c.env.WORKFLOW.get(id);

  const response = await stub.fetch('http://internal/start', {
    method: 'POST',
    body: JSON.stringify(body)
  });

  return c.json(await response.json());
});
```

## Complete API Example

From rss-agent project patterns:

```typescript
import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';

type Bindings = {
  AI: Ai;
  FEED_CACHE: KVNamespace;
  RATE_LIMITER: DurableObjectNamespace;
};

type Variables = {
  clientId: string;
};

const app = new Hono<{ Bindings: Bindings; Variables: Variables }>();

// Global middleware
app.use('*', logger());
app.use('*', cors({
  origin: '*',
  allowMethods: ['GET', 'POST', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'X-Client-ID']
}));

// Extract client ID
app.use('*', async (c, next) => {
  const clientId = c.req.header('X-Client-ID') ||
                   c.req.header('CF-Connecting-IP') ||
                   'anonymous';
  c.set('clientId', clientId);
  await next();
});

// Health check
app.get('/health', (c) => c.text('OK'));

// Fetch and cache feed
app.post('/fetch', async (c) => {
  const { url } = await c.req.json<{ url: string }>();

  if (!url) {
    return c.json({ error: 'URL required' }, 400);
  }

  // Check cache first
  const cacheKey = `feed:${url}`;
  const cached = await c.env.FEED_CACHE.get(cacheKey, 'json');

  if (cached) {
    return c.json({ source: 'cache', data: cached });
  }

  // Fetch fresh
  const response = await fetch(url);
  const content = await response.text();

  // Cache for 15 minutes
  await c.env.FEED_CACHE.put(cacheKey, content, {
    expirationTtl: 900
  });

  return c.json({ source: 'fresh', data: content });
});

// Summarize with AI
app.post('/summarize', async (c) => {
  const { text, style = 'brief' } = await c.req.json<{
    text: string;
    style?: 'brief' | 'detailed' | 'bullets';
  }>();

  if (!text) {
    return c.json({ error: 'Text required' }, 400);
  }

  const prompts = {
    brief: 'Provide a concise 1-2 sentence summary.',
    detailed: 'Provide a comprehensive paragraph summary.',
    bullets: 'Provide 3-5 bullet points covering key information.'
  };

  const result = await c.env.AI.run(
    '@cf/mistralai/mistral-small-3.1-24b-instruct',
    {
      messages: [
        { role: 'system', content: prompts[style] },
        { role: 'user', content: text.slice(0, 32000) }
      ],
      max_tokens: 500
    }
  );

  return c.json({ summary: result.response });
});

// Error handling
app.onError((err, c) => {
  console.error('Error:', err);
  return c.json({ error: err.message }, 500);
});

app.notFound((c) => {
  return c.json({ error: 'Not Found' }, 404);
});

export default app;
```

## Testing with Vitest

```typescript
import { describe, it, expect } from 'vitest';
import app from '../src/index';

describe('API', () => {
  it('responds to health check', async () => {
    const res = await app.request('/health');
    expect(res.status).toBe(200);
    expect(await res.text()).toBe('OK');
  });

  it('requires URL for fetch', async () => {
    const res = await app.request('/fetch', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({})
    });
    expect(res.status).toBe(400);
  });
});
```

## Anti-Patterns

- **Not typing bindings** - Always define `Bindings` type for type safety
- **Blocking middleware** - Use `await next()` properly
- **Missing error handling** - Always add `onError` and `notFound` handlers
- **Large response bodies** - Stream large responses instead
- **Not using context variables** - Use `c.set()`/`c.get()` for request-scoped data

## References

- Hono Documentation: https://hono.dev
- Hono with Cloudflare Workers: https://hono.dev/getting-started/cloudflare-workers
- Patterns adapted from [rss-agent](https://github.com/mpazaryna/rss-agent) project
