---
created_on: 2026-05-06
---

# Orchestra as SDLC — Language Refinement and Agentic Velocity Guard

## The Starting Point

The session opened with an external analysis of Orchestra's positioning — the argument that Orchestra isn't a novel methodology, it's the SDLC Matt has practiced for 35 years, encoded so agents can execute it. The framing: every component traces to a proven discipline. PRD = spec-driven development. ADR = Nygard 2011. Implement = branch/commit/test cycle. The novel layer is the runtime — agents executing against artifacts as primary input rather than humans translating from them.

The original analysis raised two objections: single-conductor assumption and missing post-merge phases. Both turned out to be wrong. The conductor is already an agent (multi-conductor is architecturally solved), and `orchestra-implement` is the right half of the pipeline. The analysis was thinking about the methodology from the outside; reading the actual skills dissolved both concerns.

The refinement direction that survived: lean heavily into SDLC language while keeping Orchestra's metaphor intact. Orchestra IS the SDLC — the metaphor teaches it, the SDLC language grounds it.

## What Changed

### orchestra-program — Major Rewrite

The programme is the right metaphor for this skill: it's the document handed to you before the performance begins. We rewrote it to match that purpose.

Added **The Roots** — an ancestry table mapping each Orchestra component to its SDLC predecessor. Nothing was invented, everything was encoded. The table makes the credibility claim checkable rather than asserted.

Added **The Governing Principle**: *The score is written before the performance begins.* Agents execute against artifacts, not instructions. A conductor without a score is improvising. An agent without a spec is guessing.

Split the Pipeline into two named halves: **Score — Requirements & Design** and **Performance — Build & Deliver**. This naming now runs consistently through the Pipeline table, the Skill Index, and the headers. The Skill Index gained a third group: **Persistent Record — Spans the Lifecycle** for ADR, devlog, and UML — the programme notes that exist independently of any single work item.

`orchestra-plan` and `orchestra-eval` were missing from the index entirely. Added.

### ClickUp Removal

ClickUp was hardcoded in five skill bodies — `prd`, `ticket`, `spec`, `plan`, `milestone`. All replaced with tool-agnostic language ("issue tracker", "ticket-id"). Orchestra is a methodology, not a ClickUp integration. The `clickup-backfill` skill exists for teams using ClickUp; the methodology itself shouldn't assume it.

### orchestra-prd — Milestone Constraint Removed

The PRD skill opened with "Generate a PRD for a work item that traces back to a milestone." Both the description and prerequisites required an active milestone as a precondition. That's too narrow — a PRD can originate from a ticket, a stakeholder request, a spike finding, or a decision made mid-session.

The prerequisite now reads: "a milestone gap is not required to write a PRD." Step 6 (Update the Milestone) is now conditional — if an active milestone exists, link it; if not, note it in the output and skip. The quality check softened from "context traces back to a milestone" to "context explains why this work matters — and traces to a milestone if one exists."

### Agentic Velocity Guard — orchestra-implement

This was the sharpest insight of the session.

At agentic speed, a large amount of work can be committed, reviewed, and merged before anyone asks "why did we build this and does it serve the roadmap?" The danger isn't orphaned work items — it's that orphaned work items accumulate silently. The map stops matching the territory, and the map becomes useless.

Added a pre-flight milestone traceability check to `orchestra-implement`, after loading the spec but before creating the branch. It reads the roadmap, scans every milestone's materials table, and checks whether this work item appears anywhere.

If found: note the milestone in the report and proceed.

If not found: surface an advisory and wait for explicit confirmation before continuing.

> "This work item does not appear in any milestone's materials table — it has no stated goal it serves. Proceed anyway, or assign it to a milestone first?"

This is advisory, not a blocker. At agentic speed, work sometimes moves faster than the roadmap. The check makes the gap visible so the human consciously decides, rather than silently accepting scope drift. The comment in the skill says exactly this — so a future agent reading it understands the tradeoff is deliberate.

The realization behind this: in human-paced development, a developer pauses to think before writing code. Agents don't pause. They're always ready to execute. The human gate is the only thing stopping them. The milestone check is a gate inserted at the last responsible moment — after planning is done, before any code is written.

### Bugs Fixed

`orchestra-roadmap` Bootstrap Mode had a duplicate Step 3. "Milestones" and "Draft the Roadmap" were both labeled Step 3. Steps 4 and 5 followed, putting the numbering off by one.

`orchestra-review` had Step 8 (Write the Devlog) appearing after the Quality Checks section. Quality Checks read as the final gate; then step 8 appeared after it. Structurally wrong — devlog writing is part of the review process, not a postscript. Moved above Quality Checks. Added to the checklist.

### Language Tightened

`orchestra-review` quality checks required all three TDD tiers as a hard FAIL with no qualifier. Non-code work items — docs, ADRs, config — would incorrectly fail. All three TDD checks now read "if the work item involves code."

`orchestra-spec` and `orchestra-plan` had pytest syntax (`@pytest.mark.integration`, `pytest with no flags`) in the policy tier descriptions. The detailed Python tooling tables lower in the spec skill are intentionally stack-specific — those stay. The *policy* layer (what the tiers are, what they mandate) should be stack-agnostic. Removed pytest syntax from descriptions, replaced with language about default and non-default suites.

## The Smell Discussion

One thread worth recording: is it a code smell to have a work item without a milestone?

It IS a smell — but a mild one, and the distinction matters. The SDLC principle it violates is traceability: every piece of work should trace to a goal. The severity depends on whether it's temporary or permanent. Orphaned work is a yellow flag; work that stays permanently outside the roadmap is a red flag — the map stopped matching the territory.

The faster you move, the more load-bearing the score becomes. A slow team can recover from an undocumented detour. An agentic team can be three milestones deep in the wrong direction before a human looks up. This is why the velocity guard in `orchestra-implement` is advisory rather than blocking — the right answer is visible friction, not hard stops.

## What's Next

The `orchestra-milestone` reverse check — orphaned work items that exist in `.orchestra/work/` but don't appear in any milestone — was identified as a gap and deferred. It's the cleanup surface that catches yellow flags before they become red ones.
