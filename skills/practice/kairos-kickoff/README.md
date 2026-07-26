# kairos-kickoff

Quick morning orientation — surface ClickUp tasks, carry-overs, project gaps, and intensity patterns.

## Quick Start

```
/kairos:kickoff
```

Run at the start of each workday (Mon-Fri only). Takes under 2 minutes.

## What It Does

1. **Weekend gate** — stops immediately on Saturday or Sunday
2. **Yesterday check** — verifies the previous working day's note has a Shutdown section. If missing, prompts for a quick catch-up and writes it before proceeding
3. **Frog enforcement** — checks if yesterday's named frog was completed. Holds the plan until it's eaten or acknowledged as blocked
4. **Gathers context silently** — reads previous daily note, `projects/` folder, this week's weekly note, recent daily notes, and queries ClickUp for today's assigned tasks
5. **Outputs a single concise block** — yesterday's summary, today's ClickUp tasks, active project gaps, persistent carry-overs, and intensity warnings
6. **Creates today's daily note** — pulls focus from ClickUp and the weekly plan; no questions asked

### Intensity Guard

If the previous day was intensity 5, kickoff flags it directly and requires dialing back. Two consecutive intensity-5 days triggers an escalation: "Today is a reset day."

## See Also

- `kairos-shutdown` — the paired end-of-day ritual
- `kairos-weekly-plan` — the weekly planning draft
- `knote` — capture thoughts mid-day
