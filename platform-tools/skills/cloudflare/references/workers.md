# Workers Fundamentals

Cloudflare Workers are serverless functions that run at the edge, close to your users.

## Module Worker Pattern

The modern approach uses ES module syntax:

```typescript
export interface Env {
  AI: Ai;
  FEED_CACHE: KVNamespace;
  RATE_LIMITER: DurableObjectNamespace;
}

export default {
  async fetch(
    request: Request,
    env: Env,
    ctx: ExecutionContext
  ): Promise<Response> {
    // Handle request
    return new Response('Hello World');
  },

  // Optional: scheduled handler for cron triggers
  async scheduled(
    event: ScheduledEvent,
    env: Env,
    ctx: ExecutionContext
  ): Promise<void> {
    ctx.waitUntil(doScheduledWork(env));
  }
};
```

## Environment Bindings

Define your bindings in `wrangler.toml` and type them:

```typescript
// Type-safe environment
export interface Env {
  // AI binding
  AI: Ai;

  // KV namespaces
  FEED_CACHE: KVNamespace;
  SESSIONS: KVNamespace;

  // Durable Objects
  RATE_LIMITER: DurableObjectNamespace;

  // Environment variables
  API_KEY: string;
  DEBUG: string;

  // R2 buckets
  ASSETS: R2Bucket;

  // D1 databases
  DB: D1Database;
}
```

## Request Handling

### URL Parsing

```typescript
async fetch(request: Request, env: Env): Promise<Response> {
  const url = new URL(request.url);

  // Path and search params
  const path = url.pathname;           // '/api/users'
  const id = url.searchParams.get('id'); // '123'

  // Method check
  if (request.method !== 'POST') {
    return new Response('Method Not Allowed', { status: 405 });
  }
}
```

### Body Parsing

```typescript
// JSON body
const body = await request.json<{ url: string; options?: object }>();

// Form data
const formData = await request.formData();
const file = formData.get('file') as File;

// Text
const text = await request.text();
```

### Headers

```typescript
// Read headers
const clientId = request.headers.get('X-Client-ID') || getClientIP(request);
const contentType = request.headers.get('Content-Type');

// Get client IP
function getClientIP(request: Request): string {
  return request.headers.get('CF-Connecting-IP') ||
         request.headers.get('X-Forwarded-For')?.split(',')[0] ||
         'unknown';
}
```

## Response Patterns

### JSON Response Helper

```typescript
function jsonResponse(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}

// Usage
return jsonResponse({ success: true, data: result });
return jsonResponse({ error: 'Not found' }, 404);
```

### Error Response Mapping

```typescript
function getHttpStatus(errorCode: string): number {
  const statusMap: Record<string, number> = {
    'INVALID_URL': 400,
    'MISSING_FIELD': 400,
    'RATE_LIMITED': 429,
    'NOT_FOUND': 404,
    'PARSE_ERROR': 422,
    'TIMEOUT': 504,
    'INTERNAL_ERROR': 500
  };
  return statusMap[errorCode] || 500;
}
```

## Pathname-Based Routing

Simple routing without a framework:

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    // CORS preflight
    if (request.method === 'OPTIONS') {
      return handleCORS();
    }

    switch (url.pathname) {
      case '/health':
        return handleHealth();

      case '/fetch':
        if (request.method !== 'POST') return methodNotAllowed();
        return handleFetch(request, env);

      case '/batch':
        if (request.method !== 'POST') return methodNotAllowed();
        return handleBatch(request, env);

      case '/summarize':
        if (request.method !== 'POST') return methodNotAllowed();
        return handleSummarize(request, env);

      default:
        return new Response('Not Found', { status: 404 });
    }
  }
};

function methodNotAllowed(): Response {
  return new Response('Method Not Allowed', { status: 405 });
}

function handleCORS(): Response {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, X-Client-ID'
    }
  });
}
```

## Wrangler Configuration

### Basic `wrangler.toml`

```toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"

# KV Namespaces
[[kv_namespaces]]
binding = "FEED_CACHE"
id = "abc123"

# AI binding
[ai]
binding = "AI"

# Durable Objects
[[durable_objects.bindings]]
name = "RATE_LIMITER"
class_name = "RateLimiter"

[[migrations]]
tag = "v1"
new_classes = ["RateLimiter"]
```

### Multi-Environment Setup

```toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"

# Shared AI binding
[ai]
binding = "AI"

# Production
[env.production]
[[env.production.kv_namespaces]]
binding = "FEED_CACHE"
id = "prod-kv-id-here"

# Staging
[env.staging]
[[env.staging.kv_namespaces]]
binding = "FEED_CACHE"
id = "staging-kv-id-here"

# Development
[env.dev]
[[env.dev.kv_namespaces]]
binding = "FEED_CACHE"
id = "dev-kv-id-here"
```

Deploy to specific environment:
```bash
wrangler deploy --env production
wrangler deploy --env staging
wrangler dev --env dev
```

## Background Tasks

Use `ctx.waitUntil()` for work that should continue after response:

```typescript
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    // Do quick work for response
    const result = processRequest(request);

    // Schedule background work (doesn't block response)
    ctx.waitUntil(logAnalytics(request, env));
    ctx.waitUntil(updateCache(result, env));

    return jsonResponse(result);
  }
};

async function logAnalytics(request: Request, env: Env): Promise<void> {
  // This runs after the response is sent
  await env.ANALYTICS.put(/* ... */);
}
```

## Error Handling Pattern

```typescript
async function handleSummarize(request: Request, env: Env): Promise<Response> {
  try {
    // Validate request
    const body = await request.json<{ text: string }>();
    if (!body.text) {
      return jsonResponse({ error: 'Missing text field' }, 400);
    }

    // Rate limit check
    const clientId = request.headers.get('X-Client-ID') || 'anonymous';
    const limited = await checkRateLimit(clientId, env);
    if (limited) {
      return jsonResponse({ error: 'Rate limited' }, 429);
    }

    // Do work
    const result = await summarize(body.text, env);
    return jsonResponse({ success: true, summary: result });

  } catch (error) {
    console.error('Summarize error:', error);
    return jsonResponse({ error: 'Internal error' }, 500);
  }
}
```

## Testing with Vitest

```typescript
// vitest.config.ts
import { defineWorkersConfig } from '@cloudflare/vitest-pool-workers/config';

export default defineWorkersConfig({
  test: {
    poolOptions: {
      workers: {
        wrangler: { configPath: './wrangler.toml' }
      }
    }
  }
});
```

```typescript
// test/index.test.ts
import { env, createExecutionContext, waitOnExecutionContext } from 'cloudflare:test';
import { describe, it, expect } from 'vitest';
import worker from '../src/index';

describe('Worker', () => {
  it('responds to health check', async () => {
    const request = new Request('http://localhost/health');
    const ctx = createExecutionContext();
    const response = await worker.fetch(request, env, ctx);
    await waitOnExecutionContext(ctx);

    expect(response.status).toBe(200);
    expect(await response.text()).toBe('OK');
  });
});
```

## References

- Patterns adapted from [rss-agent](https://github.com/mpazaryna/rss-agent) project
- Cloudflare Workers Documentation
