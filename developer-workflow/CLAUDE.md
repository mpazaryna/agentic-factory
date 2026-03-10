# Developer Workflow

The daily developer practice: understand context, explore code, investigate problems, report work, ensure quality, manage git.

## Components

### Skills
- **dev-context** — Context architecture for ADRs, design docs, specs, and plans
- **dev-explore** — Codebase exploration and documentation generation
- **dev-inquiry** — Technical investigations, spikes, comparisons, and decisions
- **dev-reports** — Journals, devlogs, and status updates from git history

### Agents
- **quality-control-enforcer** — Reviews and validates work quality, catches workarounds and shortcuts
- **work-completion-summarizer** — Creates concise summaries when tasks finish

### Commands
- **git/commit** — Conventional Commit workflow (no push)
- **git/push** — Stage, commit, push with governance
- **git/issue** — Fetch GitHub issue for coding agent analysis

## How They Work Together

The dev-* skills form the core loop: `dev-context` establishes what exists, `dev-explore` maps the codebase, `dev-inquiry` investigates specific questions, `dev-reports` captures what was done. The `quality-control-enforcer` agent validates output quality across all work. The `work-completion-summarizer` closes the loop by generating summaries. Git commands handle the mechanics of committing and pushing.

Typical sequence: dev-context → dev-explore → dev-inquiry → (do work) → quality-control-enforcer → dev-reports → git/commit → git/push.

## Conventions
- All skills use the `dev-` prefix for the core workflow family
- Git commands live under a `git/` subdirectory (commit, push, issue)
- Reports should follow the project's existing documentation conventions

## What's Missing
- PR review workflow skill (code review patterns, feedback structure)
- Branch management commands (feature branch creation, merge strategies)
- Debugging workflow skill (systematic debugging approach)
