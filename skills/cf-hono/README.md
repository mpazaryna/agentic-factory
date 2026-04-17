# hono

Background knowledge for the Hono framework on Cloudflare Workers: routing, middleware, type-safe handlers, and error handling.

## What It Does

This skill is background knowledge — Claude loads it automatically when building APIs with Hono on Cloudflare. It is not invoked directly.

It covers:

- **Typed bindings**: `Hono<{ Bindings: Bindings }>` for type-safe access to `c.env` (KV, AI, Durable Objects)
- **Routing**: `app.get()`, `app.post()`, `app.route()` for nested route composition
- **Middleware**: `app.use()` for auth, CORS, and logging
- **Request parsing**: `c.req.json()`, `c.req.query()`, `c.req.param()`
- **Error handling**: Global error handler via `app.onError()`

The skill includes a working setup example showing Hono wired to a Workers AI binding.

## File Structure

Detailed patterns live in `workers/references/hono.md` — the shared Cloudflare reference library.

## See Also

- `workers` — Workers entry point and environment bindings
- `workers-ai` — AI model inference patterns used inside Hono handlers
- `durable-objects` — Stateful backends accessed through Hono routes
- `kv` — Edge caching accessed through Hono handlers
