# kv

Background knowledge for Cloudflare KV: edge key-value storage, caching strategies, TTL, and namespace management.

## What It Does

This skill is background knowledge — Claude loads it automatically when implementing caching or edge storage on Cloudflare Workers. It is not invoked directly.

It covers:

- **KV binding**: Declared in `wrangler.toml`, accessed via `env.NAMESPACE_NAME`
- **Core operations**: `put` (with TTL), `get` (with type casting), `delete`
- **TTL options**: `expirationTtl` in seconds or `expiration` as a Unix timestamp
- **Caching strategies**: Cache-aside, write-through, TTL-based invalidation
- **Value types**: `text`, `json`, `arrayBuffer`, `stream`

The skill includes working TypeScript snippets for read, write, and delete operations.

## File Structure

Detailed patterns live in `workers/references/kv.md` — the shared Cloudflare reference library.

## See Also

- `workers` — Workers fundamentals and `wrangler.toml` configuration
- `durable-objects` — Transactional stateful storage for more complex patterns
