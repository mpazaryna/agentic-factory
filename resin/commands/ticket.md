---
description: Work a ClickUp ticket through its full lifecycle — fetch, implement, UAT, docs, close.
argument-hint: [agent|uat|docs|close] [task-id or search query]
---

## Context

- Each ticket gets its own branch: `ticket/{id}-{short-name}`
- Branch is created from `main`, merged back to `main` via PR when complete
- ClickUp workspace has MCP tools available
- Project conventions live in `CLAUDE.md`, ADRs in `.orchestra/decisions/`
- **Never overwrite a ticket's description.** Use `clickup_update_task` only for status, dates, priority, and assignees. All investigation results, triage decisions, and progress updates go in **comments** (`clickup_create_task_comment`).

## Usage

```
/ticket <task-id>              # Human-in-loop (fetch & review)
/ticket agent <task-id>        # Agent mode (fully autonomous)
/ticket uat <task-id>          # Phase 2 (UAT testing)
/ticket docs <task-id>         # Phase 3 (doc review)
/ticket close <task-id>        # Phase 4 (merge & close)
```

## Phase Detection

Parse `$ARGUMENTS` to determine which mode/phase:
- If first word is `agent` → **Agent Mode** (remaining args = task ID)
- If first word is `uat` → Phase 2 (remaining args = task ID)
- If first word is `docs` → Phase 3 (remaining args = task ID)
- If first word is `close` → Phase 4 (remaining args = task ID)
- Otherwise → Phase 1, human-in-loop (all args = task ID or search query)

---

## Agent Mode — Fully Autonomous

**Invocation:** `/ticket agent <task-id>`

The agent runs the full ticket lifecycle without human checkpoints. Same phases as human-in-loop, but pauses are replaced with build gates, confidence assessment, and ClickUp comments.

**Do NOT use `AskUserQuestion` at any point during agent mode.** If you cannot proceed, escalate (see Escalation below).

### Step 1: Load & Comprehend

1. Fetch the ticket with `clickup_get_task` (with `subtasks: true`) and `clickup_get_task_comments`
2. Update ticket status to `in progress` with `clickup_update_task`
3. **Orient in the codebase:**
   - Read any ADRs or specs referenced in the ticket
   - If UI work: read `ADR-000-platform-config`
   - If SOAP/AI work: read `ADR-000-apple-intelligence` + `ADR-019`
   - Glob for related files, check `.orchestra/specs/` for existing specs
4. **Assess confidence** (see Confidence Assessment below)
   - If **Low** → escalate immediately, do not proceed
5. Evaluate the ticket checklist internally:
   - Clear objective, scope, acceptance criteria, technical pointers, dependencies
   - Infer t-shirt size from codebase exploration
   - Resolve ambiguities from codebase context — do NOT ask the user

### Step 2: Post Agent Plan to ClickUp

Post a structured comment to the ticket using `clickup_create_task_comment`:

```
## Agent Plan
**Confidence:** [High/Medium/Low]
**Size:** [XS/S/M/L]
**Files:** [list of files to modify]

### Understanding
[What the agent thinks the problem is — 1-2 sentences]

### Approach
[Bullet list of planned changes]

### Risk
[Assessment: UI-only, data model, architectural, etc.]
```

**Do not wait for approval. Continue immediately.**

### Step 3: Branch & Implement

1. Create branch: `git checkout main && git pull && git checkout -b ticket/{task-id}-{short-name}`
2. Implement the changes following all `CLAUDE.md` conventions
3. Only work on this ticket's scope — if you discover unrelated issues, note them in the result comment but do not fix them

### Step 4: Build Gate

Run both builds:
```bash
cd native/pab && xcodebuild -project pab.xcodeproj -scheme pab-macOS -configuration Debug build
cd native/pab && xcodebuild -project pab.xcodeproj -scheme pab-iOS -configuration Debug -destination 'platform=iOS Simulator,name=iPhone 17 Pro' build
```

- If both pass → continue
- If a build fails → read the error, fix the issue, rebuild
- **Up to 3 self-fix attempts.** After 3 failures → escalate

**For doc-only changes:** skip the build gate entirely.

### Step 5: Commit & Push

1. `git status --short` to review changes
2. Stage files intentionally (no `git add .`)
3. Commit with Conventional Commit message:
   - Subject ≤ 72 chars, scope in kebab-case
   - Include `ClickUp: [task-id]` in the body
   - Include `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`
