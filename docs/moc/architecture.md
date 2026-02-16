---
title: Architecture Overview
type: moc
generated: 2025-11-20
last_updated: 2025-11-20
project: claude-toolkit
status: current
---

# Architecture Overview

This document describes the technical architecture of the Claude Toolkit meta-generator factory system.

## System Architecture

### Three-Layer Design

The toolkit employs a three-layer architecture for component generation:

```
┌─────────────────────────────────────────┐
│   Layer 1: Orchestration               │
│   /build command + factory-guide        │
│   (Routes requests to specialists)      │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│   Layer 2: Specialist Agents           │
│   6 dedicated guide agents              │
│   (Skills, Prompts, Agents, etc.)      │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│   Layer 3: Factory Templates           │
│   5 comprehensive templates             │
│   (5,175 lines of generation logic)    │
└─────────────────────────────────────────┘
```

---

## Layer 1: Orchestration

**Components:**
- `/build` command ([.claude/commands/build.md](../../.claude/commands/build.md))
- factory-guide agent ([.claude/agents/factory-guide.md](../../.claude/agents/factory-guide.md))

**Responsibilities:**
- Provide unified entry point
- Parse user intent (skill, prompt, agent, command, hook)
- Delegate to appropriate specialist
- Support dual-mode operation (guided vs direct)

**Design Pattern:** Orchestrator with specialist delegation

**Implementation:**
```markdown
/build           → factory-guide → specialist selection
/build skill     → skills-guide (direct)
/build prompt    → prompts-guide (direct)
/build agent     → agents-guide (direct)
/build command   → commands-guide (direct)
/build hook      → hooks-guide (direct)
```

---

## Layer 2: Specialist Agents

**Six Specialized Agents:**

1. **factory-guide** (250 lines)
   - Role: Main orchestrator
   - Model: haiku (for speed)
   - Tools: Read, Grep
   - [Source](../../.claude/agents/factory-guide.md)

2. **skills-guide** (8,496 lines)
   - Role: Build multi-file Skills
   - Uses: SKILLS_FACTORY_PROMPT template
   - [Source](../../.claude/agents/skills-guilde.md)

3. **prompts-guide** (9,288 lines)
   - Role: Generate mega-prompts
   - Uses: PROMPTS_FACTORY_PROMPT template
   - [Source](../../.claude/agents/prompts-guide.md)

4. **agents-guide** (10,293 lines)
   - Role: Create Claude Code agents
   - Uses: AGENTS_FACTORY_PROMPT template
   - [Source](../../.claude/agents/agents-guide.md)

5. **commands-guide** (12,189 lines)
   - Role: Build slash commands
   - Uses: MASTER_SLASH_COMMANDS_PROMPT template
   - [Source](../../.claude/agents/commands-guide.md)

6. **hooks-guide** (9,544 lines)
   - Role: Generate workflow hooks
   - Uses: HOOKS_FACTORY_PROMPT template
   - [Source](../../.claude/agents/hooks-guide.md)

**Design Pattern:** Specialist with template delegation

---

## Layer 3: Factory Templates

**Five Comprehensive Templates:**

| Template | Lines | Purpose | Location |
|----------|-------|---------|----------|
| SKILLS_FACTORY_PROMPT | 1,012 | Skill generation logic | [.claude/templates/](../../.claude/templates/SKILLS_FACTORY_PROMPT.md) |
| PROMPTS_FACTORY_PROMPT | 1,152 | Prompt generation | [.claude/templates/](../../.claude/templates/PROMPTS_FACTORY_PROMPT.md) |
| AGENTS_FACTORY_PROMPT | 1,123 | Agent generation | [.claude/templates/](../../.claude/templates/AGENTS_FACTORY_PROMPT.md) |
| MASTER_SLASH_COMMANDS_PROMPT | 1,031 | Command generation | [.claude/templates/](../../.claude/templates/MASTER_SLASH_COMMANDS_PROMPT.md) |
| HOOKS_FACTORY_PROMPT | 857 | Hook generation | [.claude/templates/](../../.claude/templates/HOOKS_FACTORY_PROMPT.md) |

**Total:** 5,175 lines of generation logic

**Template Structure:**
- Understanding section (what the component is)
- Critical formatting rules
- Validation requirements
- File cleanliness standards
- Methodology and best practices
- Examples (correct and incorrect)

---

## Key Architectural Decisions

### 1. Pure Markdown Configuration (No Code Execution)

**Decision:** Use markdown files instead of executable code

**Rationale:**
- No security concerns from untrusted code
- Easy to read, edit, and version control
- Works across all platforms without runtime dependencies
- Claude natively understands markdown

**Trade-offs:**
- Less powerful than code generation
- Requires verbose templates
- Manual parsing by Claude

**Implementation:**
- All agents are markdown files
- All templates are markdown files
- All commands are markdown files
- YAML frontmatter for metadata

---

### 2. Interactive Q&A Over Configuration Files

**Decision:** Use conversational Q&A flows instead of JSON/YAML config

**Rationale:**
- Lower barrier to entry for new users
- Reduces syntax errors and validation issues
- Allows context-aware follow-up questions
- Natural in Claude Code's interface

**Trade-offs:**
- Less automation for power users
- Requires more interaction
- Harder to batch process

