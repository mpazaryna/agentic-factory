# Agentic Factory

A plugin marketplace for Claude Code. Reusable skills and agents organized into **practice domains** — each domain is a self-contained, installable plugin.

## Quick Start

### Add the marketplace

```
/plugin marketplace add mpaz/agentic-factory
```

### Install a plugin

```
/plugin install orchestra@agentic-factory
/plugin install developer-workflow@agentic-factory
/plugin install codebase-analysis@agentic-factory
```

### Use skills

Skills are invoked with the `plugin-name:skill-name` namespace:

```
/orchestra:prd
/orchestra:scaffold
/developer-workflow:commit
/developer-workflow:push
/codebase-analysis:acb ./src
```

## Available Plugins

### Dev

| Plugin | Skills | Description |
|--------|--------|-------------|
| **developer-workflow** | dev-context, dev-explore, dev-inquiry, commit, push, branch, issue, factory | Context, exploration, inquiry, reporting, git |
| **codebase-analysis** | acb, skills-auditor, playwright, rebuild-context, rebuild-readme, research-task, technical-decision, spike-driven-dev, prime-web-dev | Architecture analysis, auditing, testing |
| **swift-development** | swift-lang, swift-ui, swiftui-submission-prep | Swift/SwiftUI patterns, App Store submission |
| **frontend-design** | frontend-design | Production-grade frontend interface design |

### Product

| Plugin | Skills | Description |
|--------|--------|-------------|
| **product-planning** | prd-template-guidance | Ticket refinement, PRDs, specs, execution |

### Content

| Plugin | Skills | Description |
|--------|--------|-------------|
| **anti-slop** | anti-slop | Clean prose style guide banning LLM cliches |
| **writing** | writing | SEO blog post creation with approval workflow |

### Platform

| Plugin | Skills | Description |
|--------|--------|-------------|
| **cloudflare** | workers, hono, workers-ai, durable-objects, kv | Cloudflare Workers development |
| **fork-terminal** | fork | Fork terminal sessions with agentic coding tools |
| **goose** | recipes, recipe-analysis | Goose recipe creation and document analysis |

### PM

| Plugin | Skills | Description |
|--------|--------|-------------|
| **orchestra** | scaffold, prd, spec, ticket, conduct, milestone, roadmap, devlog, conventions | Agent knowledge base methodology |
| **clickup** | open, investigate, agent, close, conventions | ClickUp ticket lifecycle |
| **senior-pm** | portfolio-health, risk-analysis, resource-planning | Portfolio health, risk, resource planning |
| **pkm** | kickoff, shutdown, interstitial, weekly-plan, weekly-review, weekly-summary, monthly-summary, remarkable | Personal knowledge management rituals |

### Domain

| Plugin | Description |
|--------|-------------|
| **yoga** | Multi-agent yoga class planning (agents only) |

## Plugin Structure

Every plugin follows this pattern:

```
plugin-name/
├── .claude-plugin/plugin.json   # Makes it installable
├── CLAUDE.md                    # Authoring context
├── skill-one/SKILL.md           # Skill (direct child of plugin root)
├── skill-two/SKILL.md
├── skill-two/references/        # Supporting files for skills
└── agent-name/agent.md          # Agent definition (optional)
```

Skills are direct children of the plugin root — not nested under a `skills/` subdirectory. The `"skills": "./"` field in `plugin.json` discovers `*/SKILL.md` one level deep.

## Updating Plugins

After making changes to a plugin:

1. Bump `version` in the plugin's `.claude-plugin/plugin.json`
2. Sync the version in `.claude-plugin/marketplace.json`
3. Commit and push
4. In consumer projects: `rm -rf ~/.claude/plugins/cache/agentic-factory`
5. Restart Claude (quit and relaunch — reload is not sufficient)

## Authoring

Build components in real projects first, then promote proven ones into the factory:

```bash
cd pm/orchestra && claude   # Open plugin as authoring workspace
```

See [CLAUDE.md](CLAUDE.md) for full conventions and quality standards.

## Design Principles

- **Organic over generated** — Components are built through real work, not templated
- **Context separation** — Skills discover project context at runtime, never hardcode it
- **Pure markdown** — Structured configurations, no executable code
- **Flat discovery** — Skills as direct plugin children, matching Claude Code's discovery model
