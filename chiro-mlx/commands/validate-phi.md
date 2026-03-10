---
description: Run comprehensive PHI validation checks for HIPAA compliance
tags: [phi, hipaa, safety, validation]
---

# PHI Validation

Run comprehensive PHI validation to ensure HIPAA compliance before training or deployment.

## What to Run

```bash
uv run python scripts/validate_phi_removed.py
```

## Expected Output

**✅ SAFE:** Should see:
```
✅ NO PHI DETECTED!
   Safe to commit to git and deploy to app.
```

**⚠️ DANGER:** If PHI detected:
```
❌ PHI DETECTED!
   Found potential PHI in training data:
   - Patient names
   - Dates
   - Other identifiers

   DO NOT COMMIT OR DEPLOY!
```

## Response to PHI Detection

If PHI is detected:

1. **STOP ALL OPERATIONS** - Do not train, commit, or deploy
2. **Alert user immediately** with details
3. **Suggest remediation:**
   - Re-run chunk-pdf with PHI scrubbing
   - Check `scripts/extract_text_from_pdf.py` PHI removal logic
   - Manually review `data/raw/soap_notes.json` (if safe to do so)

## When to Run This

**ALWAYS run before:**
- Training models (`/train` command runs this automatically)
- Committing to git
- Deploying to Xcode
- Any operation that moves data out of mlx/tmp/

**Files Checked:**
- `data/raw/soap_notes.json`
- `data/training/*.json`
- Training data files

**Files NOT Checked (safe):**
- `data/models/*.npz` (binary weights, no text)
- `data/models/*.safetensors` (binary weights, no text)
- `data/models/*_metadata.json` (stats only, no clinical text)

## HIPAA Compliance Note

This validation is CRITICAL for HIPAA compliance. The app processes PHI locally, but we must ensure NO PHI ever leaves the local machine in:
- Git commits
- Model files
- Documentation
- Logs

Neural network weights (*.npz, *.safetensors) do NOT contain PHI - they are learned patterns, not memorized text.
