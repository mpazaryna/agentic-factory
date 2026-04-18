# Workers AI

Run AI models at the edge with Cloudflare Workers AI.

## Setup

### Wrangler Configuration

```toml
# wrangler.toml
[ai]
binding = "AI"
```

### TypeScript Types

```typescript
export interface Env {
  AI: Ai;
}
```

## Basic Model Invocation

```typescript
const result = await env.AI.run(
  '@cf/mistralai/mistral-small-3.1-24b-instruct',
  {
    messages: [
      { role: 'system', content: 'You are a helpful assistant.' },
      { role: 'user', content: 'What is the capital of France?' }
    ]
  }
);

// Result: { response: "The capital of France is Paris." }
```

## Available Models

### Text Generation (Chat)

| Model | Use Case |
|-------|----------|
| `@cf/mistralai/mistral-small-3.1-24b-instruct` | General purpose, high quality |
| `@cf/meta/llama-3.1-8b-instruct` | Fast, good for simple tasks |
| `@cf/meta/llama-3.1-70b-instruct` | Most capable, slower |
| `@cf/qwen/qwen1.5-14b-chat-awq` | Multilingual support |

### Text Embeddings

| Model | Dimensions |
|-------|------------|
| `@cf/baai/bge-base-en-v1.5` | 768 |
| `@cf/baai/bge-large-en-v1.5` | 1024 |

### Image Generation

| Model | Output |
|-------|--------|
| `@cf/stabilityai/stable-diffusion-xl-base-1.0` | Images |
| `@cf/bytedance/stable-diffusion-xl-lightning` | Fast images |

## Summarization Pattern

From the rss-agent project:

```typescript
const PRIMARY_MODEL = '@cf/mistralai/mistral-small-3.1-24b-instruct';
const MAX_INPUT_LENGTH = 32000;

type SummaryStyle = 'brief' | 'detailed' | 'bullets';

const STYLE_PROMPTS: Record<SummaryStyle, string> = {
  brief: 'Provide a concise 1-2 sentence summary of the key point.',
  detailed: 'Provide a comprehensive paragraph summarizing all main points.',
  bullets: 'Provide 3-5 bullet points covering the key information.'
};

export async function summarizeText(
  text: string,
  env: Env,
  style: SummaryStyle = 'brief'
): Promise<{ success: boolean; summary?: string; error?: string }> {
  // Validate input
  if (!text || text.trim().length === 0) {
    return { success: false, error: 'Empty input' };
  }

  // Truncate to avoid token limits (preserve word boundaries)
  const truncated = truncateText(text, MAX_INPUT_LENGTH);

  try {
    const result = await env.AI.run(PRIMARY_MODEL, {
      messages: [
        { role: 'system', content: STYLE_PROMPTS[style] },
        { role: 'user', content: truncated }
      ],
      max_tokens: 500
    });

    const summary = extractResponse(result);
    return { success: true, summary };

  } catch (error) {
    console.error('AI summarization failed:', error);
    return { success: false, error: 'AI processing failed' };
  }
}

function truncateText(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;

  // Find last word boundary before limit
  const truncated = text.slice(0, maxLength);
  const lastSpace = truncated.lastIndexOf(' ');
  return lastSpace > 0 ? truncated.slice(0, lastSpace) : truncated;
}

function extractResponse(result: unknown): string {
  if (typeof result === 'string') return result;
  if (typeof result === 'object' && result !== null) {
    const obj = result as Record<string, unknown>;
    return String(obj.response || obj.text || obj.content || '');
  }
  return '';
}
```

## Streaming Responses

For long-form generation, stream the response:

```typescript
export async function streamSummary(
  text: string,
  env: Env
): Promise<ReadableStream> {
  const stream = await env.AI.run(
    '@cf/mistralai/mistral-small-3.1-24b-instruct',
    {
      messages: [
        { role: 'user', content: `Summarize: ${text}` }
      ],
      stream: true
    }
  );

  return stream;
}

// In handler
app.post('/stream', async (c) => {
  const { text } = await c.req.json();
  const stream = await streamSummary(text, c.env);

  return new Response(stream, {
    headers: { 'Content-Type': 'text/event-stream' }
  });
});
```

## Text Embeddings

Generate embeddings for semantic search:

