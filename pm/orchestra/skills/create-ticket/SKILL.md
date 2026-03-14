---
name: create-ticket
description: "Create a ClickUp ticket from an approved spec — push the execution contract to the task tracker with proper description, links, and acceptance criteria. Use when a spec is approved and ready for execution."
argument-hint: "<spec-path or work-item-name>"
disable-model-invocation: true
---

# Create Ticket

Push an approved spec to ClickUp as an executable ticket. The ticket becomes the contract that `/open` or `/agent` picks up.

## Prerequisites

- `.env` with `CLICKUP_API_KEY`
- CONTEXT.md with team ID and list ID (or use the list from CLAUDE.md)
- An approved spec at `.orchestra/work/{id}-{name}/spec.md`
- The parent PRD at `.orchestra/work/{id}-{name}/prd.md`

## Steps

### 1. Read the Spec and PRD

- Find the spec from $ARGUMENTS
- Read both `spec.md` and `prd.md` from the work item folder
- Extract: title, objective, acceptance criteria, approach summary

### 2. Compose the Ticket

Build the ClickUp ticket description:

```
## Objective
{From PRD — what "done" looks like}

## Approach
{Summarized from spec — high-level steps}

## Acceptance Criteria
- [ ] {From spec — testable criteria}
- [ ] {Each one a checkbox}

## References
- PRD: .orchestra/work/{id}-{name}/prd.md
- Spec: .orchestra/work/{id}-{name}/spec.md
- Milestone: {link to parent milestone PRD}
```

### 3. Determine Priority and Size

Based on the spec:
- **Priority**: Urgent (blocker) / High (milestone-critical) / Normal / Low
- **Size estimate**: Based on number of steps and complexity

Ask the user to confirm priority if unclear.

### 4. Create the Ticket

Source the API key:
```bash
export CLICKUP_API_KEY=$(grep CLICKUP_API_KEY .env | cut -d '=' -f2)
```

Create via ClickUp API:
```bash
curl -s -X POST -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
  -d '{"name":"[title]","description":"[composed description]","status":"to do","priority":[priority]}' \
  "https://api.clickup.com/api/v2/list/[LIST_ID]/task"
```

Use the list ID from CONTEXT.md or CLAUDE.md.

### 5. Update the Work Item

- Rename the work item folder to include the ClickUp task ID: `{clickup-id}-{name}/`
- Update the spec status to "In Progress" if work begins immediately
- Update the milestone PRD materials table with the ClickUp link

### 6. Report

```
## Ticket Created
- **Title:** {title}
- **ID:** {clickup-id}
- **URL:** {clickup-url}
- **Priority:** {priority}
- **Status:** to do

**Traceability:**
- Milestone: {milestone name}
- PRD: .orchestra/work/{id}-{name}/prd.md
- Spec: .orchestra/work/{id}-{name}/spec.md

Ready for `/open {clickup-id}` or `/agent {clickup-id}`
```

## Rules

- Never create a ticket without an approved spec
- Always include traceability links (PRD, spec, milestone)
- Always update the milestone materials table after creation
- The ticket description should be self-contained — an agent reading only the ticket should understand what to do
