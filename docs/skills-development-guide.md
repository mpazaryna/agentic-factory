---
title: Claude Code Skills Development Guide
description: Comprehensive reference for building efficient Claude Code skills using Progressive Disclosure Architecture (PDA)
source: Rick Hightower / Spillwave Solutions
---

# Claude Code Skills Development Guide

## What Are Skills

Skills are custom extensions that teach Claude domain-specific expertise beyond built-in tools. They activate on-demand when needed, injecting specialized instructions into Claude's context.

**Skills can:**
- Generate specialized content (diagrams, reports, documentation)
- Integrate with external services (Notion, Confluence, Jira)
- Automate multi-step workflows
- Provide domain expertise (company processes, internal tools)
- Extend capabilities (custom file formats, proprietary APIs)

## Skill Structure

### Minimum Requirements

```
skill-name/
└── SKILL.md    # Required - must match folder name
```

### Full PDA Structure

```
skill-name/
├── SKILL.md           # Core logic only (1,500-2,000 words target)
├── references/        # Detailed docs loaded on-demand
├── scripts/           # Executable code (not loaded into context)
└── assets/            # Templates, images for output
```

### Required YAML Frontmatter

```yaml
---
name: skill-name      # hyphen-case, lowercase alphanumeric + hyphens only
description: |        # What it does and WHEN Claude should use it
  This skill should be used when...
---
```

### Optional Frontmatter Fields

```yaml
license: MIT
allowed-tools: Read, Grep, Glob  # Pre-approved tools
metadata:
  custom-key: value
```

### Validation Rules

1. SKILL.md must exist
2. Must start with `---` (YAML frontmatter)
3. Must have valid frontmatter format (closed with `---`)
4. Must contain `name:` field
5. Must contain `description:` field
6. Name must be hyphen-case: `^[a-z0-9-]+$`
7. Name cannot start/end with hyphen or have consecutive hyphens
8. Description cannot contain angle brackets (`<` or `>`)

---

## Core Skill Patterns

Three patterns cover 90% of use cases:

### Pattern 1: Generator Skills

Create content from user descriptions.

```markdown
# [Type] Generator Skill

**Purpose:** Generate [content type] from user requirements

**Process:**
1. Analyze user requirements and goals
2. Generate [content type] using domain best practices
3. Validate output for correctness and quality
4. Present to user with refinement options
```

**Examples:** Diagram generators, report generators, code scaffolding

### Pattern 2: Integrator Skills

Connect to external services.

```markdown
# [Service] Integration Skill

**Purpose:** Integrate with [external service]

**Process:**
1. Understand user's goal and requirements
2. Prepare data in format required by [service]
3. Call [tool/script/API] to perform action
4. Handle response (success, errors, warnings)
5. Report results to user with actionable details
```

**Examples:** Notion uploader, Confluence publisher, Jira ticket creator

### Pattern 3: Converter Skills

Transform content between formats.

```markdown
# [Format A] to [Format B] Converter

**Purpose:** Convert content between formats

**Process:**
1. Read source file
2. Parse [Format A] structure
3. Transform to [Format B] structure
4. Write output file
5. Verify conversion accuracy and completeness
```

**Examples:** Markdown to PDF, Jupyter to Python, DOCX to Markdown

---

## Progressive Disclosure Architecture (PDA)

### The Problem

Traditional skills load everything upfront. A 50KB skill loads all documentation every time, even when only 5KB is needed. This causes:
- Token waste (80-90% unused context)
- Slower responses
- Higher costs
- Maintenance difficulty
- Context pollution

### The Solution

**"A skill should be an orchestrator, not an encyclopedia."**

PDA separates concerns into four roles:
1. **Skill prompt** (orchestrator): Contains routing logic
2. **Reference files** (library): Detailed documentation, loaded on-demand
3. **Scripts** (workers): Handle mechanical work like API calls
4. **AI reasoning** (intelligence): Error handling, adaptation, UX

### When to Use PDA

**Apply PDA when skill:**
- Has >10KB of reference documentation
- Supports multiple distinct use cases
- Integrates with external APIs or complex tools
- Requires mechanical processing
- Will grow over time

**Stay basic when skill:**
- Total size <5KB
- All information always needed
- Simple workflow
- Stable and focused

### PDA Decision Checklist

```
□ Skill has >10KB documentation
□ Multiple use cases need different documentation
□ External API integration required
□ Complex processing needed
□ Skill will grow and evolve over time

If 2+ checked → Use PDA
If 0-1 checked → Basic skill is fine
```

---

