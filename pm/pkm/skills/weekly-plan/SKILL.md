---
name: Weekly Plan
description: Start-of-week planning session to set priorities and goals
source: original
collected: 2025-02-05
tags: [pkm, weekly, planning, load-management, obsidian]
---

# Weekly Plan

Start-of-week planning session. Every non-archived project should be moving toward completion or archive.

## Core Principle

With agentic workflows, the constraint isn't capacity - it's attention. You can run multiple agents in parallel. The question for each project is: "What attention does this get this week?"

**Sustainable pace is non-negotiable.** The system calculates recommended load based on trailing metrics. You can override, but it's logged. See [[load-calculation-spec]] for the math.

**The standing sequence expands by default.** Core projects (Chiro, Resin) are the standing sequence -- familiar, flowing, always there. There's always another issue, another backlog item. Left unchecked, they fill every available block. The modification -- encouraged projects getting a single agent run -- is where the growth happens. The weekly plan must protect space for the modification, not hope it fits after the standing sequence.

**Name the frog.** "Admin" is too vague to start. Every day needs a named frog -- one specific admin task eaten before Block 1. The weekly plan assigns frogs for Monday and seeds the pattern for the rest of the week.

## Workflow

1. **Calculate load (FIRST)**

   Read trailing 7-14 days from daily notes:
   - `intensity` ratings (1-5)
   - `blocks` worked
   - `projects` touched

   Calculate:
   ```
   trailing_intensity = avg(intensity[]) over 7 days
   trailing_load = avg(blocks × project_count) over 7 days
   weeks_hot = consecutive weeks where avg_daily_load > 6
   ```

   Determine recommended load:
   ```
   IF illness_flag in last 7 days:
       recommended_daily = 3 (50% capacity)

   ELSE IF trailing_intensity >= 4.0:
       recommended_daily = 4 (70% capacity)

   ELSE IF weeks_hot >= 2:
       recommended_daily = 4 (70% capacity)

   ELSE IF trailing_intensity >= 3.5:
       recommended_daily = 5 (85% capacity)

   ELSE:
       recommended_daily = 6 (sustainable)
   ```

   Output the calculation visibly:
   ```
   ## Load Calculation

   Trailing 7 days:
   - Avg intensity: 4.2
   - Avg daily load: 9.3
   - Illness flag: yes (Wed-Fri)

   → Recommended daily load: 3 (recovery week)
   → Max blocks/day: 2
   → Max projects: 1-2
   ```

2. **Gather starting position**
   - Read `_data/projects/*.md` files to get ALL projects (exclude archived)
   - Read `_data/tasks/*.md` files to get professional one-off tasks
   - Get GitHub backlog counts for projects with repos:
     ```bash
     gh issue list --repo <owner/repo> --state open --json number --jq 'length'
     ```
   - Read last week's weekly summary for context

2. **Create or update weekly file**
   - File: `50-log/weekly/YYYY/YYYY-WNN.md`
   - Use template from `_templates/paz-weekly-plan.md`

3. **Fill Starting Position section**
   - Populate GitHub Backlog table with current open counts
   - Summarize last week's key outcomes under "Last Week"

4. **Project Triage - ALL non-archived projects**

   For each project, ask the appropriate question based on status:

   **Active (standing sequence):** "What's the commitment for [project]?"
   - Required weekly focus
   - Agent should be running on this
   - But: the standing sequence does NOT get to fill all blocks. Cap it. Leave room for the modification.

   **Encouraged (the modification):** "What specific agent task does [project] get this week?"
   - Not "will it get touched?" -- that's how it gets skipped. The question is **what**, not **if**.
   - Assign a concrete task: one issue, one spike, one feature. "Try tree pose, use the wall."
   - Schedule it into specific daily blocks during step 8. Don't leave it floating.
   - If the answer is "after Chiro/Resin" -- that's reaching for the phone during savasana. Push back.
   - Review last week: did the modification land? If not, this week needs a stronger commitment.

   **Paused:** "Why is [project] paused? Can we unblock or should we archive?"
   - Paused should be temporary, not permanent
   - Either find path to unblock or archive it
   - Consider: can an agent spike to investigate the blocker?

   **Concept:** "Should we start [project]? What's the first step?"
   - Define scope or archive
   - Consider: can an agent spike to define scope?

