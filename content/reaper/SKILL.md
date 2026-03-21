---
name: reaper
description: "Curated RSS news briefing — fetches feeds from a URL or OPML file, filters by hot/ignore topics, outputs a scannable digest. Use when you want a news briefing or ask what's new."
allowed-tools: Read, Bash
disable-model-invocation: false
---

# Reaper — Curated News Briefing

Fetch, filter, and curate a news briefing from RSS feeds. No MCP server needed — uses a bundled Python script.

## Setup

- A `feeds.toml` file in `~/.feeds/` with your preferences (hot/ignore topics, default OPML)
- One or more OPML files in `~/.feeds/` with your subscriptions
- Python 3.8+ (standard library only — no pip install needed)

## How It Works

The skill uses `${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py` to fetch feeds. The script takes a URL or OPML file and returns JSON.

```bash
# Single feed
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py https://blog.cloudflare.com/rss/

# All feeds from an OPML file
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py --opml ~/.feeds/tech.opml

# Limit entries per feed
python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py --opml ~/.feeds/tech.opml --limit 5
```

## What to Do

1. Read `~/.feeds/feeds.toml` to get:
   - The default OPML file path (under `[sources]`)
   - The `hot` topics list — things to surface and prioritize
   - The `ignore` topics list — things to suppress entirely

2. If the user specified a URL, fetch that single feed:
   ```bash
   python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py <url>
   ```

3. If the user specified an OPML file, or no specific source (use default from feeds.toml):
   ```bash
   python3 ${CLAUDE_SKILL_DIR}/tools/fetch_feeds.py --opml <path>
   ```

4. Parse the JSON output. **Filter** the entries:
   - Drop anything matching an `ignore` topic (check title and summary)
   - Score the rest: entries matching `hot` topics get priority
   - Keep non-hot entries only if they are genuinely significant or surprising

5. **Curate** down to the 15-20 most relevant entries.

6. **Format** the output as a briefing using the format below.

## Output Format

```
# Briefing — {Month Day, Year}

## Hot

Stories matching your hot topics, ranked by relevance.

- **Story title** — One-sentence summary of why this matters.
  _Source: Feed Name_ · [link](url)

## Notable

Significant stories outside your stated interests.

- **Story title** — One-sentence summary.
  _Source: Feed Name_ · [link](url)

## Radar

Quick mentions — one line each.

- [Story title](url) — _Source_
```

## Rules

- Lead with hot-topic matches under **Hot**. These are the user's stated interests — give them priority.
- **Notable** is for stories that don't match hot topics but are genuinely significant.
- **Radar** is for everything else worth a glance — one line, no summary.
- Do NOT include anything matching ignore topics. Drop them silently.
- Do NOT include job posts, sponsored content, or low-substance items.
- Do NOT add preamble or closing remarks. Just the briefing.
- Be concise. One sentence per summary. The user scans this, not reads essays.
- If a feed failed to fetch, mention it briefly at the bottom: `_Failed: Feed Name (reason)_`

## Examples

User: "briefing"
> Use default OPML from feeds.toml, full briefing.

User: "briefing from finance.opml"
> Use `~/.feeds/finance.opml` instead.

User: "what's new on cloudflare"
> Fetch `https://blog.cloudflare.com/rss/` directly, single-feed briefing.

User: "what's new in AI"
> Use default OPML but weight AI/ML stories heavily, shrink other sections.
