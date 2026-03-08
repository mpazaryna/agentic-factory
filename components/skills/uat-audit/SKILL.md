---
name: uat-audit
description: Audit and enforce UAT folder organization. Use when creating/updating UAT files, auditing docs/uat/ for violations, or ensuring manifest coverage. Runs deterministic checks via embedded script, uses agent judgment for content remediation.
---

# UAT Folder Audit & Enforcement

Validate and enforce `docs/uat/` structure against the spec. Two layers: a deterministic Python script for structural checks, and agent judgment for content quality and remediation.

## Quick Start

```bash
# Run all checks
uv run .claude/skills/uat-audit/audit-uat-folder.py

# Machine-readable output (for agent consumption)
uv run .claude/skills/uat-audit/audit-uat-folder.py --json

# Specific checks
uv run .claude/skills/uat-audit/audit-uat-folder.py --naming        # R1: filenames
uv run .claude/skills/uat-audit/audit-uat-folder.py --format-check  # R2: sections
uv run .claude/skills/uat-audit/audit-uat-folder.py --coverage      # R3: manifest
uv run .claude/skills/uat-audit/audit-uat-folder.py --sync-map      # R7: ClickUp map
```

## When to Use This Skill

### After creating or updating a UAT file
Run the audit to verify your changes conform. Fix any violations before committing.

### As part of tk-agent or tk-close
Before closing a ticket that touched `docs/uat/`, run the audit. If violations exist, fix them.

### Periodic maintenance
Run `--all --json` to get a full health check. Remediate violations.

## Workflow: Audit & Remediate

### Step 1: Run the audit script
```bash
uv run .claude/skills/uat-audit/audit-uat-folder.py --json
```

### Step 2: Read the output
Parse the JSON. Violations are grouped by rule (R1-R7). Each violation has:
- `rule`: which requirement it violates
- `file`: the affected file
- `message`: what's wrong
- `fixable`: whether an agent can auto-fix it

### Step 3: Fix structural violations (no judgment needed)
These are deterministic fixes:
- **R1 (naming):** Rename file to match `{id}-{slug}.md` pattern
- **R2 (heading):** Fix H1 to `# {id} — {Title}` with em dash
- **R2 (metadata):** Remove Priority/Status/ClickUp blocks
- **R3 (orphaned):** Add the ID to the most relevant guide in `manifest.json` (use the ID numbering scheme in the spec to determine which guide)
- **R7 (sync-map):** Add missing ID to `.sync-map.json` (ClickUp ID can be "TBD" if unknown)

### Step 4: Fix content violations (judgment needed)
Read `spec.md` in this skill folder for the full requirements, then:
- **R4 (walkthrough too short):** Expand the walkthrough — write for end users, explain what the feature does and how to reach it
- **R4 (walkthrough too long):** Trim — keep it under 1000 words
- **R5 (steps not numbered):** Restructure into numbered steps with imperative mood

### Step 5: Re-run audit to verify
```bash
uv run .claude/skills/uat-audit/audit-uat-folder.py
```

Zero violations = done.

## Workflow: Create a New UAT File

### Step 1: Determine the ID
Read the spec's ID numbering scheme (in `spec.md` in this skill folder). Find the feature area range (e.g., 300s for a core feature area). Glob `docs/uat/{range}*.md` to find the next available ID.

### Step 2: Create the file

```markdown
# {id} — {Title}

## Walkthrough

{100-1000 words, written for end users. Explain what the feature does, how to
get there, and what the user will see. Include screenshot refs if helpful:
![description](../screenshots/{id}-description.png)}

## Steps

1. Navigate to {location}
2. Tap/click {element}
3. Verify {expected result}
4. ...

## Notes

- {Platform caveats, edge cases, known limitations}
```

### Step 3: Update manifest.json
Add the ID to the appropriate guide(s) in `docs/guides/manifest.json`.

### Step 4: Update .sync-map.json
Add `"{id}": { "clickup_id": "{task_id}", "file": "{id}-{slug}.md" }` to the `tasks` object in `docs/uat/.sync-map.json`. Use the ClickUp task ID if known, or `"TBD"`.

### Step 5: Run audit
```bash
uv run .claude/skills/uat-audit/audit-uat-folder.py
```

## Spec Reference

The full spec is at `.claude/skills/uat-audit/spec.md`. Read it when you need:
- Acceptance criteria for each requirement (R1-R11)
- ID numbering scheme (which range for which feature area)
- Content quality standards for walkthroughs and steps

## Files in This Skill

| File | Purpose |
|------|---------|
| `SKILL.md` | This file — orchestration instructions |
| `spec.md` | Full requirements spec (R1-R11, acceptance criteria, ID scheme) |
| `audit-uat-folder.py` | Deterministic audit script (R1-R7 structural checks) |

## What the Script Checks vs What the Agent Checks

| Check | Script | Agent |
|-------|--------|-------|
| R1: Filename pattern | Yes | — |
| R2: Section structure | Yes | — |
| R2: Section content quality | — | Yes (read spec) |
| R3: Manifest coverage | Yes | Yes (picks which guide) |
| R4: Walkthrough word count | Yes | Yes (quality, clarity) |
| R5: Steps numbered | Yes | Yes (imperative mood, testability) |
| R6: Flat directory | Yes | — |
| R7: Sync-map coverage | Yes | — |
