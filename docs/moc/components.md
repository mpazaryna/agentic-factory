---
title: Components Catalog
type: moc
generated: 2025-11-20
last_updated: 2025-11-20
project: claude-toolkit
status: current
---

# Components Catalog

This document catalogs all components in the Claude Toolkit system, organized by type and function.

## Factory System Components

### Orchestration Components

#### /build Command
- **Location:** [.claude/commands/build.md](../../.claude/commands/build.md)
- **Type:** Slash command
- **Lines:** 251
- **Purpose:** Unified entry point for all factory operations
- **Modes:** Guided (`/build`) and Direct (`/build skill|prompt|agent|command|hook`)
- **Delegates to:** factory-guide agent or specialist directly

#### factory-guide Agent
- **Location:** [.claude/agents/factory-guide.md](../../.claude/agents/factory-guide.md)
- **Type:** Orchestrator agent
- **Lines:** 250
- **Model:** haiku (for speed)
- **Tools:** Read, Grep
- **Purpose:** Route user requests to appropriate specialist
- **Delegates to:** One of 5 specialist agents

---

### Specialist Agent Components

#### skills-guide Agent
- **Location:** [.claude/agents/skills-guilde.md](../../.claude/agents/skills-guilde.md)
- **Lines:** 8,496
- **Purpose:** Build multi-file Claude Skills
- **Questions:** 4-5
- **Uses Template:** SKILLS_FACTORY_PROMPT.md
- **Output:** SKILL.md + README.md + HOW_TO_USE.md + samples + ZIP
- **Generated Count:** 12+ skills

**Key Responsibilities:**
- Ask domain, use cases, Python/prompts choice, special requirements
- Validate YAML frontmatter (kebab-case, required fields)
- Enforce file cleanliness standards
- Generate complete skill package
- Create ZIP for distribution

#### prompts-guide Agent
- **Location:** [.claude/agents/prompts-guide.md](../../.claude/agents/prompts-guide.md)
- **Lines:** 9,288
- **Purpose:** Generate mega-prompts for any LLM
- **Uses Template:** PROMPTS_FACTORY_PROMPT.md
- **Presets:** 69 across 15 domains
- **Output Formats:** XML, Claude, ChatGPT, Gemini

#### agents-guide Agent
- **Location:** [.claude/agents/agents-guide.md](../../.claude/agents/agents-guide.md)
- **Lines:** 10,293
- **Purpose:** Create Claude Code agents with enhanced YAML
- **Questions:** 5-6
- **Uses Template:** AGENTS_FACTORY_PROMPT.md
- **Output:** Agent .md file with YAML frontmatter

#### commands-guide Agent
- **Location:** [.claude/agents/commands-guide.md](../../.claude/agents/commands-guide.md)
- **Lines:** 12,189
- **Purpose:** Build Claude slash commands
- **Questions:** 4-6
- **Uses Template:** MASTER_SLASH_COMMANDS_PROMPT.md
- **Patterns:** Simple, Multi-Phase, Agent-Style
- **Output:** Command .md file with YAML frontmatter

#### hooks-guide Agent
- **Location:** [.claude/agents/hooks-guide.md](../../.claude/agents/hooks-guide.md)
- **Lines:** 9,544
- **Purpose:** Generate Claude Code hooks
- **Questions:** 5-7
- **Uses Template:** HOOKS_FACTORY_PROMPT.md
- **Output:** hook.json + README.md

---

### Factory Template Components

#### SKILLS_FACTORY_PROMPT Template
- **Location:** [.claude/templates/SKILLS_FACTORY_PROMPT.md](../../.claude/templates/SKILLS_FACTORY_PROMPT.md)
- **Lines:** 1,012
- **Purpose:** Complete skill generation logic and rules
- **Used by:** skills-guide agent

**Sections:**
- Understanding Claude Skills
- Critical Formatting Rules (YAML, naming, cleanliness)
- File structure requirements
- Validation checkpoints
- Examples (correct/incorrect)
- Best practices
- Quality standards

#### PROMPTS_FACTORY_PROMPT Template
- **Location:** [.claude/templates/PROMPTS_FACTORY_PROMPT.md](../../.claude/templates/PROMPTS_FACTORY_PROMPT.md)
- **Lines:** 1,152
- **Purpose:** Mega-prompt generation with 69 presets

#### AGENTS_FACTORY_PROMPT Template
- **Location:** [.claude/templates/AGENTS_FACTORY_PROMPT.md](../../.claude/templates/AGENTS_FACTORY_PROMPT.md)
- **Lines:** 1,123
- **Purpose:** Agent generation with enhanced YAML

#### MASTER_SLASH_COMMANDS_PROMPT Template
- **Location:** [.claude/templates/MASTER_SLASH_COMMANDS_PROMPT.md](../../.claude/templates/MASTER_SLASH_COMMANDS_PROMPT.md)
- **Lines:** 1,031
- **Purpose:** Slash command generation following Anthropic patterns

