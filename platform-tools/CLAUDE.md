# Platform Tools

Platform-specific utilities and integrations. Components here serve specific platforms or tools rather than a general practice workflow.

## Components

### Skills
- **cloudflare** — Cloudflare Workers development patterns and conventions
- **fork-terminal** — Fork terminal sessions for agentic coding tools
- **goose-recipes** — Create and validate Goose recipes
- **goose-recipe-analysis** — Goose recipes for document analysis and transformation
- **uat-audit** — Audit and enforce UAT folder structure and organization

## How They Work Together

These are largely independent — each serves a specific platform. Cloudflare stands alone for Workers projects. The goose-* pair works together for Goose recipe workflows. fork-terminal is a utility for any multi-agent setup. uat-audit validates testing structure.

## Conventions
- Each skill is self-contained for its platform
- Platform skills should detect the relevant tech stack before activating
- New platform skills go here until a critical mass warrants their own domain

## When to Break This Up
If several skills accumulate for a single platform (e.g., 3+ AWS skills, or 3+ Google Cloud skills), consider promoting that platform to its own practice domain.
