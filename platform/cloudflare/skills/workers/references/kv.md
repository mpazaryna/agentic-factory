# KV Storage

Cloudflare Workers KV is a global, low-latency key-value store for caching and configuration data.

## Setup

### Wrangler Configuration

```toml
# wrangler.toml
[[kv_namespaces]]
binding = "FEED_CACHE"
id = "your-namespace-id"

# Preview namespace for local dev
[[kv_namespaces]]
binding = "FEED_CACHE"
id = "your-preview-namespace-id"
preview_id = "your-preview-namespace-id"
```

Create namespaces:
```bash
wrangler kv:namespace create "FEED_CACHE"
wrangler kv:namespace create "FEED_CACHE" --preview
```

### TypeScript Types

```typescript
export interface Env {
  FEED_CACHE: KVNamespace;
  SESSIONS: KVNamespace;
  CONFIG: KVNamespace;
}
```

## Basic Operations

### Write

```typescript
// Simple write
await env.FEED_CACHE.put('key', 'value');

// Write with TTL (expires in 1 hour)
await env.FEED_CACHE.put('key', 'value', { expirationTtl: 3600 });

// Write with absolute expiration
await env.FEED_CACHE.put('key', 'value', {
  expiration: Math.floor(Date.now() / 1000) + 3600
});

// Write JSON
await env.FEED_CACHE.put('user:123', JSON.stringify({ name: 'Alice', age: 30 }));

// Write with metadata
await env.FEED_CACHE.put('article:456', content, {
  metadata: { author: 'Bob', published: Date.now() }
});
```

### Read

```typescript
// Simple read
const value = await env.FEED_CACHE.get('key');
if (value === null) {
  // Key doesn't exist
}

// Read as JSON
const user = await env.FEED_CACHE.get('user:123', 'json');

// Read as ArrayBuffer (for binary data)
const data = await env.FEED_CACHE.get('file:abc', 'arrayBuffer');

// Read as stream (for large values)
const stream = await env.FEED_CACHE.get('large:data', 'stream');

// Read with metadata
const result = await env.FEED_CACHE.getWithMetadata('article:456', 'text');
if (result.value) {
  console.log(result.value);           // Content
  console.log(result.metadata);        // { author: 'Bob', published: ... }
}
```

### Delete

```typescript
await env.FEED_CACHE.delete('key');
```

### List Keys

```typescript
// List all keys
const list = await env.FEED_CACHE.list();
for (const key of list.keys) {
  console.log(key.name, key.expiration, key.metadata);
}

// List with prefix
const userKeys = await env.FEED_CACHE.list({ prefix: 'user:' });

// Paginated listing
let cursor: string | undefined;
do {
  const result = await env.FEED_CACHE.list({ cursor, limit: 100 });
  for (const key of result.keys) {
    console.log(key.name);
  }
  cursor = result.list_complete ? undefined : result.cursor;
} while (cursor);
```

## Caching Pattern

From rss-agent project:

```typescript
interface CacheOptions {
  ttl?: number;      // TTL in seconds
  staleWhileRevalidate?: number;
}

async function getOrFetch<T>(
  key: string,
  fetcher: () => Promise<T>,
  env: Env,
  options: CacheOptions = {}
): Promise<T> {
  const { ttl = 3600, staleWhileRevalidate = 60 } = options;

  // Try cache first
  const cached = await env.FEED_CACHE.getWithMetadata<{ fetchedAt: number }>(key, 'json');

  if (cached.value !== null) {
    const age = (Date.now() - (cached.metadata?.fetchedAt || 0)) / 1000;

    // Fresh cache hit
    if (age < ttl) {
      return cached.value as T;
    }

    // Stale but usable - return stale, revalidate in background
    if (age < ttl + staleWhileRevalidate) {
      // Don't await - let it run in background
      revalidateCache(key, fetcher, env, ttl).catch(console.error);
      return cached.value as T;
    }
  }

  // Cache miss or expired - fetch fresh
  return fetchAndCache(key, fetcher, env, ttl);
}

async function fetchAndCache<T>(
  key: string,
  fetcher: () => Promise<T>,
  env: Env,
  ttl: number
): Promise<T> {
  const data = await fetcher();

  await env.FEED_CACHE.put(key, JSON.stringify(data), {
    expirationTtl: ttl + 60, // Keep slightly longer for stale-while-revalidate
    metadata: { fetchedAt: Date.now() }
  });

  return data;
}

async function revalidateCache<T>(
  key: string,
  fetcher: () => Promise<T>,
  env: Env,
  ttl: number
): Promise<void> {
  try {
    await fetchAndCache(key, fetcher, env, ttl);
  } catch (error) {
    console.error(`Revalidation failed for ${key}:`, error);
  }
}
```

## Feed Caching Example

