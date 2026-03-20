---
name: kickoff
description: "Quick morning orientation — surface ClickUp tasks, carry-overs, project gaps, and intensity patterns. Use when starting the workday."
allowed-tools: Read, Glob, Grep, Bash, Write
disable-model-invocation: false
---

# Kickoff

Quick morning orientation - under 2 minutes. Synthesize, don't list.

## Weekend Gate

First, determine the day of week. If today is Saturday or Sunday: "It's the weekend. No kickoff." Stop.

## Determine Today's Date

Establish today's date from the system environment (provided as "Today's date: YYYY-MM-DD"). Use this to:
- Calculate yesterday's date for reading the previous daily note (skip weekends -- if today is Monday, yesterday is Friday)
- Calculate the ISO week number for the weekly file

## Gather Context (silently)

Read these in parallel, don't output yet:
1. Previous working day's daily note - find Shutdown section (Tomorrow, Carry-over)
2. `projects/` folder - scan for active and encouraged projects
3. This week's weekly note (`kairos/weekly/YYYY/YYYY-WNN.md`)
4. Recent daily notes - check which active projects have had focus this week
5. Query ClickUp via MCP for today's assigned tasks

## Query ClickUp

Use ClickUp MCP tools to get today's tasks:
- Tasks assigned to today (by due date or start date)
- Include task name, list/project, status, priority

These tasks form the day's tactical plan. The weekly plan provides strategic context; ClickUp provides the execution list.

## Present Summary

Output a single concise block. Only include sections that have content.

```
## Kickoff - YYYY-MM-DD (DayName)

[Previous day's "Tomorrow" item if present]
[Today's ClickUp tasks]
[Active project gaps if any haven't had focus this week]
[Persistent blockers if same item 3+ days]

```

### What to Flag

- **Active project gaps**: "Chiro hasn't had focus yet this week" (it's Thursday)
- **Persistent carry-over**: "Resin bill - day 9" not just "Carry-over: Resin bill"
- **ClickUp task load**: If today has too many tasks for the day's capacity, flag it
- **Consecutive intensity 5 days**: Check previous day's frontmatter `intensity` field. If it was intensity 5, today MUST dial back. Two intensity-5 days in a row leads to depletion, not productivity. Flag it directly:

```
Yesterday was intensity 5. Two consecutive burn days leads to
depletion -- you've seen this pattern before. Today is a 3.
Protect the energy. What can you cut or defer?
```

If the last TWO working days were both intensity 5, escalate: "Two burn days back-to-back. Today is a reset day, not a catch-up day. Reduce blocks, simplify the plan."

### What to Skip

- Inbox counts (not actionable in kickoff)
- Weekly progress fractions ("2 of 5 complete")
- Projects without issues

## Eat the Frog

Before anything else, check the previous working day's daily note for a named frog (the "Tomorrow's frog" from shutdown).

**If the frog was named but not completed:**

This is the forcing function. The daily plan is paused until the frog is addressed.

```
Yesterday's frog: [specific task]. It didn't get done.
We're not moving to the standing sequence until this is handled.
Do it now, or tell me it's blocked (and why).
```

- **If blocked** (waiting on someone, needs info): Acknowledge, replace with a new frog, proceed with the day. Blocked is not avoided.
- **If not blocked, just skipped:** Hold the line. No Block 1 until the frog is eaten. This is the discipline.

**If no frog was named, or it was completed:**

```
Name today's frog. One specific task, before Block 1.
(Or "nothing pending" to move on.)
```

If they name one, record it as the first item in the daily note Focus section. If nothing's pending, move on. Don't invent frogs.

**The principle:** A named frog gets eaten. If you skip the frog, the practice pauses until you come back to it.

## Create Daily Note

Don't ask for focus -- pull it from ClickUp and the weekly plan.

1. Create today's daily note if it doesn't exist (use template pattern from recent notes)
2. Set the Focus section:
   - **Frog** first (named at previous shutdown or just now)
   - **ClickUp tasks** for today, listed by priority
   - **Project focus** from weekly plan context
3. Add From Yesterday context (synthesized from previous day's shutdown)

```markdown
# Focus

- **Frog:** [named task]
- [ClickUp task 1]
- [ClickUp task 2]
- [Project focus from weekly plan]
```

## Example Output

```
## Kickoff - 2026-03-03 (Tuesday)

Yesterday: Chiro billing codes, R-code bug fix. Intensity 4.
Today's ClickUp: ADR-019 voice artifact normalization, E&M office visit codes, Illium Factory blog post.

Daily note created.
```

Short. Synthesized. Actionable. Create the daily note in a single pass -- don't pause to ask for focus.

## Principles

- **Synthesize, don't list** - "Chiro (day 4)" not "Carry-over: Chiro backlog"
- **Skip what's empty** - Don't mention what's not there
- **Be conversational** - No forced multiple choice
- **Quick by default** - Expand only if asked
- **Flag patterns** - Recurring blockers, active project gaps
- **ClickUp is the task list** - Don't duplicate it, reference it
- **Mon-Fri only** - No weekend kickoffs
- **Marathon, not sprint** - Consecutive intensity-5 days are a red flag, not a badge
