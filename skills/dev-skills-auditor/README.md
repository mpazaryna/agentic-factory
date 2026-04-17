# skills-auditor

Audit any plugin in this repo for compliance with Claude Code skill and agent best practices.

## Why

Skills and agents in the Agentic Factory are distributed to real projects via the plugin marketplace. Poor frontmatter, missing descriptions, or implicit tool access don't just break conventions — they degrade the experience for every project that installs the plugin. This skill catches those issues before they ship.

It checks 25 rules across four categories:

- **Frontmatter (F1–F12)** — name format, description quality, tool restrictions, context/fork correctness, side-effect guards
- **Content (C1–C4)** — SKILL.md length, supporting file references, path conventions, script permissions
- **Agents (A1–A7)** — name, description, tool restrictions, model specification, system prompt quality
- **Plugin Structure (P1–P7)** — plugin.json validity, naming consistency, no nested components

Each rule has a severity: **ERROR** (must fix), **WARN** (should fix), or **INFO** (consider fixing).

## How to use

```
/codebase-analysis:skills-auditor ./dev/codebase-analysis
/codebase-analysis:skills-auditor ./platform/cloudflare
/codebase-analysis:skills-auditor ./pm/clickup
```

Pass the path to any plugin folder in this repo.

## What it produces

1. **`analysis.md`** — written to the audited plugin's root folder (e.g., `./dev/codebase-analysis/analysis.md`). Contains the full audit report with pass/fail per rule, per component, plus suggested fixes.
2. **Console summary** — brief output with total counts and top issues to fix first.

The skill never writes fixes directly to skill or agent files. It reports what to fix and you decide what to apply.

## Standards reference

The quality standards this skill enforces are documented in the root `CLAUDE.md` under **Skill Quality Standards**. That section is the source of truth — update it there, and the audit skill follows.
