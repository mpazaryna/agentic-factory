# CLAUDE.md

Kairos is the AI-augmented productivity system. The name references kairos -- the right or opportune moment -- as opposed to chronos (sequential time). The system maintains the daily rhythm so the human can focus on the work.

## Philosophy

Traditional productivity systems make you the executor. Kairos inverts this: the AI reads notes, queries task systems, and writes the daily record. The human reads the output and engages when they choose to. The ceremony is optional; the data capture is not.

## Components

### Skills

**Daily Rituals:**
- **kickoff** — Morning orientation: carry-overs, project status, daily focus
- **knote** — Quick timestamped thought capture throughout the day
- **shutdown** — End-of-day closure: accomplishments, blockers, intensity, tomorrow's frog

**Weekly:**
- **weekly-plan** — Start-of-week planning with load calculation and project triage
- **weekly-finalize** — Finalize the weekly plan after reviewing decisions in ClickUp
- **review** — Review at weekly, monthly, or quarterly zoom (dispatches to sub-documents)

**Utilities:**
- **remarkable** — Extract dated entries from Remarkable PDF notebooks into knotes

### Agent: Monk

Named after Thelonious Monk. Keeps his own time.

Monk runs kickoff and shutdown autonomously -- reads ClickUp, daily notes, weekly plan, and project data, then writes the daily note with coaching embedded as content, not questions. Designed for cron or dispatch triggers.

Monk loads the sibling skills as domain expertise:
- **kickoff** — `${CLAUDE_PLUGIN_DIR}/kickoff/SKILL.md`
- **shutdown** — `${CLAUDE_PLUGIN_DIR}/shutdown/SKILL.md`
- **knote** — `${CLAUDE_PLUGIN_DIR}/knote/SKILL.md`

## Data Layout

Two-folder convention: `kairos/` owns time, `projects/` owns work.

```
workspace/
├── projects/                         # shared canonical data — read by all agents
│   └── *.md
├── kairos/                           # kairos-specific state
│   ├── logs/
│   │   ├── daily/YYYY/YYYY-MM-DD.md
│   │   ├── weekly/YYYY/YYYY-WNN.md
│   │   ├── monthly/YYYY/YYYY-MM.md
│   │   ├── quarterly/YYYY/YYYY-QN.md
│   │   └── yearly/YYYY.md
│   ├── knotes/YYYY/MM/YYYY-MM-DD-HHMMSS.md
│   ├── life-areas/goals.md
│   ├── roadmaps/*.md
│   ├── devlog/
│   └── tools/
│       ├── clickup-today.sh
│       └── calendar-week.sh
└── .env
```

Monk reads from (never asks for):
- ClickUp API via `kairos/tools/clickup-today.sh`
- Daily notes (`kairos/logs/daily/`)
- Weekly plan (`kairos/logs/weekly/`)
- Project records (`projects/`)

## Design Principles

1. **Read everything, ask nothing.** No `AskUserQuestion`. If Monk can't determine something, it writes a callout in the note.
2. **Write coaching, not prompts.** "Day 4 without a modification" goes into the note as an observation, not a question.
3. **ClickUp is the source of truth.** Open tasks stay open. Don't narrate what the system already tracks.
4. **Gaps are visible, not guilty.** Missing data is flagged, not judged.
5. **The board is the score.** If a project has tickets, they get picked up. If it doesn't, there's nothing to execute.
