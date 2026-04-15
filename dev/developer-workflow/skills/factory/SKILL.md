---
name: factory
description: "Agentic Factory gateway — install, discover, promote, and manage components from the factory toolkit. Use when the user wants to manage factory plugins and components."
disable-model-invocation: false
---

# Agentic Factory Gateway

You are the factory gateway — the single entry point for managing reusable Claude Code components (skills, agents, commands) across projects.

## Configuration

- **Factory repo path:** ~/workspace/agentic-factory
- **Registry file:** registry.yaml (in factory repo root)

## Subcommands

Parse `$ARGUMENTS` to determine which subcommand to run:

```
/factory <subcommand> [args...]
```

Supported: `list`, `install`, `promote`, `check`, `update`, `rebuild-registry`, `help`

If no subcommand or unknown subcommand, show help.

---

## help

```
Agentic Factory — component management

Usage:
  /factory list [--scope general|domain-specific] [--type skill|agent|command] [--search <query>]
  /factory install <name|--all> [--global|--project] [--scope general]
  /factory promote <source-path> [--name <name>] [--type <type>] [--scope <scope>]
  /factory check [--global|--project]
  /factory update [<name>|--all] [--global|--project]
  /factory rebuild-registry

Factory repo: ~/workspace/agentic-factory
```

## list

1. Read `~/workspace/agentic-factory/registry.yaml`
2. Parse and apply filters: `--scope`, `--type`, `--search`
3. Display grouped by type then scope

## install

1. Read registry, find component(s)
2. Resolve dependencies
3. Determine target: `--global` → `~/.claude/`, `--project` → `.claude/`
4. Copy files, skip identical, prompt on diff
5. Report installed/skipped

**Context budget warning:** If installing >40 skills globally, warn about context budget.

## promote

1. Read source files, infer name/type from path
2. Validate factory conventions (kebab-case, frontmatter)
3. **Context separation check** — scan for domain-leak indicators (hardcoded paths, specific app names, tech stack assumptions)
4. Copy to factory, update registry

## check

Compare installed components against factory. Report: up-to-date, stale, not installed.

## update

Re-install stale components from factory. Show diffs before overwriting.

## rebuild-registry

Scan `~/workspace/agentic-factory/components/` and regenerate `registry.yaml`.
