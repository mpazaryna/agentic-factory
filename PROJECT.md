# Agentic Factory - Project Portfolio

## Elevator Pitch

Agentic Factory is a meta-generator factory system for Claude Code that enables developers to rapidly build custom Skills, Prompts, Agents, Commands, and Hooks through interactive guided workflows. Built entirely from markdown configurations and YAML frontmatter, it provides a portable, plugin-based development toolkit that transforms Claude Code into an extensible AI-powered development environment.

## Context & Problem

As Claude Code adoption grows, developers need ways to extend and customize its capabilities for their specific workflows and domains. However, creating properly structured Claude Code components requires understanding multiple formats (YAML frontmatter, markdown documentation, skill structures, agent configurations), following naming conventions, and maintaining consistency across files. This creates friction for developers who want to build custom tooling but don't want to manually maintain complex configuration files or remember intricate formatting rules.

Additionally, teams and individual developers often build similar patterns repeatedly, lacking a systematic way to capture, validate, and distribute custom Claude Code components. There was no unified approach to:
- Generate production-ready Claude Code components with proper validation
- Maintain consistency across Skills, Agents, Commands, and Hooks
- Package and distribute custom tooling across projects
- Guide users through component creation without requiring deep format knowledge

## Solution & Approach

Agentic Factory solves this through a meta-generator factory system built on three key principles:

**1. Guided Generation Over Manual Creation**
Rather than requiring developers to write YAML frontmatter and markdown manually, the toolkit uses interactive Q&A workflows (4-11 questions depending on component type) that gather requirements and automatically generate complete, validated output.

**2. Specialist Agent Architecture**
The system employs an orchestration pattern with six specialized agents:
- A factory-guide orchestrator that routes requests
- Five specialist agents (skills-guide, prompts-guide, agents-guide, commands-guide, hooks-guide)
- Each specialist uses comprehensive factory templates (857-1,152 lines) encoding best practices

**3. Portability and Self-Containment**
The entire factory system resides in a `.claude/` directory that can be copied to any project, instantly providing meta-generation capabilities. Plugin distribution through marketplace.json enables easy installation across multiple projects.

## Technical Implementation

### Architecture

The factory uses a three-layer architecture:

**Layer 1: Factory Orchestration**
- `/build` command serves as the entry point
- `factory-guide.md` orchestrator delegates to specialist agents
- Supports both guided mode (`/build`) and direct mode (`/build skill|prompt|agent|command|hook`)

**Layer 2: Specialist Agents**
Six specialized markdown-based agents in `.claude/agents/`:
- `factory-guide.md` - Main orchestrator (250 lines)
- `skills-guide.md` - Generates multi-file Skills with Python support
- `prompts-guide.md` - Creates mega-prompts from 69 presets across 15 domains
- `agents-guide.md` - Builds Claude Code agents with enhanced YAML frontmatter
- `commands-guide.md` - Generates slash commands with validation
- `hooks-guide.md` - Creates workflow automation hooks with safety checks

**Layer 3: Factory Templates**
Five comprehensive templates in `.claude/templates/` (5,175 total lines):
- `SKILLS_FACTORY_PROMPT.md` (1,012 lines) - Skill generation logic
- `PROMPTS_FACTORY_PROMPT.md` (1,152 lines) - Prompt generation with 69 presets
- `AGENTS_FACTORY_PROMPT.md` (1,123 lines) - Agent generation with YAML validation
- `MASTER_SLASH_COMMANDS_PROMPT.md` (1,031 lines) - Command generation following Anthropic patterns
- `HOOKS_FACTORY_PROMPT.md` (857 lines) - Hook generation with safety validation

### Technology Stack

**Core Technologies:**
- **Markdown** - Primary format for all configurations, documentation, and templates
- **YAML Frontmatter** - Metadata and configuration for Skills, Agents, and Commands
- **JSON** - Plugin configuration and marketplace distribution
- **Bash** - Command execution and file management

**Claude Code Integration:**
- Agent system with tools specification (Read, Grep, Write, Bash)
- Skill system with sample inputs/outputs
- Slash command system with description frontmatter
- Hook system for workflow automation

