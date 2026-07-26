# weekly-finalize

Finalize the weekly plan after reviewing and acting on decisions in ClickUp.

## Quick Start

```
/weekly-finalize
```

Run after you've reviewed the `/weekly-plan` draft in Obsidian and acted on the decision checkboxes in ClickUp.

## What It Does

Quick close-out, not a work session:

1. Reads the current week's plan file
2. Checks the Decisions section — unchecked items get a brief confirmation ("Did you handle X in ClickUp, or skipping this week?")
3. Re-reads ClickUp via the weekly script to verify the week shape matches what the user set up — updates Week Shape if the frog, heaviest day, or roadmap coverage changed
4. Adds `finalized: true` to the frontmatter — signals to `/kickoff` that the plan is locked
5. Confirms: "W[NN] finalized. Ready for Monday kickoff."

Near-zero interaction if all decision checkboxes are already checked. Respects any edits the user made in Obsidian.

## Notes

- The user acts on decisions in ClickUp directly — this skill reads the result, not performs it
- Never regenerates the draft — only updates Week Shape if reality changed
- Run once, after `/weekly-plan` draft is reviewed

## See Also

- `weekly-plan` — generates the draft that this skill finalizes
- `kickoff` — reads the finalized plan each morning
