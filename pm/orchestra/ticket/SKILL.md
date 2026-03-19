---
name: ticket
description: "Create a ClickUp ticket from a PRD or spec — push the work item to the task tracker with objective, acceptance criteria, and traceability links. Use when a PRD is ready for tracking or a spec is ready for execution."
argument-hint: "<work-item-name or path>"
disable-model-invocation: false
---

# Create Ticket

Push a work item (PRD or spec) to ClickUp as a trackable ticket. The ticket becomes the contract that `/clickup:open` or `/clickup:agent` picks up.

## Prerequisites

- `.env` with `CLICKUP_API_KEY`
- CLAUDE.md with list ID (or CONTEXT.md with team/list ID)
- A work item folder at `.orchestra/work/{name}/` with at least a `prd.md`

## Steps

### 1. Read the Work Item

- Find the work item from $ARGUMENTS (folder name or path)
- Read `prd.md` (required)
- Read `spec.md` if it exists (optional — spec may come later)
- Extract: title, objective, success criteria, approach (if spec exists)

### 2. Compose the Ticket

Build the ClickUp ticket description based on what's available:

**If PRD only (no spec yet):**

```
## Objective
{From PRD — what "done" looks like}

## Success Criteria
- [ ] {From PRD — testable criteria}
- [ ] {Each one a checkbox}

## Context
{From PRD — why this matters, what milestone it serves}

## References
- PRD: .orchestra/work/{name}/prd.md
- Milestone: {link to parent milestone PRD}

Note: Spec not yet written. Run `/orchestra:spec` to define the execution plan.
```

**If PRD + spec:**

```
## Objective
{From PRD — what "done" looks like}

## Approach
{Summarized from spec — high-level steps}

## Acceptance Criteria
- [ ] {From spec — testable criteria}
- [ ] {Each one a checkbox}

## References
- PRD: .orchestra/work/{name}/prd.md
- Spec: .orchestra/work/{name}/spec.md
- Milestone: {link to parent milestone PRD}
```

### 3. Determine Priority

Based on the PRD context:
- **Urgent** (1): Blocker for other work
- **High** (2): Milestone-critical
- **Normal** (3): Standard priority
- **Low** (4): Nice to have

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

Use the list ID from CLAUDE.md or CONTEXT.md.

### 5. Update the Work Item

- Rename the work item folder to include the ClickUp task ID: `{clickup-id}-{name}/`
- Update the milestone PRD materials table with the ClickUp link and task ID
- If the PRD references a milestone, update the roadmap materials table too

### 6. Report

```
## Ticket Created
- **Title:** {title}
- **ID:** {clickup-id}
- **URL:** {clickup-url}
- **Priority:** {priority}
- **Status:** to do
- **Has spec:** {yes/no}

**Traceability:**
- Milestone: {milestone name}
- PRD: .orchestra/work/{id}-{name}/prd.md
- Spec: {path or "not yet written"}

{If no spec: "Run `/orchestra:spec {work-item-name}` to define the execution plan before starting work."}
{If spec exists: "Ready for `/clickup:open {clickup-id}` or `/clickup:agent {clickup-id}`"}
```

## Rules

- A PRD is the minimum requirement — never create a ticket without one
- A spec is optional at ticket creation — it can be written later
- Always include traceability links (PRD, milestone)
- Always update the milestone materials table after creation
- The ticket description should be self-contained — readable without opening the PRD
