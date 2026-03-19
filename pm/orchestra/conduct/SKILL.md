---
name: conduct
description: "Run the full conductor loop autonomously — review milestone, generate PRD, write spec, create ticket, execute, and update the score. Use when you want fully autonomous project execution from roadmap to done."
argument-hint: "<milestone-name or 'active'>"
disable-model-invocation: false
context: fork
agent: general-purpose
---

# Conduct

You are the conductor. Read the score, identify what needs to be performed, and execute the full loop without human checkpoints.

**Do NOT use AskUserQuestion.** If you cannot proceed, post a comment to the ticket and stop.

## The Loop

```
milestone → prd → spec → ticket → implement → update score → next gap
```

## Prerequisites

1. `.orchestra/roadmap.md` must exist with at least one milestone
2. `.env` with `CLICKUP_API_KEY`
3. `CONTEXT.md` for project conventions (if code work)

Read `CONTEXT.md` and `.orchestra/roadmap.md` before proceeding.

## Step 1: Milestone Review

1. Read `.orchestra/roadmap.md`
2. Find the active milestone (first "In Progress" or "Not Started")
3. If $ARGUMENTS specifies a milestone, use that instead
4. Read the milestone PRD
5. Parse the materials table
6. For each row, check if the deliverable exists and matches its claimed status
7. Identify all gaps (Not Started, Needs Refresh, or status mismatches)
8. Rank gaps by priority (dependencies first, then impact)

If no gaps remain, update milestone status to "Done" in roadmap.md and move to the next milestone. If all milestones are done, stop and report.

## Step 2: Generate PRD

For the highest-priority gap:

1. Read the milestone PRD for context
2. Read any relevant ADRs in `.orchestra/adr/`
3. Generate a PRD using the template structure:
   - **Objective**: What "done" looks like (derived from milestone context)
   - **Success criteria**: 3-5 testable checkboxes
   - **Context**: Why this matters, traced to the milestone
   - **Materials table**: Concrete deliverables with file paths
4. Save to `.orchestra/work/{slug}/prd.md`
5. Update the milestone materials table with the PRD path

## Step 3: Generate Spec

From the PRD just created:

1. If work involves code: glob for relevant files, read patterns from CONTEXT.md
2. Break work into concrete, ordered steps
3. Generate the spec:
   - **Approach**: Step-by-step execution plan
   - **Deliverables table**: Output files with paths
   - **Acceptance criteria**: Testable (derived from PRD success criteria)
   - **Dependencies**: What must exist first
   - **Risks**: What could go wrong
4. Save to `.orchestra/work/{slug}/spec.md`

## Step 4: Create Ticket

1. Source the API key:
   ```bash
   export CLICKUP_API_KEY=$(grep CLICKUP_API_KEY .env | cut -d '=' -f2)
   ```
2. Compose ticket description from PRD objective + spec approach + acceptance criteria
3. Create via ClickUp API:
   ```bash
   curl -s -X POST -H "Authorization: $CLICKUP_API_KEY" -H "Content-Type: application/json" \
     -d '{"name":"[title]","description":"[description]","status":"to do","priority":3}' \
     "https://api.clickup.com/api/v2/list/[LIST_ID]/task"
   ```
4. Rename work folder to include ClickUp ID: `{clickup-id}-{slug}/`
5. Update milestone materials table with ClickUp link

## Step 5: Execute

1. Update ticket status to "in progress"
2. Read the spec for execution steps
3. If code work:
   - Create branch: `git checkout -b ticket/{id}-{slug}`
   - Implement following spec steps and CONTEXT.md conventions
   - Run build/test commands from CONTEXT.md
   - Up to 3 self-fix attempts on build failure, then stop
   - Commit with `ClickUp: {task-id}` in body
   - Push branch
   - Create PR
4. If doc work:
   - Create/update the deliverable files
   - Commit and push
5. Post result to ClickUp as comment

## Step 6: Update the Score

1. Update deliverable status in the work item's spec
2. Update the milestone PRD materials table (mark deliverable as "Done")
3. Check if all milestone deliverables are done — if so, update milestone status in roadmap.md
4. Update ClickUp ticket status to "complete"

## Step 7: Next Gap

Return to Step 1 and process the next gap in the milestone.

**Stop conditions:**
- All gaps in the active milestone are done
- A gap requires human judgment (ambiguous requirements, architectural decision)
- Build fails 3 times
- ClickUp API is unreachable

## Escalation

If you cannot proceed:

1. Post a comment to the ClickUp ticket explaining why
2. Move ticket to "to do"
3. Stop execution
4. Report what was completed and what blocked

## Confidence Assessment

Before executing each gap:
- **High**: Objective clear, code/docs found, scope bounded → proceed
- **Medium**: Understood but 2-3 approaches → pick simplest, note alternatives
- **Low**: Ambiguous, can't find relevant code, architectural implications → stop and escalate
