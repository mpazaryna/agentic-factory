---
name: audit
description: "Audit and enforce UAT folder organization. Use when creating/updating UAT files, auditing docs/uat/ for violations, or ensuring manifest coverage. Runs deterministic checks via Python script, uses agent judgment for content remediation."
---

# UAT Folder Audit & Enforcement

Validate and enforce `docs/uat/` structure against the spec. Two layers: a deterministic Python script for structural checks, and agent judgment for content quality and remediation.

## Quick Start

```bash
# Run all checks
uv run ${CLAUDE_SKILL_DIR}/audit-uat-folder.py

# Machine-readable output
uv run ${CLAUDE_SKILL_DIR}/audit-uat-folder.py --json

# Specific checks
uv run ${CLAUDE_SKILL_DIR}/audit-uat-folder.py --naming        # R1: filenames
uv run ${CLAUDE_SKILL_DIR}/audit-uat-folder.py --format-check  # R2: sections
uv run ${CLAUDE_SKILL_DIR}/audit-uat-folder.py --coverage      # R3: manifest
uv run ${CLAUDE_SKILL_DIR}/audit-uat-folder.py --sync-map      # R7: ClickUp map
```

## Workflow: Audit & Remediate

### Step 1: Run the audit script
```bash
uv run ${CLAUDE_SKILL_DIR}/audit-uat-folder.py --json
```

### Step 2: Read the output
Violations grouped by rule (R1-R7) with `rule`, `file`, `message`, `fixable` fields.

### Step 3: Fix structural violations (deterministic)
- **R1 (naming):** Rename to `{id}-{slug}.md`
- **R2 (heading):** Fix H1 to `# {id} — {Title}` with em dash
- **R2 (metadata):** Remove Priority/Status/ClickUp blocks
- **R3 (orphaned):** Add ID to relevant guide in `manifest.json`
- **R7 (sync-map):** Add missing ID to `.sync-map.json`

### Step 4: Fix content violations (judgment needed)
Read [spec.md](spec.md) for full requirements, then:
- **R4 (walkthrough too short):** Expand — write for end users
- **R4 (walkthrough too long):** Trim to under 1000 words
- **R5 (steps not numbered):** Restructure into numbered imperative steps

### Step 5: Re-run audit to verify
Zero violations = done.

## Workflow: Create a New UAT File

1. **Determine ID**: Read spec's numbering scheme, glob `docs/uat/{range}*.md` for next available
2. **Create file** with H1, Walkthrough, Steps, Notes sections
3. **Update manifest.json** — add ID to appropriate guide
4. **Update .sync-map.json** — add ID with ClickUp task ID
5. **Run audit** to verify

## What Script Checks vs Agent Checks

| Check | Script | Agent |
|-------|--------|-------|
| R1: Filename pattern | Yes | — |
| R2: Section structure | Yes | — |
| R2: Content quality | — | Yes |
| R3: Manifest coverage | Yes | Yes (picks guide) |
| R4: Walkthrough length | Yes | Yes (quality) |
| R5: Steps numbered | Yes | Yes (imperative mood) |
| R6: Flat directory | Yes | — |
| R7: Sync-map coverage | Yes | — |

## Spec Reference

Full requirements at [spec.md](spec.md) — read for acceptance criteria, ID numbering scheme, and content standards.
