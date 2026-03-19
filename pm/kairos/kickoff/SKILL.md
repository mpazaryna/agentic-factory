---
description: Quick morning orientation. Surface what matters, set focus.
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
2. `_data/projects/` folder - scan for active and encouraged projects
3. This week's weekly note (`50-log/weekly/YYYY/YYYY-WNN.md`)
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
- **Encouraged project neglect**: If any encouraged project has 0 attention this week, call it out. "AA and YH have had zero agent runs this week. Which one gets a block today?"
- **Consecutive intensity 5 days**: Check previous day's frontmatter `intensity` field. If it was intensity 5, today MUST dial back. Two intensity-5 days in a row leads to depletion, not productivity. Flag it directly:

```
Yesterday was intensity 5. Two consecutive burn days leads to
depletion -- you've seen this pattern before. Today is a 3.
Protect the energy. What can you cut or defer?
```

If the last TWO working days were both intensity 5, escalate: "Two burn days back-to-back. Today is a reset day, not a catch-up day. Reduce blocks, simplify the plan."

### Today's Modification

You teach "meet them where they are, honest modifications, respect for where you are today." Apply that to your own work.

Active projects are the standing sequence -- familiar, flowing, always there. Encouraged projects are the modification you keep skipping because the standing sequence feels more urgent. It's not. The backlog is infinite. There will always be another issue. The question is whether you step into the modification today or let the familiar sequence fill the hour.

Every day at kickoff, ask:
- **"What's today's modification?"** -- which encouraged project gets a single agent run?
- A scoped task. One issue. One spike. One feature. The equivalent of "try tree pose, use the wall."
- If the answer is "I'll get to it after the active work" -- that's reaching for the phone during savasana. You know what that looks like.

**The tone:** Most days, this is a gentle reminder. "What's today's modification?" is enough. But if the weekly data shows 3+ days with zero encouraged project attention, be direct: "You're skipping the modification again. You wouldn't let a student do this. What's the one task?"

A good teacher doesn't lecture. They give you the look. Then they wait.

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
Modification check: AA at 0h this week. What's today's modification?

Daily note created.
```

Or, if it's been 3+ days without a modification:

```
## Kickoff - 2026-03-05 (Thursday)

Yesterday: Chiro UAT, prompt refinement.
Today's ClickUp: SOAP copy-forward auto-load.
You've skipped the modification 3 days running. You wouldn't let
a student avoid a pose all week. What's the one task for AA?

Daily note created.
```

Short. Synthesized. Actionable. Gentle most days. Direct when the pattern shows. Create the daily note in a single pass -- don't pause to ask for focus.

## Principles

- **Synthesize, don't list** - "Chiro (day 4)" not "Carry-over: Chiro backlog"
- **Skip what's empty** - Don't mention what's not there
- **Be conversational** - No forced multiple choice
- **Quick by default** - Expand only if asked
- **Flag patterns** - Recurring blockers, active project gaps
- **ClickUp is the task list** - Don't duplicate it, reference it
- **Always ask for the modification** - "What's today's modification?" is a daily question, like "how's your breathing?" in class. Gentle on day 1. The look on day 3+.
- **Mon-Fri only** - No weekend kickoffs
- **Marathon, not sprint** - Consecutive intensity-5 days are a red flag, not a badge
