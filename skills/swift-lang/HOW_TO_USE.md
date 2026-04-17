# How to Use swift-lang

## Activation

The skill activates when you ask about Swift language features:

- "Help me create a macro that..."
- "How do I use async/await with..."
- "Explain actor isolation"
- "What's the best way to test..."
- "How can I optimize memory usage in..."

## Example Prompts

### Macros

```
Create a macro that adds a computed property for debug description
```

```
I want to build a macro that adds UserDefaults get/set to properties
```

### Concurrency

```
How do I properly use TaskGroup to fetch multiple URLs concurrently?
```

```
When should I use @MainActor vs dispatching to main?
```

### Testing

```
Show me how to write parameterized tests with Swift Testing
```

```
What's the best strategy for testing async code?
```

### Generics

```
When should I use any Protocol vs some Protocol?
```

```
How do I design a protocol with associated types?
```

## Progressive Loading

The skill uses lazy loading - only the relevant reference files are loaded based on your question. This keeps context focused and efficient.

## Combined with swift-ui

For UI-related questions, use alongside `swift-ui`:

- `swift-lang` for the language features (macros, concurrency, testing)
- `swift-ui` for view patterns, state management, animations, architecture
