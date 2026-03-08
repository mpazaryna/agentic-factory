---
description: "Refine a ClickUp ticket into a formal PRD. Investigates the codebase, formalizes business intent, and writes a PRD to .orchestra/prds/."
argument-hint: "<task-id>"
---

Use the `clickup-refiner` agent to produce a PRD for ClickUp task `$ARGUMENTS`.

Steps:

1. Read your agent memory at `.claude/agent-memory/clickup-refiner/MEMORY.md`
2. Read the PRD template at `.orchestra/work/TEMPLATES/prd.md`
3. Fetch the ticket via `mcp__clickup__clickup_get_task` with task_id `$ARGUMENTS` and `subtasks: true`
4. Investigate the codebase to understand how the relevant area works today — check ADRs in `.orchestra/adr/`, existing work items, and source code
5. Draft a PRD following the template — focus on business intent, not technical implementation
6. Present your findings and the proposed PRD to the user — do NOT write anything yet
7. After user approval, create `.orchestra/work/{task-id}-{short-name}/` and write `prd.md` there
8. Update the ClickUp ticket description to link to the PRD
9. Update your agent memory with anything learned
