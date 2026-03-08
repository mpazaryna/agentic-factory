# ADR-002: Context Separation for Reusable Components

**Date**: 2026-03-08
**Status**: Accepted
**Ticket**: [86e08c1a1](https://app.clickup.com/t/86e08c1a1)

## Context

Components built inside domain projects (chiro, resin, yellow-house) often contain hardcoded references to project-specific paths, app names, API endpoints, and tech stack assumptions. These references prevent reuse in other projects.

## Decision

General-purpose components must **never hardcode domain context**. Instead, they discover context at runtime from:

1. **CLAUDE.md** — project-level instructions always in context
2. **Codebase inspection** — agent explores the repo to discover architecture
3. **Arguments** — user passes context when invoking
4. **Convention files** — ADRs, .editorconfig, project-specific configs discovered by the agent

Domain-leak indicators that disqualify a component from `scope: general`:
- Hardcoded project-specific directory paths
- Named references to specific apps, products, or clients
- Tech stack assumptions without "if detected" / "when present" qualifiers
- Fixed output paths without discovery logic
- Specific API endpoints, service names, or tenant references

The `/factory promote` command scans for these violations and flags them as warnings.

## Consequences

- Components that were project-specific (e.g., `clickup-refiner` for chiro) get refactored into generic versions (e.g., `ticket-refiner`) that work anywhere
- Components that can't be generalized stay in `components/domain/<project>/` — still managed by the factory, just scoped
- Slightly more complex component design — authors must think in terms of discovery rather than hardcoding
