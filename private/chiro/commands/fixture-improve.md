---
description: "Run a fixture E2E test, analyze failures, fix root causes, rerun, commit."
argument-hint: "<fixture-number | next | status | run-all>"
---

## Purpose

Autonomous improvement loop for AI pipeline fixture tests (001-014).
Runs the full pipeline (Apple Intelligence + factory workers + clinical rules),
analyzes failures against John's expected output, fixes root causes, and commits gains.

## Files

- **Test files:** `native/pab/pabTests/AI/Narratives/Fixture{NNN}*Tests.swift`
- **Fixture docs:** `docs/fixtures/{NNN}-*.md` (John's expected output is the source of truth)
- **Prompt templates:** `native/pab/pab/Kits/ContentKit/` (`.md` files + Swift definitions)
- **Clinical rules:** `native/pab/pab/Features/Notes/Factory/Resources/ClinicalKnowledge/`
- **Factory workers:** `native/pab/pab/Features/Notes/Factory/` (`*Worker.swift`)
- **AI service:** `native/pab/pab/Features/Notes/Services/DecomposedSOAPService.swift`
- **Test base:** `native/pab/pabTests/AI/Extraction/AIExtractionTestBase.swift`

## Modes

Parse `$ARGUMENTS`:

### `<fixture-number>` (e.g., `012` or `12`)

Improve a specific fixture:

1. **Run the test:**
   ```bash
   cd native/pab && xcodebuild build-for-testing -project pab.xcodeproj -scheme pab-macOS -testPlan PipelineTests -configuration Debug 2>&1 | grep -E "SUCCEEDED|FAILED"
   xcodebuild test-without-building -project pab.xcodeproj -scheme pab-macOS -testPlan PipelineTests -only-testing:"pabTests-macOS/Fixture{NNN}{Name}Tests" -configuration Debug 2>&1
   ```

2. **Report the score:** X/Y passing = Z/10. List every failing test name and the assertion message.

3. **Root cause analysis.** For each failure, classify:
   - **Prompt gap** — AI didn't extract something that's in the dictation → fix prompt template
   - **Rule gap** — clinical rules didn't add/catch something → add/modify rule in `*_derived.json` or worker
   - **Worker bug** — factory worker logic error → fix worker code
   - **AI hallucination** — AI fabricated content not in dictation → add guard or tune prompt
   - **Test too strict** — assertion expects something not derivable from dictation → fix test

4. **Read the fixture markdown** (`docs/fixtures/{NNN}-*.md`) to understand John's expected output and complexity notes.

5. **Trace the failure** through the code:
   - For subjective failures → read `DecomposedSOAPService` subjective prompt
   - For objective/findings failures → read objective prompt + `ObjectiveWorker`
   - For dysfunction failures → check `segmentalDysfunctions` extraction
   - For plan failures → read plan prompt + `PlanWorker`
   - For hallucination → check `mustNotContain` guards and prompt instructions

6. **Propose the fix** — describe what you'll change and why. Wait for approval.

7. **Implement the fix.**

8. **Rerun the fixture test.** Verify score improved.

9. **Regression check** — run 2-3 other fixtures (especially ones with similar patterns) to verify no regression.

10. **Commit** if score improved:
    ```
    fix(pipeline): <what changed>

    Fixture {NNN}: X/Y → X'/Y' (Z/10)
    Root cause: <prompt gap | rule gap | worker bug | hallucination>

    Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
    ```

### `next`

Pick the lowest-scoring fixture to improve:

1. Run all 14 fixture tests (or read last results if recent)
2. Rank by score ascending
3. Present the worst fixture with its failures
4. Proceed with the improvement loop above

### `status`

Show current scores across all 14 fixtures:

1. Run all fixtures:
   ```bash
   cd native/pab
   for suite in Fixture001DaveTests Fixture002KarinTests Fixture003NeckThoracicTests Fixture004LowBackTests Fixture005FootTests Fixture006JoeTests Fixture007MelissaTests Fixture008RachelTests Fixture009MichaelTests Fixture010BrianTests Fixture011LauraTests Fixture012MarkTests Fixture013DanielTests Fixture014KevinTests; do
     echo "=== $suite ==="
     xcodebuild test-without-building -project pab.xcodeproj -scheme pab-macOS -testPlan PipelineTests -only-testing:"pabTests-macOS/$suite" -configuration Debug 2>&1 | grep "Executed" | tail -1
   done
   ```
2. Present scorecard table: fixture | pass/total | score/10
3. Highlight fixtures below 8.0

### `run-all`

Run all 14 fixtures and report scores without attempting fixes.
Same as `status` but also captures and displays the specific failing test names.

## Root Cause Decision Tree

```
Assertion failed
├── Content missing from output (assertContains failed)
│   ├── Content IS in dictation → PROMPT GAP
│   │   └── Fix: tune the relevant section's prompt template
│   ├── Content NOT in dictation but John expects it → TEST TOO STRICT
│   │   └── Fix: relax or remove the assertion
│   └── Content should come from rules → RULE GAP
│       └── Fix: add rule to *_derived.json or worker
├── Content present that shouldn't be (assertNotContains failed)
│   ├── AI fabricated it → HALLUCINATION
│   │   └── Fix: add negative instruction to prompt or add worker guard
│   └── Rules legitimately added it → TEST TOO STRICT
│       └── Fix: remove the mustNotContain assertion
└── Wrong section (content in subjective instead of objective, etc.)
    └── PROMPT GAP — section boundaries unclear
        └── Fix: clarify section instructions in prompt template
```

## Priority Order

When choosing what to fix first within a fixture:
1. **Hallucinations** — false content is worse than missing content
2. **Subjective** — patient complaints must be accurate
3. **Objective findings** — exam findings drive diagnosis
4. **Dysfunctions** — affects assessment codes
5. **Plan** — most tolerance for variation

## Rules

- **One fixture per cycle.** Fix, verify, commit, then move on.
- **Never modify John's Expected Output.** If the test seems wrong, check against the markdown.
- **Prefer prompt/rule fixes over test relaxation.** Only mark a test "too strict" if the assertion truly can't be satisfied from the dictation.
- **Always regression check** after a fix — at minimum run the fixture you changed + one other.
- **Bump `ClinicalRuleSeeder.currentSeedVersion`** if you modify any `*_derived.json` file.
