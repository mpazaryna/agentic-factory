# ADR-004: Skills 2.0 Migration — Commands to Skills, Flat Plugin Hierarchy

**Date**: 2026-03-13
**Status**: Accepted

## Context

Claude Code Agent Skills 2.0 unified commands and skills into a single system. Skills in `.claude/skills/` became the recommended path over `.claude/commands/`, supporting directories, richer frontmatter (`context: fork`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `agent`, `model`), and subagent execution.

The factory had a dual structure: `commands/` folders with thin wrappers that invoked `skills/`, plus standalone commands that could have been skills. This created maintenance overhead and prevented leveraging Skills 2.0 features.

Additionally, the directory layout was inconsistent — some plugins sat at root level (`content-creation/`, `product-planning/`), while others were nested under grouping folders (`project-management/clickup/`). The `private/` folder contained project-specific tools that violated cohesion by separating skills from their implementation code.

## Decision

1. **Convert all commands to skills.** Every `commands/*.md` becomes `skills/<name>/SKILL.md` with proper frontmatter. Delete all `commands/` folders.

2. **Apply Skills 2.0 features where they fit:**
   - `context: fork` for autonomous/research skills (clickup agent, issue fetcher, research-task, technical-decision)
   - `disable-model-invocation: true` for side-effect workflows (git commit, push, branch, scaffold)
   - `user-invocable: false` for background knowledge (cloudflare skills, anti-slop, orchestra conventions)
   - `allowed-tools` for scoped execution (issue fetcher: `Bash(gh *)`)

3. **Enforce consistent hierarchy.** Top-level folders are organizational groupings only (`dev/`, `pm/`, `platform/`, `content/`, `product/`, `domain/`). Plugins always live exactly one level down. No `plugin.json` at the grouping level.

4. **Remove project-specific tools.** Delete `private/` — project-specific skills belong in the project repo as `.claude/skills/`, not in the factory.

5. **Break monolith plugins into focused ones.** `platform-tools` became 3 independent plugins (cloudflare, fork-terminal, goose). `content-creation` became 2 (anti-slop, writing). `senior-pm` skill split into 3 (portfolio-health, risk-analysis, resource-planning).

6. **Rename for brevity.** `content-creation/` → `content/`, `project-management/` → `pm/`, `platform-tools/` → `platform/`.

## Consequences

- Zero `commands/` folders remain in the repo
- 15 independently installable plugins across 6 groupings
- Every skill leverages appropriate Skills 2.0 frontmatter
- Marketplace works from both local path and GitHub (`mpazaryna/agentic-factory`)
- Skill names describe what they do, never repeat the plugin name
- `prompts/` folder absorbed — pkm became a plugin, yoga became a plugin, anti-slop became a background skill, ios-prompts became a reference file
