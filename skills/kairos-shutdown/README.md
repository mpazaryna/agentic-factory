# kairos-shutdown

End-of-day capture — ClickUp completion check, uncommitted work, intensity rating, and tomorrow's frog.

## Quick Start

```
/kairos:shutdown
```

Run at the end of each workday (Mon-Fri only). Takes under 3 minutes.

## What It Does

1. **Weekend gate** — skips Saturday and Sunday
2. **Detect target day** — handles late shutdowns (running the next morning for yesterday); asks which day to close if ambiguous
3. **Checks uncommitted work** — runs `git status` in active project repos; surfaces any unstaged changes
4. **ClickUp completion check** — runs the clickup-today script to get completed and open tasks for the day; presents the count and asks about carry-overs
5. **Asks only what data can't tell** — blockers, project status changes, intensity (1-5), and block count
6. **Intensity guard** — flags two consecutive intensity-5 days and pushes back on "I'll be fine"
7. **Writes to the daily note** — updates frontmatter (intensity, blocks, projects) and the Shutdown section
8. **Names the next frog** — prompts for one specific task to anchor tomorrow's kickoff

Friday shutdown prompts for a potential Monday frog instead of tomorrow's.

## See Also

- `kairos-kickoff` — the paired morning ritual that reads this data
- `kairos-weekly-plan` — weekly planning draft
- `review` — generates the weekly retrospective
