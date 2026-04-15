---
name: hono
description: "Hono framework patterns for Cloudflare Workers: routing, middleware, type-safe handlers, request validation, error handling. Use when building APIs with Hono on Cloudflare."
user-invocable: false
---

# Hono Framework on Cloudflare Workers

## Setup

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

## Key Patterns

- **Typed bindings**: `Hono<{ Bindings: Bindings }>` for type-safe `c.env` access
- **Routing**: `app.get()`, `app.post()`, `app.route()` for nested routes
- **Middleware**: `app.use()` for auth, CORS, logging
- **Request validation**: `c.req.json()`, `c.req.query()`, `c.req.param()`
- **Error handling**: `app.onError()` for global error handler

## Reference

For detailed patterns, see [references/hono.md](../workers/references/hono.md).
