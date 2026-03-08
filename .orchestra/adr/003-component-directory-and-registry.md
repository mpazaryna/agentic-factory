# ADR-003: Component Directory Structure and Registry

**Date**: 2026-03-08
**Status**: Accepted
**Ticket**: [86e08c1a1](https://app.clickup.com/t/86e08c1a1)

## Context

The factory repo had components scattered across top-level directories (`skills/`, `agents/`, `commands/`) mixed with factory infrastructure in `.claude/`. No manifest existed to track what was available or where things should install.

## Decision

Introduce `components/` as the canonical home for installable components, with a `registry.yaml` manifest and per-component `meta.yaml` metadata.

```
components/
  skills/<name>/       # General-purpose skills
  agents/<name>/       # General-purpose agents
  commands/<name>/     # General-purpose commands
  domain/<project>/    # Domain-specific, organized by source project
```

Each component directory contains:
- **Installable files** (SKILL.md, agent.md, command .md files, templates)
- **meta.yaml** — type, scope, description, install_files, install_target, dependencies, tags
- **README.md** (optional, not installed)

`registry.yaml` at repo root is the single manifest, regenerable from `meta.yaml` files via `/factory rebuild-registry`.

## Consequences

- Clear separation: `.claude/` = factory infrastructure, `components/` = installable components
- `meta.yaml` per component enables automated registry rebuilds and install logic
- Domain-specific components in `components/domain/` are trivially excludable for public fork derivation
- Legacy top-level directories (`skills/`, `agents/`, `commands/`) still exist but are superseded