**Development Infrastructure:**
- Git for version control with conventional commits
- Plugin marketplace for distribution
- Local marketplace configuration for testing
- Workspace configuration for IDE integration

### Key Design Decisions

**1. Pure Markdown Configuration (No Code Execution)**

*Rationale:* Using markdown instead of executable code provides several advantages:
- No security concerns from running untrusted code
- Easy to read, edit, and version control
- Works across all platforms without runtime dependencies
- Claude natively understands markdown for processing instructions

This design choice makes the toolkit accessible to non-programmers while maintaining power and flexibility.

**2. Interactive Q&A Over Configuration Files**

*Rationale:* Rather than requiring users to write JSON or YAML config files, the toolkit uses conversational Q&A flows:
- Lower barrier to entry for new users
- Reduces syntax errors and validation issues
- Allows for context-aware follow-up questions
- Feels natural in Claude Code's conversational interface

The trade-off is less automation for power users, but this is mitigated by the direct mode (`/build skill`) that skips orchestration.

**3. Self-Contained .claude/ Directory**

*Rationale:* Making the factory system fully portable enables:
- Copy `.claude/` to any project for instant meta-generation
- No external dependencies or documentation directories
- Consistent tooling across all projects
- Easy distribution via git or file copy

This "toolkit in a folder" approach maximizes reusability and reduces cognitive load.

**4. Specialist Agent Delegation Pattern**

*Rationale:* Instead of a monolithic generator, the system delegates to specialists:
- Each agent focuses on one component type (Skills, Prompts, etc.)
- Easier to maintain and update individual specialists
- Can optimize each agent's model usage (factory-guide uses haiku for speed)
- Users can invoke specialists directly for faster workflows

The orchestrator adds a routing layer but provides valuable guidance for new users.

**5. Comprehensive Factory Templates**

*Rationale:* Using detailed templates (857-1,152 lines each) instead of code generation:
- Encodes best practices and quality standards
- Provides examples and anti-patterns
- Includes validation rules and formatting requirements
- Serves as documentation for maintainers

The templates are verbose but ensure high-quality, consistent output.

## Key Features

1. **Unified /build Command** - Single entry point for generating Skills, Prompts, Agents, Commands, or Hooks with intelligent routing to specialist agents

2. **Interactive Guided Workflows** - 4-11 question flows that gather requirements and automatically generate complete, validated components

3. **Five Specialist Generators** - Dedicated agents for Skills (multi-file), Prompts (69 presets), Agents (YAML frontmatter), Commands (slash syntax), and Hooks (workflow automation)

4. **Comprehensive Factory Templates** - 5,175 lines of generation logic encoding best practices, validation rules, and quality standards

5. **Portable .claude/ System** - Self-contained directory that can be copied to any project for instant meta-generation capabilities

6. **Plugin Distribution** - Marketplace-based installation system for easy deployment across multiple projects

7. **Automatic Validation** - Built-in format checking for YAML frontmatter, kebab-case naming, file structure, and mandatory sections

8. **File Cleanliness Standards** - Automatic cleanup of backup files, Python cache, and development artifacts to ensure professional output

9. **Production-Ready Output** - Generates complete packages with SKILL.md, README.md, HOW_TO_USE.md, sample data, and installation instructions

10. **12+ Pre-Generated Skills** - Working examples including repo-summarizer, yoga-class-planner, commit-helper, frontend-design, and more

## Outcomes & Metrics

**Productivity Improvements:**
- Reduced component creation time from hours to minutes (5-15 minute interactive sessions vs manual hours)
- Generated 12+ production-ready skills demonstrating factory effectiveness
- Single `/build` command replaces dozens of manual file operations

**Quality Consistency:**
- 100% of generated components include proper YAML frontmatter validation
- Automatic kebab-case naming enforcement across all skills
- Mandatory sections ensure complete documentation (README, HOW_TO_USE, samples)

