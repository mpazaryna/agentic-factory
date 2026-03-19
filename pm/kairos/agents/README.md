# Kairos Agents

## Monk

Named after Thelonious Monk. The autonomous timekeeper.

Monk runs the daily rhythm -- kickoff in the morning, shutdown in the evening -- without stopping to ask questions. He reads the pkm skills (kickoff, shutdown, interstitial) as his subject matter expertise, then performs.

### Install

```
/plugin install kairos@agentic-factory
```

Monk is included in the kairos plugin. No separate installation needed.

### Human-in-the-Loop

Use the kairos skills directly. You drive each step:

```
/kairos:kickoff              # Morning orientation (interactive)
/kairos:shutdown             # End-of-day capture (interactive)
/kairos:interstitial         # Quick note capture
```

Each skill stops and asks questions. You respond, refine, approve. The skills are the same knowledge Monk uses -- you're just keeping time manually.

### Autonomous (Monk)

Agents are not slash commands. They're invoked conversationally or via cron/dispatch:

```
"ask monk to run kickoff"
"have monk do the shutdown"
"monk shutdown for 2026-03-18"
```

Monk will:
1. Load pkm skills as domain expertise
2. Read ClickUp, daily notes, weekly plan, project data
3. Write the daily note with coaching embedded as callouts
4. Report what was written and flag any gaps

**No questions asked.** If Monk can't determine something (e.g., intensity is ambiguous), he writes a callout in the note and moves on.

### When to Use Which

| Situation | Approach |
|-----------|----------|
| Foggy morning, need orientation | Human-in-the-loop with `/pkm:kickoff` |
| Clear day, tickets are groomed | "ask monk to run kickoff" or cron |
| End of day, want to reflect | Human-in-the-loop with `/pkm:shutdown` |
| Missed shutdown, closing out next morning | "monk shutdown for [date]" |
| Cron job, fully autonomous | Dispatch Monk on schedule |

### How Monk Uses Skills

Monk is not a replacement for the pkm skills -- he's built on top of them. Before executing, he reads:

- **kickoff** — `${CLAUDE_PLUGIN_DIR}/kickoff/SKILL.md`
- **shutdown** — `${CLAUDE_PLUGIN_DIR}/shutdown/SKILL.md`
- **interstitial** — `${CLAUDE_PLUGIN_DIR}/interstitial/SKILL.md`

The skills are the sheet music. Monk is the one who keeps time.

### Prerequisites

1. Vault with `50-log/daily/`, `50-log/weekly/`, `_data/projects/`
2. `_tools/clickup-today.sh` for task queries
3. `.env` with `CLICKUP_API_KEY`
