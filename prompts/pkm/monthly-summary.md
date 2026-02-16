---
name: Monthly Summary
description: Generate monthly retrospective from daily and weekly notes
source: original
collected: 2025-02-05
tags: [pkm, monthly, retrospective, metrics, obsidian]
---

# Monthly Summary

Reads all daily notes, weekly summaries, Clockify timesheets, and GitHub metrics for the month. Generates an in-depth retrospective that surfaces patterns invisible at the weekly level.

## Core Principle

Monthly summaries answer questions weekly summaries can't: Is the portfolio moving in the right direction? Are the right projects getting attention? Are paused projects accumulating or resolving? Is the system (load calculation, routines, admin) actually working?

## Workflow

1. **Determine current month**
   - Get today's date
   - Monthly file: `50-log/monthly/YYYY/YYYY-MM.md`
   - Create folder if needed

2. **Read all weekly summaries for the month**
   - Find weekly files that overlap with this month in `50-log/weekly/YYYY/`
   - These are the primary source -- they already contain synthesized data
   - Extract: project status tables, Clockify totals, GitHub metrics, accomplishments, patterns

3. **Read all daily notes for the month**
   - Find all daily notes from the 1st through today (or end of month)
   - Read each one completely - Focus, Log, Shutdown sections
   - Note which days have notes and which are missing
   - Extract: intensity scores, block counts, project lists, routine completions, carry-overs

4. **Aggregate Clockify data**
   - Pull Clockify totals from each weekly summary's Time Tracking section
   - If weekly summaries are missing Clockify data, look for CSVs on Desktop:
     `~/Desktop/Clockify_Time_Report_Detailed_*_DD_MM_YYYY-DD_MM_YYYY.csv`
   - Calculate monthly totals:
     - Total hours
     - Hours per project (full month)
     - Billable vs non-billable
     - Weekly trend (hours per week -- increasing, steady, decreasing?)

5. **Read ALL project status**
   - Read `_data/projects/*.md` files to get ALL projects
   - Track: active, encouraged, stable, completed, paused, concept
   - Exclude only archived

6. **Aggregate GitHub metrics**
   - Pull GitHub tables from each weekly summary
   - For each project with a `repo:` property, also run current counts:
     ```bash
     gh issue list --repo <owner/repo> --state open --json number --jq 'length'
     gh api repos/<owner/repo>/commits --jq '[.[] | select(.commit.author.date > "<month-start>")] | length'
     ```
   - Calculate monthly totals: issues opened, closed, net change, total commits

7. **Analyze**

   **Portfolio health**
   - How many projects are active vs encouraged vs stable vs paused vs concept?
   - Did any projects change status this month? (Track the transitions)
   - Are paused projects accumulating or resolving?
   - Is the portfolio getting leaner or wider?

   **Active project accountability**
   - For each active project: how many weeks got focus? Clockify hours? Commits?
   - For each encouraged project: did it get touched? How often?
   - Cross-reference: planned hours (from weekly targets) vs actual hours (Clockify)

   **Load and energy**
   - Average daily intensity across the month
   - Average blocks per working day
   - Load trend by week (ramping up, steady, burning out?)
   - Sick days, rest days, recovery weeks

   **Routine consistency**
   - Morning practice: how many days completed vs working days?
   - Streak data if visible from daily notes
   - Admin: did the daily 30-min blocks happen? Carry-over patterns?

   **Accomplishments**
   - Roll up from weekly summary Accomplishments sections
   - Identify the month's biggest wins

   **Themes and patterns**
   - What projects dominated attention?
   - What got neglected despite being planned?
   - Recurring blockers across weeks
   - Energy patterns (early week vs late week, Mon vs Fri)
   - Carry-over patterns (what keeps slipping?)

   **Gaps**
   - Intended but didn't happen
   - Persistent carry-overs that never resolved
   - Projects that stalled without a deliberate pause

   **System evaluation**
   - Did the load calculation system work? (recovery weeks honored, steady weeks held)
   - Did the weekly plan commitments translate to actual work?
   - Did routines stick?
   - Did admin get done or carry over?

8. **Write monthly file**
   - Create or overwrite `50-log/monthly/YYYY/YYYY-MM.md`
   - Full file, not appended

