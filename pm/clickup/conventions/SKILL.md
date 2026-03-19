---
name: clickup-conventions
description: "ClickUp project conventions: status flow (to do → in progress → uat → complete), comment templates, branch naming, and ticket hygiene rules. Loaded automatically when working with ClickUp tickets."
user-invocable: false
---

# ClickUp Conventions

## Status Flow

```
to do → in progress → uat → complete
```

All statuses are **lowercase**. Transition via the REST API:

```bash
curl -s -X PUT -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
  -d '{"status":"in progress"}' "https://api.clickup.com/api/v2/task/$TASK_ID"
```

| Transition | When |
|-----------|------|
| → `in progress` | Branch created, work starting |
| → `uat` | Code complete, PR ready, awaiting user acceptance testing |
| → `complete` | UAT passed, PR merged |
| → `to do` | Escalation or abandonment — work paused, needs input |

## Comment Templates

### Agent Plan (posted before starting work)

```
## Agent Plan
**Confidence:** [High/Medium/Low]
**Size:** [XS/S/M/L]
**Files:** [list of files to modify]

### Understanding
[1-2 sentences]

### Approach
[Bullet list of planned changes]

### Risk
[UI-only, data model, architectural, etc.]
```

### Agent Result (posted after work is done)

```
## Agent Result
**PR:** #[number] (merged)
**Files changed:** [count]
**Build:** ✓

### Changes
[Bullet summary]

### Notes
[Unrelated issues discovered, observations for follow-up]
```

### Investigation Notes (posted after investigation)

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

### Agent Escalation (posted when stuck)

```
## Agent Escalation
**Reason:** [ambiguity/build-failure/architectural]

### Details
[What was attempted, what failed, what needs human input]

### Options
[2-3 interpretations or approaches if applicable]
```

## Rules

- **Never overwrite a ticket's description.** All updates go in comments via the REST API (`POST /task/{id}/comment`).
- **Never create or delete tickets** without explicit user instruction.
- **Never change priority, assignee, or dates** without user approval.
- **Status is the only field** commands update autonomously (and only in the documented flow).
- **Branch naming:** `ticket/{task-id}-{short-name}` where short-name is 2-3 kebab-case words from the title.
- **Commits reference tickets:** body includes `ClickUp: [task-id]`.
