# workers-ai

Background knowledge for Cloudflare Workers AI: edge model inference, text generation, summarization, and streaming responses.

## What It Does

This skill is background knowledge — Claude loads it automatically when integrating AI models into Cloudflare Workers. It is not invoked directly.

It covers:

- **AI binding**: Declared in `wrangler.toml`, accessed via `env.AI`
- **Model invocation**: `env.AI.run(model, options)` with system + user message pattern
- **Available models**: Mistral, Llama, and other models on Cloudflare's edge network
- **Token management**: Setting `max_tokens`, truncating long inputs before sending
- **Streaming**: `stream: true` option for streaming responses

Anti-patterns: ignoring token limits, not handling model errors or timeouts, sending unbounded user input directly to the model.

The skill includes a working TypeScript example using `@cf/mistralai/mistral-small-3.1-24b-instruct`.

## File Structure

Detailed patterns live in `workers/references/workers-ai.md` — the shared Cloudflare reference library.

## See Also

- `workers` — Workers fundamentals and `wrangler.toml` configuration
- `hono` — Routing layer for exposing AI endpoints as HTTP handlers
