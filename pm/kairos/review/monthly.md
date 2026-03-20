# Monthly Review Template

Writes to `kairos/monthly/YYYY/YYYY-MM.md`. Create folder if needed.

## Pre-Flight

1. **Weekly reviews** -- read all `kairos/weekly/YYYY/YYYY-WNN.md` files overlapping this month. These are the primary source.
2. **Project data** -- read `projects/*.md` for current status
3. **Goals** -- read `kairos/life-areas/goals.md`
4. **Score** -- read `kairos/roadmaps/` for milestone context

Only read daily notes if weekly reviews are missing data.

## Output

```markdown
---
tags: [monthly, review]
date: YYYY-MM
---

# Monthly Review -- YYYY-MM

*Generated: YYYY-MM-DD*

## The Month in Brief

[2-3 sentences. The story, not the metrics.]

## Where the Month Went

| Milestone | Weeks with attention | Notes |
|-----------|---------------------|-------|
| Professional | 4/4 | Chiro dominated, Resin steady |
| Music | 3/4 | Missed W10 (illness) |
| Art | 2/4 | Class started W12 |
| Personal | 2/4 | Yoga steady, connections sporadic |
| Travel | 1/4 | DC booked W11 |

## Portfolio Movement

| Project | Status | Direction | Notes |
|---------|--------|-----------|-------|
| Chiro | active | Forward | [from weekly data] |

**Status changes this month:**
- [project]: [old] -> [new] (why)

## Time (Clockify aggregate)

**Monthly total: XX.Xh** (billable: XX.Xh)

| Project | Hours | % of Total |
|---------|-------|------------|
| Chiro | X.Xh | X% |

**Weekly trend:**
| Week | Hours |
|------|-------|
| W09 | X.Xh |

## Health (LooseIt aggregate)

[Averaged from weekly reviews. Trend over the month.]

## Goals Check

*Source: [[30-resource/planner/life-areas/goals]]*

| Life Area | Goal | Evidence This Month | Assessment |
|-----------|------|---------------------|------------|
| Career | 70k freelance | Clockify billable hours, project progress | [on track / needs attention / no data] |

## Patterns

**What dominated:** [where the time went]
**What grew:** [milestones that gained momentum]
**What faded:** [milestones that lost attention -- only flag if actionable]
**System health:** [did the weekly plan → kickoff → shutdown loop hold?]

## Next Month

[Brief -- what carries forward, what's coming up]
```

## Notes

- Monthly trusts weekly reviews. Don't re-derive what's already synthesized.
- Update `goals.md` status annotations if warranted.
- Be honest but not judgmental. "Resin got 0h" is data. "You neglected Resin" is editorializing.
