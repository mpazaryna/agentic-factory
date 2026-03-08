---
description: Automatically validate model quality after training and suggest next steps
tags: [quality, validation, proactive, training]
trigger: after-training-complete
---

# Quality Checker Skill

**Purpose:** Automatically validate model quality after training completes and guide the user on next steps.

## When to Activate

Activate this skill AUTOMATICALLY when:
- `/train` command completes successfully
- `manage.py train-all` finishes
- New model files detected in `data/models/`
- User asks "is training done?" or "did it work?"

## What to Do

### 1. Verify Training Completed

Check that ALL required files exist and are recent:
```bash
ls -lt data/models/
```

Required files (all should exist and have recent timestamps):
- `icd.safetensors` + `icd_metadata.json`
- `cpt.safetensors` + `cpt_metadata.json`
- `vertebral.safetensors` + `vertebral_metadata.json`

### 2. Parse Quality Metrics

Read each `*_metadata.json` file and extract:
- `vocab_size` - vocabulary size
- `output_size` - number of output classes
- `training_date` - when trained
- `loss` or `final_loss` - training loss
- Any error messages or warnings

### 3. Compare with Previous Version

```bash
# Get previous metadata
git show HEAD:mlx/data/models/icd_metadata.json 2>/dev/null

# Compare
# - Vocab size change
# - Loss change
# - Date difference
```

### 4. Calculate Quality Level

Based on training data size (count from metadata or training files):
- 72 notes → B+ (87%)
- 107 notes → B+ (88%)
- 150 notes → A- (90-92%)
- 300 notes → A (93-95%)
- 500+ notes → A+ (96-98%)

### 5. Provide Verdict

**✅ If Quality Improved:**
```
🎉 Quality Check: IMPROVED!

📊 Results Summary:
   Overall: B+ → A- (+3% improvement)
   Training data: 72 → 150 notes

   ICD-10: Loss 0.146 → 0.120 (-17.8%) ✅
   CPT: Loss 0.051 → 0.040 (-21.7%) ✅
   Vertebral: Loss 0.347 → 0.301 (-13.3%) ✅

✅ All models show improvement
✅ Ready for deployment

🚀 Recommended next steps:
1. Deploy to Xcode (/deploy-guide)
2. Test in PAB app
3. Commit with: "mlx: trained on 150 notes (A- quality, +78 notes)"

Deploy now? [Yes, guide me] [Show quality details] [Not yet]
```

**⚠️ If Quality Stable:**
```
📊 Quality Check: STABLE

Training completed successfully, but metrics similar to previous version.
This is normal if data volume hasn't increased significantly.

Current: B+ (87%) - 72 notes
Next milestone: 150 notes → A- (90-92%)

💡 Suggestion: Wait for next data delivery before deploying.
Need 78 more notes to reach A- quality.
```

**❌ If Quality Regressed:**
```
⚠️ Quality Check: REGRESSION DETECTED

One or more models show decreased performance:
   ICD-10: Loss 0.120 → 0.165 (+37.5%) ❌ WORSE

🚨 DO NOT DEPLOY

Possible causes:
- Bad data in recent PDF
- Training data corruption
- Hyperparameter issue

🔧 Recommended action:
1. Review recent training logs: logs/train-all_*.log
2. Check recent PDF quality
3. Restore from backup:
   cp archive/models/$(ls -t archive/models/ | head -1)/* data/models/

Investigate regression? [Yes] [Show logs] [Restore backup]
```

### 6. Proactive Suggestions

Based on quality results, suggest:

**After successful training:**
- Run `/deploy-guide` to deploy models
- Suggest git commit message
- Offer to help test in PAB app

**If milestone reached:**
- Celebrate! (150 notes, 300 notes, 500 notes)
- Suggest tagging the release
- Share quality progression stats

**If near milestone:**
- Show notes needed for next level
- Encourage next data delivery

## Integration with Other Skills

Works alongside:
- `/train` command (triggers this skill)
- `/quality-check` command (manual version)
- `phi-guardian` skill (ensures PHI safety before deployment)

## Example Interaction

```
[Training completes...]

Quality Checker (auto-activated):

🎉 Training Complete! Running quality analysis...

📊 Quality Check Results:
════════════════════════════════════════════════════════════

🎯 Milestone Reached! A- Quality Achieved! 🎉

Training progression:
  72 notes (Oct 24) → 150 notes (Nov 10) = +108%
  B+ (87%) → A- (90%) = +3% improvement

All 3 models improved:
  ✅ ICD-10: -17.8% loss
  ✅ CPT: -21.7% loss
  ✅ Vertebral: -13.3% loss

Next milestone: 300 notes → A quality (needs +150 more)

🚀 Ready to deploy these improved models?

What would you like to do?
[Deploy to Xcode] [Show deployment guide] [Check details] [Not yet]
```

## Quality Thresholds

Use these thresholds to determine verdict:

**IMPROVED:** Any of these true:
- Loss decreased by >5% on any model
- Vocabulary increased by >10%
- New output classes added

**STABLE:** All of these true:
- Loss changed <5%
- Vocabulary changed <10%
- No new classes

**REGRESSED:** Any of these true:
- Loss increased by >10%
- Vocabulary decreased by >5%
- Training errors/warnings present
- Loss > 0.5 on any model
