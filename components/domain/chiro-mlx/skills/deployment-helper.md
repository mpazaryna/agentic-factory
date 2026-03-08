---
description: Guide user through Xcode deployment process after successful training
tags: [deployment, xcode, proactive, workflow]
trigger: after-quality-check-pass
---

# Deployment Helper Skill

**Purpose:** Proactively guide users through deploying trained models to Xcode after quality validation passes.

## When to Activate

Activate this skill AUTOMATICALLY when:
- Quality check shows improvement
- User says "yes" to deployment
- User asks "how do I deploy?" or "what's next?"
- Training completed + quality checked + PHI validated

## Prerequisites Checklist

Before starting deployment, verify:

```bash
# 1. PHI validation passed
uv run python scripts/validate_phi_removed.py
# Must show: ✅ NO PHI DETECTED!

# 2. Models exist and are recent
ls -lt data/models/*.safetensors
# All 3 models should be recent (today)

# 3. Quality check passed
# (Should already be done by quality-checker skill)
```

If any prerequisite fails, STOP and address it first.

## Guided Deployment Process

### Step 1: Prepare for Deployment

```
📦 Deployment Preparation
════════════════════════════════════════════════════════════

Ready to deploy 3 models to Xcode:
✅ icd.safetensors (842 KB)
✅ cpt.safetensors (838 KB)
✅ vertebral.safetensors (839 KB)

Plus 3 metadata files:
✅ icd_metadata.json
✅ cpt_metadata.json
✅ vertebral_metadata.json

Total: 6 files, ~2.5 MB

Continue? [Yes] [Show file details] [Cancel]
```

### Step 2: Open Xcode (if user agrees)

```
Opening Xcode project...
```

```bash
open ../native/pab/pab.xcodeproj
```

```
✅ Xcode project opened

📋 Next steps in Xcode:
1. In Project Navigator (⌘1), find: pab → Resources → MLX
2. If MLX folder doesn't exist, create it (Right-click Resources → New Group)
3. Ready to copy files

Press Enter when ready to continue...
```

### Step 3: Guide File Copying

```
📁 Copy these 6 files FROM mlx/data/models/ TO Xcode Resources/MLX/:

In Xcode:
1. Right-click "Resources/MLX" folder
2. Choose "Add Files to pab..."
3. Navigate to: <full_path>/mlx/data/models/
4. Select these files:
   ☐ icd.safetensors
   ☐ icd_metadata.json
   ☐ cpt.safetensors
   ☐ cpt_metadata.json
   ☐ vertebral.safetensors
   ☐ vertebral_metadata.json
5. Ensure "Add to targets" has "pab" CHECKED
6. Click "Add"

🎯 Pro tip: You can select all 6 files at once with ⌘-click

Done copying files? [Yes] [Need help] [Show me again]
```

### Step 4: Verify Target Membership

```
🎯 Verifying target membership...

For EACH of the 6 files you just added:
1. Select file in Project Navigator
2. Open File Inspector (⌘⌥1) on the right
3. Under "Target Membership"
4. ✅ Ensure "pab" is CHECKED

All 6 files have "pab" checked? [Yes] [Show me how] [Having trouble]
```

### Step 5: Build Test

```
🔨 Testing build...
```

```bash
cd ../native/pab
xcodebuild -project pab.xcodeproj -scheme pab -configuration Debug build
```

**If build succeeds:**
```
✅ Build successful!

Models deployed and ready to test.

📱 Next: Test in app
1. Run the app (⌘R in Xcode)
2. Navigate to: Chiropractic → SOAP Notes
3. Enable MLX features:
   ☑️ Show ICD-10 Suggestions
   ☑️ Show Vertebral Processing
   ☑️ Show CPT Suggestions
4. Generate a test SOAP note
5. Verify quality improved

Ready to test? [Yes, run app] [Skip testing] [Back]
```

**If build fails:**
```
❌ Build failed!

Common issues:
1. Target membership not set → Go back to Step 4
2. Files in wrong location → Should be in Resources/MLX/
3. Missing metadata files → Need all 6 files

Check build errors:
[Show errors] [Try again] [Get help]
```

### Step 6: Post-Deployment

After successful test:

```
🎉 Deployment successful!

✅ Models loaded in app
✅ Quality improved
✅ Ready to commit

📝 Suggested git commit:

cd ../../mlx
git add data/models/*.safetensors data/models/*_metadata.json
git commit -m "mlx: trained on 150 notes (A- quality, +78 notes)"

# Optional: Tag milestone
git tag -a mlx-v1.2 -m "150 notes: A- quality milestone"

Commit now? [Yes] [Edit message] [Not yet]
```

## Troubleshooting Guide

Provide context-aware help for common issues:

### Issue: "Can't find Resources folder"
```
Resources folder should be inside the "pab" project folder in Xcode.

If missing:
1. Right-click "pab" folder
2. New Group → Name it "Resources"
3. Right-click "Resources"
4. New Group → Name it "MLX"

Try again? [Yes] [Show screenshot]
```

### Issue: "Build error: File not found"
```
This usually means target membership isn't set.

Fix:
1. Select EACH of the 6 model files
2. File Inspector (⌘⌥1)
3. Under "Target Membership", check "pab"

All files must have this checkbox!

Try again? [Yes]
```

### Issue: "No MLX predictions showing"
```
Models deployed but not working? Check:

1. MLX checkboxes enabled in SOAP view:
   Settings → Enable MLX features

2. Check console logs in Xcode for errors:
   View → Debug Area → Show Debug Area (⌘⇧Y)

3. Verify all 6 files copied:
   - 3 *.safetensors
   - 3 *_metadata.json

Need detailed debugging? [Yes] [Check logs]
```

## Safety Checks

Throughout deployment, continuously verify:
- ✅ Only deploying model files (no training data)
- ✅ PHI validation passed
- ✅ Quality improved (no regression)
- ✅ Build succeeds before testing
- ✅ Testing confirms improvement

## Integration

Works with:
- `quality-checker` skill (triggers this)
- `/deploy-guide` command (manual version)
- `phi-guardian` skill (ensures safety)

## Example Full Interaction

```
[After training + quality check passes...]

Deployment Helper (auto-activated):

🎉 Quality improved! Ready to deploy?

Deployment will:
1. Copy 6 files to Xcode Resources/MLX/
2. Build and test the app
3. Commit to git if successful

Time estimate: 5-10 minutes

Start deployment? [Yes] [Show me what will happen] [Not yet]

[User: Yes]

📦 Opening Xcode project...
✅ Xcode opened

[... walks through steps 1-6 ...]

🎉 Deployment complete!

Summary:
✅ 6 files deployed to Xcode
✅ Build successful
✅ App tested, quality improved
✅ Committed to git: "mlx: trained on 150 notes (A- quality)"

🎯 Milestone reached: A- quality with 150 notes!
Next target: 300 notes → A quality

Great work! 🚀
```
