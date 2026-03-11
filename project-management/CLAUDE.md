# Project Management

Project management practice: ticket lifecycle, portfolio health, risk analysis, and resource planning. Each subdomain is a self-contained folder with its own commands and skills.

## Structure

```
project-management/
├── .claude-plugin/plugin.json    ← registers all subdomain paths
├── CLAUDE.md
├── clickup/                      ← ticket lifecycle via ClickUp REST API
│   ├── commands/
│   └── skills/
└── senior-pm/                    ← portfolio health, risk, capacity planning
    ├── commands/
    └── skills/
```

Adding a new subdomain (e.g., `linear/`, `scrum-master/`) means creating the folder and adding its paths to plugin.json.

## Prerequisites

- `CONTEXT.md` in the project root (generate via `/context-rebuild` or from `templates/CONTEXT.stub.md`)
- `.env` in the project root with `CLICKUP_API_KEY=pk_...` (for ClickUp commands)

## Subdomains

### clickup/

Ticket lifecycle management via ClickUp REST API.

**Commands:**
- **clickup/open** — Fetch a ticket, evaluate, create branch, plan & implement
- **clickup/investigate** — Analyze a ticket, discuss, refine — no code changes
- **clickup/agent** — Autonomous ticket execution — no human checkpoints
- **clickup/close** — UAT check, doc review, PR, merge, mark complete

**Skills:**
- **clickup-conventions** — Status flow, comment templates, ticket hygiene

### senior-pm/

Portfolio management, risk analysis, resource capacity planning, executive reporting.

**Commands:**
- **senior-pm** — Entry point for portfolio health, risk, capacity, and reporting tasks

**Skills:**
- **senior-pm** — Portfolio management expertise: health scoring, risk quantification (EMV, Monte Carlo), resource capacity planning, prioritization frameworks (WSJF, RICE, ICE), executive reporting. Includes Python analysis scripts and reference templates.

## Command vs Skill Pattern

- **Skills** hold the knowledge — Claude auto-invokes them when relevant
- **Commands** are user entry points — explicit actions the user triggers
- A command can be a thin wrapper that delegates to a skill
- Each subdomain manages its own commands/ and skills/ independently

## What's Missing

- GitHub Issues subdomain (`github-issues/`)
- Linear subdomain (`linear/`)
- Scrum master subdomain (`scrum-master/`)
- Confluence/docs subdomain
