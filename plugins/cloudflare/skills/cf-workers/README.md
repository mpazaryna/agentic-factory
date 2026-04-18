# workers

Background knowledge for Cloudflare Workers fundamentals: module exports, request handling, environment bindings, and Wrangler configuration.

## What It Does

This skill is background knowledge — Claude loads it automatically when building serverless edge functions on Cloudflare. It is not invoked directly.

It covers:

- **Module export pattern**: Default export with `fetch(request, env, ctx)` handler
- **Request/Response handling**: Standard Web API patterns (URL parsing, routing by pathname)
- **Environment bindings**: Typed via `Env` interface — AI, KV namespaces, Durable Object namespaces, secrets
- **Wrangler configuration**: `wrangler.toml` structure for bindings, routes, and environments
- **Multi-environment setup**: `[env.staging]` and `[env.production]` blocks
- **Background tasks**: `ctx.waitUntil()` for non-blocking async work

Anti-patterns: synchronous main-thread blocking, missing `ctx.waitUntil()`, hardcoded secrets.

## File Structure

```
references/
  workers.md            Detailed Workers patterns and examples
  hono.md               Hono framework routing patterns
  kv.md                 KV storage operations
  workers-ai.md         AI model inference patterns
  durable-objects.md    Durable Objects stateful patterns
```

The `references/` folder is the shared library for all Cloudflare skills — `hono`, `kv`, `workers-ai`, and `durable-objects` all point here.

## See Also

- `hono` — Routing framework built on top of Workers
- `kv` — Edge key-value storage
- `workers-ai` — AI model inference at the edge
- `durable-objects` — Stateful coordination and WebSockets
