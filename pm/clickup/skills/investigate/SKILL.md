---
name: investigate
description: "Investigate a ClickUp ticket — analyze scope, discuss open questions, and refine before starting work. Use when a user wants to assess a ticket's readiness, clarify requirements, or refine acceptance criteria without writing code."
argument-hint: "<task-id or search query>"
disable-model-invocation: false
---

## Prerequisite

1. **CONTEXT.md** is required. Check for `CONTEXT.md` in the project root. If it does not exist, STOP and tell the user:
   > CONTEXT.md not found. Generate one with `/context-rebuild` or use the stub template from the agentic-factory repo (`templates/CONTEXT.stub.md`).

2. **ClickUp API key** is required. Read `.env` from the project root and extract `CLICKUP_API_KEY`. If missing, STOP and tell the user:
   > CLICKUP_API_KEY not found in .env. Add it: `echo "CLICKUP_API_KEY=pk_..." >> .env`

Read `CONTEXT.md` before proceeding — you'll need it for directory structure, conventions, and ADR locations.

## ClickUp API Reference

```bash
-H "Authorization: $CLICKUP_API_KEY"
```

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Get task | GET | `https://api.clickup.com/api/v2/task/{task_id}?include_subtasks=true` |
| Get comments | GET | `https://api.clickup.com/api/v2/task/{task_id}/comment` |
| Post comment | POST | `https://api.clickup.com/api/v2/task/{task_id}/comment` |
| Search tasks | GET | `https://api.clickup.com/api/v2/team/{team_id}/task?name={query}` |

## Load Ticket

Source the API key:
```bash
export CLICKUP_API_KEY=$(grep CLICKUP_API_KEY .env | cut -d '=' -f2)
```

1. If `$ARGUMENTS` looks like a task ID (e.g., `86e065njp`), fetch directly:
   ```bash
   curl -s -H "Authorization: $CLICKUP_API_KEY" "https://api.clickup.com/api/v2/task/$TASK_ID?include_subtasks=true"
   curl -s -H "Authorization: $CLICKUP_API_KEY" "https://api.clickup.com/api/v2/task/$TASK_ID/comment"
   ```
2. If it looks like a search query, search first using the team ID from CONTEXT.md External Integrations section:
   ```bash
   curl -s -H "Authorization: $CLICKUP_API_KEY" "https://api.clickup.com/api/v2/team/$TEAM_ID/task?name=$QUERY"
   ```
   Present matches, ask user to pick one, then fetch.

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

Using the directory structure and ADR locations from `CONTEXT.md`:

- Read any ADRs or specs referenced in the ticket
- Read relevant ADRs for the type of work
- Glob for related files in spec/decision directories listed in CONTEXT.md
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

1. Post a comment via the API:
   ```bash
   curl -s -X POST -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
     -d '{"comment_text":"## Investigation Notes\n\n..."}' \
     "https://api.clickup.com/api/v2/task/$TASK_ID/comment"
   ```
   Comment content:
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
2. Ask the user if they want to update priority or size fields

## Rules

- **Never change the ticket's status.** Investigation is pre-work.
- **Never create a branch.** Stay on current branch.
- **Never overwrite a ticket's description.** All updates go in comments.
- **This is a discussion, not execution.** Do not implement code changes.
