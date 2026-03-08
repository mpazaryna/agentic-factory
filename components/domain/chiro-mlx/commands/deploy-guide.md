---
description: Guide user through deploying trained models to Xcode Resources/MLX/
tags: [deployment, xcode, workflow]
---

# Deploy Models to Xcode

Guide the user through deploying newly trained models to the PAB app.

## Prerequisites Check

Before deployment, verify:

1. **PHI Validation:** Run `/validate-phi` - MUST show "NO PHI DETECTED"
2. **Models Trained:** Check that `data/models/` has recent *.safetensors files
3. **Quality Check:** Review metadata to ensure quality didn't regress

## Deployment Steps

Walk the user through this process:

### Step 1: Open Xcode Project
```bash
open ../native/pab/pab.xcodeproj
```

### Step 2: Navigate to Resources
In Xcode:
1. Project Navigator (⌘1)
2. Expand "pab" folder
3. Find "Resources" folder
4. Find "MLX" folder (create if missing)

### Step 3: Replace Model Files

**Files to copy FROM `mlx/data/models/` TO Xcode `Resources/MLX/`:**

✅ Required files:
- `icd.safetensors` → `Resources/MLX/icd.safetensors`
- `icd_metadata.json` → `Resources/MLX/icd_metadata.json`
- `cpt.safetensors` → `Resources/MLX/cpt.safetensors`
- `cpt_metadata.json` → `Resources/MLX/cpt_metadata.json`
- `vertebral.safetensors` → `Resources/MLX/vertebral.safetensors`
- `vertebral_metadata.json` → `Resources/MLX/vertebral_metadata.json`

⚠️ Optional (fallback):
- `*.npz` files (NPZ format, safetensors is preferred)

❌ Do NOT copy:
- Training data (*.json in data/training/)
- Raw SOAP notes (data/raw/soap_notes.json)
- Any files containing clinical text

### Step 4: Verify Target Membership

For EACH file added/replaced in Xcode:
1. Select file in Project Navigator
2. Open File Inspector (⌘⌥1)
3. Under "Target Membership"
4. ✅ Ensure "pab" is CHECKED

### Step 5: Build and Test
```bash
cd ../native/pab
xcodebuild -project pab.xcodeproj -scheme pab -configuration Debug build
```

If build succeeds:
1. Run the app
2. Navigate to Chiropractic SOAP view
3. Enable MLX checkboxes:
   - ☑️ Show ICD-10 Suggestions
   - ☑️ Show Vertebral Processing
   - ☑️ Show CPT Suggestions
4. Generate a test SOAP note
5. Verify quality improved

### Step 6: Commit to Git (if quality improved)

```bash
cd ../../mlx
git add data/models/*.safetensors data/models/*_metadata.json
git commit -m "mlx: trained on <total_notes> notes (<quality> quality)"

# Optional: Tag milestone
git tag -a mlx-v1.2 -m "150 notes: A- quality milestone"
```

## Common Issues

**Issue:** "File not found in bundle"
**Fix:** Check target membership is set to "pab"

**Issue:** "Model loading failed"
**Fix:** Ensure both .safetensors AND _metadata.json are copied

**Issue:** "No predictions showing"
**Fix:** Check MLX checkboxes are enabled in SOAP view

## Safety Checklist

Before deployment, verify:
- ✅ PHI validation passed
- ✅ All 6 required files copied
- ✅ Target membership set to "pab"
- ✅ Build succeeds
- ✅ Quality improved in testing
- ✅ Git commit message is descriptive

## What NOT to Do

- ❌ Do NOT copy training data files
- ❌ Do NOT copy raw SOAP notes
- ❌ Do NOT commit without testing
- ❌ Do NOT deploy if quality regressed
