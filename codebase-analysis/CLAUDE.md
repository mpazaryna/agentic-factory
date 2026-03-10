# Codebase Analysis

Understand, audit, test, and document codebases. Analysis-first development practices.

## Components

### Skills
- **spike-driven-dev** — Spike-driven development methodology with TDD and risk reduction

### Agents
- **convention-auditor** — Audits codebase compliance against discovered conventions
- **research-docs-fetcher** — Fetches, processes, and organizes web content into structured markdown

### Commands
- **acb** — Analyze Codebase: modular, template-driven analysis with tech-specific templates (base, typescript, ios-swift, android-kotlin, jest-testing, mcp-server, cloudflare-worker)
- **context-rebuild** — Regenerate CONTEXT.md and README.md from codebase state
- **prime-web-dev** — Quick web codebase comprehension primer
- **playwright** — Playwright browser automation and E2E test generation

## How They Work Together

`acb` is the heavy-hitter — it produces structured codebase analysis using tech-specific templates. `context-rebuild` keeps documentation in sync. `prime-web-dev` is the quick-start for web projects. `convention-auditor` validates that code follows the patterns `acb` discovers. `research-docs-fetcher` brings in external documentation. `spike-driven-dev` provides the methodology for exploratory analysis before committing to implementation.

## Conventions
- ACB templates live in `commands/acb/templates/` — add new templates for new tech stacks
- Analysis output should be structured markdown
- Convention auditing reads patterns from project config (CLAUDE.md, ADRs), not hardcoded rules

## What's Missing
- Dependency analysis skill (outdated packages, security vulnerabilities)
- Architecture diagramming (generate diagrams from code structure)
