---
name: rss
description: "Fetch RSS feeds and curate a scannable news briefing. Use when you want a news briefing or ask what's new."
allowed-tools: Read, Write, Bash
disable-model-invocation: false
---

# RSS — Curated News Briefing

Fetch RSS feeds using the bundled Python script at `${CLAUDE_SKILL_DIR}/../tools/fetch_feeds.py`. The script reads OPML files from the vault's `data/opml/` folder.

## Setup

Place OPML subscription files in `data/opml/` in the working directory:

```
data/opml/
├── tech.opml
├── business.opml
└── [any .opml files]
```

## How to Fetch

```bash
# All feeds from an OPML file
python3 ${CLAUDE_SKILL_DIR}/../tools/fetch_feeds.py --opml data/opml/tech.opml

# Single feed by URL
python3 ${CLAUDE_SKILL_DIR}/../tools/fetch_feeds.py https://blog.cloudflare.com/rss/

# Limit entries per feed
python3 ${CLAUDE_SKILL_DIR}/../tools/fetch_feeds.py --opml data/opml/tech.opml --limit 5
```

The script returns JSON. Parse it to build the briefing.

## Steps

1. Check `data/opml/` for available OPML files. If none exist, tell the user to add their subscriptions there and stop.

2. Run the fetch script:
   ```bash
   python3 ${CLAUDE_SKILL_DIR}/../tools/fetch_feeds.py --opml data/opml/tech.opml
   ```

3. Parse the JSON output. Filter and curate to the 15-20 most relevant entries.

4. Write the briefing to `kairos/briefings/YYYY-MM-DD.md` using this EXACT format:

```markdown
---
tags: [briefing]
date: YYYY-MM-DD
feeds: [number of feeds]
---

# Briefing — Month Day, Year

## Hot

- **Story title** — One-sentence summary of why this matters.
  _Source: Feed Name_ · [link](url)

## Notable

- **Story title** — One-sentence summary.
  _Source: Feed Name_ · [link](url)

## Radar

- [Story title](url) — _Source_
```

5. After writing the file, output ONLY: `Briefing written to kairos/briefings/YYYY-MM-DD.md`

## Rules

- No emoji.
- No preamble or closing remarks.
- One sentence per summary.
- Drop sponsored content or low-substance items.
- Output the briefing format EXACTLY as shown above. Do not summarize it conversationally.