```typescript
async function getEmbedding(text: string, env: Env): Promise<number[]> {
  const result = await env.AI.run(
    '@cf/baai/bge-base-en-v1.5',
    { text }
  );

  return result.data[0]; // 768-dimensional vector
}

// Batch embeddings
async function getEmbeddings(texts: string[], env: Env): Promise<number[][]> {
  const result = await env.AI.run(
    '@cf/baai/bge-base-en-v1.5',
    { text: texts }
  );

  return result.data;
}
```

## Image Generation

```typescript
async function generateImage(prompt: string, env: Env): Promise<ArrayBuffer> {
  const result = await env.AI.run(
    '@cf/stabilityai/stable-diffusion-xl-base-1.0',
    { prompt }
  );

  return result; // PNG image as ArrayBuffer
}

// Return as response
app.post('/generate-image', async (c) => {
  const { prompt } = await c.req.json();
  const image = await generateImage(prompt, c.env);

  return new Response(image, {
    headers: { 'Content-Type': 'image/png' }
  });
});
```

## Prompt Engineering Patterns

### System Prompts by Task

```typescript
const SYSTEM_PROMPTS = {
  summarize: `You are a summarization assistant. Extract key points concisely.
              Do not add opinions. Stick to the facts presented.`,

  classify: `You are a classification assistant. Categorize the input into
             one of the provided categories. Respond with only the category name.`,

  extract: `You are an extraction assistant. Extract the requested information
            in JSON format. Only include fields that are present in the input.`,

  translate: `You are a translation assistant. Translate the input to the
              target language. Preserve formatting and tone.`
};
```

### Structured Output

```typescript
async function extractEntities(text: string, env: Env) {
  const result = await env.AI.run(PRIMARY_MODEL, {
    messages: [
      {
        role: 'system',
        content: `Extract entities from the text. Return valid JSON only:
                  { "people": [], "places": [], "organizations": [] }`
      },
      { role: 'user', content: text }
    ]
  });

  try {
    return JSON.parse(extractResponse(result));
  } catch {
    return { people: [], places: [], organizations: [] };
  }
}
```

## Caching AI Results

Avoid redundant AI calls:

```typescript
async function summarizeWithCache(
  text: string,
  env: Env
): Promise<string> {
  // Create cache key from content hash
  const hash = await hashText(text);
  const cacheKey = `summary:${hash}`;

  // Check cache
  const cached = await env.SUMMARY_CACHE.get(cacheKey);
  if (cached) return cached;

  // Generate summary
  const result = await summarizeText(text, env);
  if (result.success && result.summary) {
    // Cache for 24 hours
    await env.SUMMARY_CACHE.put(cacheKey, result.summary, {
      expirationTtl: 86400
    });
    return result.summary;
  }

  throw new Error(result.error || 'Summarization failed');
}

async function hashText(text: string): Promise<string> {
  const encoder = new TextEncoder();
  const data = encoder.encode(text);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}
```

## Rate Limiting AI Calls

Protect against abuse:

```typescript
const AI_RATE_LIMIT = 10; // requests per minute per client

async function checkAIRateLimit(
  clientId: string,
  env: Env
): Promise<boolean> {
  const key = `ai-rate:${clientId}`;
  const current = await env.RATE_CACHE.get(key);
  const count = current ? parseInt(current) : 0;

  if (count >= AI_RATE_LIMIT) {
    return true; // Rate limited
  }

  await env.RATE_CACHE.put(key, String(count + 1), {
    expirationTtl: 60
  });

  return false;
}
```

## Error Handling

```typescript
async function safeAICall<T>(
  fn: () => Promise<T>,
  fallback: T
): Promise<T> {
  try {
    return await fn();
  } catch (error) {
    if (error instanceof Error) {
      // Log specific error types
      if (error.message.includes('rate limit')) {
        console.warn('AI rate limited');
      } else if (error.message.includes('context length')) {
        console.warn('Input too long for model');
      } else {
        console.error('AI error:', error.message);
      }
    }
    return fallback;
  }
}

// Usage
const summary = await safeAICall(
  () => summarizeText(text, env),
  { success: false, error: 'AI unavailable' }
);
```

## References

- Patterns adapted from [rss-agent](https://github.com/mpazaryna/rss-agent) project
- Cloudflare Workers AI Documentation
- Cloudflare AI Models Catalog