#### HOOKS_FACTORY_PROMPT Template
- **Location:** [.claude/templates/HOOKS_FACTORY_PROMPT.md](../../.claude/templates/HOOKS_FACTORY_PROMPT.md)
- **Lines:** 857
- **Purpose:** Hook generation with safety validation

---

## Generated Skills (Output Components)

### Production Skills

**repo-summarizer**
- **Location:** [skills/repo-summarizer/](../../skills/repo-summarizer/)
- **Generated:** 2025-11-19
- **Purpose:** Analyzes repositories and generates PROJECT.md portfolio documents

**project-moc-generator**
- **Location:** [skills/project-moc-generator/](../../skills/project-moc-generator/)
- **Generated:** 2025-11-20
- **Purpose:** Generates Map of Content documentation for software projects
- **Current Test:** Running on claude-toolkit (this documentation!)

**Other Skills:**
- yoga-class-planner - Plans yoga class sequences
- commit-helper - Git commit assistance
- frontend-design - Frontend design excellence
- technical-decision - Decision analysis
- goose-recipes - Recipe builder
- goose-recipe-analysis - Recipe analysis
- internal-comms - Communication templates
- code-reviewer - Code quality review
- spike-driven-dev - Development methodology
- learn-project - Project learning

**Total:** 12+ skills successfully generated

---

## Plugin Components

### Example Plugins

**hello-world Plugin**
- **Location:** [plugins/hello-world/](../../plugins/hello-world/)
- **Version:** 1.0.0
- **Category:** example
- **Purpose:** Demonstrate basic slash commands

**git-start-new Plugin**
- **Location:** [plugins/git-start-new/](../../plugins/git-start-new/)
- **Version:** 1.0.0
- **Purpose:** Start new feature workflow

**decide-technical Plugin**
- **Location:** [plugins/decide-technical/](../../plugins/decide-technical/)
- **Version:** 1.0.0
- **Purpose:** Explore technical options

**research-task Plugin**
- **Location:** [plugins/research-task/](../../plugins/research-task/)
- **Version:** 1.0.0
- **Purpose:** Research particular tasks or concepts

---

## Command Components

### Git Commands

**git:commit** - Stage and create conventional commits
**git:push** - Stage, commit, and push with governance
**git:issue** - Fetch GitHub issue details

### Other Commands

**research/task** - Research particular tasks
**tools/playwright** - Playwright testing guidance
**prime/mcp_dev** - Understanding MCP server codebases
**prime/web_dev** - Understanding web development projects

---

## Configuration Components

### Plugin Marketplace Configuration
- **Location:** [.claude-plugin/marketplace.json](../../.claude-plugin/marketplace.json)
- **Purpose:** Local marketplace configuration for testing
- **Defines:** 4 plugins with metadata, versions, keywords

### Claude Settings
- **Location:** [.claude/settings.local.json](../../.claude/settings.local.json)
- **Purpose:** Local Claude Code settings

---

## Documentation Components

### Core Documentation

**README.md** - Project overview and installation
**CLAUDE.md** - Claude Code instructions
**PROJECT.md** - Portfolio documentation (398 lines)
**CHANGELOG.md** - Project change history

### Existing Docs Folder

**installation.md** - Setup and deployment guide
**components.md** - Overview of agents, commands, templates
**usage.md** - How to use the toolkit
**maintenance.md** - Meta-tooling and inspiration

### Generated MOC Documentation

**docs/moc/README.md** - Main map of content entry point
**docs/moc/features.md** - Feature catalog
**docs/moc/architecture.md** - Architecture documentation
**docs/moc/components.md** - This document

---

## Component Statistics

**Factory System:**
- Orchestration components: 2 (build command + factory-guide)
- Specialist agents: 5
- Factory templates: 5 (5,175 total lines)

**Generated Outputs:**
- Skills: 12+
- Plugins: 4
- Commands: 10+

**Documentation:**
- Core docs: 4 (README, CLAUDE, PROJECT, CHANGELOG)
- Docs folder: 4 existing + 4 MOC files
- Total markdown files: 50+

**Codebase Size:**
- .claude/ directory: 320K
- skills/: 548K
- commands/: 16K
- .claude-plugin/: 4K

---

## Component Dependencies

```
/build command
    ↓
factory-guide agent
    ↓
Specialist agents (one of 5)
    ↓
Factory templates (one of 5)
    ↓
Generated outputs (skills, prompts, agents, commands, hooks)
```

**No External Dependencies:**
- All components self-contained in `.claude/`
- Relative path references throughout
- Portable across projects

---

## Related Documentation

- [Features](./features.md) - What components do
- [Architecture](./architecture.md) - How components work together
- [Main MOC](./README.md) - Entry point

---

**Last Updated:** 2025-11-20
**Generated By:** project-moc-generator skill
