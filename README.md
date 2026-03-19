# Agentic Factory

A plugin marketplace for Claude Code. Reusable **skills** and **agents** organized into practice domains — each domain is a self-contained, installable plugin.

Built on the [Claude Code plugin architecture](https://github.com/anthropics/claude-plugins-official).

## Skills vs Agents

Plugins contain two types of components:

| | Skills | Agents |
|--|--------|--------|
| **What** | Domain knowledge, templates, interactive workflows | Autonomous executors that read skills and act |
| **Invocation** | Slash commands: `/orchestra:prd` | Conversational: "ask lenny to review the milestones" |
| **Human involvement** | Presents work for approval | No checkpoints — decides and documents |
| **File format** | `skill-name/SKILL.md` | `agents/agent-name.md` |
| **Discovery** | Listed under "Skills" in `/plugin` | Listed under "Agents" in `/plugin` |

**Skills are the sheet music. Agents are the conductors who read it and perform.**

An agent loads its sibling skills as subject matter expertise before executing. This means the same domain knowledge powers both interactive and autonomous workflows.

## Quick Start

### Add the marketplace

```
/plugin marketplace add mpaz/agentic-factory
```

### Install a plugin

```
/plugin install orchestra@agentic-factory
/plugin install developer-workflow@agentic-factory
/plugin install product-planning@agentic-factory
```

### Use skills (slash commands)

```
/orchestra:prd <gap-name>
/orchestra:milestone active
/developer-workflow:commit
/codebase-analysis:acb ./src
```

### Use agents (conversational)

```
"ask lenny to review the active milestones"
"have lenny run the full loop on M2"
"can slim refine this ticket into a PRD"
```

## Available Plugins

### Dev

| Plugin | Skills | Agents | Description |
|--------|--------|--------|-------------|
| **developer-workflow** | dev-context, dev-explore, dev-inquiry, commit, push, branch, issue, factory | — | Context, exploration, inquiry, reporting, git |
| **codebase-analysis** | acb, skills-auditor, playwright, rebuild-context, rebuild-readme, research-task, technical-decision, spike-driven-dev, prime-web-dev | — | Architecture analysis, auditing, testing |
| **swift-development** | swift-lang, swift-ui, swiftui-submission-prep | — | Swift/SwiftUI patterns, App Store submission |
| **frontend-design** | frontend-design | — | Production-grade frontend interface design |

### Product

| Plugin | Skills | Agents | Description |
|--------|--------|--------|-------------|
| **product-planning** | prd-template-guidance, ticket-refiner, prd-to-spec, spec-executor | **slim** | Ticket refinement, PRDs, specs, execution |

### Content

| Plugin | Skills | Agents | Description |
|--------|--------|--------|-------------|
| **anti-slop** | anti-slop | — | Clean prose style guide banning LLM cliches |
| **writing** | writing, synthesis-executor | — | SEO blog post creation with approval workflow |

### Platform

| Plugin | Skills | Agents | Description |
|--------|--------|--------|-------------|
| **cloudflare** | workers, hono, workers-ai, durable-objects, kv | — | Cloudflare Workers development |
| **fork-terminal** | fork | — | Fork terminal sessions with agentic coding tools |
| **goose** | recipes, recipe-analysis | — | Goose recipe creation and document analysis |

### PM

| Plugin | Skills | Agents | Description |
|--------|--------|--------|-------------|
| **orchestra** | scaffold, prd, spec, ticket, conduct, milestone, roadmap, devlog, conventions | **lenny** | Agent knowledge base methodology |
| **clickup** | open, investigate, agent, close, conventions | — | ClickUp ticket lifecycle |
| **senior-pm** | portfolio-health, risk-analysis, resource-planning | — | Portfolio health, risk, resource planning |
| **pkm** | kickoff, shutdown, interstitial, weekly-plan, weekly-review, weekly-summary, monthly-summary, remarkable | — | Personal knowledge management rituals |

### Domain

| Plugin | Skills | Agents | Description |
|--------|--------|--------|-------------|
| **yoga** | orchestrator, anatomy-expert, asana-strategist, professor, theme-developer | — | Yoga class planning |

## Plugin Structure

```
plugin-name/
├── .claude-plugin/plugin.json   # Makes it installable
├── CLAUDE.md                    # Authoring context
├── skill-one/SKILL.md           # Skill (slash command)
├── skill-two/SKILL.md
├── skill-two/references/        # Supporting files
└── agents/                      # Autonomous agents
    └── agent-name.md
```

- **Skills** are direct children of the plugin root as `name/SKILL.md`
- **Agents** live in `agents/name.md` with minimal frontmatter (`name`, `description`, `model`)
- The plugin system discovers both by directory convention — no manifest field needed for agents

## Updating Plugins

After making changes to a plugin:

1. Bump `version` in the plugin's `.claude-plugin/plugin.json`
2. Sync the version in `.claude-plugin/marketplace.json`
3. Commit and push
4. In consumer projects: `rm -rf ~/.claude/plugins/cache/agentic-factory`
5. Restart Claude (quit and relaunch — reload is not sufficient)

**Version bump on every change — no exceptions.** The cache keys on version number. No bump means stale copies.

## Authoring

Build components in real projects first, then promote proven ones into the factory:

```bash
cd pm/orchestra && claude   # Open plugin as authoring workspace
```

Use `/release` to auto-detect changed plugins, validate structure, bump versions, and sync marketplace.json.

See [CLAUDE.md](CLAUDE.md) for full conventions and quality standards.

## Design Principles

- **Skills as knowledge, agents as execution** — Same domain expertise powers both interactive and autonomous workflows
- **Organic over generated** — Components are built through real work, not templated
- **Context separation** — Skills discover project context at runtime, never hardcode it
- **Pure markdown** — Structured configurations, no executable code
- **Flat discovery** — Matching [Anthropic's official plugin architecture](https://github.com/anthropics/claude-plugins-official)
