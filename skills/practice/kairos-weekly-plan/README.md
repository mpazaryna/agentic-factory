# kairos-weekly-plan

Draft the start-of-week plan — project triage, load calculation, and priority setting.

## Quick Start

```
/kairos:weekly-plan
```

Run once on Sunday or Monday. Never rerun mid-week — mid-week changes go in ClickUp directly.

## What It Does

Fully autonomous — no questions, no interaction. Gathers everything silently, writes the draft, and reports where it is.

**Pre-flight reads:**
- `kairos/roadmaps/` — the score (domains, milestones, objectives)
- `projects/*.md` — project records and roadmap domain assignments
- Recent devlog, last week's plan + summary, trailing 5-7 daily notes
- ClickUp tickets dated for the week (Sun-Sat)
- Apple Calendar events via `kairos/tools/calendar-week.sh`

**Draft includes:**
- Roadmap Pulse table — each domain, this week's tickets, active projects, flags
- Load calculation from trailing intensity/blocks data
- Calendar events grouped by day
- Flags (overdue items, overstacked days, dark domains, approaching deadlines)
- Open decisions as markdown checkboxes with clickable ClickUp task IDs
- Week Shape — frog, heaviest/lightest day, roadmap coverage, theme

After writing, tells the user: "Draft ready. Review in Obsidian, then run `/weekly-finalize`."

## Supporting Files

- `reference.md` — load thresholds, status question definitions, evaluation criteria

## See Also

- `weekly-finalize` — locks the plan after reviewing decisions in ClickUp
- `kairos-kickoff` — daily orientation that reads the weekly plan
- `review` — end-of-week retrospective
