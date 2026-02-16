---
title: Features Overview
type: moc
generated: 2025-11-20
last_updated: 2025-11-20
project: agentic-factory
status: current
---

# Features Overview

This document catalogs all currently implemented features in the Agentic Factory project.

## Core Features (Currently Implemented)

### 1. Factory System (Meta-Generator)

**Status:** ✅ Fully Operational

The centerpiece of Agentic Factory - an interactive system for building custom Claude Code components.

**What It Does:**
- Provides unified `/build` command for all component types
- Guides users through 4-11 question workflows
- Generates complete, validated output with proper formatting
- Creates production-ready components with documentation

**Components:**
- Skills Factory - Build multi-file Skills
- Prompts Factory - Generate mega-prompts (69 presets)
- Agents Factory - Create workflow agents
- Commands Factory - Build slash commands
- Hooks Factory - Generate workflow hooks

**Implementation Files:**
- `.claude/commands/build.md` - Entry point command
- `.claude/agents/factory-guide.md` - Orchestrator
- `.claude/agents/*-guide.md` - 5 specialist agents
- `.claude/templates/*.md` - 5 factory templates

**Evidence of Success:**
- 12+ generated skills in `skills/`
- All with proper YAML frontmatter validation
- Complete documentation packages
- Production-ready ZIP files

---

### 2. Skills Factory

**Status:** ✅ Implemented (1,012 line template)

**What It Builds:**
Multi-file Claude Skills with optional Python code, sample data, and complete documentation.

**Current Capabilities:**
- Interactive Q&A (4-5 questions)
- YAML frontmatter validation
- Kebab-case name enforcement
- File cleanliness standards
- Automatic ZIP packaging

**Generated Skills Examples:**
- `repo-summarizer` - Portfolio documentation
- `project-moc-generator` - This MOC system!
- `yoga-class-planner` - Domain planner
- `commit-helper` - Git workflow
- `frontend-design` - Design excellence
- `technical-decision` - Decision analysis
- `goose-recipes` - Recipe builder
- `internal-comms` - Communication templates
- `code-reviewer` - Code quality review
- `spike-driven-dev` - Development methodology
- `learn-project` - Project learning
- `goose-recipe-analysis` - Recipe analysis

**Template Location:** [.claude/templates/SKILLS_FACTORY_PROMPT.md](../../.claude/templates/SKILLS_FACTORY_PROMPT.md)

**Usage:** `/build skill`

---

### 3. Prompts Factory

**Status:** ✅ Implemented (1,152 line template)

**What It Builds:**
Production-ready mega-prompts for any LLM (ChatGPT, Claude, Gemini).

**Current Capabilities:**
- 69 presets across 15 domains
- Quick-start (30 seconds) or custom (2 minutes)
- Multiple output formats (XML, Claude, ChatGPT, Gemini)
- Role-based prompt engineering

**Template Location:** [.claude/templates/PROMPTS_FACTORY_PROMPT.md](../../.claude/templates/PROMPTS_FACTORY_PROMPT.md)

**Usage:** `/build prompt`

---

### 4. Agents Factory

**Status:** ✅ Implemented (1,123 line template)

**What It Builds:**
Claude Code agents with enhanced YAML frontmatter for specialized workflows.

**Current Capabilities:**
- Agent definition with tools, model, color, field, expertise
- YAML validation
- Markdown-based instructions
- Workflow specialization

**Factory Agents Created:**
- `factory-guide` - Main orchestrator
- `skills-guide` - Skills builder
- `prompts-guide` - Prompts generator
- `agents-guide` - Agents builder
- `commands-guide` - Commands builder
- `hooks-guide` - Hooks builder

**Template Location:** [.claude/templates/AGENTS_FACTORY_PROMPT.md](../../.claude/templates/AGENTS_FACTORY_PROMPT.md)

**Usage:** `/build agent`

---

### 5. Commands Factory

**Status:** ✅ Implemented (1,031 line template)

**What It Builds:**
Custom slash commands following Anthropic patterns.

**Current Capabilities:**
- Simple, Multi-Phase, and Agent-Style command patterns
- YAML frontmatter with description
- Markdown-based instructions
- Bash permission configuration

