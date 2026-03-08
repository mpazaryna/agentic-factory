---
description: "Investigate a ticket — discuss, analyze, and refine before starting work."
argument-hint: "<task-id or search query>"
---

## Load Ticket

1. If `$ARGUMENTS` looks like a task ID (e.g., `86e065njp`), fetch directly:
   - `clickup_get_task` with `subtasks: true`
   - `clickup_get_task_comments`
2. If it looks like a search query, search first:
   - `clickup_search` with `keywords`, filter `asset_types: ["task"]`
   - Present matches, ask user to pick one, then fetch

**Do NOT change the ticket's status.** It stays where it is.

**Present as:**

```
# [Task Name]
> ID: [id] | Status: [status] | Priority: [priority] | Assignee: [assignee]
> URL: [url]

## Description
[full description]

## Subtasks
[list if any]

## Comments
[summarize key points]
```

## Orient (No Branch)

Stay on the current branch. Do not create a branch or switch branches.

- Read any ADRs or specs referenced in the ticket
- If UI work: read `ADR-000-platform-config`
- If SOAP/AI work: read `ADR-000-apple-intelligence` + `ADR-019`
- Glob `.orchestra/decisions/` and `.orchestra/specs/` for related context
- Read relevant source files to understand current state

## Analyze

Present a structured analysis to the user:

```
## Analysis

### Clarity
- Is "done" obvious? [yes/no + explanation]
- Acceptance criteria: [explicit / inferred / missing]

### Scope
- Size estimate: [S/M/L/XL]
- Bounded or could sprawl? [assessment]
- Files likely involved: [list]

### Technical Context
- Related ADRs/specs: [list]
- Existing patterns to follow: [list]
- Dependencies or blockers: [list]

### Risks & Open Questions
- [numbered list of concerns, ambiguities, or design decisions]

### Suggestions
- [improvements to the ticket description or criteria]
- [recommended approach if clear enough]
```

## Discuss

Use `AskUserQuestion` to engage the user. This is a conversation — work through the open questions, trade ideas, and refine understanding together.

## Refine (Optional)

If the discussion produces improvements to the ticket:

1. Post a comment via `clickup_create_task_comment` summarizing:
   ```
   ## Investigation Notes

   ### Clarifications
   [decisions made during discussion]

   ### Acceptance Criteria (Refined)
   - [ ] [criterion 1]
   - [ ] [criterion 2]

   ### Recommended Approach
   [brief technical plan]

   ### Open Items
   [anything still unresolved]
   ```
2. Ask the user if they want to update priority or size fields via `clickup_update_task`

## Rules

- **Never change the ticket's status.** Investigation is pre-work.
- **Never create a branch.** Stay on current branch.
- **Never overwrite a ticket's description.** All updates go in comments (`clickup_create_task_comment`).
- **This is a discussion, not execution.** Do not implement code changes.
