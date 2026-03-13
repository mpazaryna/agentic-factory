# Developer Workflow

The daily developer practice: understand context, explore code, investigate problems, report work, ensure quality, manage git.

## Skills

### Core Workflow
- **dev-context** — Context architecture for ADRs, design docs, specs, and plans
- **dev-explore** — Codebase exploration and documentation generation
- **dev-inquiry** — Technical investigations, spikes, comparisons, and decisions
- **dev-reports** — Journals, devlogs, and status updates from git history

### Git Operations
- **commit** — Conventional Commit workflow with governance (no push)
- **push** — Stage, commit, push with governance
- **issue** — Fetch GitHub issue for analysis (runs in forked context)
- **branch** — Create a new feature branch from main with safety checks

### Tooling
- **factory** — Agentic Factory gateway for managing plugins and components

## Agents
- **quality-control-enforcer** — Reviews and validates work quality
- **work-completion-summarizer** — Creates concise summaries when tasks finish

## Typical Sequence

dev-context → dev-explore → dev-inquiry → (do work) → quality-control-enforcer → dev-reports → /commit → /push
