---
name: skills-auditor
description: "Audit plugin skills and agents for compliance with Claude Code best practices — checks frontmatter, descriptions, tool restrictions, structure, and naming. Use when improving plugin quality or before publishing."
argument-hint: "<plugin-folder-path>"
allowed-tools: Read, Write, Glob, Grep, Bash
disable-model-invocation: false
---

# Audit Skills

Audit a plugin folder for compliance with Claude Code skill and agent best practices.

## Variables

PLUGIN_PATH: $ARGUMENTS

## Workflow

If no `PLUGIN_PATH` is provided, STOP and ask the user to provide it.

### Step 1: Discover Plugin Structure

1. Verify `.claude-plugin/plugin.json` exists and is valid JSON
2. Scan `skills/` for all SKILL.md files
3. Scan `agents/` for all agent definition files
4. Check for CLAUDE.md at plugin root
5. Build inventory of all components to audit

### Step 2: Audit Each Skill

For every SKILL.md found, check each rule below. Track pass/fail per skill.

#### Frontmatter Rules

| Rule | Check | Severity |
|------|-------|----------|
| **F1: name exists** | `name` field present in frontmatter | ERROR |
| **F2: name format** | kebab-case only (lowercase, hyphens, numbers), ≤64 chars | ERROR |
| **F3: name matches directory** | `name` field matches the containing directory name | WARN |
| **F4: description exists** | `description` field present | ERROR |
| **F5: description quality** | ≥50 chars, starts with action verb, contains "Use when" or similar trigger phrase | WARN |
| **F6: allowed-tools explicit** | `allowed-tools` field is present | WARN |
| **F7: allowed-tools minimal** | No tools listed that the skill doesn't need (check skill body for tool usage signals) | INFO |
| **F8: argument-hint present** | If skill uses `$ARGUMENTS` or `$N`, `argument-hint` should exist | WARN |
| **F9: context:fork has task** | If `context: fork`, skill body contains actionable instructions (not just reference) | ERROR |
| **F10: context:fork has agent** | If `context: fork`, `agent` field is specified | WARN |
| **F11: side-effects guarded** | Plugin skills should have `disable-model-invocation: false` (true hides them from slash commands when installed). Only project-local `.claude/skills/` may use `true`. | WARN |
| **F12: no unknown fields** | Frontmatter only contains recognized fields | INFO |

#### Content Rules

| Rule | Check | Severity |
|------|-------|----------|
| **C1: length** | SKILL.md ≤500 lines. If longer, reference material should be in supporting files | WARN |
| **C2: supporting files referenced** | If `references/`, `templates/`, `scripts/` exist, they're referenced from SKILL.md | WARN |
| **C3: paths use CLAUDE_SKILL_DIR** | References to skill-local files use `${CLAUDE_SKILL_DIR}`, not relative paths | WARN |
| **C4: scripts executable** | Any scripts in `scripts/` have shebangs and are executable | ERROR |

### Step 3: Audit Each Agent

For every agent definition file, check:

| Rule | Check | Severity |
|------|-------|----------|
| **A1: name exists** | `name` field present | ERROR |
| **A2: name format** | kebab-case | ERROR |
| **A3: description exists** | `description` field present | ERROR |
| **A4: description quality** | Explains when Claude should delegate to this agent | WARN |
| **A5: tools explicit** | `tools` field is present (principle of least privilege) | WARN |
| **A6: model specified** | `model` field present (haiku/sonnet/opus) | INFO |
| **A7: system prompt exists** | Markdown body after frontmatter has clear role + instructions | WARN |

### Step 4: Audit Plugin Structure

| Rule | Check | Severity |
|------|-------|----------|
| **P1: plugin.json valid** | `.claude-plugin/plugin.json` exists and parses as valid JSON | ERROR |
| **P2: plugin.json has name** | `name` field in plugin.json is kebab-case | ERROR |
| **P3: plugin.json has version** | `version` field follows semver | WARN |
| **P4: plugin.json has description** | `description` field exists | WARN |
| **P5: no nested components** | No `skills/` or `agents/` inside `.claude-plugin/` | ERROR |
| **P6: CLAUDE.md exists** | Plugin root has CLAUDE.md | WARN |
| **P7: naming consistency** | All skill/agent names use kebab-case throughout | ERROR |

### Step 5: Write Analysis Report

Write the full audit report to `{PLUGIN_PATH}/analysis.md`. This file is the persistent artifact of the audit — it stays in the plugin folder for reference and tracking over time.

Use this structure for the file:

```markdown
# Plugin Audit: {plugin-name}

**Path**: {PLUGIN_PATH}
**Date**: {today}
**Skills**: {count} | **Agents**: {count}

## Summary

| Severity | Count |
|----------|-------|
| ERROR    | {n}   |
| WARN     | {n}   |
| INFO     | {n}   |
| PASS     | {n}   |

## Plugin Structure
- P1: {PASS/FAIL} — plugin.json valid
- P2: {PASS/FAIL} — plugin.json has name
...

## Skills

### {skill-name}
- F1: {PASS/FAIL} — name exists
- F2: {PASS/FAIL} — name format
...

### {skill-name}
...

## Agents

### {agent-name}
- A1: {PASS/FAIL} — name exists
...

## Top Issues (by impact)

1. {Most impactful issue + suggested fix}
2. {Next issue + suggested fix}
3. ...

## Suggested Fixes

{For each ERROR and WARN, a specific actionable fix}
```

### Step 6: Summarize to User

After writing the file, print a brief summary to the user:
- Total pass/fail counts
- Number of ERRORs and WARNs
- Path to the written `analysis.md`
- Top 3 highest-impact issues to fix first

Do NOT write fixes to skill/agent files. Only report them in `analysis.md`. The user decides what to apply.

## Recognized Frontmatter Fields

Skills: `name`, `description`, `argument-hint`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `model`, `hooks`

Agents: `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `memory`, `hooks`, `color`, `background`, `isolation`

## Description Quality Signals

**Good signals** (any of these = likely good):
- Starts with action verb: Analyze, Audit, Generate, Review, Research, Explain, Build, Deploy, Convert
- Contains trigger phrase: "Use when", "Use for", "Use after", "Use proactively"
- Mentions specific domain/context

**Bad signals** (any of these = likely bad):
- Under 30 characters
- Generic words only: "helper", "tool", "processor", "thing"
- No use-case context
- Just restates the name
