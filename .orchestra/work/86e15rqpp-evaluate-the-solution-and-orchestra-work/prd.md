---
ticket: 86e15rqpp
status: complete
created_on: 2026-04-30
---

# Add Execution Pipeline to Orchestra

Orchestra covers the left side of the development lifecycle — ticket → PRD → spec → gherkin — but has no skills for the right side. Once a spec is approved, the methodology goes silent.

Sand Castle's planner → implementer → reviewer → merger pattern surfaced the gap clearly. We don't need Sand Castle as a dependency. We need the same four stages as native orchestra skills.

## Objective

Add three execution skills — `orchestra-implement`, `orchestra-review`, `orchestra-merge` — that complete the orchestra pipeline from approved spec to merged branch.

## Success Criteria

- [ ] `orchestra-implement` exists: takes an approved spec, creates a branch, executes steps, commits progress, marks complete
- [ ] `orchestra-review` exists: checks every acceptance criterion with evidence, produces a PASS/FAIL verdict, marks reviewed
- [ ] `orchestra-merge` exists: merges a reviewed branch to main, resolves conflicts, closes the work item
- [ ] Status vocabulary is end-to-end: `draft` → `approved` → `in-progress` → `complete` → `reviewed` → `closed`
- [ ] Each skill has clear boundaries — no skill crosses into the next stage's responsibility

## Context

The insight from studying Sand Castle: the pipeline stages are the right unit of abstraction. The Q&A → PRD → spec phase already works in orchestra and produces a spec tight enough to hand off. What was missing was anything to hand off to.

Skills are the right layer — not sub-agents. Once the skills are solid, AFK execution is a trivial loop controller. The hard part is the skill definitions, not the automation.

## Materials

| Deliverable | Path | Status |
|---|---|---|
| Implement skill | `skills/orchestra-implement/SKILL.md` | Done |
| Review skill | `skills/orchestra-review/SKILL.md` | Done |
| Merge skill | `skills/orchestra-merge/SKILL.md` | Done |

## References

- Sand Castle (`@aihero/sandcastle`) — source of the pipeline pattern, not adopted as a dependency
- `skills/dev-enforcer/SKILL.md` — informs the review skill's quality checks
