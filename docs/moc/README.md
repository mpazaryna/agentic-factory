---
title: Agentic Factory - Map of Content
type: moc
generated: 2025-11-20
last_updated: 2025-11-20
project: agentic-factory
status: current
---

# Agentic Factory - Map of Content

**A meta-generator factory system for building custom Claude Code components through interactive guided workflows.**

## Quick Navigation

- **[Features](./features.md)** - Core capabilities and what the toolkit can do
- **[Architecture](./architecture.md)** - System design and technical decisions
- **[Components](./components.md)** - Detailed component catalog

## Project Overview

Agentic Factory is a collection of specialized agents, commands, templates, and a powerful factory system for creating custom Claude Code components. The toolkit enables developers to rapidly build Skills, Prompts, Agents, Commands, and Hooks through interactive guided workflows.

### Current State (As of 2025-11-20)

**Technology Stack:**
- Pure markdown configurations
- YAML frontmatter for metadata
- JSON for plugin configuration
- Bash for automation
- No code execution (markdown-driven)

**Key Statistics:**
- 21 markdown files in `.claude/` directory
- 6 specialized factory guide agents
- 5 comprehensive factory templates (5,175 total lines)
- 12+ generated skills in `skills/`
- 4 example plugins in `plugins/`

## Core Features

### 1. Factory System (Meta-Generator)
The `/build` command provides unified access to component generation:
- Skills Factory - Multi-file capabilities
- Prompts Factory - Mega-prompt generation (69 presets)
- Agents Factory - Workflow specialists
- Commands Factory - Slash commands
- Hooks Factory - Workflow automation

**Status:** ✅ Fully implemented with 12+ generated skills

### 2. Plugin Distribution System
- Local marketplace configuration
- Plugin-based architecture
- Cross-project installation

**Status:** ✅ Implemented with 4 example plugins

### 3. Portable .claude/ Directory
- Self-contained factory system
- No external dependencies
- Copy-to-project portability

**Status:** ✅ Fully self-contained

## Architecture Highlights

**Three-Layer Design:**
1. **Orchestration Layer** - `/build` command + factory-guide
2. **Specialist Layer** - 6 dedicated guide agents
3. **Template Layer** - 5 comprehensive factory templates

See [architecture.md](./architecture.md) for complete technical overview.

## Key Design Decisions

- **Pure Markdown Over Code** - Security and portability
- **Interactive Q&A Over Config Files** - Lower barrier to entry
- **Specialist Delegation Pattern** - Scalable maintenance
- **Self-Contained .claude/** - Instant portability

See [architecture.md](./architecture.md) for detailed rationale.

## Generated Outputs

The toolkit has successfully generated:

**Skills (12+):**
- repo-summarizer - Portfolio documentation generator
- project-moc-generator - This MOC system!
- yoga-class-planner - Domain-specific planner
- commit-helper - Git workflow assistant
- frontend-design - Design excellence skill
- [See all in features.md](./features.md)

**Plugins (4):**
- hello-world - Example plugin
- git-start-new - Feature workflow
- decide-technical - Decision research
- research-task - Research workflow

## Repository Structure

```
agentic-factory/
├── .claude/                   # Factory system (portable)
│   ├── agents/               # 6 specialist agents
│   ├── commands/             # /build command
│   ├── templates/            # 5 factory templates
│   └── skills/               # Installed skills
├── .claude-plugin/           # Plugin configuration
├── commands/                 # Example commands
├── plugins/                  # Example plugins
├── skills/         # Generated skill outputs
└── docs/                     # Documentation
    └── moc/                  # This MOC system
```

## Quick Start

1. **Install as Plugin:**
   ```bash
   claude-code plugin marketplace add /path/to/agentic-factory/.claude-plugin
   claude-code plugin install agentic-factory@agentic-factory-local
   ```

2. **Build Something:**
   ```bash
   /build skill    # Create a custom skill
   /build agent    # Create a custom agent
   /build command  # Create a slash command
   ```

3. **Explore Generated Skills:**
   - Check `skills/` for examples
   - Review `skills/repo-summarizer/` for portfolio docs
   - Test `skills/project-moc-generator/` (this skill!)

## Related Resources

- **Main README**: [../../README.md](../../README.md)
- **Portfolio Documentation**: [../../PROJECT.md](../../PROJECT.md)
- **Changelog**: [../../CHANGELOG.md](../../CHANGELOG.md)
- **Claude Instructions**: [../../CLAUDE.md](../../CLAUDE.md)

## For Developers

**Working on the factory system?**
- See [architecture.md](./architecture.md) for system design
- Review [components.md](./components.md) for detailed catalog

**Building custom components?**
- Use `/build` command for guided generation
- Review `skills/` for examples
- Check factory templates in `.claude/templates/`

## Project Status

**Current Phase:** Production-ready with active development

**Recent Additions:**
- repo-summarizer skill (2025-11-19)
- project-moc-generator skill (2025-11-20)
- Comprehensive PROJECT.md portfolio documentation
- Enhanced git workflow commands

**Next Steps:**
- Template versioning system
- Output validation commands
- Factory status dashboard
- Installation automation

---

**Last Updated:** 2025-11-20
**Generated By:** project-moc-generator skill
**Project:** agentic-factory by [@mpazaryna](https://github.com/mpazaryna)
