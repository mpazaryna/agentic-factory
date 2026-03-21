---
name: reaper
description: "Curated RSS news briefing — fetches feeds from vault OPML files or a URL, filters and curates a scannable digest. Use when you want a news briefing or ask what's new."
allowed-tools: Read, Write, Bash
disable-model-invocation: false
---

# Reaper — Curated News Briefing

Fetch, filter, and curate a news briefing from RSS feeds. OPML files live in the vault at `data/opml/`.

## Setup

Place your OPML subscription files in `data/opml/` in the working directory:

```
data/
└── opml/
    ├── tech.opml
    ├── business.opml
    └── [any other .opml files]
```

## How It Works

```bash
# Fetch from vault OPML
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py --opml data/opml/tech.opml

# Single feed by URL
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py https://blog.cloudflare.com/rss/

# Limit entries per feed
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py --opml data/opml/tech.opml --limit 5
```

## What to Do

1. Check `data/opml/` for available OPML files. If none exist, tell the user to add their subscriptions there.

2. Determine which feeds to use:
   - Default: first available OPML in `data/opml/`
   - User specifies "business", "tech", etc.: match to filename
   - User provides a URL: fetch that single feed

3. Fetch and parse the JSON output.

4. Filter and curate to 15-20 entries.

5. Write the briefing to `kairos/briefings/YYYY-MM-DD.md`.

## Output Format

```markdown
---
tags: [briefing]
date: YYYY-MM-DD
feeds: [count]
---

# Briefing — {Month Day, Year}

## Hot

- **Story title** — One-sentence summary of why this matters.
  _Source: Feed Name_ · [link](url)

## Notable

- **Story title** — One-sentence summary.
  _Source: Feed Name_ · [link](url)

## Radar

- [Story title](url) — _Source_
```

## Rules

- No emoji. Clean markdown only.
- No preamble or closing remarks. Just the briefing.
- One sentence per summary. The user scans, not reads.
- Drop job posts, sponsored content, low-substance items silently.
- Write to file, then report the path.
- If a feed failed to fetch, note at the bottom: `_Failed: Feed Name (reason)_`