## Technique 1: Reference Files & Lazy Loading

### Structure

```
.claude/skills/
├── plantuml.md (3KB - routing logic only)
└── reference/
    ├── sequence_diagrams.md (8KB - loaded when needed)
    ├── class_diagrams.md (10KB - loaded when needed)
    └── flowcharts.md (5KB - loaded when needed)
```

### Skill Router Example

```markdown
# PlantUML Skill

Generate PlantUML diagrams from descriptions and render to PNG.

**Supported Diagram Types:**
- Sequence diagrams (interactions over time)
- Class diagrams (object-oriented structure)
- ER diagrams (entity relationships)
- Flowcharts (process flows)

**Process:**
1. **Analyze Request** - Identify diagram type from user description
2. **Load Reference**
   - Sequence diagrams → Read reference/sequence_diagrams.md
   - Class diagrams → Read reference/class_diagrams.md
   - ER diagrams → Read reference/er_diagrams.md
   - Flowcharts → Read reference/flowcharts.md
3. **Generate Code** - Use loaded syntax to create PlantUML code
4. **Render Diagram** - Execute: `plantuml -tpng diagram.puml`
```

### Organization Strategies

**By Use Case** (recommended):
```
reference/
├── sequence_diagrams.md
├── class_diagrams.md
└── flowcharts.md
```

**By Complexity Level** (educational):
```
reference/
├── basic_syntax.md
├── intermediate_patterns.md
└── advanced_features.md
```

**By Feature Area** (complex tools):
```
reference/
├── participants.md
├── messages.md
├── control_flow.md
└── styling.md
```

### Conditional Loading Patterns

**Simple Switch:**
```markdown
- If "sequence" mentioned → Read reference/sequence.md
- If "class" mentioned → Read reference/class.md
- If "flow" mentioned → Read reference/flowcharts.md
```

**Progressive Loading:**
```markdown
**Initial:** Read reference/basic_syntax.md
**If advanced features needed:** Read reference/advanced_features.md
**If custom styling requested:** Read reference/styling.md
```

### Token Savings Example

Traditional: 50KB loaded every time
PDA: 3KB core + 8KB reference = 11KB
**Savings: 78%**

---

## Technique 2: Scripts for Mechanical Work

### The Principle

Scripts handle mechanical operations (API calls, data processing). AI provides intelligence and user experience. This achieves zero token cost for implementation details.

### Script Design Patterns

**Single Responsibility:**
```
scripts/
├── upload_notion.py      # Upload markdown to Notion
├── download_notion.py    # Download Notion page
├── search_notion.py      # Search workspace
└── create_database.py    # Create new database
```

**Clear Input/Output Contract:**
```python
"""
Input:
    sys.argv[1]: file_path (string)
    sys.argv[2]: database_id (string)
    env: NOTION_TOKEN (string)
Output:
    stdout: "SUCCESS: <url>" or "ERROR: <code> - <message>"
    exit code: 0 (success) or 1 (error)
"""
```

**Structured Error Messages:**
```python
# Good - AI can parse and handle
print("ERROR: 404 - Database not found: abc123")
print("ERROR: 401 - Authentication failed")
print("ERROR: Network timeout")

# Bad - AI can't distinguish error types
print("Something went wrong")
```

**Environment-Based Configuration:**
```python
# Good
api_token = os.environ.get("NOTION_TOKEN")

# Bad - security risk
api_token = "secret_abc123"
```

### Skill Prompt Example

```markdown
# Notion Uploader Skill

**Process:**
1. **Identify Target File** - Find relevant .md file
2. **Identify Target Database** - Get database ID or search
3. **Upload File**
   - Execute: `python3 scripts/upload_notion.py <file_path> <database_id>`
4. **Interpret Results**
   - `SUCCESS: <page_url>` → Report success with URL
   - `ERROR: 404` → Database not found, search for alternatives
   - `ERROR: 401` → Guide user through token setup
   - `ERROR: Network timeout` → Offer retry options
```

---

## Technique 3: AI Resilience Layer

### The Principle

Traditional scripts fail hard and stop. The AI layer transforms failures into opportunities for guidance and recovery.

### Error Recovery Flow

```
Script Error → AI Interprets → Recovery Strategy → User Guidance or Auto-Fix
```

Every error path leads to either user guidance or automated recovery. No dead ends.

### Error Handling in Skill Prompts

