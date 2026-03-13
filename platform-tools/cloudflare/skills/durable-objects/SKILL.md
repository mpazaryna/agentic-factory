---
name: durable-objects
description: "Cloudflare Durable Objects: stateful workflows, WebSockets, coordination, rate limiting, alarm scheduling. Use when building stateful services on Cloudflare."
user-invocable: false
---

# Durable Objects

## Key Concepts

- **Durable Object classes**: State persisted across requests
- **State persistence**: `this.state.storage` for key-value, SQL, or transactional storage
- **Alarm scheduling**: `this.state.storage.setAlarm()` for deferred execution
- **WebSocket handling**: Built-in WebSocket pair support
- **Coordination patterns**: Single-instance guarantee for mutual exclusion

## Anti-Patterns

- Creating new Durable Object instances unnecessarily
- Not using `blockConcurrencyWhile()` for initialization
- Missing error handling in alarm callbacks

## Reference

For detailed patterns, see [references/durable-objects.md](../workers/references/durable-objects.md).
