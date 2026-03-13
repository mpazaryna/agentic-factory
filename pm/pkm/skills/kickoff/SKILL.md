---
name: Morning Kickoff
description: Quick morning orientation. Surface what matters, set focus.
source: original
collected: 2025-02-05
tags: [pkm, daily, planning, routines, obsidian]
---

# Kickoff

Quick morning orientation - under 2 minutes. Synthesize, don't list.

## Determine Today's Date

First, establish today's date from the system environment (provided as "Today's date: YYYY-MM-DD"). Use this to:
- Calculate yesterday's date for reading the previous daily note
- Determine the day of week (Saturday = end of week)
- Calculate the ISO week number for the weekly file

## Gather Context (silently)

Read these in parallel, don't output yet:
1. Yesterday's daily note - find Shutdown section (Tomorrow, Carry-over)
2. `_data/projects/` folder - scan for tier-1 and tier-2 projects
3. This week's weekly note (`50-log/weekly/YYYY/YYYY-WNN.md`)
4. Recent daily notes - check which tier-1 projects have had focus this week
5. All routine files in `_data/routines/` - check frontmatter for due calculations
6. All task files in `_data/tasks/` - check for pending/in_progress tasks

## Calculate Due Routines

For each routine in `_data/routines/` where `status: active`:

**Daily routines** (`frequency: daily`):
- Due if `last_completed` is empty OR `last_completed` < today

**Weekly routines** (`frequency: weekly`):
- Due if `last_completed` is empty OR `last_completed` < 7 days ago

**Interval routines** (`frequency: 3 months`, `60 days`, etc.):
- Parse the interval (e.g., "3 months" = 90 days, "60 days" = 60)
- Due if `last_completed` is empty OR `last_completed` + interval < today

**Flag anomalies:**
- Daily routine with `last_completed` > 7 days ago: "Haven't done X in N days — still daily?"
- Any routine with `last_completed` > 30 days ago: "X is 30+ days overdue"

## Present Summary

Output a single concise block. Only include sections that have content.

```
## Kickoff - YYYY-MM-DD (DayName)

[Yesterday's "Tomorrow" item if present]
[Calendar items for today if any]
[Tier 1 alert if chiro or resin haven't had focus this week]
[Persistent blockers if same item 3+ days]

What's your focus today?
```

### What to Flag

