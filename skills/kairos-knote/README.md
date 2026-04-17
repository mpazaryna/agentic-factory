# knote

Capture a quick timestamped thought as a knote.

## Quick Start

```
/kairos:knote
"We figured out the sync issue was a race condition. Knote that."
"knote: API rate limit is 100 req/min"
```

## What It Does

Two capture modes:

- **Explicit invocation** — prompts "What's on your mind?" and waits
- **Natural language** — recognizes "knote that", "log that", "capture that", "quick note:", or any statement followed by a capture instruction, and saves immediately

Creates a file at `kairos/knotes/YYYY/MM/YYYY-MM-DD-HHMMSS.md` with `tags: [knote]` frontmatter. Confirms with the path and stops — no follow-up.

Works well with voice dictation (Wispr). Knotes accumulate and can be reviewed during shutdown or weekly review.

## See Also

- `interstitial` — similar capture but saves to `50-log/interstitial/` (PKM vault pattern)
- `kairos-shutdown` — reviews the day's captures at end of day
