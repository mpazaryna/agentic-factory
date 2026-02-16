# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Is

Agentic Factory is a meta-generator factory system for building custom Claude Code components — Skills, Prompts, Agents, Commands, and Hooks — through interactive guided workflows. Everything is pure markdown and YAML frontmatter. There is no executable code.

## Directory Layout

- `.claude/` — Portable factory system (agents, commands, templates, skills)
- `skills/` — Pre-built skill families (`dev-*`, `design-*`, plus domain-specific)
- `agents/` — Specialized agents (quality control, research, summarization)
- `commands/` — Additional slash commands
- `curated-prompts/` — Standalone prompts organized by domain
- `plugins/` — Example Claude Code plugins
- `docs/` — Documentation, devlogs, and reports

## Conventions

### Naming
- All component names use **kebab-case** (e.g., `dev-inquiry`, `yoga-class-planner`)
- Skill directories match their YAML frontmatter `name` field

### Component Formats
- **Skills**: YAML frontmatter with `name` and `description`, plus SKILL.md, README.md, HOW_TO_USE.md, and sample data
- **Agents**: YAML frontmatter with `name`, `description`, `color`, and agent-specific fields
- **Commands**: YAML frontmatter with `description`, markdown body with Run/Read/Report sections
- **Curated Prompts**: YAML frontmatter with `name`, `description`, `source`, `collected`, `tags`

### Factory System
- The `/build` command is the entry point — it routes to specialist guide agents in `.claude/agents/`
- Each guide agent uses a corresponding template from `.claude/templates/`
- The `.claude/` directory is fully self-contained and portable to other projects

### Where Things Go
- New skills → `skills/<skill-name>/`
- New agents → `agents/<agent-name>/`
- New commands → `commands/<command-name>/`
- New curated prompts → `curated-prompts/<domain>/`
- Factory infrastructure → `.claude/`
