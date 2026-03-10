---
description: Run complete MLX training workflow with PHI validation and quality checks
tags: [training, workflow, phi-safety]
---

# MLX Training Workflow

Run the complete training pipeline with automatic PHI validation and quality checks.

## Usage

If I provide a PDF file path, run the full pipeline including PDF extraction:
```bash
uv run python manage.py full-pipeline --pdf <pdf_path>
```

If no PDF is provided, assume data is already extracted and run:
```bash
uv run python manage.py extract-training
uv run python manage.py train-all
```

## Safety Checks

**CRITICAL: Before training starts, ALWAYS run:**
```bash
uv run python scripts/validate_phi_removed.py
```

If this shows any PHI detected, **STOP** and alert the user immediately. Do not proceed with training.

## After Training

1. Show model metadata from `data/models/*_metadata.json`
2. Compare quality metrics with previous version (if available in git history)
3. Proactively offer deployment guidance
4. Suggest git commit message based on:
   - Number of total training notes
   - Quality level achieved
   - Change description

## Example Flow

```
You: /train tmp/new-batch.pdf

Claude:
✅ Running full pipeline...
   → Chunking PDF
   → Extracting text with PHI scrubbing
   → Validating PHI removed
   → Extracting training data
   → Training models

📊 Training Complete!

ICD-10 Model:
  Vocab: 314 → 328 (+14)
  Output: 7 → 8 (+1 new code)
  Loss: 0.1460 → 0.1203 (improved)

CPT Model:
  Vocab: 201 → 215 (+14)
  Output: 4 (unchanged)
  Loss: 0.0505 → 0.0398 (improved)

Vertebral Model:
  Vocab: 189 → 203 (+14)
  Output: 17 → 18 (+1 new level)
  Loss: 0.3465 → 0.3012 (improved)

🎉 Quality improved across all models!

📤 Ready to deploy?
[Deploy to Xcode] [Show deployment guide] [Not yet]
```

## What NOT to Do

- Do NOT modify manage.py or scripts
- Do NOT skip PHI validation
- Do NOT automatically commit to git (always ask first)
- Do NOT copy files to Xcode automatically (guide user instead)
