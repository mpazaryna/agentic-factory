---
description: "Translate a validated PRD into a technical spec. Reads the PRD, investigates the codebase, and writes a spec to the work item folder."
argument-hint: "<task-id>"
---

Use the `spec-writer` agent to produce a technical spec for ClickUp task `$ARGUMENTS`.

Steps:

1. Read your agent memory at `.claude/agent-memory/spec-writer/MEMORY.md`
2. Read the spec template at `.orchestra/work/TEMPLATES/spec.md`
3. Fetch the ticket via `mcp__clickup__clickup_get_task` with task_id `$ARGUMENTS`
4. Find and read the PRD at `.orchestra/work/` matching this task ID (look for `{task-id}-*/prd.md`)
5. If no PRD exists, stop and tell the user to run `/refine-ticket $ARGUMENTS` first
6. Deep-dive the codebase: read relevant source files, ADRs in `.orchestra/adr/`, and existing work items
7. Design the implementation — map every PRD acceptance criterion to a technical approach
8. Present the proposed spec to the user — do NOT write anything yet
9. After user approval, write `spec.md` into the existing `.orchestra/work/{task-id}-{name}/` folder alongside the PRD
10. Update the ClickUp ticket description to link to the spec
11. Update your agent memory with anything learned
