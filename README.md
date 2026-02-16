# Agentic Factory

A meta-generator factory system for building custom Claude Code components — Skills, Prompts, Agents, Commands, and Hooks — through interactive guided workflows.

## Overview

Agentic Factory provides structured markdown-based configurations that guide Claude Code through various development tasks:

- **Skill Families** - Organized collections of progressive-disclosure skills for developer workflow and design
- **Factory System** - Meta-generator for creating Skills, Prompts, Agents, Commands, and Hooks
- **Specialized Agents** - Code review, documentation fetching, and work summarization
- **Pre-configured Commands** - Systematic codebase exploration and git workflows

## Skill Families

### dev-* (Developer Workflow)

Skills for the developer thinking and artifact generation process:

| Skill | Purpose |
|-------|---------|
| **dev-inquiry** | Investigation & technical decisions (Feynman-style exploration, spikes, scoring) |
| **dev-explore** | Codebase understanding (analyze, MOC, portfolio modes) |
| **dev-reports** | Journals & status reports (git journal, devlog, 22A/22B) |
| **dev-context** | Context scaffolding (ADR, Design, Spec, Plan templates) |

### design-* (UI Design)

Skills for design theory and platform-specific implementation:

| Skill | Purpose |
|-------|---------|
| **design-principles** | Universal theory (typography, color, hierarchy, motion, accessibility) |
| **design-web** | Web/CSS implementation (variables, components, backgrounds, responsive) |
| **design-swiftui** | SwiftUI implementation (views, state, layout, animation, accessibility) |
| **design-review** | Audits & submission (App Store, accessibility audit, design checklist) |

Each skill follows **progressive disclosure architecture**:
- Small orchestrator SKILL.md (~60-80 lines) routes to focused reference files
- Reference files go deep on specific topics
- Reduces cognitive overhead while maintaining depth

## Factory System

Build custom Claude Code components with guided workflows:

```
/build → Choose: Skills | Prompts | Agents | Commands | Hooks
      → Answer 4-11 questions
      → Get production-ready output
```

The factory system lives in `.claude/` and is fully portable—copy to any project for instant meta-generator functionality.

## Structure

```
agentic-factory/
├── .claude/                     # Core configuration (portable)
│   ├── agents/                  # Factory guide agents
│   ├── commands/                # Slash commands (/build, /git:*)
│   ├── templates/               # Factory templates
│   └── skills/                  # Core skills (journal, repo-summarizer)
│
├── skills/                      # Skill families
│   ├── dev-inquiry/             # Investigation & decisions
│   ├── dev-explore/             # Codebase understanding
│   ├── dev-reports/             # Journals & reports
│   ├── dev-context/             # Context scaffolding
│   ├── design-principles/       # Universal design theory
│   ├── web-design/              # Web/CSS implementation
│   └── design-review/           # Audits & submission
│
├── agents/                      # Specialized agents
├── commands/                    # Slash commands
└── CLAUDE.md                    # Claude Code instructions
```

## Quick Start

Copy a skill family to your project:

```bash
# Developer workflow skills
cp -r skills/dev-* /path/to/your/project/.claude/skills/

# Design skills
cp -r skills/design-* /path/to/your/project/.claude/skills/

# Factory system (meta-generator)
cp -r .claude/ /path/to/your/project/
```

## Documentation

- **[Components](docs/components.md)** - Detailed overview of agents, commands, and templates
- **[Usage](docs/usage.md)** - How to use the toolkit in your projects
- **[Maintenance](docs/maintenance.md)** - Meta-tooling and inspiration

## Key Features

- **Progressive Disclosure** - Small orchestrators route to deep reference files
- **Portable & Self-Contained** - Copy skill folders to any project
- **No Code Execution** - Pure markdown configurations
- **Modular Design** - Pick and choose components as needed
- **Technology-Specific** - Tailored templates for iOS/Swift, Web, TypeScript, etc.
