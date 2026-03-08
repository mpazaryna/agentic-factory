# Agentic Factory Context

> Dynamic development context — Last updated: 2026-03-08
> See README.md for stable documentation

## Project Identity

- **Name:** agentic-factory
- **Purpose:** Meta-generator factory system for building custom Claude Code components (Skills, Agents, Commands, Hooks)
- **Type:** Pure markdown/YAML — no executable code (except install tooling)
- **Repo:** Private (public fork planned as agentic-factory-public)

## Tech Stack

- **Runtime:** None — consumed by Claude Code
- **Languages:** Markdown, YAML frontmatter
- **Tooling:** Claude Code CLI, git, GitHub CLI (gh)
- **Package Manager:** None (npm planned for Phase 3 distribution)

## Directory Structure

```
.claude/              Factory system (agents, commands, templates) — DO NOT install from here
components/           Installable components (the product)
  skills/             16 general-purpose skills
  agents/             5 general-purpose agents
  commands/           5 general-purpose command groups
  domain/             Domain-specific components by project
    chiro/            Chiropractic iOS/macOS app
    chiro-base/       Chiro support tooling
    chiro-mlx/        MLX model training
    resin/            Data pipeline platform
    yellow-house/     SwiftUI project
registry.yaml         Component manifest (generated from meta.yaml files)
skills/               Legacy skill location (pre-components/)
agents/               Legacy agent location (pre-components/)
commands/             Legacy command location (pre-components/)
curated-prompts/      Standalone prompts by domain
plugins/              Example Claude Code plugins
docs/                 Documentation and devlogs
```

## Conventions

- **Naming:** All components use kebab-case
- **Skills:** YAML frontmatter with `name` + `description`, plus SKILL.md
- **Agents:** YAML frontmatter with `name`, `description`, `color`, agent-specific fields
- **Commands:** YAML frontmatter with `description`, markdown body
- **Metadata:** Each component has `meta.yaml` with scope (general/domain-specific), dependencies, tags
- **Context separation:** General-purpose components must NOT hardcode domain context — inject via CLAUDE.md, CONTEXT.md, or codebase inspection at runtime

## Key Files

| File | Purpose |
|------|---------|
| `registry.yaml` | Component manifest — all 64 components with metadata |
| `PRD-component-sharing.md` | Requirements for the component sharing system |
| `SPEC-component-sharing.md` | Technical spec for implementation |
| `CLAUDE.md` | Project instructions for Claude Code |
| `.claude/commands/build.md` | Entry point for the factory system |

## Agent Knowledge Base (.orchestra/)

This project does not use `.orchestra/` (it's a factory, not a product codebase). Projects that consume factory components may use the `.orchestra/` pattern:

```
.orchestra/
├── adr/        Architecture Decision Records (long-lived constraints)
├── work/       Per-ticket work items (PRDs + specs)
│   ├── TEMPLATES/
│   │   ├── prd.md
│   │   └── spec.md
│   └── {ticket-id}-{name}/
│       ├── prd.md       Business intent (produced by ticket-refiner)
│       └── spec.md      Technical contract (produced by prd-to-spec)
├── devlog/     Chronological development journal (by quarter)
└── README.md
```

**Pipeline:** `/refine-ticket` → prd.md → validate → `/write-spec` → spec.md → `/tk-open` → implement

Factory agents (ticket-refiner, prd-to-spec) discover and use this structure when present.

## Dependencies Between Components

- `context-rebuild` command generates `CONTEXT.md` → consumed by `ticket-refiner` agent
- `acb` command loads templates from `templates/` subdirectory
- `ticket-refiner` (planned) depends on CONTEXT.md existing in the target project
- `ticket-refiner` discovers `.orchestra/` for work item output and ADR context
- `prd-to-spec` (planned) depends on ticket-refiner output format and `.orchestra/work/` structure
