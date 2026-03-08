# Component Sharing Foundation

**Date**: 2026-03-08
**Ticket**: [86e08c1a1](https://app.clickup.com/t/86e08c1a1)
**Branch**: `feat/component-sharing-foundation`

---

## What Was Done

Built the complete component sharing and distribution system for agentic-factory, covering Phases 0-2 of the spec.

### Phase 0: Bootstrap
- Created the factory gateway command (`/factory`)
- Installed globally to `~/.claude/commands/factory.md`
- Supports subcommands: list, install, promote, check, update, rebuild-registry

### Phase 1: Foundation
- Created `components/` directory structure with skills, agents, commands, and domain subdirectories
- Promoted **64 components** from 6 source projects (chiro, chiro-mlx, chiro-base, resin, yellow-house, pazland-astro)
- Breakdown: 16 general skills, 8 general agents, 6 general commands, 34 domain-specific components across 5 domains
- Created `meta.yaml` for all 35 general components
- Generated `registry.yaml` manifest
- Context-separated 3 agents: `ticket-refiner`, `prd-to-spec`, `convention-auditor` (refactored from domain-hardcoded originals)

### Phase 2: Install & Discover
- Full `/factory install` logic with conflict detection, dependency resolution, and skip-if-identical
- `/factory list` with `--scope`, `--type`, `--search` filters
- `/factory promote` with context separation scanning
- `/factory check` and `/factory update` for drift detection
- `/factory rebuild-registry` for manifest regeneration

## Commits

1. `d435135` — feat: component sharing foundation — promote 64 components from 6 projects
2. `f168362` — feat: context-separated agents and CONTEXT.md convention
3. `5d7d485` — feat: factory gateway command — bootstrap for component management
4. `de744c7` — fix: factory gateway installs as single file, not subdirectory

## Key Decisions

- **ADR-001**: Bootstrap-first gateway — single markdown file, no scripts
- **ADR-002**: Context separation — components discover context at runtime, never hardcode
- **ADR-003**: Component directory and registry — `components/` with `meta.yaml` + `registry.yaml`

## What's Left

- **Phase 3** (separate ticket 86e08c1u2): npm packaging, public fork derivation, `agentic-factory-public` repo
- Legacy top-level directories (`skills/`, `agents/`, `commands/`) still exist alongside `components/` — migration deferred
