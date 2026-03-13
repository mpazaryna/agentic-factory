---
name: workers
description: "Cloudflare Workers fundamentals: module exports, request handling, environment bindings, Wrangler config, multi-environment setup. Use when building serverless edge functions on Cloudflare."
user-invocable: false
---

# Cloudflare Workers Fundamentals

## Worker Entry Point (Module)

```typescript
export interface Env {
  AI: Ai;
  FEED_CACHE: KVNamespace;
  MY_DURABLE_OBJECT: DurableObjectNamespace;
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);

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

## Key Concepts

- **Module export pattern**: Default export with `fetch` handler
- **Request/Response handling**: Standard Web API patterns
- **Environment bindings**: Typed via `Env` interface — AI, KV, Durable Objects, secrets
- **Wrangler configuration**: `wrangler.toml` for bindings, routes, environments
- **Multi-environment**: `[env.staging]` / `[env.production]` blocks in wrangler.toml
- **Background tasks**: Use `ctx.waitUntil()` for work that shouldn't block the response

## Anti-Patterns

- Blocking the main thread with synchronous operations
- Not using `ctx.waitUntil()` for background tasks
- Hardcoding secrets (use environment variables)

## Reference

For detailed patterns, see [references/workers.md](references/workers.md).
