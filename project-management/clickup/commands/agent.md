---
description: "Autonomous ticket execution — no human checkpoints."
argument-hint: "<task-id>"
---

**Do NOT use `AskUserQuestion` at any point.** If you cannot proceed, escalate.

## Prerequisite

1. **CONTEXT.md** is required. Check for `CONTEXT.md` in the project root. If it does not exist, STOP and escalate:
   > CONTEXT.md not found. Cannot execute autonomously without project context. Generate one with `/context-rebuild` or use the stub template from the agentic-factory repo (`templates/CONTEXT.stub.md`).

2. **ClickUp API key** is required. Read `.env` from the project root and extract `CLICKUP_API_KEY`. If missing, STOP and escalate:
   > CLICKUP_API_KEY not found in .env. Cannot interact with ClickUp.

Read `CONTEXT.md` before proceeding — you'll need it for build commands, directory structure, conventions, test commands, and ADR locations.

## ClickUp API Reference

```bash
-H "Authorization: $CLICKUP_API_KEY"
```

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Get task | GET | `https://api.clickup.com/api/v2/task/{task_id}?include_subtasks=true` |
| Get comments | GET | `https://api.clickup.com/api/v2/task/{task_id}/comment` |
| Post comment | POST | `https://api.clickup.com/api/v2/task/{task_id}/comment` |
| Update task | PUT | `https://api.clickup.com/api/v2/task/{task_id}` |

## Step 1: Load & Comprehend

Source the API key:
```bash
export CLICKUP_API_KEY=$(grep CLICKUP_API_KEY .env | cut -d '=' -f2)
```

1. Fetch the task and comments:
   ```bash
   curl -s -H "Authorization: $CLICKUP_API_KEY" "https://api.clickup.com/api/v2/task/$TASK_ID?include_subtasks=true"
   curl -s -H "Authorization: $CLICKUP_API_KEY" "https://api.clickup.com/api/v2/task/$TASK_ID/comment"
   ```
2. Update status to `in progress`:
   ```bash
   curl -s -X PUT -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
     -d '{"status":"in progress"}' "https://api.clickup.com/api/v2/task/$TASK_ID"
   ```
3. Orient in codebase using `CONTEXT.md`:
   - Read ADRs/specs referenced in the ticket
   - Read relevant ADRs for the type of work (check CONTEXT.md conventions and Agent Knowledge Base sections)
   - Glob for related files in spec/decision directories listed in CONTEXT.md
4. Assess confidence (see below)
   - **Low** → escalate immediately, do not proceed

## Step 2: Post Plan to ClickUp

```bash
curl -s -X POST -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
  -d '{"comment_text":"## Agent Plan\n**Confidence:** ...\n**Size:** ...\n**Files:** ...\n\n### Understanding\n...\n\n### Approach\n...\n\n### Risk\n..."}' \
  "https://api.clickup.com/api/v2/task/$TASK_ID/comment"
```

**Do not wait for approval. Continue immediately.**

## Step 3: Branch & Implement

```bash
git checkout main && git pull
git checkout -b ticket/{task-id}-{short-name}
```

Implement following the project's conventions from `CONTEXT.md`. Only work on this ticket's scope — note unrelated issues in the result comment but do not fix them.

## Step 4: Build Gate

Run the project's build/test commands from the `CONTEXT.md` Tech Stack section.

- All pass → continue
- Build fails → read error, fix, rebuild
- **Up to 3 self-fix attempts.** After 3 → escalate

**Doc-only changes:** skip the build gate.

## Step 5: Commit & Push

1. `git status --short`
2. Stage files intentionally (no `git add .`)
3. Commit following the project's conventions from `CONTEXT.md`:
   - Conventional Commit, subject ≤ 72 chars, scope in kebab-case
   - Body: `ClickUp: [task-id]`
   - Body: `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`
4. `git push -u origin ticket/{task-id}-{short-name}`

## Step 6: Doc Review

1. Check if any documentation files referenced in `CONTEXT.md` need updating
2. If doc generation scripts are listed in CONTEXT.md, run them
3. Commit and push doc changes if any

## Step 7: Close

```bash
gh pr create --title "[ticket-title]" --body "$(cat <<'EOF'
## Summary
[1-3 bullet points]

## Test plan
- [x] Build: pass
- [Agent mode — autonomous execution]

ClickUp: [task-id]

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
gh pr merge --squash --delete-branch
git checkout main && git pull
```

Update ClickUp status to `complete`:
```bash
curl -s -X PUT -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
  -d '{"status":"complete"}' "https://api.clickup.com/api/v2/task/$TASK_ID"
```

## Step 8: Post Result to ClickUp

```bash
curl -s -X POST -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
  -d '{"comment_text":"## Agent Result\n**PR:** #[number] (merged)\n**Files changed:** [count]\n**Build:** ✓\n\n### Changes\n...\n\n### Notes\n..."}' \
  "https://api.clickup.com/api/v2/task/$TASK_ID/comment"
```

## Confidence Assessment

- **High** — Problem clear, code found, scope bounded, existing patterns cover it. Proceed.
- **Medium** — Understood but 2-3 valid approaches. Pick simplest, note alternatives in plan. Proceed.
- **Low** — Ambiguous requirements, can't find code, architectural implications beyond ADRs. **Escalate.**

## Escalation

1. Post comment:
   ```bash
   curl -s -X POST -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
     -d '{"comment_text":"## Agent Escalation\n**Reason:** ...\n\n### Details\n...\n\n### Options\n..."}' \
     "https://api.clickup.com/api/v2/task/$TASK_ID/comment"
   ```
2. Move ticket to `to do`:
   ```bash
   curl -s -X PUT -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
     -d '{"status":"to do"}' "https://api.clickup.com/api/v2/task/$TASK_ID"
   ```
3. **Stop execution.**

## Rules

- **Never overwrite a ticket's description.** Use comments only.
- **Only this ticket's scope.** Unrelated issues → note in result, don't fix.
