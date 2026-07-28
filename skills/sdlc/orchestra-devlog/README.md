# orchestra-devlog

> The engineer's journal — the story behind the commits, for whoever works here next.

Output goes to `.orchestra/devlog/`.

## Quick Start

```
"Journal this"
"Journal the last 4 hours"
"Write a devlog about the auth changes"
```

## Report Types

| Type | Purpose | Trigger |
|------|---------|---------|
| **Git Journal** | Summarize work from commit history | "journal this", "journal today" |
| **Devlog** | Narrative work documentation | "devlog", "write a devlog" |

## How It Works

1. The skill identifies the report type from the request
2. It loads the matching template from `examples/`
3. For git journals it reads commit history automatically
4. It writes the formatted entry to `.orchestra/devlog/`

## Examples

**Git Journal** — after a coding session:

```
"Journal this refactor"
→ Reads recent commits
→ Structured summary: decisions, files changed, next steps
```

**Devlog** — explaining work to whoever picks it up next:

```
"Write a devlog about the auth changes"
→ Narrative format with context, decisions, learnings
```

## Structure

```
orchestra-devlog/
├── SKILL.md              # Orchestrator (routes to templates)
├── README.md             # This file
├── HOW_TO_USE.md         # Detailed usage
├── evals/
└── examples/
    ├── github-journal.md # Git-based journal template
    └── devlog.md         # Narrative devlog template
```

## Related

Part of the `sdlc/` orchestra loop — see [../README.md](../README.md). The devlog
is written throughout, but most often alongside `orchestra-implement` and at the
close of a session.
