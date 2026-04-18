# durable-objects

Background knowledge for Cloudflare Durable Objects: stateful workflows, WebSockets, coordination, and alarm scheduling.

## What It Does

This skill is background knowledge — Claude loads it automatically when working on Cloudflare projects that use Durable Objects. It is not invoked directly.

It covers:

- **State persistence**: `this.state.storage` API for key-value, SQL, and transactional storage
- **Alarm scheduling**: `setAlarm()` for deferred execution
- **WebSocket handling**: Built-in WebSocket pair support on Durable Object classes
- **Coordination patterns**: Single-instance guarantee for mutual exclusion across concurrent requests
- **Anti-patterns**: Unnecessary instance creation, missing `blockConcurrencyWhile()` on init, unhandled alarm errors

## File Structure

Detailed patterns live in `workers/references/durable-objects.md` — the shared Cloudflare reference library.

## See Also

- `workers` — Workers fundamentals and environment bindings
- `hono` — Routing layer often paired with Durable Objects
- `kv` — Edge key-value storage for simpler caching use cases