## Output Format

Write to `50-log/monthly/YYYY/YYYY-MM.md`:

```markdown
---
tags: [monthly, retrospective]
date: YYYY-MM
---

# Monthly Summary - YYYY-MM

*Generated: YYYY-MM-DD HH:MM*

## Overview

- Working days: X
- Days with notes: X / Y
- Average intensity: X.X
- Average blocks/day: X.X
- Weeks covered: W01, W02, W03, W04
- Notable: [illness, travel, recovery weeks, etc.]

## Portfolio Snapshot

| Status | Count | Projects |
|--------|-------|----------|
| active | N | [list] |
| encouraged | N | [list] |
| stable | N | [list] |
| completed | N | [list] |
| paused | N | [list] |
| concept | N | [list] |

**Status changes this month:**
- [project]: status A -> status B (why)

**Portfolio trend:** [getting leaner/wider/stable]

## Project Progress

### Active Projects

#### [Project Name]
- Weeks of focus: X / Y
- Clockify hours: X.Xh
- Commits: N
- Issues: opened N, closed N, net +/-N
- Key accomplishments: [list]
- Status: [current state, trajectory]

### Encouraged Projects

#### [Project Name]
- Weeks touched: X / Y
- Clockify hours: X.Xh
- Commits: N
- Assessment: [getting attention or drifting?]

### Stable/Completed Projects

- **[Project]:** [any notable activity or confirms no attention needed]

### Paused/Concept Review

- **[Project]:** Paused since [when]. Blocker: [X]. Trend: [resolving/accumulating/stale]

## Time Tracking (Clockify)

**Monthly total: XX.Xh** (billable: XX.Xh, non-billable: XX.Xh)

| Project | Hours | Billable | % of Total |
|---------|-------|----------|------------|
| [project] | X.Xh | Yes/No | X% |

| Week | Hours | Trend |
|------|-------|-------|
| W01 | X.Xh | |
| W02 | X.Xh | |
| W03 | X.Xh | |
| W04 | X.Xh | |

**Planned vs Actual (monthly aggregate):**

| Project | Target | Actual | Delta |
|---------|--------|--------|-------|
| [project] | X.Xh | X.Xh | +/-X.Xh |

## GitHub Activity

*Monthly totals*

| Project | Open (EOM) | Closed | Opened | Net | Commits |
|---------|------------|--------|--------|-----|---------|
| [project](url) | N | N | N | +/-N | N |

**Total commits: N**
**Net issue change: +/-N**

## Routine Consistency

| Routine | Days Completed | Working Days | Rate |
|---------|---------------|--------------|------|
| Morning practice | X | Y | X% |
| Admin (30 min) | X | Y | X% |

**Streaks:** [longest morning practice streak, etc.]
**Carry-over patterns:** [what kept slipping, how long]

## Accomplishments

- [rolled up from weekly summaries, biggest wins first]

## Patterns

**What dominated attention:**
- [projects/activities that consumed the most hours and commits]

**What got neglected:**
- [planned but consistently skipped -- why?]

**Energy and load:**
- [weekly intensity trend, burnout signals, recovery patterns]

**Recurring blockers:**
- [things that blocked progress across multiple weeks]

## System Evaluation

**Load calculation:** [Did it work? Recovery weeks honored? Steady weeks held?]
**Weekly commitments:** [Did plans translate to work? What was the plan-to-actual ratio?]
**Routines:** [Did they stick? What broke the streaks?]
**Admin:** [Daily blocks happening or carry-over pattern?]

## Insights

[Learnings, surprises, reflections. What would you do differently?]

## Next Month

[Suggested focus based on monthly patterns. Course corrections. Projects to elevate, archive, or spike.]
```

## Notes

- Can be run multiple times - overwrites entire file
- Reads weekly summaries first (they have pre-synthesized data), then daily notes for detail
- More reflective than weekly - look for larger patterns across 4-5 weeks
- Be honest about gaps - that's the value
- Track ALL non-archived projects, not just active
- Create `50-log/monthly/YYYY/` folder if it doesn't exist
- Paused projects that sit for a full month without a spike or decision should be flagged
- Compare planned vs actual hours to calibrate future weekly targets
