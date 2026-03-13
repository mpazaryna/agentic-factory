# ADR-005: Public Marketplace on GitHub

**Date**: 2026-03-13
**Status**: Accepted

## Context

The agentic-factory repo was private. After the Skills 2.0 migration removed all project-specific content (`private/` folder, client-specific commands, `.env` files), there was no reason to keep it private. The repo now contains only reusable, general-purpose plugins.

## Decision

Make `mpazaryna/agentic-factory` a public GitHub repository. The marketplace is accessible to anyone via:

```
/plugin marketplace add mpazaryna/agentic-factory
/plugin install <plugin-name>@agentic-factory
```

## Consequences

- Anyone can install plugins from the factory
- The `.env` file is gitignored — no secrets in the repo
- Project-specific tools (chiro, chiro-mlx, chiro-base) were already removed
- The `_audit/` folder contains archived snapshots from old projects — review and clean if needed
- Future contributions from the community become possible