**Reusability:**
- Portable `.claude/` directory enables instant deployment to new projects
- Plugin marketplace system allows one-time installation across all projects
- 5 comprehensive templates (5,175 lines) encode reusable generation patterns

**Developer Experience:**
- Interactive Q&A reduces cognitive load compared to remembering format specifications
- Direct mode (`/build skill`) provides power-user shortcuts
- Generated files include installation instructions and testing guidance

## Technical Challenges & Solutions

### Challenge 1: File Cleanliness and Output Quality

**Problem:** Initial factory implementations generated working components but left behind backup files (.backup, .bak), Python cache directories (__pycache__/), and internal documentation (SUMMARY.md) that polluted the skills/ directory. This created unprofessional deliverables and confused users about which files were intended for distribution.

**Solution:** Implemented mandatory cleanup protocol in factory templates:
- Added explicit "File Cleanliness Standards" section (44 lines) in SKILLS_FACTORY_PROMPT.md:671
- Defined deliverable file whitelist (SKILL.md, README.md, HOW_TO_USE.md, *.py, samples)
- Created blacklist for backup files, cache directories, and internal docs
- Required validation step before ZIP creation to verify only clean files exist
- Used Edit tool operations (automatic backup handling) instead of Write + manual backups

This ensures generated skills are professional and ready for immediate distribution.

### Challenge 2: YAML Frontmatter Validation and Consistency

**Problem:** Skills and Agents require properly formatted YAML frontmatter with specific fields (name in kebab-case, description, tools, model, etc.). Manual creation often resulted in syntax errors, incorrect casing, or missing required fields that broke Claude Code integration.

**Solution:** Built validation into factory templates at multiple checkpoints:
- Dedicated "YAML Frontmatter (MANDATORY)" section in each factory template (SKILLS_FACTORY_PROMPT.md:68-100)
- Explicit kebab-case requirements with correct/incorrect examples
- Automated validation that checks name format, description presence, and required fields
- Specialist agents verify YAML before finalizing output
- Templates include anti-patterns to prevent common mistakes

This reduced YAML errors to near-zero in generated components.

### Challenge 3: Portability Without External Dependencies

**Problem:** Initial design had factory templates in a separate `documentation/` directory, creating dependencies that broke when copying `.claude/` to new projects. Users couldn't use the factory system without also copying external files, reducing portability.

**Solution:** Made `.claude/` directory completely self-contained:
- Moved all factory templates into `.claude/templates/` (5 templates totaling 5,175 lines)
- Updated all factory guide agents to reference templates using relative paths (`.claude/templates/...`)
- Ensured no dependencies on external directories
- Documented portability in README.md:119-126 with copy-paste instructions

Now `cp -r .claude/ ~/new-project/` provides instant meta-generation capabilities.

### Challenge 4: Agent Orchestration and Delegation

**Problem:** Users needed different component types (Skills vs Prompts vs Agents) but didn't want to remember which specialist agent to invoke. Direct invocation created a steep learning curve while providing five separate entry points was confusing.

**Solution:** Implemented orchestrator pattern with dual-mode operation:
- Created `factory-guide.md` orchestrator that presents clear options (1-5 choices)
- Supported guided mode (`/build`) for new users with friendly Q&A
- Added direct mode (`/build skill|prompt|agent|command|hook`) for power users
- Orchestrator delegates to appropriate specialist based on user choice
- Used lightweight haiku model for orchestrator to minimize latency

This provides both discoverability for beginners and efficiency for experienced users.

### Challenge 5: Template Maintenance and Consistency

**Problem:** Five factory templates (5,175 total lines) needed to maintain consistent quality standards, formatting requirements, and validation rules. Manual updates were error-prone and could cause templates to drift from each other.

**Solution:** Established template governance structure:
- Created shared patterns across all templates (YAML frontmatter rules, file cleanliness standards)
- Used consistent section organization (Capabilities, Input Requirements, Output Format, etc.)
- Included example-driven documentation (correct/incorrect examples throughout)
- Documented template structure in CLAUDE.md for maintainability
- Leveraged toolkit-consistency-reviewer agent for validation