**Mitigation:**
- Direct mode (`/build skill`) for power users
- 4-11 questions (reasonable length)
- Clear, focused questions

**Implementation:**
- Specialist agents ask 4-11 questions
- Questions tailored to component type
- Answers used to generate output

---

### 3. Self-Contained .claude/ Directory

**Decision:** All factory system files live in `.claude/` with no external dependencies

**Rationale:**
- Instant portability (`cp -r .claude/ ~/project/`)
- No broken references when copying
- Consistent tooling across all projects
- Easy to distribute

**Trade-offs:**
- Duplicate content across projects
- Harder to centralize updates
- Larger per-project footprint

**Mitigation:**
- Plugin marketplace for centralized distribution
- Relative path references throughout
- Self-update capability (future)

**Implementation:**
- All templates in `.claude/templates/`
- All agents in `.claude/agents/`
- All commands in `.claude/commands/`
- All skills in `.claude/skills/`
- No references to `../` outside `.claude/`

---

### 4. Specialist Delegation Pattern

**Decision:** Use multiple specialist agents instead of one monolithic generator

**Rationale:**
- Each agent focuses on one component type
- Easier to maintain and update
- Can optimize each agent's model usage
- Users can invoke specialists directly

**Trade-offs:**
- More files to maintain
- Orchestrator adds complexity
- Potential duplication across specialists

**Mitigation:**
- Shared patterns across templates
- factory-guide provides routing
- Direct mode for experienced users

**Implementation:**
- factory-guide orchestrates
- 5 specialists (skills, prompts, agents, commands, hooks)
- Each specialist uses one template
- Clear separation of concerns

---

### 5. Comprehensive Factory Templates

**Decision:** Use detailed 857-1,152 line templates instead of compact code

**Rationale:**
- Encode best practices and quality standards
- Provide examples and anti-patterns
- Include validation rules and formatting
- Serve as documentation for maintainers

**Trade-offs:**
- Verbose (5,175 total lines)
- Harder to parse for Claude
- Requires more context window

**Mitigation:**
- Clear structure with sections
- Examples throughout
- Validation checkpoints

**Implementation:**
- Each template is self-contained
- Consistent structure across all 5
- Mandatory sections (formatting, cleanliness, validation)

---

## Technology Stack

### Core Technologies

**Markdown:**
- Primary format for all configurations
- GitHub-flavored markdown
- CommonMark specification
- Standard linking `[text](path)`

**YAML Frontmatter:**
- Metadata for Skills, Agents, Commands
- Kebab-case naming enforcement
- Required fields validation
- Examples: `name`, `description`, `tools`, `model`

**JSON:**
- Plugin configuration (marketplace.json)
- Sample data for skills
- Configuration files

**Bash:**
- Command execution
- File management
- Git operations
- No complex scripting

### Claude Code Integration

**Agent System:**
- YAML frontmatter with `name`, `description`, `tools`, `model`, `color`, `field`, `expertise`
- Markdown-based instructions
- Tool specification (Read, Grep, Write, Bash)

**Skill System:**
- SKILL.md with YAML frontmatter
- Optional Python modules
- Sample inputs/outputs (JSON)
- Usage documentation

**Slash Command System:**
- YAML frontmatter with `description`
- Markdown-based instructions
- Bash permissions

**Hook System:**
- hook.json configuration
- Event-based triggers
- Safety validation

---

## Data Flow

### Skill Generation Flow

```
User → /build skill
     ↓
factory-guide (if used) or direct
     ↓
skills-guide agent
     ↓
Ask 4-5 questions
     ↓
Read SKILLS_FACTORY_PROMPT template
     ↓
Generate SKILL.md + README.md + HOW_TO_USE.md + samples
     ↓
Validate YAML frontmatter
     ↓
Check file cleanliness
     ↓
Create ZIP package
     ↓
Output to skills/[skill-name]/
```

---

## Portability Design

### Self-Containment Strategy

**Goal:** Copy `.claude/` directory to any project for instant meta-generation

**Implementation:**
1. All factory templates in `.claude/templates/`
2. All guide agents reference templates using relative paths
3. No dependencies on external `documentation/` or other directories
4. All resources bundled in `.claude/`

**Verification:**
```bash
cp -r .claude/ ~/new-project/
cd ~/new-project
# /build works immediately, no setup needed
```

---

## Validation Architecture

### YAML Frontmatter Validation

**Enforcement Points:**
1. Template includes validation rules
2. Specialist agent checks format before finalizing
3. Mandatory validation section in templates

**Validation Rules:**
- Name must be kebab-case
- Description must be present and concise
- Required fields for each component type
- No syntax errors in YAML

### File Cleanliness Standards

**Enforcement Points:**
1. Template defines deliverable whitelist
2. Template defines artifact blacklist
3. Mandatory cleanup before ZIP creation

**Deliverables:**
- SKILL.md, README.md, HOW_TO_USE.md
- Python files (if needed)
- Sample data
- Configuration examples

**Artifacts (Removed):**
- Backup files (.backup, .bak)
- Python cache (__pycache__/)
- Internal summaries
- Development artifacts

---

## Related Documentation

- [Components](./components.md) - Component details
- [Features](./features.md) - Feature catalog
- [Main MOC](./README.md) - Entry point

---

**Last Updated:** 2025-11-20
**Generated By:** project-moc-generator skill
