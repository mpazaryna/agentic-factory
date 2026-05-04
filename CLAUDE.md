# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Is

Agentic Factory is a curated skill and agent library for Claude Code. Skills are proven, reusable components built in real projects and promoted here when they earn their place.

## Directory Layout

```
agents/     — Agent definitions (eddie, lenny, monk, slim)
skills/     — 34 skills, flat, domain-prefixed
```

### Skill Domains

| Prefix | Domain | Skills |
|--------|--------|--------|
| `orchestra-` | Agent knowledge base methodology | adr, devlog, milestone, prd, roadmap, scaffold, spec, ticket, uml |
| `kairos-` | AI-augmented daily/weekly rhythm | kickoff, shutdown, knote, review, weekly-plan, weekly-finalize |
| `yoga-` | Yoga class planning (multi-agent) | anatomy-expert, asana-strategist, orchestrator, professor, theme-developer |
| `cf-` | Cloudflare Workers platform | workers, workers-ai, hono, kv, durable-objects |
| `swift-` | Swift/SwiftUI development | swift-lang, swift-ui, swiftui-submission-prep |
| `feynman-` | Technical investigation | inquiry, decision |
| `dev-` | Developer tooling | enforcer, playwright, skills-auditor |
| `writing-` | Prose style | no-slop |

## Skill Structure

Each skill is a directory inside `skills/`:

```
skills/
└── domain-skill-name/
    ├── SKILL.md          # Required — frontmatter + instructions
    ├── README.md         # Human-readable companion
    └── references/       # Optional supporting material
```

### SKILL.md Frontmatter

| Field | When Required | Notes |
|-------|--------------|-------|
| `name` | Always | kebab-case, matches directory name exactly |
| `description` | Always | 50+ chars, action verb, includes "Use when..." |
| `allowed-tools` | Always | Explicit — never rely on implicit full-session access |
| `context: fork` | Research/verbose skills | Runs in isolated subagent |
| `agent` | When `context: fork` | `Explore`, `Plan`, or `general-purpose` |
| `argument-hint` | When skill takes args | Shown to users |
| `user-invocable: false` | Background knowledge only | Claude loads silently |

### Anti-Patterns

- Missing `allowed-tools` — implicit full-session access
- `context: fork` on passive reference material — nothing to fork
- `disable-model-invocation: true` on any skill here — hides from slash commands
- Descriptions without "Use when..." — Claude can't auto-load

## Agents

Agents live in `agents/` as flat markdown files with YAML frontmatter:

| Agent | Purpose |
|-------|---------|
| `monk` | Kairos autonomous daily rhythm |
| `lenny` | Orchestra conductor |
| `eddie` | RSS news briefing |
| `slim` | Product planning |

## Conventions

- All names **kebab-case** with domain prefix (e.g., `orchestra-prd`, `kairos-kickoff`)
- Skill directory name must match `name` field in frontmatter
- New skills: build in a project first, promote here when proven
- Project-specific skills stay in the project repo as `.claude/skills/`
- MCP servers → separate repos (`~/workspace/mcp-<name>/`), not here