5. **Task Triage - Professional one-off tasks**

   Review `_data/tasks/*.md` for non-project tasks (courses, certifications, professional development):

   | Task | Status | This Week | Notes |
   |------|--------|-----------|-------|
   | Sean Allen iOS Course | in_progress | 1-2 hours | Learning |

   For each task:
   - **pending**: "Will this get attention this week?"
   - **in_progress**: "What's the next milestone?"
   - **completed**: Graduate to `30-resource/` (move content, delete task file). The task was scaffolding; the resource is the lasting value.

6. **Add commitments**
   - Specific deliverables for the week
   - Reference GitHub issues if relevant (e.g., `chiro#130`)
   - Include task milestones if applicable

7. **Add notes**
   - Any context, constraints, or known calendar impacts

8. **Build daily schedules (respecting load calculation)**

   The working day is a fixed container. Three blocks, all deep work. The load calculation determines what goes *in* the blocks (project assignment, intensity), not whether you show up.

   **EAT THE FROG FIRST:** Every day starts with a named frog -- one specific admin task before Block 1. Not "admin." A named task: "process physical mail," "pay electric bill," "reply to Kevin's email." The frog is eaten before the standing sequence begins. If it's not named during weekly planning, kickoff will ask for it. If yesterday's frog wasn't eaten, kickoff pauses the daily plan until it's handled. January showed what happens without this: 7 days of admin carry-over.

   **The Standard Day (every day, every week type):**
   ```
   8:00-8:30    Frog (named admin task)
   8:30-10:30   Block 1 - Active project (standing sequence)
   10:30-11:00  Transition 1
   11:00-1:00   Block 2 - Active project (standing sequence)
   1:00-1:30    Lunch
   1:30-3:30    Block 3 - Encouraged project (modification)
   3:30-4:00    Transition 2
   4:00-5:00    Wind-down / light work / overflow
   5:00-5:30    Shutdown
   ```

   **Block assignment is structural, not a suggestion:**
   - **Blocks 1 & 2:** Active projects only. The standing sequence. Chiro, Resin, Swift Mastery -- assigned during weekly planning.
   - **Block 3:** Encouraged projects only. The modification. AA, YH, Dailyframe -- assigned during weekly planning.

   The standing sequence gets 4 hours of deep work per day. That's substantial. Block 3 is protected space for the modification. It doesn't become "overflow Chiro" because the backlog is long. The backlog is always long. That's not a reason.

   **Weekly block assignment table** (built during step 4, Project Triage):

   | Day | Block 1 | Block 2 | Block 3 (Modification) |
   |-----|---------|---------|------------------------|
   | Mon | Chiro   | Resin   | AA                     |
   | Tue | Chiro   | Swift   | YH                     |
   | Wed | Resin   | Chiro   | AA                     |
   | Thu | Chiro   | Resin   | Dailyframe             |
   | Fri | Resin   | Chiro   | AA                     |

   This table is the weekly plan's primary output. Every block has a name. No ambiguity at kickoff.

   **How load modulates the standard day:**

   - **Recovery (daily load ≤ 3):** All 3 blocks happen. Block 3 stays as the modification -- agent-driven work on encouraged projects is ideal for lower energy. Blocks 1-2 may be lighter (review, planning, agent-assisted) rather than pure greenfield.
   - **Steady (daily load 4-6):** All 3 blocks at normal intensity. The standard operating mode.
   - **Heavy (daily load > 6):** All 3 blocks at full intensity, and the 4:00-5:00 wind-down becomes a 4th block for active project overflow. Block 3 remains the modification -- heavy weeks don't eat it. Time-limited: max 2 consecutive weeks, then mandatory step-down.

   - Adjust for calendar conflicts (meetings, appointments)
   - Assign projects to blocks based on triage AND load limits