- **Tier 1 gaps**: "Chiro hasn't had focus yet this week" (it's Thursday)
- **Persistent carry-over**: "Chiro backlog - day 4" not just "Carry-over: Chiro backlog"
- **Calendar conflicts**: Only if something scheduled might affect focus choice
- **In-progress tasks**: Surface any `_data/tasks/` with `status: in_progress` (e.g., "Sean Allen iOS course in progress")
- **Encouraged project neglect**: If any encouraged project has 0 commits and 0h this week, call it out explicitly. "AA and YH have had zero agent runs this week. Which one gets a block today?"

### Today's Modification

You teach "meet them where they are, honest modifications, respect for where you are today." Apply that to your own work.

Core projects (Chiro, Resin) are the standing sequence -- familiar, flowing, always there. Encouraged projects are the modification you keep skipping because the standing sequence feels more urgent. It's not. The backlog is infinite. There will always be another issue on Chiro. The question is whether you step into the modification today or let the familiar sequence fill the hour.

Every day at kickoff, ask:
- **"What's today's modification?"** -- which encouraged project gets a single agent run?
- A scoped task. One issue. One spike. One feature. The equivalent of "try tree pose, use the wall."
- If the answer is "I'll get to it after Chiro/Resin" -- that's reaching for the phone during savasana. You know what that looks like.

**The tone:** Most days, this is a gentle reminder. "What's today's modification?" is enough. But if the weekly data shows 3+ days with zero encouraged project attention, be direct: "You're skipping the modification again. You wouldn't let a student do this. What's the one task?"

A good teacher doesn't lecture. They give you the look. Then they wait.

### What to Skip

- Inbox counts (not actionable in kickoff)
- Empty calendar days
- Weekly progress fractions ("2 of 5 complete")
- Projects without issues

## Eat the Frog

Before anything else, check yesterday's daily note for a named frog (the "Tomorrow's frog" from last night's shutdown). Also check for overdue routines, physical mail, bills, or any admin that's been sitting.

**If yesterday's frog was named but not completed:**

This is the forcing function. The daily plan is paused until the frog is addressed.

```
Yesterday's frog: [specific task]. It didn't get done.
We're not moving to the standing sequence until this is handled.
Do it now, or tell me it's blocked (and why).
```

- **If blocked** (waiting on someone, needs info): Acknowledge, replace with a new frog, proceed with the day. Blocked is not avoided.
- **If not blocked, just skipped:** Hold the line. No Block 1 until the frog is eaten. This is the discipline. January showed what happens without it: 7 days of carry-over.

**If no frog was named yesterday, or it was completed:**

```
Name today's frog. One specific admin task, before Block 1.
(mail, bills, emails, errands, overdue items -- or "nothing pending")
```

If they name one, record it as the first item in the daily note Focus section. If nothing's pending, move on. Don't invent frogs.

**The principle:** A named frog gets eaten. "Admin" sits on the plate forever. And if you skip the frog, the practice pauses until you come back to it. That's not punishment -- it's the same thing you'd tell a student who keeps skipping the foundational pose to chase the advanced one.

## Ask Focus

Simple open question: "What's your focus today?"

Don't use AskUserQuestion with predefined options. Let the user type freely.

## Create/Update Daily Note

After user responds:
1. Create today's daily note if it doesn't exist (use template pattern from recent notes)
2. Set the Focus section
3. Add the **Plan** section -- pull today's schedule table from the weekly note's Daily Schedules section. Match on day name (e.g., "Wednesday Feb 4"). Copy the time/block/activity table verbatim. This is the intention from the weekly plan, not a commitment -- shutdown captures reality.
4. Add From Yesterday context
5. Populate the Routines section with due items:

```markdown
## Plan

| Time | Block | Activity |
|------|-------|----------|
| 7:00-7:45 | Morning | Routines |
| 8:30-10:30 | Block 1 | Chiro |
| 10:30-11:00 | Transition | Piano or Yoga |
| 11:00-1:00 | Block 2 | Resin |
| 1:00-1:30 | Lunch | |
| 1:30-2:00 | Admin | Email, mail, follow-ups |
| 2:00-4:00 | Block 3 | Authentic Advantage (CompassKit) |
| 4:00 | Shutdown | |
```

If no daily schedule exists for today in the weekly note, skip this section.

```markdown
# Routines

## Morning Practice
- [ ] Alternate Nostril Breathing [🎬](link)
- [ ] Hanuman Chalisa [🎬](link)
- [ ] Ganesha Mantra
- [ ] Music
- [ ] Home Yoga Practice

## Due Today
- [ ] Review Next Week's Calendar *(weekly)*

## Overdue
- [ ] Butcher Block maintenance *(14 days overdue)*
```

Group by context (morning practice together, then other due items, then overdue).
Include links where the routine has a `link` field.
Show days overdue for non-daily items.

## Example Output

```
## Kickoff - 2026-02-03 (Tuesday)

Yesterday: Chiro Red Flag feature, Resin QA.
Modification check: AA and YH both at 0h this week.
What's today's modification?
5 morning routines due.

What's your focus today?
```

Or, if it's been 3+ days without a modification:

```
## Kickoff - 2026-02-05 (Thursday)

Yesterday: Resin QA, Chiro backlog.
You've skipped the modification 3 days running. You wouldn't let
a student avoid a pose all week. What's the one task for AA or YH?
3 morning routines due.

What's your focus today?
```

Short. Synthesized. Actionable. Gentle most days. Direct when the pattern shows.

## Tier Reference

Read from `_data/` frontmatter:
- **Tier 1** (weekly required): Check if touched this week, flag if not
- **Tier 2** (weekly encouraged): Gentle nudge if dormant 2+ weeks
- **Active/Paused**: Don't mention unless user asks

## Principles

- **Synthesize, don't list** - "Chiro (day 4)" not "Carry-over: Chiro backlog"
- **Skip what's empty** - No calendar? Don't mention it
- **Be conversational** - No forced multiple choice
- **Quick by default** - Expand only if asked
- **Flag patterns** - Recurring blockers, tier 1 gaps
- **Always ask for the modification** - "What's today's modification?" is a daily question, like "how's your breathing?" in class. Gentle on day 1. The look on day 3+.
- **Treat your own projects like students** - You'd never let a student skip a pose for three weeks and call it fine. Don't do it to AA and YH.
