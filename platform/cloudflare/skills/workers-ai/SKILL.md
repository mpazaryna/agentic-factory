---
name: workers-ai
description: "Cloudflare Workers AI: edge model inference, text generation, summarization, streaming responses. Use when integrating AI models into Cloudflare Workers."
user-invocable: false
---

# Workers AI

## AI Call Pattern

```typescript
const result = await env.AI.run(
  '@cf/mistralai/mistral-small-3.1-24b-instruct',
  {
    messages: [
      { role: 'system', content: 'You are a helpful assistant.' },
      { role: 'user', content: prompt }
    ],
    max_tokens: 500
  }
);
```

## Key Concepts

- **AI binding**: Declared in `wrangler.toml`, accessed via `env.AI`
- **Model invocation**: `env.AI.run(model, options)`
- **Available models**: Mistral, Llama, and others on Cloudflare's edge
- **Prompt engineering**: System + user message pattern
- **Token management**: Set `max_tokens`, truncate long inputs
- **Streaming**: Use `stream: true` for streaming responses

## Anti-Patterns

- Ignoring token limits with AI models
- Not handling model errors/timeouts
- Sending unbounded user input without truncation

## Reference

For detailed patterns, see [references/workers-ai.md](../workers/references/workers-ai.md).
