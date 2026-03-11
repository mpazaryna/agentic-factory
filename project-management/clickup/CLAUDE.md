# ClickUp

ClickUp ticket lifecycle management. Commands read `CONTEXT.md` at runtime for build commands, file paths, and conventions. Uses the ClickUp REST API via `CLICKUP_API_KEY` in `.env`.

## Prerequisites

- `CONTEXT.md` in the project root
- `.env` with `CLICKUP_API_KEY=pk_...`

## Commands
- **open** — Fetch a ticket, evaluate, create branch, plan & implement (interactive)
- **investigate** — Analyze a ticket, discuss, refine — no code changes
- **agent** — Autonomous ticket execution — no human checkpoints
- **close** — UAT check, doc review, PR, merge, mark complete

## Skills
- **clickup-conventions** — Status flow, comment templates, ticket hygiene
