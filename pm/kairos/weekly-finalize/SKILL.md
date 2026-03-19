---
description: Finalize the weekly plan after reviewing and acting on decisions in ClickUp.
---

# Weekly Finalize

Run after you've reviewed the `/weekly-plan` draft and acted on decisions in ClickUp. This is a quick close-out, not a work session.

## Workflow

1. **Read the current week's plan** -- `50-log/weekly/YYYY/YYYY-WNN.md`

2. **Check decisions** -- read the Decisions section:
   - Checked items = handled in ClickUp already
   - Unchecked items = ask briefly: "Did you handle [X] in ClickUp, or skipping this week?"

3. **Verify week shape** -- re-read ClickUp via `_tools/clickup-today.sh` for Mon-Fri to confirm the shape matches what the user set up. If the frog, heaviest day, or score coverage changed based on the user's ClickUp moves, update the Week Shape section.

4. **Mark finalized** -- add `finalized: true` to frontmatter. This signals to `/kickoff` that the plan is locked.

5. **Confirm** -- "W[NN] finalized. Ready for Monday `/kickoff`."

## Notes

- The user acts on decisions in ClickUp directly, not through this skill
- This skill reads the result of those actions, not performs them
- Should be near-zero interaction if all checkboxes are checked
- Don't regenerate the draft -- only update Week Shape if ClickUp reality changed
- If the user edited the file in Obsidian (changed theme, added notes), respect those changes
