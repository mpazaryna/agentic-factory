---
description: "Fetch a ticket, create a branch, and start working."
argument-hint: "<task-id or search query>"
---

## Prerequisite

1. **CONTEXT.md** is required. Check for `CONTEXT.md` in the project root. If it does not exist, STOP and tell the user:
   > CONTEXT.md not found. Generate one with `/context-rebuild` or use the stub template from the agentic-factory repo (`templates/CONTEXT.stub.md`).

2. **ClickUp API key** is required. Read `.env` from the project root and extract `CLICKUP_API_KEY`. If missing, STOP and tell the user:
   > CLICKUP_API_KEY not found in .env. Add it: `echo "CLICKUP_API_KEY=pk_..." >> .env`

Read `CONTEXT.md` before proceeding — you'll need it for build commands, directory structure, conventions, and ADR locations.

## ClickUp API Reference

All ClickUp operations use the REST API v2 with curl. Always pass the API key as a header:

```bash
-H "Authorization: $CLICKUP_API_KEY"
```

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Get task | GET | `https://api.clickup.com/api/v2/task/{task_id}?include_subtasks=true` |
| Get comments | GET | `https://api.clickup.com/api/v2/task/{task_id}/comment` |
| Post comment | POST | `https://api.clickup.com/api/v2/task/{task_id}/comment` |
| Update task | PUT | `https://api.clickup.com/api/v2/task/{task_id}` |
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
3. Update status to `in progress`:
   ```bash
   curl -s -X PUT -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
     -d '{"status":"in progress"}' "https://api.clickup.com/api/v2/task/$TASK_ID"
   ```

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

## Evaluate

Check the ticket against:
- [ ] Clear objective — is "done" obvious?
- [ ] Scope — bounded or could sprawl?
- [ ] Acceptance criteria — explicit or inferred?
- [ ] Technical pointers — files, ADRs, components referenced?
- [ ] Dependencies — blocked by other tickets?

Ask clarifying questions with `AskUserQuestion` for any gaps. **Do not proceed until ambiguities are resolved.**

## Create Branch

```bash
git checkout main && git pull
git checkout -b ticket/{task-id}-{short-name}
```

If already on another branch:
```bash
git fetch origin && git checkout -b ticket/{task-id}-{short-name} origin/main
```

`{short-name}` = 2-3 kebab-case words from the ticket title. **Verify you're on the new branch before writing code.**

## Orient

Using the directory structure and ADR locations from `CONTEXT.md`:

- Read any ADRs or specs referenced in the ticket
- Read relevant ADRs for the type of work (check `CONTEXT.md` conventions and Agent Knowledge Base sections)
- Glob for related files in spec/decision directories listed in CONTEXT.md
- If multi-session: create a spec file in the project's spec directory

## Plan & Implement

Enter plan mode to design the approach. Wait for user approval before coding.

After implementation, commit following the project's conventions from `CONTEXT.md`:
- Subject ≤ 72 chars, scope in kebab-case
- Body includes `ClickUp: [task-id]`
- Body includes `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`
- Stage files intentionally (no `git add .`)

Push when ready:
```bash
git push -u origin ticket/{task-id}-{short-name}
```

## Rules

- **Never overwrite a ticket's description.** Status, dates, priority, assignees only. All updates go in comments.
- **Only work on this ticket's scope.** Unrelated issues → new ClickUp ticket.
- **Abandoning:** just `git checkout main`. The branch is the isolation. Post a comment explaining why, move ticket back to `to do`.
