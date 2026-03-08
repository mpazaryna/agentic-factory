---
description: "UAT fixture regression loop — fix failing assertions, run suite, commit baseline. Temporary command for 86e069yx2."
argument-hint: "[next | subtask-id | status | run]"
---

## Purpose

Iterative improvement loop for the 14 John UAT fixtures under parent ticket 86e069yx2.
**Delete this command when all fixtures are passing and the parent ticket is closed.**

## Setup

- **Parent ticket:** 86e069yx2 (UAT Fixture Regression Suite)
- **Branch:** `ticket/86e069yx2-uat-regression` (single long-running branch, one commit per fix)
- **Fixtures JSON:** `native/pab/pabTests/Fixtures/UAT/UATFixtures.json`
- **Test file:** `native/pab/pabTests/Integration/Factory/FixtureRegressionTests.swift`
- **Results:** `docs/fixtures/regression-results.md` + `docs/fixtures/regression-results.json`
- **Fixture docs:** `docs/fixtures/###-*.md`

## Subtask IDs

| Subtask | Fixture | ClickUp ID |
|---------|---------|------------|
| 001 | Dave: Low Back Pain | 86e069z36 |
| 002 | Karin: Neck Pain | 86e069z4u |
| 003 | Neck + Thoracic Multi-Region | 86e069z5n |
| 004 | Low Back with Modality | 86e069z64 |
| 005 | Foot Injury, No Adjustment | 86e069z80 |
| 006 | Joe: Multi-Region | 86e069zer |
| 007 | Melissa: Low Back Radiating + Headaches | 86e069zgq |
| 008 | Rachel: Three Complaints | 86e069zkv |
| 009 | Michael: Shoulder + Neck | 86e069zne |
| 010 | Brian: Radiculopathy + Neuro | 86e069zxt |
| 011 | Laura: Shoulder Subscapularis + Neck | 86e06a00z |
| 012 | Mark: Knee Meniscus + Low Back | 86e06a04h |
| 013 | Daniel: Triple Complaint + ART | 86e06a07j |
| 014 | Kevin: Triple Complaint + Positive Ortho + ROM | 86e06a0b4 |

## Modes

Parse `$ARGUMENTS`:

### `next` (default if no args)

Pick the next failing assertion group to fix:

1. Read `docs/fixtures/regression-results.md`
2. Identify fixtures with failures, prioritize by:
   - Fixtures closest to passing (e.g., 2/3 groups passing)
   - ICD-10 failures before CPT before Dysfunctions (ICD-10 is most impactful)
3. Present the target:
   ```
   ## Next Target
   **Fixture:** 001-dave
   **Failing:** Dysfunctions — Missing: Pelvis, Sacrum
   **Passing:** ICD-10 (3/3), CPT (1/1)
   **Subtask:** 86e069z36
   ```
4. Investigate: read the fixture dictation, trace through relevant rules/workers, identify the gap
5. Propose the fix and wait for approval

### `<subtask-id>` (e.g., `86e069z36` or `001`)

Work on a specific fixture:

1. If numeric like `001`, map to subtask ID from the table above
2. Read the fixture from `UATFixtures.json` and current results from `regression-results.md`
3. Show current status for that fixture
4. Investigate failures and propose fix

### `status`

Show current regression status:

1. Read `docs/fixtures/regression-results.md`
2. Present the summary table
3. Compare against previous commit's results if available:
   ```bash
   git show HEAD:docs/fixtures/regression-results.md
   ```
4. Highlight what changed since last commit

### `run`

Run the regression suite and update baseline:

1. Build:
   ```bash
   cd native/pab && xcodebuild -project pab.xcodeproj -scheme pab-macOS -configuration Debug build
   ```
2. Run test:
   ```bash
   xcodebuild test -project pab.xcodeproj -scheme pab-macOS \
     -only-testing:'pabTests-macOS/FixtureRegressionTests/testAllFixturesAndReport' \
     -configuration Debug
   ```
3. Copy results from sandbox:
   ```bash
   cp ~/Library/Containers/paz.pab/Data/tmp/regression-results/regression-results.md docs/fixtures/regression-results.md
   cp ~/Library/Containers/paz.pab/Data/tmp/regression-results/regression-results.json docs/fixtures/regression-results.json
   ```
4. Diff against previous:
   ```bash
   git diff docs/fixtures/regression-results.md
   ```
5. Present the before/after summary

## Workflow

The typical loop:

1. `/uat next` — pick a target
2. Investigate and implement the fix (rule change, keyword addition, etc.)
3. `/uat run` — run regression, verify fix worked and nothing regressed
4. Commit with the fix + updated results:
   ```
   fix(rules): <what changed>

   Improves: <fixture IDs that got better>
   Regression: <X>/14 passing, <Y>/42 assertion groups

   ClickUp: 86e069yx2

   Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
   ```
5. Update subtask status in ClickUp if a fixture is now fully passing:
   - `clickup_update_task` with `status: "complete"`
   - Post a comment with the passing result
6. `/uat next` — repeat

## Branch Rules

- **Single branch:** `ticket/86e069yx2-uat-regression`
- **One commit per fix** — each commit should be a logical unit (one rule change or related set of changes)
- **Always include updated regression results** in the commit
- **Never write directly to main** — this branch gets one PR when we're done
- If not on the branch, check it out:
  ```bash
  git checkout ticket/86e069yx2-uat-regression
  ```
  If the branch doesn't exist yet, create it:
  ```bash
  git checkout main && git pull && git checkout -b ticket/86e069yx2-uat-regression
  ```

## Closing

When all 14 fixtures are passing (or we've decided the remaining failures need Apple Intelligence):

1. Create PR from `ticket/86e069yx2-uat-regression` → `main`
2. Merge with squash
3. Update parent ticket 86e069yx2 to `complete`
4. **Delete this file:** `rm .claude/commands/uat.md`
