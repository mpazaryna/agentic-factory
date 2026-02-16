# Agentic Factory

A meta-generator factory system for building custom Claude Code components — Skills, Prompts, Agents, Commands, and Hooks — through interactive guided workflows.

## What You Can Build

| Component | What It Does |
|-----------|-------------|
| **Skills** | Multi-file capabilities with deep domain knowledge |
| **Prompts** | Production-ready mega-prompts (69 presets across 15 domains) |
| **Agents** | Workflow specialists with YAML frontmatter configuration |
| **Commands** | Slash commands following Anthropic patterns |
| **Hooks** | Workflow automation with safety validation |

## Quick Start

```
/build → Choose a component type → Answer 4-11 questions → Get production-ready output
```

Or go direct:

```
/build skill
/build prompt
/build agent
/build command
/build hook
```

## Installation

The factory system lives in `.claude/` and is fully portable:

```bash
# Copy the factory to any project
cp -r .claude/ /path/to/your/project/

# Or copy individual skills
cp -r skills/dev-* /path/to/your/project/.claude/skills/
```

## Structure

```
agentic-factory/
├── .claude/              # Factory system (portable)
│   ├── agents/           # Factory guide agents
│   ├── commands/         # /build, /git:commit, /git:push
│   ├── templates/        # 5 factory templates
│   └── skills/           # Core skills
├── skills/               # Pre-built skill families (dev-*, design-*)
├── agents/               # Specialized agents
├── commands/             # Additional slash commands
├── curated-prompts/      # Standalone prompts organized by domain
└── plugins/              # Example Claude Code plugins
```

## Key Principles

- **Pure Markdown** — No code execution, just structured configurations
- **Portable** — Copy `.claude/` to any project for instant factory access
- **Modular** — Pick and choose components as needed
- **Guided** — Interactive Q&A workflows instead of manual config files
