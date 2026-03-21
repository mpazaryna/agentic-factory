---
name: reaper
description: "Curated RSS news briefing — fetches feeds from OPML, filters by hot/ignore topics, outputs a scannable digest. Use when you want a news briefing or ask what's new."
allowed-tools: Read, Write, Bash
disable-model-invocation: false
---

# Reaper — Curated News Briefing

Fetch, filter, and curate a news briefing from RSS feeds using the reaper MCP tools.

## Setup

This skill requires:
- The **reaper** MCP server configured in your environment (provides `fetch_opml`, `fetch_feed`, `read_opml` tools)
- A `feeds.toml` file in `~/.feeds/` with your preferences
- One or more OPML files in `~/.feeds/` with your subscriptions

## What to do

1. Read `~/.feeds/feeds.toml` to get:
   - The default OPML file path (under `[sources]`)
   - The `hot` topics list — things to surface and prioritize
   - The `ignore` topics list — things to suppress entirely

2. If the user specified an OPML file or path, use that instead of the default.
   Resolve relative paths against `~/.feeds/`.

3. Use the `fetch_opml` tool to fetch all feeds from the OPML file.
   Pass `limit_per_feed: 10`.

4. **Filter** the returned entries:
   - Drop anything matching an `ignore` topic (check title and summary)
   - Score the rest: entries matching `hot` topics get priority
   - Keep non-hot entries only if they are genuinely significant or surprising

5. **Curate** down to the 15–20 most relevant entries.

6. **Format** the output as a briefing using the format below.

## Output format

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
→ Use default OPML from feeds.toml, full briefing.

User: "briefing from finance.opml"
→ Use `~/.feeds/finance.opml` instead.

User: "what's new in AI"
→ Use default OPML but weight AI/ML stories heavily, shrink other sections.

User: "briefing — last 24 hours only"
→ Standard briefing but filter entries by publication date.
