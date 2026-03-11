# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Is

Agentic Factory is a plugin marketplace for Claude Code. It organizes reusable Skills, Agents, and Commands into **practice domains** — each domain is a self-contained plugin that's also an authoring workspace.

Each domain folder is three things simultaneously:
1. **An installable plugin** — `.claude-plugin/plugin.json` makes it distributable via `/plugin install`
2. **A development workspace** — `CLAUDE.md` at the folder root gives authoring context
3. **A practice specialization** — skills, agents, and commands unified by what they do, not what type they are

Components are built organically in real projects, then promoted into the factory when proven.

## Directory Layout

### Practice Domains (general)
- `developer-workflow/` — Context, exploration, inquiry, reporting, quality, git
- `product-planning/` — Ticket refinement, PRDs, specs, execution
- `codebase-analysis/` — Architecture analysis, auditing, research, testing
- `swift-development/` — Swift/SwiftUI patterns and App Store submission
- `content-creation/` — Writing, guides, frontend design, documentation, synthesis
- `platform-tools/` — Cloudflare, Goose, terminal utilities, UAT
- `project-management/clickup/` — ClickUp ticket lifecycle: open, investigate, execute, close
- `project-management/senior-pm/` — Portfolio health, risk analysis, resource planning

### Client Domains
- `chiro/` — iOS/macOS chiropractic app project
- `chiro-mlx/` — MLX model training pipeline
- `chiro-base/` — Chiro support tooling
- `resin/` — Data extraction platform

### Infrastructure
- `.claude-plugin/marketplace.json` — Root plugin marketplace catalog
- `registry.yaml` — Legacy component manifest (being phased out)
- `templates/` — Shared templates (e.g., CONTEXT.stub.md)
- `prompts/` — Standalone curated prompts (yoga, pkm, market-research, writing)
- `.orchestra/` — Project documentation (ADRs, devlog, work items)
- `.claude/` — Project-level Claude Code settings

## Domain Folder Structure

Every domain follows this pattern:

```
domain-name/
├── .claude-plugin/plugin.json    # Makes it an installable plugin
├── CLAUDE.md                     # Authoring workspace context
├── skills/                       # Agent Skills (model-invoked)
│   └── skill-name/SKILL.md
├── agents/                       # Agent definitions
│   └── agent-name.md
└── commands/                     # Slash commands (user-invoked)
    └── command-name.md
```

## Distribution

The repo is a Claude Code plugin marketplace. Install via:

```
/plugin marketplace add mpaz/agentic-factory
/plugin install developer-workflow@agentic-factory
/plugin install swift-development@agentic-factory
```

## Conventions

### Naming
- All component names use **kebab-case** (e.g., `dev-inquiry`, `swift-lang`)
- Domain folder names use **kebab-case** (e.g., `developer-workflow`, `swift-development`)
- Skill directories match their YAML frontmatter `name` field

### Component Formats
- **Skills**: YAML frontmatter with `name` and `description`, plus SKILL.md and optional references/, examples/, HOW_TO_USE.md
- **Agents**: YAML frontmatter with `name`, `description`, `color`, and agent-specific fields
- **Commands**: YAML frontmatter with `description`, markdown body

### Where Things Go
- New general components → into the appropriate practice domain
- New client components → into the client domain folder
- New practice areas → new top-level domain folder with plugin.json + CLAUDE.md
- Curated prompts → `prompts/<domain>/`
- ADRs → `.orchestra/adr/`
- Devlogs → `.orchestra/devlog/`
- Work items → `.orchestra/work/<ticket-id>/`

### Workflow
1. Build components organically in real projects
2. Promote proven components into the appropriate domain folder
3. Install domains via `/plugin install domain@agentic-factory`
4. Update via `/plugin marketplace update`
5. Author improvements by opening a domain folder as a workspace: `cd domain && claude`

## Issue Tracking

All tickets are tracked in ClickUp: https://app.clickup.com/9017822495/v/li/901711514601
