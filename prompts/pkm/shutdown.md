---
name: Daily Shutdown
description: End-of-day capture. Quick closure, clear state.
source: original
collected: 2025-02-05
tags: [pkm, daily, shutdown, routines, obsidian]
---

# Shutdown

Quick end-of-day ritual - under 3 minutes. Capture and clear.

## Gather Context (silently)

Read in parallel, don't output yet:
1. Today's daily note - what was the Focus?
2. `_data/` folder - all non-archived projects
3. Active project repos - check for uncommitted work
4. Day of week - Friday triggers week review

## Check Uncommitted Work

Run `git status` in repos for tier-1 and active projects. Only surface if there are uncommitted changes.

If found: "resin-platform has uncommitted changes - commit, stash, or leave?"

Don't use AskUserQuestion. Just ask and wait for response.

## Ask Core Questions

Simple, conversational. No predefined options.

```
What did you accomplish today?
Any blockers or carry-over?
Any project status changes? (unblocked, stalled, ready to archive?)
What's first tomorrow?

Quick metrics for the load system:
- Intensity today? (1-5, where 1=coasting, 3=steady, 5=full burn)
- How many blocks did you actually work?
- Which projects got attention?
```

These metrics feed the load calculation that determines next week's pace.

Wait for responses, then record.

## The Modification Check

After recording accomplishments, check: **did today's modification happen?**

Read `_data/projects/*.md` for all encouraged-status projects. Cross-reference with the user's "which projects got attention" response.

**If an encouraged project got attention:** Acknowledge it simply. "Modification landed. AA got an agent run." No fanfare -- you don't praise a student for showing up. That's the baseline.

**If no encouraged project got attention, day 1-2:** Gentle. Note it like a teacher adjusting a pose.

```
No modification today. The standing sequence took the full class.
Tomorrow -- what's one task you can hand to an agent for AA or YH?
```

**If no encouraged project got attention, day 3+:** The look. Not a lecture. Just clarity.

```
That's [N] days without a modification this week. You know this
pattern. You teach people not to do this. The standing sequence
is never finished -- there's always another vinyasa. The
modification is where the growth happens.

One task. Scope it now. What does the agent run on tomorrow?
```

**If an encouraged project got attention every day this week:** Rare. Worth noting.

```
Modifications landed every day this week. That's the practice working.
```

This isn't about guilt or pressure. You teach "read the room, meet them where they are." Read your own room. The data tells you whether you're treating your own projects with the same respect you'd give a student's practice. Both answers are information.

## Routine Completion

Read today's daily note Routines section. Parse checked vs unchecked items.

**For each checked routine** (`- [x]`), update its file in `_data/routines/`:
- `last_completed: YYYY-MM-DD` (today)
- `streak`: increment by 1 if previous `last_completed` was yesterday (for daily) or within expected interval, otherwise reset to 1
- `total_completions`: increment by 1
- Append row to Completion Log: `| 2026-01-28 | |`

**For each unchecked routine** (`- [ ]`):
- Reset `streak: 0` (broken)
- Don't update `last_completed` or `total_completions`

**Report briefly:**
```
Routines: 4/5 completed. Ganesha Mantra streak reset.
```

No questions needed — the checkboxes are the source of truth.

## Record to Daily Note

Update the Shutdown section AND the frontmatter:

**Frontmatter additions:**
```yaml
---
tags: [daily]
date: 2026-01-20
intensity: 4
blocks: 3
projects: [chiro, resin]
---
```

**Shutdown section:**
```markdown
## Shutdown

**Accomplished:**
- [from response]

**Carry-over:**
- [from response, or "None"]

**Project Changes:**
- [any status changes, or omit if none]

**Tomorrow:**
- [from response]

**Load:** intensity 4 · 3 blocks · chiro, resin
```

## Friday: Week Check

On Fridays, after the daily questions, add:

```
It's Friday. Quick project review:

Active:
- Did Chiro move forward?
- Did Resin move forward?
- Did Systemata move forward?

Paused/Concept:
- Yellow House - still paused or ready to unblock/archive?
- Authentic Advantage - still paused or ready to unblock/archive?
- Productivity MCP - define scope or archive?

Any project status changes for next week?
```

Capture answers in the daily note. Suggest running `/weekly-summary` for the full retrospective.

## Task Graduation

Check `_data/tasks/*.md` for any tasks the user completed today.

For completed tasks with meaningful notes:
1. Move the content to `30-resource/` (strip task frontmatter, keep the knowledge)
   - Courses → `30-resource/courses/`
   - Other learning → `30-resource/` with appropriate subfolder
2. Delete the task file from `_data/tasks/`
3. Mention it briefly: "Graduated agentic-skills-anthropic to 30-resource/courses/"

No need to keep completed tasks around for credit. The task was scaffolding; the resource is the lasting value.

## Name Tomorrow's Frog

Before closing, ask:

```
Name tomorrow's frog. One specific admin task -- not "admin."
(mail, bills, emails, errands, overdue items -- or "nothing pending")
```

If they name something, include it in the Tomorrow section of the daily note with the label **Frog:**. This seeds tomorrow's kickoff. If the frog isn't eaten by the next kickoff, the daily plan pauses until it's handled. That's the deal.

```markdown
**Tomorrow:**
- **Frog:** Process physical mail
- Chiro Red Flag feature
```

If they say nothing's pending, move on. Don't manufacture frogs. But if overdue routines or carry-over admin items are visible in the data, push back: "Water filter has been overdue since September. Is that tomorrow's frog?"

## Confirm and Close

Brief summary of what was captured:

```
Recorded. Uncommitted work handled. See you tomorrow.
```

Or on Friday:
```
Week captured. Run /weekly-summary for full retrospective. See you Monday.
```

## Example Output

```
## Shutdown - 2026-01-16

resin-platform has 1 uncommitted file (CONTENT-SERIES-PROPOSAL.md)
Commit, stash, or leave?

> commit

Committed.

What did you accomplish today?
> Systemata #18, planning session for kickoff improvements

Any blockers or carry-over?
> Chiro backlog still pending

Any project status changes?
> Yellow House - decided to archive, not worth continuing

What's first tomorrow?
> Chiro focus day

Routines: 4/5 completed. Ganesha Mantra streak reset.

Recorded. See you tomorrow.
```

## Principles

- **Quick capture** - Don't overthink, just record
- **Uncommitted code is a smell** - Surface it, let user decide
- **Conversational** - No forced choices or multi-select
- **Project status changes matter** - Capture when things unblock, stall, or archive
- **Friday covers ALL projects** - Not just tier-1, everything non-archived
- **Closure over documentation** - The goal is to clear your head
- **Routines are data** - Track completion to reveal patterns, not to judge
- **Streaks reward consistency** - But breaking one isn't failure, it's information
- **The standing sequence expands by default** - Core projects are never finished. There's always another vinyasa. The modification (encouraged projects) is where the growth is. You teach "meet them where they are" -- meet your own projects where they are. One agent run counts. Zero is the pattern you're breaking.
