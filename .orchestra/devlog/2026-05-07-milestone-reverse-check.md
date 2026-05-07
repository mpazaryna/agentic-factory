---
created_on: 2026-05-07
---

# Milestone Reverse Check — Closing the Loop on Scope Drift

## What Changed

Yesterday's devlog ended with one deferred item: `orchestra-milestone` only ran the forward check — what's in the milestone but missing from the repo. It didn't run the reverse — what's in the repo but missing from any milestone.

Today: added it.

`orchestra-milestone` now has a Step 3 that globs `.orchestra/work/*/`, builds the union of all tracked paths across all milestone materials tables in the roadmap, and surfaces any work item folder that doesn't appear in any of them. The report gets an "Orphaned Work Items" section when something is found; the section is omitted entirely when everything is clean.

Step 5 (Propose Work) was extended to cover orphaned items — for each one, suggest: assign to an existing milestone, create a new milestone, or acknowledge as intentional one-off work.

## Why This Matters

The implement pre-flight check (added yesterday) catches orphaned work *before* it starts. The milestone reverse check catches orphaned work *after* it lands — when someone runs a milestone review and finds items in the repo that the roadmap doesn't know about.

Together they close the scope drift loop:

```
pre-flight (implement)   → visible friction at the start of agentic work
reverse check (milestone) → cleanup surface after the fact
```

Neither is a hard stop. The methodology stays permissive — fast-moving work is expected, and sometimes the map genuinely lags the territory. The goal is that the gap is always named and always surfaced, never silently swallowed.

## One Observation

The deferred item was written into yesterday's devlog under "What's Next." The agent picked it up from there this morning without re-explanation. That's the devlog functioning as intended — programme notes for whoever (or whatever) comes next.
