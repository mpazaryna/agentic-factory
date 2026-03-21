---
name: reaper
description: "Curated RSS news briefing — fetches feeds from bundled OPML files or a URL, filters and curates a scannable digest. Use when you want a news briefing or ask what's new."
allowed-tools: Read, Bash
disable-model-invocation: false
---

# Reaper — Curated News Briefing

Fetch, filter, and curate a news briefing from RSS feeds. OPML files are bundled — no external config needed.

## Available Feeds

| File | Description |
|------|-------------|
| `${CLAUDE_SKILL_DIR}/opml/tech.opml` | AI/ML, tech news, development (7 feeds) |
| `${CLAUDE_SKILL_DIR}/opml/business.opml` | Finance, markets, startups (4 feeds) |

## How It Works

```bash
# All tech feeds (default)
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py --opml ${CLAUDE_SKILL_DIR}/opml/tech.opml

# Business feeds
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py --opml ${CLAUDE_SKILL_DIR}/opml/business.opml

# Single feed by URL
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py https://blog.cloudflare.com/rss/

# Limit entries per feed
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py --opml ${CLAUDE_SKILL_DIR}/opml/tech.opml --limit 5
```

## What to Do

1. Determine which feeds to use:
   - Default (no qualifier): `tech.opml`
   - "business" or "startups": `business.opml`
   - Specific URL provided: fetch that single feed

2. Fetch the feeds:
   ```bash
   python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py --opml ${CLAUDE_SKILL_DIR}/opml/<file>.opml
   ```

3. Parse the JSON output. **Filter** the entries:
   - Drop job posts, sponsored content, low-substance items
   - Identify genuinely significant or surprising stories
   - Curate down to the 15-20 most relevant entries

4. **Format** the output as a briefing:

```
# Briefing — {Month Day, Year}

## Hot

Top stories — the most significant items across all feeds.

- **Story title** — One-sentence summary of why this matters.
  _Source: Feed Name_ · [link](url)

## Notable

Worth knowing — significant but not leading.

- **Story title** — One-sentence summary.
  _Source: Feed Name_ · [link](url)

## Radar

Quick mentions — one line each.

- [Story title](url) — _Source_
```

## Rules

- No emoji. Clean markdown only.
- No preamble or closing remarks. Just the briefing.
- One sentence per summary. The user scans, not reads.
- Drop job posts, sponsored content, low-substance items silently.
- If a feed failed to fetch, note at the bottom: `_Failed: Feed Name (reason)_`

## Examples

User: "what's new" or "news"
> Fetch tech.opml, full briefing.

User: "business news" or "startup news"
> Fetch business.opml.

User: "what's new on cloudflare"
> Fetch `https://blog.cloudflare.com/rss/` directly.
