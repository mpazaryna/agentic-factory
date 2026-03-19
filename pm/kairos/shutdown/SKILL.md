---
description: End-of-day capture. Quick closure, clear state.
---

# Shutdown

Quick end-of-day ritual - under 3 minutes. Capture and clear.

## Weekend Gate

If the target day is Saturday or Sunday, skip. No weekend shutdowns.

## Detect Target Day

Before gathering context, determine which day this shutdown is for.

1. Check the previous working day's daily note for a `## Shutdown` section.
2. Check today's daily note for a `## Shutdown` section.

**If the previous working day's note exists but has no Shutdown section:** This is likely a late shutdown. Confirm with the user:

```
Looks like [previous day] didn't get a shutdown. Closing out that day or today?
```

Wait for response. The answer determines the **target day**.

**If both have Shutdown sections or the previous day has one:** Target day is today. Proceed normally.

**If the user explicitly says "shutdown for [date]":** Use that as the target day.

Track whether this is a **late shutdown** (target day < today). This affects the frog question later.

## Gather Context (silently)

Read in parallel, don't output yet:
1. Target day's daily note - what was the Focus?
2. Current week's plan (`50-log/weekly/`) - what was planned for today? What's planned for tomorrow? Are encouraged projects intentionally skipped this week?
3. `_data/projects/*.md` - all non-archived projects
4. Active project repos - check for uncommitted work
5. ClickUp tasks assigned to the target day - use `_tools/clickup-today.sh [DATE] --shutdown` to get both open AND completed tasks (including subtasks closed today without a start_date)

## Check Uncommitted Work

Run `git status` in repos for active projects. Only surface if there are uncommitted changes.

If found: "resin-platform has uncommitted changes - commit, stash, or leave?"

Don't use AskUserQuestion. Just ask and wait for response.

## Check ClickUp Task Completion

Run `_tools/clickup-today.sh [DATE] --shutdown` to get the full picture:
- Tasks with start_date today (open and completed)
- Tasks closed today that had no start_date (subtasks, ad-hoc work)

Surface the summary: how many completed, how many still open. The ClickUp data tells you which projects got attention -- don't ask the user to repeat this.

```
ClickUp: 11 of 13 tasks completed today. Open: "Pipeline Phase 2", "Sean Allen Course" -- carry to tomorrow or reschedule?
```

## Ask Core Questions

Simple, conversational. No predefined options.

ClickUp data already tells you what was accomplished and which projects got attention. Don't ask the user to repeat what the data shows. Instead, present the summary and ask only what the data can't tell you:

```
ClickUp shows [N] tasks completed today across [projects].
[list key completions]
[N] still open: [list] -- carry to tomorrow or reschedule?

Any blockers or carry-over beyond those?
Any project status changes? (unblocked, stalled, ready to archive?)

Quick metrics for the load system:
- Intensity today? (1-5, where 1=coasting, 3=steady, 5=full burn)
- How many blocks did you actually work?
```

These metrics feed the load calculation that determines next week's pace.

### Intensity Guard

After capturing today's intensity, check the previous working day's frontmatter for its `intensity` value.

**If today is intensity 5 AND the previous day was also intensity 5:**

```
Two burn days in a row. You've seen this pattern before --
it leads to depletion, not throughput. Tomorrow must be a 3
or lower. What can you cut or simplify from tomorrow's plan?
```

Don't accept "I'll be fine" or "I'll see how I feel." The data is clear: consecutive intensity-5 days produce a crash. A deliberate recovery day is not lost productivity -- it's what prevents losing the next three days. Marathon, not sprint.

**If today is intensity 5 (but the previous day wasn't):**

Note it without alarm, but seed the awareness:

```
Intensity 5 today. Keep tomorrow at 3-4 to avoid the
consecutive burn pattern. What's a lighter plan?
```

Wait for responses, then record.

## The Modification Check

After recording accomplishments, check: **did today's modification happen?**

**First, check the weekly plan.** If encouraged projects are marked as intentionally skipped this week, skip the modification check entirely. The weekly plan is the authority on this -- don't second-guess a deliberate decision.

If modifications are expected this week, read `_data/projects/*.md` for all encouraged-status projects. Cross-reference with the ClickUp completion data (which projects got attention is already known from the task query).

**If an encouraged project got attention:** Acknowledge it simply. "Modification landed. AA got an agent run." No fanfare.

**If no encouraged project got attention, day 1-2:** Gentle.

```
No modification today. The standing sequence took the full class.
Tomorrow -- what's one task you can hand to an agent for AA or YH?
```

**If no encouraged project got attention, day 3+:** The look.

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

## Record to Daily Note

Update the **target day's** daily note -- Shutdown section AND frontmatter:

**Frontmatter additions:**
```yaml
---
tags: [daily]
date: 2026-03-03
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

**Late shutdown note:** If this is a late shutdown, add annotation:

```markdown
## Shutdown (recorded Mar 4)
```

## Name the Next Frog

Before closing, ask about the frog. **Adapt based on timing:**

**Same-day shutdown:**
```
Name tomorrow's frog. One specific task -- not "admin."
(Or "nothing pending")
```

**Late shutdown (running the next morning):**
```
Name today's frog. One specific task -- not "admin."
(Or "nothing pending")
```

**Friday shutdown:** Tomorrow is the weekend. No frog needed. But ask:
```
Anything lingering that should be Monday's frog?
```

If they name something, include it in the Tomorrow section with the label **Frog:**. This seeds the next kickoff.

```markdown
**Tomorrow:**
- **Frog:** Follow up with Joe on billing
- Chiro UAT continues
```

## Confirm and Close

Brief summary of what was captured:

**Same-day shutdown:**
```
Recorded. Uncommitted work handled. See you tomorrow.
```

**Late shutdown:**
```
[Day] closed out. Recorded to [date]'s note. Ready for today.
```

**Friday shutdown:**
```
Week captured. Run /weekly-summary for full retrospective. Have a good weekend.
```

## Principles

- **Quick capture** - Don't overthink, just record
- **Uncommitted code is a smell** - Surface it, let user decide
- **ClickUp completion check** - Surface incomplete tasks, don't let them disappear
- **Conversational** - No forced choices or multi-select
- **Project status changes matter** - Capture when things unblock, stall, or archive
- **Closure over documentation** - The goal is to clear your head
- **Mon-Fri only** - No weekend shutdowns
- **Late shutdown beats no shutdown** - A retroactive close-out the next morning is better than a gap in the record
- **The standing sequence expands by default** - The modification is where the growth is. One agent run counts. Zero is the pattern you're breaking.
- **Marathon, not sprint** - Two consecutive intensity-5 days is a pattern that leads to depletion. The shutdown is the last chance to catch this before tomorrow's kickoff inherits the momentum.