```markdown
**Error Interpretation:**

If error contains "404" or "not found":
  - Resource doesn't exist
  - Use search tool to find valid resources
  - Present options to user
  - Retry with correct resource

If error contains "401" or "unauthorized":
  - Authentication failed
  - Provide step-by-step credential setup guide
  - Wait for user to configure

If error contains "Network" or "timeout":
  - Connection issue (likely transient)
  - Offer immediate retry or delayed retry
  - Track retry attempts (max 3)

If error contains "409" or "conflict":
  - Resource conflict
  - Present resolution options (update, rename, append)
  - Execute chosen resolution

If error is unrecognized:
  - Show full error message
  - Guide user to script documentation
```

### AI Resilience Patterns

**Retry with Correction:**
1. Interpret specific error
2. Identify if correctable
3. Apply correction or guide user
4. Retry automatically
5. Report result

**Graceful Degradation:**
1. Recognize script isn't working
2. Explain what script would have done
3. Offer manual alternative workflow
4. Guide through manual process

**Progressive Disclosure:**
1. Initial attempt: Simple, optimistic path
2. First failure: Try automatic recovery
3. Second failure: Try alternative approach
4. Third failure: Detailed debugging with user
5. Persistent failure: Expert troubleshooting guide

---

## Best Practices

### Description Quality

Use third-person with specific triggers:
```yaml
# Good
description: This skill should be used when the user asks to "create a hook",
  "add a PreToolUse hook", or mentions hook events.

# Bad
description: Helps with hooks.
```

### Writing Style

Use imperative/infinitive form:
```markdown
# Good
To create a diagram, load the reference file first.
Validate inputs before processing.

# Bad
You should create a diagram by loading the reference file.
```

### SKILL.md Size

- Target: 1,500-2,000 words
- Maximum: ~5,000 words
- Move detailed content to `references/`

### Reference Files

**Do:**
- Keep focused: One topic per file
- Name descriptively: `sequence_diagrams.md` not `ref1.md`
- Include practical examples
- Aim for 5-15KB per file

**Don't:**
- Create monolithic files (defeats lazy loading)
- Over-granularize (<2KB files)
- Create >20KB files
- Skip examples

### Scripts

**Do:**
- Clear input/output contracts
- Structured, parseable errors
- Environment-based secrets
- Single responsibility per script

**Don't:**
- Vague error messages
- Hardcoded secrets
- Silent failures
- Catch-all exception handlers

---

## Templates

### Skill Prompt Template

```markdown
# [Skill Name]

[One-line description]

**When to use:**
- [Trigger condition 1]
- [Trigger condition 2]

**Process:**
1. **[Step 1 Name]**
   - [Action to take]
   - If [condition]: [specific handling]

2. **[Step 2 Name]** (Load Reference if needed)
   - If [condition 1]: Read reference/[file1].md
   - If [condition 2]: Read reference/[file2].md

3. **[Step 3 Name]** (Execute Script if needed)
   - Execute: `[script command with args]`
   - Monitor output for success/error patterns

4. **[Step 4 Name]** (Interpret Results)
   - If SUCCESS: [action]
   - If ERROR [pattern]: [recovery]

**Error Handling:**
- ERROR pattern 1 → [recovery strategy]
- ERROR pattern 2 → [recovery strategy]

**Requirements:**
- [System dependencies]
- [Python packages]
- [Environment variables]
```

### Script Template

```python
#!/usr/bin/env python3
"""
[One-line description]

Usage:
    python3 script.py <arg1> <arg2>

Environment:
    API_TOKEN: [Description]

Returns:
    0: Success (prints "SUCCESS: <value>")
    1: Error (prints "ERROR: <code> - <message>")
"""
import sys
import os

def main(arg1, arg2):
    try:
        # Validate inputs
        if not validate(arg1, arg2):
            print("ERROR: Invalid input parameters")
            return 1

        # Perform operation
        result = perform_operation(arg1, arg2)

        print(f"SUCCESS: {result}")
        return 0

    except NotFoundError as e:
        print(f"ERROR: 404 - Resource not found: {str(e)}")
        return 1
    except AuthenticationError:
        print("ERROR: 401 - Authentication failed")
        return 1
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: script.py <arg1> <arg2>")
        sys.exit(1)
    sys.exit(main(sys.argv[1], sys.argv[2]))
```

---

## Quick Reference Checklist

```
□ SKILL.md exists with valid YAML frontmatter
□ name: hyphen-case, matches folder name
□ description: third-person, specific triggers
□ Body uses imperative form (not "you should")
□ Core content under 3,000 words
□ Detailed docs moved to references/
□ All referenced files exist
□ Scripts are executable and documented
□ Error handling covers common failure modes
□ Token usage optimized (lazy loading where beneficial)
```
