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

### Dev machine (symlink)

Symlink individual skills directly into `~/.claude/skills/` for live editing:

```bash
for skill in ~/workspace/agentic-factory/skills/*/; do
  ln -sf "$skill" ~/.claude/skills/$(basename "$skill")
done
```

## Authoring

Build in a real project first. Promote here when the skill is proven and generic enough to reuse.

Each skill needs:
- `SKILL.md` — YAML frontmatter (`name`, `description`, `allowed-tools`) + instructions
- `README.md` — human-readable companion

See [CLAUDE.md](CLAUDE.md) for conventions and quality standards.