While templates remain verbose, they now share consistent patterns that make maintenance predictable.

## Learnings & Growth

**Skills Developed:**

1. **Agent-Based System Design** - Learned to architect multi-agent systems using orchestrators and specialists, balancing delegation patterns with direct invocation for different user skill levels

2. **Markdown-Driven Development** - Discovered the power of pure markdown configurations for creating extensible systems without code execution, enabling security and portability

3. **Template Engineering** - Built comprehensive generation templates (857-1,152 lines each) that encode domain knowledge, validation rules, and quality standards in a maintainable format

4. **YAML Configuration Management** - Developed deep understanding of frontmatter validation, kebab-case conventions, and metadata structures for Claude Code integration

5. **Plugin Distribution Systems** - Learned marketplace-based plugin architecture for distributing toolkits across multiple projects with version management

**Key Insights:**

1. **Interactive Q&A Beats Configuration Files** - Users strongly prefer conversational flows over writing JSON/YAML configs, even if it requires more questions upfront

2. **Portability Requires Ruthless Self-Containment** - Any external dependency breaks the "copy folder, get functionality" promise. Everything must live in `.claude/` directory.

3. **Validation Must Be Mandatory, Not Optional** - File cleanliness and YAML validation can't be suggestions; they must be enforced steps in the generation workflow

4. **Examples > Documentation** - Including correct/incorrect examples in templates proved far more effective than prose explanations of formatting rules

5. **Specialist Delegation Scales Better Than Monoliths** - Breaking generation into five specialist agents simplified maintenance compared to a single monolithic generator

**Process Improvements:**

- Established "File Cleanliness Standards" as a mandatory phase before any ZIP creation
- Created dual-mode operation (guided vs direct) to serve both beginner and power users
- Implemented relative path references throughout to maintain portability
- Used consistent template structure across all five factory templates for predictability

## Future Enhancements

**Short Term:**

1. **Template Versioning** - Add version numbers to factory templates to enable migration paths when formats evolve

2. ~~**Output Validation Command**~~ - **DONE**: `/validate skill|agent|command|curated-prompt <path>` command and `component-validator` agent

3. **Factory Status Dashboard** - Implement `/factory-status` command showing history of generated components with timestamps and locations

4. **Installation Helpers** - Build `/install-skill` and `/install-hook` commands to automate moving generated output to correct directories

5. **Test Automation** - Add `/test-factory skill-name` command that validates generated components work correctly

**Medium Term:**

6. **Multi-Format Export** - Support generating Skills in different output formats (ZIP, tar.gz, npm package) based on distribution needs

7. **Preset Library Expansion** - Grow prompts-guide from 69 presets to 100+ covering more specialized domains

8. **Template Customization** - Allow users to create custom factory templates for organization-specific patterns

9. **Batch Generation** - Support generating multiple related components in one session (e.g., "build agent + command + hook for code review workflow")

10. **Quality Metrics** - Track generated component usage and iterate on factory templates based on success patterns

**Long Term:**

11. **Community Marketplace** - Enable sharing generated Skills and Agents through a community repository

12. **AI-Assisted Template Evolution** - Use Claude to analyze successful generated components and suggest factory template improvements

13. **Cross-Project Sync** - Build system to sync updated factory templates across all projects using the toolkit

14. **Domain-Specific Factories** - Create specialized factories for common domains (FinTech, Healthcare, E-commerce) with pre-configured validations

15. **Visual Factory Builder** - Develop UI for building factory templates through drag-and-drop instead of markdown editing

## Project Links

- **Repository:** https://github.com/mpazaryna/agentic-factory
- **Local Directory:** `/Users/mpaz/workspace/agentic-factory`
- **Key Files:**
  - Factory orchestrator: `.claude/agents/factory-guide.md`
  - Build command: `.claude/commands/build.md`
  - Skills template: `.claude/templates/SKILLS_FACTORY_PROMPT.md`
  - README: `README.md`
  - Project instructions: `CLAUDE.md`

