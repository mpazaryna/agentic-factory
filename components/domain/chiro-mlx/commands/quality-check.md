---
description: Analyze model quality metrics and compare with previous versions
tags: [quality, validation, metrics]
---

# Model Quality Check

Analyze trained model quality and compare with previous versions.

## What to Check

### 1. Model Metadata
Parse `data/models/*_metadata.json` files and show:
- Vocabulary size (should grow with more data)
- Output classes (codes/levels)
- Training date
- Loss metrics (lower is better)
- Any training notes/warnings

### 2. Compare with Previous Version

Use git to find previous model metadata:
```bash
# Get previous version of metadata
git show HEAD~1:mlx/data/models/icd_metadata.json

# Compare with current
diff <(git show HEAD~1:mlx/data/models/icd_metadata.json) data/models/icd_metadata.json
```

### 3. Quality Indicators

**✅ Good Signs:**
- Vocabulary increased (more patterns learned)
- Loss decreased (better predictions)
- Output classes stable or increased (new codes/levels)
- Training data increased

**⚠️ Warning Signs:**
- Loss increased (potential overfitting or data quality issue)
- Vocabulary decreased (possible data loss)
- Training failed to complete

**❌ Red Flags:**
- Massive vocabulary jump (>50%) - might indicate bad data
- Loss > 0.5 for any model - poor quality
- Missing metadata files

### 4. Quality Level Estimation

Based on training data count:
- **72 notes** → B+ (87%)
- **107 notes** → B+ (88%)
- **150 notes** → A- (90-92%)
- **300 notes** → A (93-95%)
- **500+ notes** → A+ (96-98%)

## Example Output

```
📊 Model Quality Analysis
════════════════════════════════════════════════════════════

🎯 Overall Quality: B+ → A- (IMPROVED! 🎉)
   Training data: 72 → 150 notes (+108%)

📈 ICD-10 Model:
   Vocabulary: 314 → 328 (+4.5%) ✅
   Output: 7 → 8 codes (+1) ✅
   Loss: 0.1460 → 0.1203 (-17.6%) ✅ IMPROVED
   Status: ✅ Ready for deployment

📈 CPT Model:
   Vocabulary: 201 → 215 (+7.0%) ✅
   Output: 4 codes (stable) ✅
   Loss: 0.0505 → 0.0398 (-21.2%) ✅ IMPROVED
   Status: ✅ Ready for deployment

📈 Vertebral Model:
   Vocabulary: 189 → 203 (+7.4%) ✅
   Output: 17 → 18 levels (+1) ✅
   Loss: 0.3465 → 0.3012 (-13.1%) ✅ IMPROVED
   Status: ✅ Ready for deployment

✅ All models show improvement
✅ Safe to deploy to production

Recommendation: Deploy and commit with message:
"mlx: trained on 150 notes (A- quality, +78 notes)"
```

## What to Do Based on Results

**If Quality Improved:**
1. Suggest deployment via `/deploy-guide`
2. Suggest git commit message
3. Celebrate the milestone! 🎉

**If Quality Stable:**
1. Note that more data may be needed
2. Suggest waiting for next data delivery

**If Quality Regressed:**
1. **STOP** - Do not deploy
2. Investigate possible causes:
   - Bad data in recent PDF?
   - Training data corruption?
   - Hyperparameter issues?
3. Suggest restoring from backup:
   ```bash
   cp archive/models/$(ls -t archive/models/ | head -1)/* data/models/
   ```

## Git Commit Suggestion Format

Based on quality check results, suggest:
```
mlx: trained on <total_notes> notes (<quality> quality, <change>)

Examples:
- "mlx: trained on 150 notes (A- quality, +78 notes)"
- "mlx: trained on 72 notes (B+ quality, initial training)"
- "mlx: trained on 300 notes (A quality, milestone reached)"
```
