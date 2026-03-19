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
- `dev/swift-development/` — Swift/SwiftUI patterns and App Store submission
- `dev/frontend-design/` — Production-grade frontend interface design

### Product
- `product/product-planning/` — Ticket refinement, PRDs, specs, execution

### Content
- `content/anti-slop/` — Clean prose style guide banning LLM clichés
- `content/writing/` — SEO blog post creation with approval workflow

### Platform
- `platform/cloudflare/` — Workers, Hono, Workers AI, Durable Objects, KV
- `platform/fork-terminal/` — Fork terminal sessions with agentic coding tools
- `platform/goose/` — Goose recipe creation and document analysis

### PM
- `pm/clickup/` — ClickUp ticket lifecycle: open, investigate, agent, close
- `pm/senior-pm/` — Portfolio health, risk analysis, resource planning
- `pm/pkm/` — Personal knowledge management: daily rituals, weekly/monthly reviews
- `pm/kairos/` — AI-augmented productivity: Monk agent for autonomous daily rhythm
- `pm/orchestra/` — Agent knowledge base methodology: .orchestra/ scaffolding, roadmaps, BDRs

### Domain
- `domain/yoga/` — Multi-agent yoga class planning for teachers

### MCP Servers
- `mcp/clickup-daily-queue/` — Daily ClickUp task queue for Claude Desktop (FastMCP)

### Infrastructure
- `.claude-plugin/marketplace.json` — Root plugin marketplace catalog
- `templates/` — Shared templates (e.g., CONTEXT.stub.md)
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

### Structure Rules
- Top-level folders are organizational groupings (dev/, product/, platform/, etc.)
- Plugins always live one level down inside groupings
- No plugin.json at the grouping level — only at the plugin level

### Where Things Go
- New general components → into the appropriate practice domain
- Project-specific tools → in the project repo as `.claude/skills/`
- New practice areas → new plugin folder with `.claude-plugin/plugin.json` + `CLAUDE.md`
- New MCP servers → `mcp/<server-name>/` with README.md, server.py, pyproject.toml

### Workflow
1. Build components organically in real projects
2. Promote proven, reusable components into the appropriate plugin
3. Install plugins via `/plugin install name@agentic-factory`
4. Update via `/plugin marketplace update`
5. Author improvements by opening a plugin folder as a workspace: `cd plugin && claude`

## Skill Quality Standards

Every skill and agent in this repo must meet these standards before merging. Use `/codebase-analysis:audit-skills` to check compliance.

### SKILL.md Frontmatter

| Field | When Required | Notes |
|-------|--------------|-------|
| `name` | Always | kebab-case, ≤64 chars, matches directory name |
| `description` | Always | 50+ chars, starts with action verb, includes "Use when..." triggers |
| `allowed-tools` | Always | Explicit — never rely on implicit full-session access |
| `disable-model-invocation` | Rarely — project-local only | **Do NOT set `true` on plugin skills** — it hides them from slash commands when installed in other projects. Only use on project-local `.claude/skills/` that should not appear as slash commands. |
| `context: fork` | Research/verbose skills | Skills that produce large output Claude shouldn't hold in main context |
| `agent` | When `context: fork` | Specify `Explore`, `Plan`, or `general-purpose` |
| `argument-hint` | When skill takes args | Show users what to pass |
| `user-invocable: false` | Background knowledge only | Skills Claude should know but users shouldn't invoke |

### Agent Frontmatter

| Field | When Required | Notes |
|-------|--------------|-------|
| `name` | Always | kebab-case, unique within plugin |
| `description` | Always | Explains when Claude should delegate to this agent |
| `tools` | Always | Explicit tool restrictions — principle of least privilege |
| `model` | Recommended | Use `haiku` for fast/simple, `sonnet` for balanced, `opus` for complex |

### Description Quality

**Formula**: `[Action verb] [what it does]. Use when [specific triggers].`

Good: `"Analyze technical options with structured comparison matrices. Use when choosing between technologies, architectures, or implementation approaches."`

Bad: `"Helper for decisions"` — too generic, Claude can't pattern-match

### Anti-Patterns

- Missing `allowed-tools` — grants implicit full-session access
- `context: fork` on passive reference material — subagent has nothing to do
- `disable-model-invocation: true` on any plugin skill — hides the skill from slash commands when installed in other projects. Only use on project-local `.claude/skills/`
- Skills over 500 lines without supporting files — move reference material to `references/`
- Descriptions without "Use when..." — Claude can't decide when to auto-load

## Issue Tracking

All tickets are tracked in ClickUp: https://app.clickup.com/9017822495/v/li/901711514601