4. Push: `git push -u origin ticket/{task-id}-{short-name}`

### Step 6: Doc Review

1. Check if any `docs/uat/*.md` files need updating
2. If UAT walkthroughs were modified, recompose guides:
   ```bash
   uv run scripts/compose-guide.py --all
   ```
3. Commit and push doc changes if any

### Step 7: Close

1. Create PR:
   ```bash
   gh pr create --title "[ticket-title]" --body "$(cat <<'EOF'
   ## Summary
   [1-3 bullet points]

   ## Test plan
   - [x] macOS build: pass
   - [x] iOS build: pass
   - [Agent mode — autonomous execution]

   ClickUp: [task-id]

   🤖 Generated with [Claude Code](https://claude.com/claude-code)
   EOF
   )"
   ```
2. Merge: `gh pr merge --squash --delete-branch`
3. Return to main: `git checkout main && git pull`
4. Update ClickUp status to `complete`

### Step 8: Post Agent Result to ClickUp

Post a structured result comment to the ticket using `clickup_create_task_comment`:

```
## Agent Result
**PR:** #[number] (merged)
**Files changed:** [count]
**Builds:** macOS ✓ | iOS ✓

### Changes
[Bullet summary of what was done and why]

### Notes
[Any unrelated issues discovered, or observations for follow-up]
```

### Confidence Assessment

After orientation (reading ticket + exploring codebase), self-assess:

- **High** — Problem is clear, relevant code found, scope is bounded, existing patterns cover it. Proceed autonomously.
- **Medium** — Problem is understood but 2-3 valid approaches exist. Pick the simplest approach, note alternatives in the plan comment. Proceed autonomously.
- **Low** — Ambiguous requirements that codebase context cannot resolve, cannot locate relevant code, or architectural implications beyond existing ADRs. **Escalate.**

### Escalation

When the agent cannot proceed:

1. Post a comment to the ticket explaining the blocker:
   ```
   ## Agent Escalation
   **Reason:** [ambiguity/build-failure/architectural]

   ### Details
   [What was attempted, what failed, what needs human input]

   ### Options
   [If applicable, list the 2-3 interpretations or approaches the agent can't choose between]
   ```
2. Move ticket to `blocked` status: `clickup_update_task` with `status: "to do"`
3. **Stop execution.** Do not attempt workarounds or guesses.

---

## Phase 1 — Fetch, Review & Implement (Human-in-Loop)

### 1a. Load Ticket

1. If the argument looks like a task ID (e.g., `abc123`, `DEV-42`), fetch it directly:
   - Use `clickup_get_task` with `task_id` and `subtasks: true`
2. If it looks like a search query, search first:
   - Use `clickup_search` with `keywords` filtered to `asset_types: ["task"]`
   - Present matching tasks and ask the user to pick one
   - Fetch the selected task with `clickup_get_task`
3. Also fetch comments with `clickup_get_task_comments` — they often contain requirements.
4. Update ticket status to `in progress`: `clickup_update_task` with `status: "in progress"`

**Present the ticket as:**

```
# [Task Name]
> ID: [id] | Status: [status] | Priority: [priority] | Assignee: [assignee]
> URL: [url]

## Description
[full description]

## Subtasks
[list if any]

## Comments
[summarize key points from comments]
```

### 1b. Evaluate & Clarify

Analyze the ticket against this checklist:

- [ ] **Clear objective** — Is it obvious what "done" looks like?
- [ ] **Scope** — Is the work bounded, or could it sprawl?
- [ ] **Acceptance criteria** — Are there explicit criteria, or do we need to infer them?
- [ ] **Technical pointers** — Does it reference files, ADRs, or components?
- [ ] **Dependencies** — Does it depend on other tickets or features?
- [ ] **T-shirt size** — Does the complexity match the estimate (if any)?

For each gap, ask a clarifying question using `AskUserQuestion`. Group related questions (max 4 per call).

**Do not proceed until all ambiguities are resolved.**

### 1c. Create Branch

Create the branch locally from `main`.

```bash
git checkout main && git pull                    # start from fresh main
git checkout -b ticket/{task-id}-{short-name}    # create ticket branch
```

If already on another ticket branch mid-work, skip the checkout:
```bash
git fetch origin && git checkout -b ticket/{task-id}-{short-name} origin/main
```

Where `{short-name}` is 2-3 kebab-case words from the ticket title (e.g., `ticket/86e03kkxw-em-absence-derivation`).

