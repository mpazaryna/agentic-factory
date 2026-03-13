# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Is

Agentic Factory is a plugin marketplace for Claude Code. It organizes reusable Skills and Agents into **practice domains** — each domain is a self-contained plugin that's also an authoring workspace.

Each plugin folder is three things simultaneously:
1. **An installable plugin** — `.claude-plugin/plugin.json` makes it distributable via `/plugin install`
2. **A development workspace** — `CLAUDE.md` at the folder root gives authoring context
3. **A practice specialization** — skills and agents unified by what they do, not what type they are

Components are built organically in real projects, then promoted into the factory when proven. Project-specific tools stay in their project repos.

## Directory Layout

### Dev
- `dev/developer-workflow/` — Context, exploration, inquiry, reporting, quality, git
- `dev/codebase-analysis/` — Architecture analysis, auditing, research, testing

### Product
- `product-planning/` — Ticket refinement, PRDs, specs, execution
- `content-creation/` — Writing, guides, frontend design, documentation, synthesis

### Languages & Frameworks
- `swift-development/` — Swift/SwiftUI patterns and App Store submission

### Platform Tools
- `platform-tools/cloudflare/` — Workers, Hono, Workers AI, Durable Objects, KV
- `platform-tools/fork-terminal/` — Fork terminal sessions with agentic coding tools
- `platform-tools/goose/` — Goose recipe creation and document analysis
- `platform-tools/uat-audit/` — UAT folder audit and enforcement

### Project Management
- `project-management/clickup/` — ClickUp ticket lifecycle: open, investigate, agent, close
- `project-management/senior-pm/` — Portfolio health, risk analysis, resource planning

### MCP Servers
- `mcp/clickup-daily-queue/` — Daily ClickUp task queue for Claude Desktop (FastMCP)

### Infrastructure
- `.claude-plugin/marketplace.json` — Root plugin marketplace catalog
- `templates/` — Shared templates (e.g., CONTEXT.stub.md)
- `prompts/` — Standalone curated prompts (yoga, pkm, market-research, writing)
- `.orchestra/` — Project documentation (ADRs, devlog, work items)
- `.claude/` — Project-level Claude Code settings

## Plugin Folder Structure

Every plugin follows this pattern:

```
plugin-name/
├── .claude-plugin/plugin.json    # Makes it an installable plugin
├── CLAUDE.md                     # Authoring workspace context
├── skills/                       # Skills (slash commands + background knowledge)
│   └── skill-name/SKILL.md
└── agents/                       # Agent definitions (optional)
    └── agent-name.md
```

Skills are the primary component type. Each skill directory contains a `SKILL.md` with YAML frontmatter that controls behavior:
- `name` — becomes the slash command
- `description` — how Claude decides when to load it
- `context: fork` — runs in an isolated subagent context
- `disable-model-invocation: true` — user-only invocation (for side-effect workflows)
- `user-invocable: false` — Claude-only background knowledge
- `allowed-tools` — restrict what tools the skill can use

## Distribution

The repo is a Claude Code plugin marketplace. Install via:

```
/plugin marketplace add mpaz/agentic-factory
/plugin install developer-workflow@agentic-factory
/plugin install cloudflare@agentic-factory
```

## Conventions

### Naming
- All component names use **kebab-case** (e.g., `dev-inquiry`, `swift-lang`)
- Plugin folder names use **kebab-case** (e.g., `developer-workflow`, `swift-development`)
- Skill directories match their YAML frontmatter `name` field
- Skill names should describe what they do, not repeat the plugin name

### Component Formats
- **Skills**: YAML frontmatter with `name` and `description`, plus SKILL.md and optional references/, examples/, scripts/
- **Agents**: YAML frontmatter with `name`, `description`, `color`, and agent-specific fields

### Where Things Go
- New general components → into the appropriate practice domain
- Project-specific tools → in the project repo as `.claude/skills/`
- New practice areas → new plugin folder with `.claude-plugin/plugin.json` + `CLAUDE.md`
- New MCP servers → `mcp/<server-name>/` with README.md, server.py, pyproject.toml
- Curated prompts → `prompts/<domain>/`

### Workflow
1. Build components organically in real projects
2. Promote proven, reusable components into the appropriate plugin
3. Install plugins via `/plugin install name@agentic-factory`
4. Update via `/plugin marketplace update`
5. Author improvements by opening a plugin folder as a workspace: `cd plugin && claude`

## Issue Tracking

All tickets are tracked in ClickUp: https://app.clickup.com/9017822495/v/li/901711514601
