# Agentic Factory

A curated skill and agent library for Claude Code. 34 skills across 8 domains, built from real work and promoted here when proven.

## Structure

```
agents/     — 4 agent definitions
skills/     — 34 skills, flat, domain-prefixed
```

## Skills

| Domain | Prefix | Skills |
|--------|--------|--------|
| Orchestra methodology | `orchestra-` | adr, devlog, milestone, prd, roadmap, scaffold, spec, ticket, uml |
| Kairos daily rhythm | `kairos-` | kickoff, shutdown, knote, review, weekly-plan, weekly-finalize |
| Yoga class planning | `yoga-` | anatomy-expert, asana-strategist, orchestrator, professor, theme-developer |
| Cloudflare Workers | `cf-` | workers, workers-ai, hono, kv, durable-objects |
| Swift / SwiftUI | `swift-` | swift-lang, swift-ui, swiftui-submission-prep |
| Feynman investigation | `feynman-` | inquiry, decision |
| Developer tooling | `dev-` | enforcer, playwright, skills-auditor |
| Writing style | `writing-` | no-slop |

## Agents

| Agent | Domain | Purpose |
|-------|--------|---------|
| `monk` | Kairos | Autonomous daily rhythm — kickoff, shutdown, weekly planning |
| `lenny` | Orchestra | Conductor — runs the full PRD → spec → execute loop |
| `eddie` | Content | RSS news briefing from OPML feeds |
| `slim` | Product | Ticket → PRD refinement |

## Install

Skills install **per project** — each repo (substation) declares the skills it
consumes. There is no global install.

### Skills you'll adapt — editable copy (capabilities)

Pull skills into the current project with the [`skills`](https://www.skills.sh)
CLI. They land in the project's agent dir, editable and committed with the repo:

```bash
npx skills@latest add mpazaryna/agentic-factory                            # choose interactively
npx skills@latest add mpazaryna/agentic-factory --skill orchestra-review   # a single skill
npx skills@latest update                                                   # re-sync from source
```

### Skills that must stay identical — read-only, versioned (contracts)

Install the marketplace plugin: a managed, read-only bundle that moves as one
unit. Read-only means it *can't* drift — you can't edit it in place, only pull a
new version.

```
/plugin marketplace add mpazaryna/agentic-factory
/plugin install skills@agentic-factory
```


## Authoring

Build in a real project first. Promote here when the skill is proven and generic enough to reuse.

Each skill needs:
- `SKILL.md` — YAML frontmatter (`name`, `description`, `allowed-tools`) + instructions
- `README.md` — human-readable companion

See [CLAUDE.md](CLAUDE.md) for conventions and quality standards.
