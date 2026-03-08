# Agentic Factory

A component registry and distribution system for AI-powered development tooling. Stores reusable Skills, Agents, Commands, Plugins, and Prompts — primarily for Claude Code, but designed to be platform-flexible.

Components are built organically in real projects, promoted into the factory when proven, and distributed back out to any project via the `/factory` gateway or Claude's native plugin system.

## What's Inside

| Type | Count | Location | Platform |
|------|-------|----------|----------|
| **Skills** | 16 general, 4 domain | `components/skills/` | Claude Code |
| **Agents** | 8 general, 5 domain | `components/agents/` | Claude Code |
| **Commands** | 6 general, 25 domain | `components/commands/` | Claude Code |
| **Plugins** | 5 | `plugins/` | Claude Code + Desktop |
| **Prompts** | 16 | `prompts/` | Any LLM |

**64 components** across 5 domains (chiro, chiro-mlx, chiro-base, resin, yellow-house), plus a curated prompt library.

## Quick Start

### 1. Install the factory gateway (one time)

```bash
# From the factory repo
cp components/commands/factory/factory.md ~/.claude/commands/factory.md
```

This gives you `/factory` in every Claude Code session.

### 2. Browse available components

```
/factory list
/factory list --scope general
/factory list --type skill --search codebase
```

### 3. Install components

```
# Install a single component globally
/factory install dev-explore --global

# Install to current project
/factory install git --project

# Install all general-purpose components
/factory install --all --scope general --project
```

### 4. Keep components current

```
# Check for stale installed copies
/factory check

# Update everything
/factory update --all
```

## Promoting Components

Built something useful in a project? Bring it home:

```
/factory promote .claude/skills/my-new-skill/ --scope general
/factory promote .claude/agents/my-agent.md --scope domain-specific --domain resin
```

The promote command scans for domain-specific hardcoding and helps you generalize components for reuse.

## Plugins

The `plugins/` directory contains packaged plugins for Claude Code and Claude Desktop with JSON manifests:

| Plugin | Description |
|--------|-------------|
| `prd-creator` | Guided PRD generation workflow with bundled skill |
| `decide-technical` | Technical decision framework with ADR output |
| `research-task` | Structured research and investigation |
| `git-start-new` | Safe feature branch creation |
| `hello-world` | Example plugin for learning the format |

## Prompts

Platform-agnostic prompts in `prompts/`, organized by domain:

- **pkm** — Personal knowledge management (weekly reviews, planning, summaries)
- **yoga** — Class planning multi-agent system (orchestrator + specialists)
- **writing** — Anti-slop writing guidelines
- **market-research** — Competitive analysis
- **ios-development** — Collected iOS development prompts

## Repository Structure

```
agentic-factory/
├── components/              # Component library
│   ├── skills/              # General-purpose skills
│   ├── agents/              # General-purpose agents
│   ├── commands/            # General-purpose commands
│   ├── templates/           # Shared templates
│   └── domain/              # Domain-specific components
│       ├── chiro/
│       ├── chiro-mlx/
│       ├── chiro-base/
│       ├── resin/
│       └── yellow-house/
├── plugins/                 # Claude Code/Desktop plugins
├── prompts/                 # Platform-agnostic prompts
├── registry.yaml            # Component manifest
├── .orchestra/              # ADRs, devlog, work items
└── docs/                    # Documentation
```

Each component has a `meta.yaml` with metadata (name, type, scope, install target, dependencies, tags) that drives the registry and installation.

## Design Principles

- **Organic over generated** — Components are built through real work, not templated into existence
- **Context separation** — General components discover project context at runtime, never hardcode it
- **Pure markdown** — No executable code in the repo, just structured configurations
- **One source of truth** — `components/` is canonical, `registry.yaml` is the manifest, `meta.yaml` per component drives everything
