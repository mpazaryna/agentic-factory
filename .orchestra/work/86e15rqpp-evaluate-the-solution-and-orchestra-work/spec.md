---
ticket: 86e15rqpp
status: complete
created_on: 2026-04-30
---

# Spec: Add Execution Pipeline to Orchestra

**PRD:** `prd.md`

---

## Objective

Write three orchestra skills that cover the execution half of the methodology: implement, review, merge. Each skill is a discrete user invocation with clear inputs, outputs, and boundaries.

---

## Approach

### Step 1 — Define the Status Vocabulary

Establish end-to-end status transitions that connect planning to execution:

`draft` → `approved` → `in-progress` → `complete` → `reviewed` → `closed`

Each skill owns one or two transitions. No skill crosses into another's territory.

### Step 2 — Write orchestra-implement

- Input: an approved spec (`status: approved`)
- Creates branch `impl/{ticket-id}`
- Flips status to `in-progress`, executes spec steps in order, commits per step
- Verifies each acceptance criterion explicitly with evidence
- Flips status to `complete`
- Output: completed branch, ready for review

### Step 3 — Write orchestra-review

- Input: a completed implementation branch (`status: complete`)
- Diffs the branch against main
- Checks every acceptance criterion with file/line evidence — no assumptions
- Checks deliverables table for missing or placeholder content
- Spot-checks the diff for shortcuts and incomplete steps
- Produces a structured PASS/FAIL report
- On PASS: flips status to `reviewed`
- On FAIL: routes back to `/orchestra-implement`

### Step 4 — Write orchestra-merge

- Input: a reviewed branch (`status: reviewed`)
- Syncs main, merges with `--no-ff`
- Resolves conflicts by preferring the implementation branch intent; surfaces ambiguous conflicts to the user
- Flips status to `closed`
- Deletes branch with safe `-d`
- Output: main updated, work item closed

---

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Implement skill | `skills/orchestra-implement/SKILL.md` | Delivered |
| Review skill | `skills/orchestra-review/SKILL.md` | Delivered |
| Merge skill | `skills/orchestra-merge/SKILL.md` | Delivered |

---

## Acceptance Criteria

- [ ] `orchestra-implement` creates a branch, steps through the spec, and updates status — no skipped steps
- [ ] `orchestra-review` produces a PASS/FAIL verdict with evidence per criterion — no assumed passes
- [ ] `orchestra-merge` uses `--no-ff` and safe `-d` — no force operations
- [ ] Each skill's `allowed-tools` is scoped correctly to what it actually needs
- [ ] No skill reaches into another's stage (implement doesn't merge, review doesn't fix, merge doesn't implement)
- [ ] Status vocabulary flows end-to-end without gaps

---

## Risks

| Risk | Mitigation |
|---|---|
| Skills too vague to run AFK | Each skill has explicit quality checks and boundary statements |
| Review passes things it shouldn't | Criterion requires file/line evidence — "looks fine" not accepted |
| Merge resolves conflicts incorrectly | Ambiguous conflicts surface to user rather than guess |