The branch only gets pushed to origin in step 1f (after implementation), keeping remote clean.

**Verify you are on the new branch before writing any code.**

### 1d. Orient & Plan

1. **Orient in the codebase:**
   - Read any ADRs or specs referenced in the ticket
   - If the ticket involves UI: read `ADR-000-platform-config`
   - If the ticket involves SOAP/AI: read `ADR-000-apple-intelligence` + `ADR-019`
   - Glob `docs/` and `.orchestra/decisions/` for related context
   - Check if a spec already exists: `.orchestra/specs/*{ticket-keywords}*`

2. **Enter plan mode** to design the implementation approach.
   - If the task is multi-session, create a spec at `.orchestra/specs/{clickup-task-number}-{short-name}.md`
   - Use `plannotator` skill to open the plan in the browser for interactive review
   - Wait for user approval before proceeding

### 1e. Implement

Do the work. Follow all project conventions from `CLAUDE.md`:

- PlatformConfig for layout values (no magic numbers)
- Three-layer AI architecture if touching SOAP/AI
- SwiftData patterns for model changes
- No ViewModels — use `@State`, `@Environment`, `@Query`

**IMPORTANT: Only work on this ticket's scope.** If you discover an unrelated bug or improvement, create a new ClickUp ticket for it — do not fix it on this branch.

### 1f. Review & Commit

1. **Code review** — use `plannotator-review` skill to open an interactive diff review in the browser. Wait for user approval before committing.

2. **Commit the work** following the `git:commit` pattern:
   - `git status --short` to review changes
   - Diff each file, verify no secrets or credentials
   - Stage files intentionally (no `git add .`)
   - Conventional Commit message (feat/fix/refactor/etc.)
   - Subject ≤ 72 chars, scope in kebab-case
   - Include the ClickUp task ID in the commit body: `ClickUp: [task-id]`

2. **Run regression tests** — if the ticket touches SOAP/AI, test against a known fixture (e.g., `docs/fixtures/006-jd-joe-multi-region.md`) BEFORE pushing.

3. **Push the branch:**
   ```bash
   git push -u origin ticket/{task-id}-{short-name}
   ```

4. **Update ClickUp ticket status** to `uat`:
   - Use `clickup_update_task` with `status: "uat"`

5. **Report:**
   ```
   ## Phase 1 Complete
   - Branch: ticket/{task-id}-{short-name}
   - Commit(s): [hash(es)] [message(s)]
   - Files changed: [count]
   - ClickUp: [task-id] → uat
   - Next: `/ticket uat {task-id}` after manual testing
   ```

---

## Phase 2 — UAT

User has tested the feature. This phase records the result.

1. Fetch the ticket to confirm it's in `uat` status
2. Ask the user:
   - Did UAT pass? Any issues found?
   - If issues: fix on the same branch, commit, re-push
   - If pass: proceed to Phase 3

---

## Phase 3 — Doc Review

1. Check if any `docs/uat/*.md` files need updating for this ticket's changes
2. If UAT walkthroughs were added or modified, recompose guides:
   ```bash
   uv run scripts/compose-guide.py --all
   ```
3. Check if an ADR is warranted (significant architectural decisions)
4. Commit doc changes on the same branch and push

---

## Phase 4 — Close

1. **Create PR** from `ticket/{task-id}-{short-name}` → `main`:
   ```bash
   gh pr create --title "[ticket-title]" --body "$(cat <<'EOF'
   ## Summary
   [1-3 bullet points]

   ## Test plan
   - [UAT results]

   ClickUp: [task-id]

   🤖 Generated with [Claude Code](https://claude.com/claude-code)
   EOF
   )"
   ```

2. **Merge the PR** (after user approval):
   ```bash
   gh pr merge --squash --delete-branch
   ```

3. **Return to main:**
   ```bash
   git checkout main && git pull
   ```

4. **Update ClickUp ticket status** to `complete`:
   - Use `clickup_update_task` with `status: "complete"`

5. **Report:**
   ```
   ## Done
   - PR: [url]
   - ClickUp: [task-id] → complete
   ```

---

## Abandoning a Ticket

If a ticket needs to be abandoned mid-work:

1. The branch contains all changes — `main` is untouched
2. Simply switch away: `git checkout main`
3. The branch can be deleted or kept for future reference
4. Update ClickUp with a comment explaining why, move back to `in progress` or `to do`

No stashing, no reverting, no force-pushing. The branch is the isolation.
