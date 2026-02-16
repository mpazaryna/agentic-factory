# cloudflare

Edge computing patterns for Cloudflare Workers, AI, and stateful services.

## Overview

This skill provides comprehensive reference documentation for building serverless applications on Cloudflare's edge platform. It covers:

- **Workers** - Serverless functions at the edge
- **Workers AI** - Run AI models globally with low latency
- **Durable Objects** - Strongly consistent stateful coordination
- **KV Storage** - Global key-value caching
- **Hono Framework** - Fast, lightweight routing

## Structure

```
cloudflare/
  SKILL.md              # Router - start here
  references/
    workers.md          # Worker fundamentals, request handling
    workers-ai.md       # AI model invocation, summarization
    durable-objects.md  # Stateful workflows, WebSockets
    kv.md               # Caching patterns, session storage
    hono.md             # Routing, middleware, API structure
```

## Use Cases

- **API Development** - RESTful services at the edge
- **AI-Powered Services** - Text summarization, embeddings, classification
- **Real-time Applications** - WebSocket servers, chat rooms
- **Stateful Workflows** - Multi-step processes with checkpoints
- **Caching Layers** - Reduce origin load, improve latency

## Quick Start

Load this skill when working on Cloudflare projects. The SKILL.md router will guide you to the appropriate reference based on what you're building.

## Patterns From

- [rss-agent](https://github.com/mpazaryna/rss-agent) - RSS feed aggregator with AI summarization
- Cloudflare Workers best practices
- Hono framework patterns

## References

- [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)
- [Workers AI](https://developers.cloudflare.com/workers-ai/)
- [Durable Objects](https://developers.cloudflare.com/durable-objects/)
- [Hono](https://hono.dev)
