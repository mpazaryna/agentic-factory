---
description: Proactively check for PHI before any git operations to ensure HIPAA compliance
tags: [phi, hipaa, safety, proactive]
trigger: before-git-commit, before-git-add
---

# PHI Guardian Skill

**Purpose:** Automatically prevent PHI leaks by checking for PHI before any git operations.

## When to Activate

Activate this skill AUTOMATICALLY when the user attempts to:
- Run `git add`
- Run `git commit`
- Use any git command that stages or commits files
- Ask me to commit changes

## What to Do

### 1. Check What's Being Added

```bash
# See what files are staged or about to be staged
git status
git diff --cached --name-only
```

### 2. Identify Risk Files

**🚨 HIGH RISK (STOP if found):**
- `data/raw/soap_notes.json`
- `data/training/*.json` (except metadata)
- `tmp/*.pdf`
- Any files in `logs/` with potential clinical text

**✅ SAFE (Allow):**
- `data/models/*.npz`
- `data/models/*.safetensors`
- `data/models/*_metadata.json`
- `manage.py`
- `scripts/*.py`
- `docs/*.md`
- `.claude/*`

### 3. Run PHI Validation

If ANY training data files are being committed (even if gitignored), run:
```bash
uv run python scripts/validate_phi_removed.py
```

### 4. Response Based on Findings

**If HIGH RISK files detected:**
```
🚨 PHI GUARDIAN ALERT!

You're about to commit files that may contain PHI:
- data/raw/soap_notes.json
- data/training/icd.json

These files should NEVER be committed to git!

✅ Safe to commit:
- data/models/*.safetensors (neural weights, no PHI)
- data/models/*_metadata.json (stats only)
- scripts/

❌ BLOCKING THIS COMMIT for HIPAA compliance.

Suggested action:
git reset HEAD data/raw/soap_notes.json
git add data/models/*.safetensors data/models/*_metadata.json
```

**If only SAFE files detected:**
```
✅ PHI Guardian: All files safe to commit

Files being committed:
- data/models/icd.safetensors
- data/models/cpt.safetensors
- data/models/vertebral.safetensors
- data/models/*_metadata.json

No PHI detected. Safe to proceed.
```

## Critical Rules

1. **NEVER allow commits of:**
   - `data/raw/soap_notes.json`
   - `data/training/*.json` (training data)
   - `tmp/*.pdf`
   - Log files with clinical text

2. **ALWAYS run validation before allowing:**
   - Any git add/commit in mlx/
   - Even if files seem safe

3. **BLOCK first, ask questions later:**
   - If uncertain, BLOCK the commit
   - Better to be cautious with PHI

## Integration with Workflow

This skill works alongside:
- `/train` command (which runs validation)
- `/validate-phi` command (manual check)
- Git workflows (automatic guardian)

## Example Interaction

```
User: git add data/

Claude (PHI Guardian activated):
🚨 STOP! PHI Guardian detected risky files:
- data/raw/soap_notes.json (HIGH RISK - contains clinical text)
- data/training/icd.json (HIGH RISK - contains SOAP note excerpts)

These files contain PHI and should NEVER be committed!

✅ Safe alternative:
git add data/models/*.safetensors data/models/*_metadata.json

This adds only the trained model weights (no PHI).

Proceed with safe version? [Yes] [Show me what's safe] [Cancel]
```

## Override (Emergency Only)

If user insists after being warned:
1. Explain HIPAA violation risk one more time
2. Suggest they review docs/PHI-SAFETY.md
3. If they still insist, defer to their judgment but log the warning

**Never automatically proceed past PHI warnings.**
