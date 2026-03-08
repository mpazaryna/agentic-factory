# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Is

Agentic Factory is a component registry and distribution system for Claude Code. It stores reusable Skills, Agents, and Commands as pure markdown/YAML, organized by scope (general-purpose vs domain-specific), and distributes them to any project via the `/factory` gateway command.

Components are built organically in real projects, then promoted into the factory when proven. There is no code generation or templating layer — Claude Code natively understands how to create skills, agents, and commands.

## Directory Layout

- `components/` — The component library (canonical home for all installable components)
  - `skills/` — General-purpose skills (16)
  - `agents/` — General-purpose agents (8)
  - `commands/` — General-purpose commands (6)
  - `templates/` — Shared templates (e.g., CONTEXT.stub.md)
  - `domain/` — Domain-specific components, organized by project
- `registry.yaml` — Component manifest (single source of truth)
- `plugins/` — Claude Code/Desktop plugin packages (JSON manifest + bundled components)
- `prompts/` — Standalone curated prompts (yoga, pkm, market-research, writing)
- `.orchestra/` — Project documentation (ADRs, devlog, work items)
- `.claude/` — Project-level Claude Code settings only

## The `/factory` Gateway

A single globally-installed command (`~/.claude/commands/factory.md`) that manages all component operations:

```
/factory list [--scope general|domain-specific] [--type skill|agent|command] [--search <query>]
/factory install <name|--all> [--global|--project] [--scope general]
/factory promote <source-path> [--name <name>] [--type <type>] [--scope <scope>]
/factory check [--global|--project]
/factory update [<name>|--all] [--global|--project]
/factory rebuild-registry
```

## Conventions

### Naming
- All component names use **kebab-case** (e.g., `dev-inquiry`, `yoga-class-planner`)
- Skill directories match their YAML frontmatter `name` field

### Component Formats
- **Skills**: YAML frontmatter with `name` and `description`, plus SKILL.md, README.md, HOW_TO_USE.md, and sample data
- **Agents**: YAML frontmatter with `name`, `description`, `color`, and agent-specific fields
- **Commands**: YAML frontmatter with `description`, markdown body

### Component Metadata
Every component in `components/` has a `meta.yaml` with: name, type, scope, description, install_files, install_target, dependencies, tags

### Where Things Go
- New components → `components/<type>s/<name>/` (via `/factory promote`)
- Domain-specific → `components/domain/<project>/<type>s/<name>/`
- Plugins → `plugins/<plugin-name>/`
- Curated prompts → `prompts/<domain>/`
- ADRs → `.orchestra/adr/`
- Devlogs → `.orchestra/devlog/`
- Work items → `.orchestra/work/<ticket-id>/`

### Workflow
1. Build components organically in real projects
2. `/factory promote` to bring proven components into the factory
3. `/factory install` to distribute components to other projects
4. `/factory check` / `/factory update` to keep installed copies current