- **Generated Examples:**
  - Repo Summarizer: `skills/repo-summarizer/`
  - Frontend Design: `skills/frontend-design/`
  - Commit Helper: `skills/commit-helper/`

## Tags

`claude-code` `ai-agents` `meta-generator` `factory-system` `markdown` `yaml` `plugin-system` `developer-tools` `code-generation` `interactive-cli` `skill-builder` `agent-orchestration` `portable-toolkit` `no-code` `prompt-engineering` `workflow-automation` `slash-commands` `hooks` `marketplace` `devtools`

## Portfolio Use Cases

### For Recruiters (30 seconds)

**What it does:** Meta-generator factory that creates custom AI components for Claude Code through interactive Q&A

**Key achievement:** Reduced component creation from hours to minutes; generated 12+ production-ready skills

**Technologies:** Markdown, YAML, agent orchestration, plugin systems

**Impact:** Portable toolkit enables rapid development of AI-powered development environments

### For Technical Interviews (2 minutes)

**System Design Question:** "How would you build an extensible plugin system for an AI coding assistant?"

**Answer:** Agentic Factory demonstrates a three-layer architecture:
1. Orchestration layer with `/build` command routing to specialist agents
2. Specialist agents (5) for different component types with interactive Q&A
3. Factory templates (5,175 lines) encoding generation logic and validation

**Key decisions:**
- Pure markdown (no code execution) for security and portability
- Q&A over config files for lower barrier to entry
- Self-contained `.claude/` directory for instant deployment
- Validation as mandatory steps, not optional checks

**Challenges solved:**
- File cleanliness with automatic cleanup protocols
- YAML validation through comprehensive templates
- Portability via relative path references
- Scalable maintenance through specialist delegation

### For Portfolio Website (1 paragraph)

Agentic Factory is a meta-generator factory system that enables developers to rapidly build custom Skills, Prompts, Agents, Commands, and Hooks for Claude Code through interactive guided workflows. Built entirely from markdown configurations and YAML frontmatter, it employs a specialist agent architecture where five dedicated generators create production-ready components with automatic validation and file cleanliness standards. The portable `.claude/` directory design allows instant deployment to any project, while the plugin marketplace system enables easy distribution across multiple projects. Key technical achievements include reducing component creation time from hours to 5-15 minutes, generating 12+ production-ready skills, and maintaining 100% YAML validation through comprehensive factory templates totaling 5,175 lines of generation logic.

### For Resume Bullet Points

- **Built meta-generator factory system** for Claude Code that reduced custom component creation time from hours to 5-15 minute interactive sessions through automated Q&A workflows

- **Architected specialist agent system** with orchestration pattern delegating to 5 specialized generators, each using comprehensive templates (857-1,152 lines) encoding validation rules and quality standards

- **Designed portable .claude/ directory** enabling instant meta-generation deployment across projects with zero external dependencies through self-contained template architecture

- **Implemented automatic validation** for YAML frontmatter, kebab-case naming, and file structure ensuring 100% of generated components meet production quality standards

- **Created plugin distribution system** with marketplace-based installation enabling one-time deployment across multiple projects, demonstrated through 12+ generated production-ready skills

### For Technical Blog Post

**Title:** "Building a Meta-Generator: How I Created a Factory System for Claude Code Components"

**Hook:** What if you could build complex AI development tools just by answering 5-7 questions? Agentic Factory demonstrates how markdown-based agent orchestration can replace traditional code generation frameworks.

**Key sections:**
1. **The Problem:** Creating Claude Code components requires intricate YAML, format knowledge, and consistency
2. **The Solution:** Three-layer architecture (orchestration, specialists, templates) with interactive Q&A
3. **Design Decisions:** Why markdown over code, Q&A over config files, portability through self-containment
4. **Challenges:** File cleanliness, YAML validation, template maintenance at scale
5. **Results:** 12+ generated skills, minutes vs hours creation time, portable across all projects

**Technical depth:** Agent delegation patterns, template engineering at 5,175 lines, validation checkpoints, relative path management for portability

**Call to action:** Fork the repo, copy `.claude/` to your project, run `/build` and generate your first custom skill