**Example Commands:**
- `/build` - Factory orchestrator
- `/git:commit` - Git commit workflow
- `/git:push` - Git push workflow
- `/git:issue` - GitHub issue fetcher

**Template Location:** [.claude/templates/MASTER_SLASH_COMMANDS_PROMPT.md](../../.claude/templates/MASTER_SLASH_COMMANDS_PROMPT.md)

**Usage:** `/build command`

---

### 6. Hooks Factory

**Status:** ✅ Implemented (857 line template)

**What It Builds:**
Claude Code hooks for workflow automation with safety validation.

**Current Capabilities:**
- hook.json generation
- Event-based triggers
- Safety validation
- README documentation

**Template Location:** [.claude/templates/HOOKS_FACTORY_PROMPT.md](../../.claude/templates/HOOKS_FACTORY_PROMPT.md)

**Usage:** `/build hook`

---

### 7. Plugin Distribution System

**Status:** ✅ Implemented

**What It Does:**
Enables distribution and installation of toolkit components across projects.

**Current Capabilities:**
- Local marketplace configuration
- Plugin metadata (name, version, description, keywords)
- Cross-project installation
- Example plugins (4 total)

**Implementation:**
- [.claude-plugin/marketplace.json](../../.claude-plugin/marketplace.json) - Marketplace config

**Example Plugins:**
- hello-world - Basic example
- git-start-new - Feature workflow
- decide-technical - Decision research
- research-task - Research workflow

---

### 8. Portable .claude/ Directory

**Status:** ✅ Fully Implemented

**What It Enables:**
Copy the entire factory system to any project for instant meta-generation.

**Current Capabilities:**
- Self-contained factory system
- No external dependencies
- Relative path references throughout
- Works in any project directory

**Implementation:**
- All factory templates in `.claude/templates/`
- All guide agents in `.claude/agents/`
- Build command in `.claude/commands/`
- Skills in `.claude/skills/`

**Portability Evidence:**
```bash
cp -r .claude/ ~/new-project/
cd ~/new-project
# /build now works immediately
```

---

### 9. Validation & Quality Standards

**Status:** ✅ Implemented in Templates

**What It Enforces:**
- YAML frontmatter format validation
- Kebab-case naming convention
- File cleanliness (no backups, cache, artifacts)
- Mandatory documentation sections
- Standard markdown link format

**Implementation:**
- Built into all factory templates
- Enforced during generation
- Checked before ZIP creation

---

### 10. Generated Skills Portfolio

**Status:** ✅ 12+ Skills Generated

**What Exists:**
A collection of working, production-ready skills demonstrating factory effectiveness.

**Skills Generated:**
1. repo-summarizer - PROJECT.md portfolio generator
2. project-moc-generator - This MOC system
3. yoga-class-planner - Class planning
4. commit-helper - Git assistance
5. frontend-design - Design excellence
6. technical-decision - Decision analysis
7. goose-recipes - Recipe builder
8. goose-recipe-analysis - Recipe analysis
9. internal-comms - Communication templates
10. code-reviewer - Code review
11. spike-driven-dev - Development methodology
12. learn-project - Project learning

**Location:** [skills/](../../skills/)

---

## Features NOT Implemented (Explicitly Excluded)

### GitHub Issues Integration
**Status:** ❌ Not Included (By Design)

**Reason:** project-moc-generator focuses on codebase analysis, not issue tracking

**Mentioned In:** project-moc-generator special requirements

---

### Obsidian Wiki-Links
**Status:** ❌ Not Used

**Reason:** Standard markdown links `[text](path)` chosen for GitHub compatibility

**Alternative:** Standard markdown linking works everywhere

---

## Feature Summary

**Total Implemented Features:** 10 major features
**Factory System Components:** 5 specialized factories
**Generated Skills:** 12+
**Example Plugins:** 4
**Template Lines:** 5,175 total

**Success Metrics:**
- ✅ All factory templates operational
- ✅ All 6 guide agents functional
- ✅ 12+ successful skill generations
- ✅ 100% YAML validation compliance
- ✅ Complete portability achieved

---

**Related:**
- [Architecture](./architecture.md)
- [Components](./components.md)
- [Main MOC](./README.md)

---

**Last Updated:** 2025-11-20
**Generated By:** project-moc-generator skill
