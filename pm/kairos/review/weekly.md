# Weekly Review Template

Appends to `kairos/weekly/YYYY/YYYY-WNN.md` under `# Weekly Summary`.

## Pre-Flight

1. **Clockify CSV** -- look for `~/Desktop/Clockify_Time_Report_Detailed_*.csv` matching the week. If not found, ask once.
2. **LooseIt email** -- user provides. If not available, note as missing.
3. **Daily notes** -- read Mon-Fri from `kairos/daily/YYYY/`
4. **ClickUp completions** -- run `kairos/tools/clickup-today.sh [DATE] --shutdown` for each day to get completed tasks
5. **The week's plan** -- read the current `kairos/weekly/YYYY/YYYY-WNN.md` for flags and decisions

## Output

```markdown
---

# Weekly Summary

*Generated: YYYY-MM-DD HH:MM*

## Where the Week Went

Walk the score milestones first. This is the lead section -- it frames the week through the year's arrangement, not through whichever project was loudest.

| Milestone | Attention | Notes |
|-----------|-----------|-------|
| Personal | Partial | Yoga daily, connections quiet |
| Art | No | Class starts next week -- normal |
| Music | Yes | Piano lesson + 3 practice sessions |
| Professional | Yes | Chiro 18h, Resin 2h |
| Travel | No | Nothing due -- normal |

[Only flag gaps where attention was expected. Don't penalize episodic milestones.]

## The Week by Milestone

Walk through each milestone briefly. Lead with life milestones, Professional last. Not every milestone needs a section -- skip ones with nothing to say.

**Personal:** [what happened or didn't -- yoga, connections, health, frogs]
**Music:** [lessons, practice]
**Professional:** [narrative of the code/business work -- this is where the ticket detail lives]

## Time (Clockify)

**Total: XX.Xh** (billable: XX.Xh)

| Project | Hours | Key Work |
|---------|-------|----------|
| Chiro | X.Xh | [brief] |

## Health (LooseIt)

| Metric | Value |
|--------|-------|
| Avg daily calories | X |
| Weight trend | X -> Y |
| Protein avg | Xg |

[Brief assessment against lipid plan goals, or "LooseIt data not provided"]

## Patterns

**What flowed:** [projects/activities that had momentum]
**What stuck:** [carry-overs, recurring blockers -- name the pattern, don't lecture]
**Frog compliance:** [eaten or carried?]
**Load:** avg intensity X.X, avg pomodoros X.X -- [trend vs last week]

## Next Week

[Brief -- what carries forward, what's coming up, any course corrections]
```

## Evaluation (internal, not written to file)

Use these to inform the Patterns section:
- Did Professional crowd out everything else?
- Were non-code commitments honored?
- Did the plan's decisions get executed in ClickUp?
- Any frog carry over 2+ days?
