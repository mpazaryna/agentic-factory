# How to Use cloudflare Skill

## Loading the Skill

When working on a Cloudflare Workers project, load this skill:

```
Load the cloudflare skill
```

## Navigation

The SKILL.md file acts as a router. Based on your task:

### Setting Up a Worker
**Reference**: `references/workers.md`
- Module export pattern
- Environment bindings
- Wrangler configuration
- Request/Response handling

### Building APIs with Hono
**Reference**: `references/hono.md`
- Route definitions
- Middleware patterns
- Request validation
- Error handling

### Adding AI Features
**Reference**: `references/workers-ai.md`
- Model selection
- Prompt engineering
- Token management
- Caching AI results

### Implementing Caching
**Reference**: `references/kv.md`
- KV operations
- TTL strategies
- Stale-while-revalidate
- Session storage

### Building Stateful Services
**Reference**: `references/durable-objects.md`
- Workflow state machines
- Rate limiting
- WebSocket servers
- Alarm scheduling

## Example Prompts

### New Worker Setup
```
I'm starting a new Cloudflare Worker. Show me the module pattern
and wrangler.toml configuration for a project with KV and AI bindings.
```

### API Development
```
I need to build a REST API with Hono. Show me how to set up routes,
middleware, and error handling for a feed aggregator.
```

### AI Integration
```
How do I call Workers AI for text summarization? I need to handle
long inputs and cache results.
```

### Stateful Workflow
```
I need to track a multi-step workflow with checkpoints. Show me
the Durable Objects pattern for this.
```

## Combining References

For complex features, you may need multiple references:

**AI-powered API with caching**:
1. `hono.md` - API structure
2. `workers-ai.md` - AI calls
3. `kv.md` - Caching layer

**Real-time collaborative app**:
1. `durable-objects.md` - WebSocket + state
2. `hono.md` - HTTP endpoints
3. `kv.md` - User sessions

## Tips

1. **Start with SKILL.md** - It has quick reference snippets
2. **Load specific references** - Don't load everything at once
3. **Check anti-patterns** - Each reference lists common mistakes
4. **Follow the learning path** - Workers -> Hono -> KV -> AI -> DO
