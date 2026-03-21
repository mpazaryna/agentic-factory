---
name: reaper
description: "Curated RSS news briefing — fetches tech feeds and curates a scannable digest. Use when you want a news briefing or ask what's new."
allowed-tools: Read, Write, Bash, WebFetch
disable-model-invocation: false
---

# Reaper — Curated News Briefing

Fetch RSS feeds, filter, and curate a briefing. Write it to a file.

## Feeds

Fetch these two feeds using WebFetch:

1. `https://blog.cloudflare.com/rss/`
2. `https://feeds.arstechnica.com/arstechnica/index`

## Steps

1. Use WebFetch to fetch each feed URL above. The response will be XML (RSS).

2. Parse the XML to extract the 10 most recent entries from each feed. For each entry extract: title, link, published date, and a brief summary.

3. Curate to the 15 most relevant entries across both feeds.

4. Write the briefing to `kairos/briefings/YYYY-MM-DD.md` using this EXACT format:

```markdown
---
tags: [briefing]
date: YYYY-MM-DD
feeds: 2
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
