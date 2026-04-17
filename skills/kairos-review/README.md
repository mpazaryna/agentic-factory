# review

Run a periodic review at weekly, monthly, quarterly, or yearly zoom — synthesize notes, surface patterns, generate retrospective.

## Quick Start

```
/review weekly
/review monthly
/review quarterly
/review yearly
```

## What It Does

One skill, four zoom levels. Data cascades up — weekly reads raw data, monthly reads weeklies, quarterly reads monthlies, yearly reads quarterlies.

### Weekly
Reads daily notes (Mon-Fri), Clockify CSV, ClickUp task completion, LooseIt email, and the week's plan. Appends a `# Weekly Summary` section to `kairos/logs/weekly/YYYY/YYYY-WNN.md`.

### Monthly
Reads weekly reviews for the month (already synthesized). Writes `kairos/logs/monthly/YYYY/YYYY-MM.md`. Covers portfolio snapshot, project movement, time trends, goals check.

### Quarterly
Reads monthly reviews. Writes `kairos/logs/quarterly/YYYY/YYYY-QN.md`. A compass check — life area review, direction check, portfolio alignment. Not a performance review.

### Yearly
Reads quarterly reviews. Writes `kairos/logs/yearly/YYYY.md`. The year in narrative: what changed, what held, what surprised you.

**Tone:** Present what happened — don't judge. "Chiro got 18h, Resin got 0h" not "You neglected Resin." Only flag gaps where attention was expected and didn't land.

Can be run multiple times at any zoom level — overwrites previous output.

## File Structure

- `weekly.md`, `monthly.md`, `quarterly.md`, `yearly.md` — full output templates for each zoom level

## See Also

- `weekly-summary` — standalone weekly summary generator
- `monthly-summary` — standalone monthly summary generator
- `kairos-shutdown` — daily capture that feeds into weekly review