```typescript
interface FeedData {
  url: string;
  title: string;
  items: FeedItem[];
  fetchedAt: number;
}

async function getFeed(url: string, env: Env): Promise<FeedData> {
  const cacheKey = `feed:${hashUrl(url)}`;

  return getOrFetch(
    cacheKey,
    async () => {
      const response = await fetch(url);
      const xml = await response.text();
      const parsed = parseFeed(xml);

      return {
        url,
        title: parsed.title,
        items: parsed.items,
        fetchedAt: Date.now()
      };
    },
    env,
    { ttl: 900, staleWhileRevalidate: 300 } // 15 min TTL, 5 min stale
  );
}

function hashUrl(url: string): string {
  // Simple hash for cache key
  let hash = 0;
  for (let i = 0; i < url.length; i++) {
    hash = ((hash << 5) - hash) + url.charCodeAt(i);
    hash |= 0;
  }
  return hash.toString(36);
}
```

## Session Storage Pattern

```typescript
interface Session {
  userId: string;
  createdAt: number;
  expiresAt: number;
  data: Record<string, unknown>;
}

const SESSION_TTL = 86400; // 24 hours

async function createSession(
  userId: string,
  env: Env
): Promise<string> {
  const sessionId = crypto.randomUUID();
  const now = Date.now();

  const session: Session = {
    userId,
    createdAt: now,
    expiresAt: now + (SESSION_TTL * 1000),
    data: {}
  };

  await env.SESSIONS.put(`session:${sessionId}`, JSON.stringify(session), {
    expirationTtl: SESSION_TTL
  });

  return sessionId;
}

async function getSession(
  sessionId: string,
  env: Env
): Promise<Session | null> {
  const session = await env.SESSIONS.get<Session>(`session:${sessionId}`, 'json');

  if (!session) return null;

  // Check if expired (belt and suspenders with TTL)
  if (Date.now() > session.expiresAt) {
    await env.SESSIONS.delete(`session:${sessionId}`);
    return null;
  }

  return session;
}

async function updateSession(
  sessionId: string,
  data: Partial<Session['data']>,
  env: Env
): Promise<boolean> {
  const session = await getSession(sessionId, env);
  if (!session) return false;

  session.data = { ...session.data, ...data };

  await env.SESSIONS.put(`session:${sessionId}`, JSON.stringify(session), {
    expirationTtl: Math.floor((session.expiresAt - Date.now()) / 1000)
  });

  return true;
}

async function deleteSession(sessionId: string, env: Env): Promise<void> {
  await env.SESSIONS.delete(`session:${sessionId}`);
}
```

## Configuration Storage

```typescript
interface AppConfig {
  features: Record<string, boolean>;
  limits: Record<string, number>;
  version: string;
}

async function getConfig(env: Env): Promise<AppConfig> {
  const config = await env.CONFIG.get<AppConfig>('app:config', 'json');

  // Return defaults if not configured
  return config || {
    features: { newUI: false, darkMode: true },
    limits: { maxRequests: 100, maxFileSize: 10485760 },
    version: '1.0.0'
  };
}

// Feature flag helper
async function isFeatureEnabled(
  feature: string,
  env: Env
): Promise<boolean> {
  const config = await getConfig(env);
  return config.features[feature] ?? false;
}
```

## Bulk Operations

```typescript
// Batch write (manual - KV doesn't have native bulk)
async function bulkPut(
  items: Array<{ key: string; value: string; ttl?: number }>,
  env: Env
): Promise<void> {
  await Promise.all(
    items.map(item =>
      env.FEED_CACHE.put(item.key, item.value, {
        expirationTtl: item.ttl
      })
    )
  );
}

// Batch delete
async function bulkDelete(keys: string[], env: Env): Promise<void> {
  await Promise.all(keys.map(key => env.FEED_CACHE.delete(key)));
}

// Delete by prefix
async function deleteByPrefix(prefix: string, env: Env): Promise<number> {
  let deleted = 0;
  let cursor: string | undefined;

  do {
    const result = await env.FEED_CACHE.list({ prefix, cursor });

    if (result.keys.length > 0) {
      await Promise.all(result.keys.map(k => env.FEED_CACHE.delete(k.name)));
      deleted += result.keys.length;
    }

    cursor = result.list_complete ? undefined : result.cursor;
  } while (cursor);

  return deleted;
}
```

## Limitations

| Limit | Value |
|-------|-------|
| Key size | 512 bytes |
| Value size | 25 MB |
| Metadata size | 1024 bytes |
| List keys per request | 1000 |
| Reads per request | 1000 |
| Writes per request | 1000 |

## Anti-Patterns

- **Using KV for high-frequency writes** - Use Durable Objects instead
- **Expecting strong consistency** - KV is eventually consistent
- **Large values** - Consider R2 for files > 1MB
- **Counting/incrementing** - Race conditions; use Durable Objects
- **Not handling null** - Always check if `get()` returns null

## References

- Patterns adapted from [rss-agent](https://github.com/mpazaryna/rss-agent) project
- Cloudflare Workers KV Documentation
