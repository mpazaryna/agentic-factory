---
description: Check MLX model status, training data, and quality metrics
tags: [status, monitoring, models]
---

# MLX Status Check

Show comprehensive status of all models, training data, and quality progression.

## What to Show

Run this command:
```bash
uv run python manage.py status
```

Then enhance the output with:

1. **Training Data Summary:**
   - Count lines in `data/training/*.json` files
   - Show total accumulated SOAP notes (if available)
   - Estimate quality level based on note count:
     - 72 notes → B+ (87%)
     - 150 notes → A- (90-92%)
     - 300 notes → A (93-95%)
     - 500+ notes → A+ (96-98%)

2. **Model Quality Progression:**
   - Parse `data/models/*_metadata.json` files
   - Compare with previous version (check git history if available)
   - Show training date and age

3. **Next Milestone:**
   - If at 72 notes: "Next target: 150 notes for A- quality"
   - If at 150 notes: "Next target: 300 notes for A quality"
   - Show notes needed to reach next milestone

4. **Deployment Status:**
   - Check if models match what's in `native/pab/pab/Resources/MLX/` (if accessible)
   - Alert if models are trained but not deployed

## Example Output

```
🏥 MLX Models Status
════════════════════════════════════════════════════════════

📊 Training Data:
   • Total SOAP notes: 72
   • ICD-10 examples: 116 training + 13 validation
   • CPT examples: 116 training + 13 validation
   • Vertebral examples: 36 training + 4 validation

🎯 Current Quality: B+ (87%)
   Next milestone: 150 notes → A- (90-92%)
   Notes needed: 78 more (+108%)

📦 Models:
   ICD-10:
      ✅ Trained: 2025-11-10 (today)
      ✅ Vocab: 314, Output: 7 codes
      ✅ Files: icd.npz, icd.safetensors, icd_metadata.json

   CPT:
      ✅ Trained: 2025-11-10 (today)
      ✅ Vocab: 201, Output: 4 codes
      ✅ Files: cpt.npz, cpt.safetensors, cpt_metadata.json

   Vertebral:
      ✅ Trained: 2025-11-10 (today)
      ✅ Vocab: 189, Output: 17 levels
      ✅ Files: vertebral.npz, vertebral.safetensors, vertebral_metadata.json

✅ All models up to date and ready for deployment
```

## Helpful Context

- Show recent git commits to `data/models/` (last 3)
- Show recent training logs (last 2 runs)
- Suggest next action based on state
