---
name: kv
description: "Cloudflare KV storage: caching, key-value operations, TTL, namespace management. Use when implementing caching or edge storage on Cloudflare Workers."
user-invocable: false
---

# KV Storage

## Operations

```typescript
// Write with TTL (1 hour)
await env.FEED_CACHE.put(key, JSON.stringify(data), { expirationTtl: 3600 });

// Read
const cached = await env.FEED_CACHE.get(key, 'json');

// Delete
await env.FEED_CACHE.delete(key);
```

## Key Concepts

- **KV binding**: Declared in `wrangler.toml`, accessed via `env.NAMESPACE_NAME`
- **TTL and expiration**: `expirationTtl` (seconds) or `expiration` (unix timestamp)
- **Caching strategies**: Cache-aside, write-through, TTL-based invalidation
- **Namespace management**: Separate namespaces for different data types
- **Value types**: `text`, `json`, `arrayBuffer`, `stream`

## Reference

For detailed patterns, see [references/kv.md](../workers/references/kv.md).
