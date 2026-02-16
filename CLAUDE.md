# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Structure

This is a Claude Code plugin repository containing specialized agents, commands, and templates. The project is organized as a collection of Markdown-based configuration files and is distributed as a Claude Code plugin for easy installation across projects.

### Directory Organization

- **.claude/** - Core Claude Code configuration (portable, self-contained)
  - **agents/** - Specialized factory guide agents
    - `factory-guide.md` - Main orchestrator for building skills, prompts, agents, commands, hooks
    - `skills-guide.md` - Interactive guide for building Claude Skills
    - `prompts-guide.md` - Interactive guide for generating mega-prompts
    - `agents-guide.md` - Interactive guide for building Claude Agents
    - `commands-guide.md` - Interactive guide for building slash commands
    - `hooks-guide.md` - Interactive guide for building Claude hooks
  - **commands/** - Slash commands for common tasks
    - `build.md` - Meta-command to build skills, prompts, agents, commands, or hooks
    - **git/** - Git-related commands
      - `commit.md` - Stage working tree changes and create a Conventional Commit
      - `issue.md` - Fetch and display GitHub issue details
      - `push.md` - Stage, commit, and push the current branch
  - **templates/** - Factory prompt templates (self-contained for portability)
    - `SKILLS_FACTORY_PROMPT.md` - Template for generating Claude Skills
    - `PROMPTS_FACTORY_PROMPT.md` - Template for generating mega-prompts
    - `AGENTS_FACTORY_PROMPT.md` - Template for generating Claude Agents
    - `MASTER_SLASH_COMMANDS_PROMPT.md` - Template for generating slash commands
    - `HOOKS_FACTORY_PROMPT.md` - Template for generating Claude hooks
  - **skills/** - Pre-built Claude Skills for use in projects
    - `journal/` - Git-first journal skill with minimal user input
    - `repo-summarizer/` - Repository analysis and documentation generator

- **.claude-plugin/** - Plugin configuration
  - `marketplace.json` - Local marketplace configuration for testing

- **agents/** - Specialized agents (quality-control-enforcer, research-agent, research-docs-fetcher, work-completion-summarizer, etc.)

- **curated-prompts/** - Collected and original prompts organized by domain
  - **art/** - Art and creative prompts
  - **ios-development/** - iOS and Swift development prompts
  - **pkm/** - Personal knowledge management prompts
  - **writing/** - Writing style, editing, and anti-slop prompts
  - **yoga/** - Yoga teaching and class planning prompts

- **commands/** - Slash commands (context, prime, research, tools, gh-issue, plan-spec, rebuild-context, rebuild-readme)
- **plugins/** - Example Claude Code plugins for reference
- **docs/** - Additional documentation and reports

## Key Components

### Agents
Factory guide agents in `.claude/agents/` help build new resources, while specialized agents in `agents/` provide task-specific functionality. Each agent follows a YAML frontmatter format with:
- `name`: Agent identifier
- `description`: When to use the agent (with examples)
- `color`: Visual indicator
- Agent-specific instructions and methodology

### Commands
Commands in `.claude/commands/` and `commands/` provide structured workflows with:
- `description`: Command purpose in frontmatter
- Sections like `Run`, `Read`, and `Report` for systematic execution

### Templates
Templates in `.claude/templates/` offer comprehensive analysis structures for different project types, focusing on:
- Implementation-ready documentation
- File-by-file breakdowns
- Actionable modification guidance
- Developer workflow integration

### Skills
Pre-built skills in `.claude/skills/` provide ready-to-use functionality that can be installed in any project, including journal generation and repository documentation.

### Curated Prompts
Collected and original prompts in `curated-prompts/`, organized by domain. Each prompt is a standalone markdown file with YAML frontmatter:
- `name`: Prompt identifier
- `description`: What the prompt does
- `source`: URL where it was found, or `original` for self-authored
- `collected`: Date added
- `tags`: Cross-domain discoverability tags

Unlike skills (deep knowledge + behavior) or agents (workflow + persona), curated prompts are portable, copy-pasteable instructions usable with any LLM.

## Usage Patterns

1. **Agent Invocation**: Agents are referenced by their name and provide specialized analysis or validation
2. **Command Execution**: Commands guide systematic exploration and documentation of codebases
3. **Template Application**: Templates structure comprehensive codebase analysis for different project types
4. **Prompt Usage**: Curated prompts are grabbed from `curated-prompts/` and used directly with any LLM

## Architecture Notes

This repository serves as a Claude Code plugin providing a configuration and template library. It doesn't contain executable code but rather provides structured markdown documents that define:
- Agent behaviors and review criteria
- Command sequences for codebase analysis
- Templates for documenting different types of projects
- Curated prompts for direct use with any LLM

The plugin is designed to enhance Claude Code's ability to understand, analyze, and document various codebases through structured approaches and specialized agent roles. It can be installed across multiple projects via the Claude Code plugin system, providing consistent tooling and workflows.

### Portability Design

The `.claude/` directory is completely self-contained and portable:
- All factory templates are in `.claude/templates/` (no external dependencies)
- All factory guide agents reference templates using relative paths (`.claude/templates/...`)
- The entire `.claude/` directory can be copied to any project for instant meta-generator functionality
- No external `documentation/` directory required - everything needed is inside `.claude/`

To use the meta-generator in a new project:
```bash
cp -r .claude/ ~/new-project/
cd ~/new-project
# Now you can use /build to generate skills, prompts, agents, commands, or hooks
```