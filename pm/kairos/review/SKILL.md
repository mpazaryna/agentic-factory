---
name: review
description: "Run a review at weekly, monthly, or quarterly zoom — synthesize notes, surface patterns, generate retrospective. Use when running periodic reviews."
argument-hint: "weekly | monthly | quarterly"
allowed-tools: Read, Glob, Grep, Bash, Write
disable-model-invocation: false
---

# Review

One skill, three zoom levels. Data cascades up -- weekly reads raw data, monthly reads weeklies, quarterly reads monthlies.

```
/review weekly    -- end of work week (Friday)
/review monthly   -- end of month
/review quarterly -- end of quarter (Mar, Jun, Sep, Dec)
```

## Core Principle

**Present what happened. Don't judge.**

The review surfaces data and patterns. It doesn't lecture about what should have been different. Not every milestone needs weekly attention -- Travel is episodic, connections are organic, art has seasons. Only flag gaps where attention was expected and didn't land (e.g., a trip 3 weeks out with no booking).

The tone from shutdown feedback applies here: ask what drove the period, then assess. The weekly plan is a starting position, not a contract.

## Tone

- Present data first, then patterns
- "Chiro got 18h, Resin got 0h" not "You neglected Resin"
- Only flag milestones where the gap is actionable
- Travel with no activity = normal. Travel with no activity before an unbooked trip = flag.
- The score has milestones with different rhythms. Respect that.

## Zoom Levels

### Weekly (`/review weekly`)

See `weekly.md` for full template.

**Reads:** Daily notes (Mon-Fri), Clockify CSV, ClickUp task completion (via shutdown script), LooseIt email, the week's plan file.

**Writes to:** `# Weekly Summary` section at bottom of `50-log/weekly/YYYY/YYYY-WNN.md`

**Key sections:** What happened (from ClickUp + daily notes), time tracking (Clockify), where the time went (which milestones got attention), health (LooseIt), patterns, next week.

### Monthly (`/review monthly`)

See `monthly.md` for full template.

**Reads:** Weekly reviews for the month (already synthesized). Daily notes only if weekly reviews are missing data.

**Writes to:** `50-log/monthly/YYYY/YYYY-MM.md`

**Key sections:** Portfolio snapshot (status changes), project movement, time trends (from weekly Clockify aggregates), where the time went across the month, goals check (reads `30-resource/planner/life-areas/goals.md`), patterns.

### Quarterly (`/review quarterly`)

See `quarterly.md` for full template.

**Reads:** Monthly reviews for the quarter (already synthesized). Life-area notes (`30-resource/planner/life-areas/`). The score (`99-orchestra/roadmap.md`).

**Writes to:** `50-log/quarterly/YYYY/YYYY-QN.md`

**Key sections:** The quarter in brief (narrative, not metrics), life area review (goals vs evidence), direction check (vision, purpose -- still true?), portfolio alignment (projects serving goals), next quarter focus.

This is a compass check, not a performance review.

## Notes

- Can be run multiple times at any zoom level -- overwrites previous output
- Each level trusts the level below. Monthly doesn't re-read daily notes if weeklies exist.
- Create folders as needed (`50-log/monthly/YYYY/`, `50-log/quarterly/YYYY/`)
- LooseIt data feeds weekly and bubbles up. If not provided at weekly, note it as missing.
- Clockify CSV: look for `~/Desktop/Clockify_Time_Report_Detailed_*.csv`. If not found, ask once.
- ClickUp shutdown data: use `_tools/clickup-today.sh [DATE] --shutdown` for completion picture
- Week = Sun-Sat. Daily notes = Mon-Fri.
