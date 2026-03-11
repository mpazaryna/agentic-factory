# Project Management

Ticket lifecycle management for any project. Commands are project-agnostic — they read `CONTEXT.md` at runtime for build commands, file paths, ADR locations, and conventions.

Currently supports **ClickUp** via REST API. The pattern is extensible to other platforms (GitHub Issues, Linear, Jira) by adding platform-specific commands under a new subfolder.

## Prerequisites

- `CONTEXT.md` in the project root (generate via `/context-rebuild` or from `templates/CONTEXT.stub.md`)
- `.env` in the project root with `CLICKUP_API_KEY=pk_...` (for ClickUp commands)

## Components

### Commands (clickup/)
- **open** — Fetch a ticket, evaluate, create branch, orient, plan & implement (interactive)
- **investigate** — Fetch a ticket, analyze scope/risks, discuss — no code changes
- **agent** — Autonomous ticket execution — no human checkpoints
- **close** — UAT check, doc review, PR, merge, mark complete

### Skills (clickup/)
- **clickup-conventions** — Comment templates, status transitions, and ticket hygiene patterns

## How They Work Together

The commands form a ticket lifecycle:

```
investigate → open → (implement) → close
      OR
investigate → agent (autonomous end-to-end)
```

Invoked as `/project-management:open`, `/project-management:agent`, etc.

- **investigate** is pre-work: read-only analysis and discussion
- **open** starts interactive work: branch, plan, implement with human checkpoints
- **agent** is autonomous: fetch → implement → PR → merge → close, no human input
- **close** wraps up: UAT, docs, PR, merge, done

All commands read `CONTEXT.md` for project-specific details (build commands, test commands, ADR paths, conventions). The commands never hardcode project paths.

## CONTEXT.md Sections Used

| Section | Used by | Purpose |
|---------|---------|---------|
| Tech Stack | open, agent | Understand what to build with |
| Directory Structure | open, investigate, agent | Navigate codebase |
| Conventions | all | Naming, commit format, architecture patterns |
| Key Files | open, agent | Entry points, config files |
| Agent Knowledge Base | open, investigate | ADR/spec locations |
| External Integrations | all | ClickUp team ID, other APIs |
| Known Constraints | agent | Avoid violating project limits |

## Conventions

- Commands are organized by platform (`clickup/`, future: `linear/`, `github-issues/`)
- Ticket descriptions are never overwritten — updates go in comments
- Branch naming: `ticket/{task-id}-{short-name}`
- Commits reference ticket ID in the body

## What's Missing

- GitHub Issues support (commands that use `gh` CLI instead of ClickUp API)
- Linear support
- Sprint/velocity analysis skills
- Ticket health dashboard