9. **Generate ICS file for Apple Calendar**
   - Create `50-log/weekly/YYYY/WNN-time-blocks.ics`
   - MUST include all events from the block assignment table:
     - Frog (8:00-8:30, Mon-Fri, named if known)
     - Block 1 (8:30-10:30) - Active project from table
     - Transition 1 (10:30-11:00)
     - Block 2 (11:00-1:00) - Active project from table
     - Lunch (1:00-1:30)
     - Block 3 (1:30-3:30) - Encouraged project from table
     - Transition 2 (3:30-4:00)
     - Wind-down (4:00-5:00)
     - Shutdown (5:00-5:30)
   - Each block's SUMMARY includes the project name from the weekly assignment table
   - Block 3 should be visually distinct -- prefix with "Modification:" so it stands out
   - User double-clicks to import into Apple Calendar for notifications
   - Generate ALL 9 events per weekday (Mon-Fri). Saturday is lighter (no frog, flexible blocks). No Sunday events.
   - ICS format -- full single-day example (repeat for each weekday with that day's projects from the assignment table):
     ```
     BEGIN:VCALENDAR
     VERSION:2.0
     PRODID:-//WNN Time Blocks//EN

     BEGIN:VEVENT
     DTSTART:20260202T080000
     DTEND:20260202T083000
     SUMMARY:Frog
     DESCRIPTION:Named admin task - eat before Block 1
     END:VEVENT

     BEGIN:VEVENT
     DTSTART:20260202T083000
     DTEND:20260202T103000
     SUMMARY:Block 1: Chiro
     DESCRIPTION:Standing sequence - Red Flag feature
     END:VEVENT

     BEGIN:VEVENT
     DTSTART:20260202T103000
     DTEND:20260202T110000
     SUMMARY:Transition 1
     END:VEVENT

     BEGIN:VEVENT
     DTSTART:20260202T110000
     DTEND:20260202T130000
     SUMMARY:Block 2: Resin
     DESCRIPTION:Standing sequence - issue closing
     END:VEVENT

     BEGIN:VEVENT
     DTSTART:20260202T130000
     DTEND:20260202T133000
     SUMMARY:Lunch
     END:VEVENT

     BEGIN:VEVENT
     DTSTART:20260202T133000
     DTEND:20260202T153000
     SUMMARY:Modification: AA
     DESCRIPTION:Encouraged project - CompassKit scope
     END:VEVENT

     BEGIN:VEVENT
     DTSTART:20260202T153000
     DTEND:20260202T160000
     SUMMARY:Transition 2
     END:VEVENT

     BEGIN:VEVENT
     DTSTART:20260202T160000
     DTEND:20260202T170000
     SUMMARY:Wind-down
     DESCRIPTION:Light work / overflow
     END:VEVENT

     BEGIN:VEVENT
     DTSTART:20260202T170000
     DTEND:20260202T173000
     SUMMARY:Shutdown
     END:VEVENT

     ... (repeat all 9 events for Tue-Fri with each day's projects)

     END:VCALENDAR
     ```

10. **Confirm**
   - Summarize the week's project attention
   - Point to ICS file for calendar import
   - Ready to start

## Output Format

Write to `50-log/weekly/YYYY/YYYY-WNN.md`:

```markdown
---
tags: [weekly, planner]
week: YYYY-WNN
---

# Starting Position

> Generated by /weekly-plan

## GitHub Backlog

| Project | Open | Link |
|---------|------|------|
| chiro | 23 | [issues](https://github.com/mpazaryna/chiro/issues) |
| systemata | 2 | [issues](https://github.com/mpazaryna/systemata/issues) |

## Last Week

- Chiro: Glass UI shipped
- Resin: Waiting on API keys

---

# Project Triage

> Every non-archived project should be moving toward completion or archive

| Project | Status | This Week | Notes |
|---------|--------|-----------|-------|
| Chiro | active | Red Flag feature | Blocks 1 & 2 |
| Resin | active | QA + deploy | Blocks 1 & 2 |
| Swift Mastery | active | Sean Allen iOS 26 | Blocks 1 & 2 (Tue, Fri) |
| Authentic Advantage | encouraged | CompassKit scope spike | Block 3 (Mon, Wed, Fri) |
| Yellow House | encouraged | Define README | Block 3 (Tue) |
| Dailyframe | encouraged | Fix 2 open issues | Block 3 (Thu) |
| Productivity MCP | concept | Skip | Not ready |

# Block Assignment

| Day | Frog | Block 1 | Block 2 | Block 3 (Modification) |
|-----|------|---------|---------|------------------------|
| Mon | Process mail | Chiro | Resin | AA |
| Tue | Pay electric | Chiro | Swift | YH |
| Wed | Reply to Kevin | Resin | Chiro | AA |
| Thu | Schedule dentist | Chiro | Resin | Dailyframe |
| Fri | File receipts | Resin | Swift | AA |
| Sat | -- | Flex | Weekly Summary | -- |

# Commitments

- Chiro: Complete Red Flag feature (chiro#139)
- Resin: Close remaining QA issues
- AA: CompassKit scope defined by Friday
- Yellow House: README and project definition

# Notes

Standing sequence capped at Blocks 1-2. Block 3 is the modification -- every day.
```

## Project Status Reference

| Status | Question | Action |
|--------|----------|--------|
| active (standing sequence) | What's the commitment? | Agent runs on this -- but cap it, don't let it fill all blocks |
| encouraged (modification) | What specific task gets an agent run? | Schedule into a block. Not "if" -- "what." |
| stable | -- | Working, not active. No weekly action unless it breaks. |
| paused | Why paused? Unblock or archive? | Spike or decide |
| concept | Start or archive? | Define scope or drop |
| archived | -- | Don't include |

## Load-Based Scheduling

The container is fixed: 3 blocks, 8:30-5:30. Load modulates intensity and project count, not the shape of the day.

| Daily Load | Blocks | Projects | Intensity | Shutdown |
|------------|--------|----------|-----------|----------|
| ≤ 3 (recovery) | 3 | 1-2 | Lighter (agent-driven, review, planning) | 5:00 |
| 4-6 (steady) | 3 | 2-3 | Normal | 5:00 |
| > 6 (heavy) | 3+1 | 2-3 | Full burn, wind-down becomes Block 4 | 5:30 |

**Constraints:**
- Heavy is time-limited: max 2 consecutive weeks
- After 2 heavy weeks, next week must be steady or recovery
- Illness flag forces recovery regardless of other metrics
- All 3 blocks are deep work regardless of load level -- you show up for Block 3

**Sustainable thresholds (calibrate over time):**
| Metric | Sustainable | Warning | Reduce |
|--------|-------------|---------|--------|
| daily_load | ≤ 6 | 7-8 | ≥ 9 |
| trailing_intensity | ≤ 3.0 | 3.5-4.0 | ≥ 4.0 |
| weeks_above_sustainable | 0-1 | 2 | ≥ 3 |

- **Sunday:** Rest day, no coding, no frogs
- **Saturday:** Coding but no frogs (weekly summary day)
- **Monday-Friday:** Frog before Block 1 is mandatory, regardless of week type
- **Pomodoro:** 30 min work / 10 min break, 3 pomos per 2h block

## Notes

- No project should be in limbo indefinitely
- Paused means "temporarily deprioritized" not "forgotten"
- Every week, paused/concept projects get the question: "Move forward or archive?"
- Agents can spike on blockers - use them
- Run `/kickoff` daily to stay oriented
- Run `/weekly-summary` at end of week to close the loop
- ICS file goes to `50-log/weekly/YYYY/WNN-time-blocks.ics` - double-click to import to Apple Calendar

## Proactive Prescription

**The system prescribes, it doesn't ask.**

When you run `/weekly-plan`, lead with the load calculation. Don't ask "what pace do you want?" - tell the user what the data says. They can override, but the default is data-driven.

```
## Load Calculation

Your trailing 7-day intensity is 4.2 with avg daily load of 9.3.
You had an illness flag Wed-Fri.

This week is a recovery week: 2 blocks/day, 1-2 projects max.

[Continue with project triage within those constraints]
```

## Weekly Evaluation Criteria

When `/weekly-summary` runs at week end, it should evaluate against these criteria:

**Modification compliance:**
- How many days did an encouraged project get an agent run?
- Were the specific tasks assigned during weekly planning actually completed?
- Did the standing sequence expand to fill blocks that were reserved for modifications?
- If 0 modifications landed: "The standing sequence filled the week again. You wouldn't let a student skip a pose all week."
- If 3+ modifications landed: "Modifications are landing. The practice is working."

**Frog compliance:**
- How many frogs were named at shutdown?
- How many were eaten the next morning?
- Any frog carry over 2+ days? (That's not a frog, that's avoidance.)
- Did the "daily plan pauses" rule get invoked? What happened?

**Standing sequence discipline:**
- Did active projects stay within their planned block allocation?
- Or did "one more issue on Chiro" eat the modification block?
- Track: planned blocks for active projects vs actual blocks spent

**Pattern visibility:**
- Is the same encouraged project getting skipped every week? (Decision needed: commit or move to paused)
- Is the same frog getting re-named without being eaten? (Break it smaller or do it now)
- Are recovery/steady week load limits being honored or overridden?

These criteria feed the weekly summary's assessment. The weekly plan sets the intention; the weekly summary checks whether the practice held.

## Doc Maintenance

After each weekly cycle, update [[load-calculation-spec]] if:

1. **Threshold calibration needed** - Observed sustainable load differs from defaults
2. **Pattern discovered** - e.g., "illness follows 2+ heavy weeks"
3. **Override outcome** - Did pushing through work or backfire?

The spec is a living document. The system maintains it, not just references it.
