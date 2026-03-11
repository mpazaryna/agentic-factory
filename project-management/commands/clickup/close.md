---
description: "Close a ticket — UAT check, doc review, PR, merge, done."
argument-hint: "<task-id>"
---

## Prerequisite

1. **CONTEXT.md** is required. Check for `CONTEXT.md` in the project root. If it does not exist, STOP and tell the user:
   > CONTEXT.md not found. Generate one with `/context-rebuild` or use the stub template from the agentic-factory repo (`templates/CONTEXT.stub.md`).

2. **ClickUp API key** is required. Read `.env` from the project root and extract `CLICKUP_API_KEY`. If missing, STOP and tell the user:
   > CLICKUP_API_KEY not found in .env. Add it: `echo "CLICKUP_API_KEY=pk_..." >> .env`

Read `CONTEXT.md` before proceeding — you'll need it for build commands and documentation paths.

## ClickUp API Reference

```bash
-H "Authorization: $CLICKUP_API_KEY"
```

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Get task | GET | `https://api.clickup.com/api/v2/task/{task_id}` |
| Post comment | POST | `https://api.clickup.com/api/v2/task/{task_id}/comment` |
| Update task | PUT | `https://api.clickup.com/api/v2/task/{task_id}` |

## Step 1: UAT Check

Source the API key:
```bash
export CLICKUP_API_KEY=$(grep CLICKUP_API_KEY .env | cut -d '=' -f2)
```

1. Fetch ticket — confirm it's in `in progress` or `uat` status:
   ```bash
   curl -s -H "Authorization: $CLICKUP_API_KEY" "https://api.clickup.com/api/v2/task/$TASK_ID"
   ```
2. Ask the user:
   - Did UAT pass? Any issues found?
   - If issues: fix on the same branch, commit, re-push, ask again
   - If pass: continue to Step 2

## Step 2: Doc Review

1. Check if any documentation files referenced in `CONTEXT.md` need updating for this ticket's changes
2. If doc generation scripts are listed in CONTEXT.md, run them
3. Check if an ADR is warranted (significant architectural decisions)
4. Commit doc changes on the same branch:
   - Conventional Commit (e.g., `docs: update [topic] for [feature]`)
   - Body: `ClickUp: [task-id]`
   - Body: `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`
5. Push: `git push`

If no doc changes needed, skip to Step 3.

## Step 3: Create PR

```bash
gh pr create --title "[ticket-title]" --body "$(cat <<'EOF'
## Summary
[1-3 bullet points]

## Test plan
- [UAT results — what was tested and by whom]

ClickUp: [task-id]

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

## Step 4: Merge

Confirm with user before merging.

```bash
gh pr merge --squash --delete-branch
git checkout main && git pull
```

## Step 5: Update ClickUp

1. Update status to `complete`:
   ```bash
   curl -s -X PUT -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
     -d '{"status":"complete"}' "https://api.clickup.com/api/v2/task/$TASK_ID"
   ```
2. Report:
   ```
   ## Done
   - PR: [url]
   - ClickUp: [task-id] → complete
   ```

## Build Commands (if needed for fixes)

Use the build/test commands from `CONTEXT.md` Tech Stack section.

## Rules

- **Never overwrite a ticket's description.** Use comments only.
- **Confirm merge with user** — don't auto-merge without approval.
