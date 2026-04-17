# swift-lang

Master advanced Swift language features: macros, concurrency, generics, networking, and testing.

## Quick Start

```
help me write a Swift macro that generates Codable conformance
how do I handle actor isolation correctly in this async code?
write tests using the Swift Testing framework
design a protocol with associated types for this use case
```

## What It Does

Background knowledge skill — loads reference material for whichever Swift language area you're working in.

| Topic | When to use |
|-------|-------------|
| **Macros** | Compile-time code generation, reducing boilerplate, building DSLs |
| **Concurrency** | async/await patterns, actor isolation, Sendable conformance, data race prevention |
| **Testing** | Swift Testing framework (`@Test`, `#expect`, parameterized tests) |
| **Generics** | Protocol design, associated types, `any` vs `some`, type erasure |
| **Optimization** | Memory management, ARC, performance profiling, reducing allocations |
| **Result Builders** | Custom DSLs, understanding `@ViewBuilder` internals |
| **Networking** | URLSession with async/await, actor-based API clients, auth and retry |

## File Structure

`references/` is organized by topic area:

```
references/
  macros/          freestanding.md, attached.md
  concurrency/     async-await.md, actors.md, sendable.md
  testing/         swift-testing.md, strategies.md
  generics/        protocols.md, existentials.md
  optimization/    memory.md, performance.md
  result-builders/ custom-dsl.md
  networking/      async-networking.md
```

## See Also

- `swift-ui` — SwiftUI view patterns, state management, layout, and architecture
