# ADR-001: Bootstrap-First Gateway Architecture

**Date**: 2026-03-08
**Status**: Accepted
**Ticket**: [86e08c1a1](https://app.clickup.com/t/86e08c1a1)

## Context

The factory needs a way to install, discover, and manage 60+ reusable Claude Code components across multiple projects. Options considered:

1. **Shell scripts** — `install.sh`, `promote.sh`, etc.
2. **npm/package manager** — Publish components as packages
3. **Single gateway command** — One globally-installed Claude Code command that reads a registry

## Decision

Use a **single globally-installed Claude Code command** (`/factory`) as the gateway to all operations. One manual install step (`~/.claude/commands/factory.md`), everything else flows through it.

The gateway reads `registry.yaml` from the factory repo at invocation time and uses Claude's built-in file tools (Read, Write, Glob, Bash) to execute operations. No executable code in the repo — pure markdown/YAML.

## Consequences

- **Zero maintenance burden** — single file, no build step, no dependencies
- **Always current** — reads the live registry on each invocation, no stale caches
- **No context cost when idle** — only the command description loads at startup (~1 line)
- **Requires factory repo on disk** — the gateway needs `~/workspace/agentic-factory` accessible
- **Self-update is manual** — if the gateway itself changes, user must re-copy it

## Alternatives Rejected

- **Shell scripts**: Would work but adds executable code, requires PATH setup, and doesn't leverage Claude's judgment for conflict resolution
- **npm packaging**: Too heavy for v1; `meta.yaml` is designed to be convertible to `package.json` later (deferred to Phase 3)
