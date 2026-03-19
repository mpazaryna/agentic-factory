# Orchestra Agents

## Lenny

Named after Leonard Bernstein. The autonomous conductor.

Lenny runs the full orchestra loop — milestone review, PRD, spec, ticket, implement, update score — without stopping to ask questions. He reads the skills (conventions, milestone, prd, spec, ticket, devlog) as his subject matter expertise, then performs.

### Install

```
/plugin install orchestra@agentic-factory
```

Lenny is included in the orchestra plugin. No separate installation needed.

### Human-in-the-Loop

Use the interactive skills directly. You drive each step:

```
/orchestra:milestone active        # Review gaps in the active milestone
/orchestra:prd <gap-name>          # Write a PRD for the gap (presents for approval)
/orchestra:spec <prd-path>         # Write a spec from the PRD (presents for approval)
/orchestra:ticket <spec-path>      # Push to ClickUp
/orchestra:devlog                  # Log the session
```

Each skill stops and asks before writing. You review, refine, approve. The skills are the same knowledge Lenny uses — you're just conducting manually.

### Autonomous (Lenny)

Agents are not slash commands. They're invoked conversationally — ask Claude to use lenny by name:

```
"ask lenny to review the active milestone"
"have lenny run the full loop on M2"
"can lenny look at the active milestones"
```

Lenny will:
1. Load all orchestra skills as domain expertise
2. Read the roadmap and find the active milestone
3. Identify gaps in the materials table
4. For each gap: write PRD → write spec → create ClickUp ticket → implement → update score
5. Move to the next gap until the milestone is done or a blocker is hit

**No approval gates.** If Lenny can't proceed (ambiguous requirements, build failures after 3 retries, unreachable API), he posts a comment to the ClickUp ticket, stops, and reports what blocked him.

### When to Use Which

| Situation | Approach |
|-----------|----------|
| Exploring a new milestone, uncertain scope | Human-in-the-loop with `/milestone` then `/prd` |
| Well-defined gaps, clear acceptance criteria | "ask lenny to run the active milestone" |
| Single PRD or spec needed | Interactive: `/orchestra:prd` or `/orchestra:spec` |
| Batch execution across multiple gaps | "have lenny run the full loop on M2" |
| First time setting up .orchestra/ | Interactive: `/orchestra:scaffold` (always manual) |

### How Lenny Uses Skills

Lenny is not a replacement for the skills — he's built on top of them. Before executing, he reads:

- **conventions** — methodology rules, folder structure, document ownership
- **milestone** — how to diff materials tables and identify gaps
- **prd** — PRD structure, objective framing, success criteria format
- **spec** — execution spec format, approach design, acceptance criteria
- **ticket** — ClickUp API patterns, status flow, comment templates
- **devlog** — session logging format

The skills are the sheet music. Lenny is the conductor who reads it and performs.

### Prerequisites

Same as the orchestra plugin:

1. `.orchestra/roadmap.md` with at least one milestone
2. `.env` with `CLICKUP_API_KEY` (for ticket creation)
3. `CONTEXT.md` (for code-related work)

Run `/orchestra:scaffold` first if the project doesn't have `.orchestra/` yet.
