# Reaper

Curated RSS news briefing skill. Fetches feeds from URLs or OPML files, filters by
user-defined hot/ignore topics, outputs a scannable digest.

No MCP server required — uses a bundled Python script (`tools/fetch_feeds.py`) that
runs with standard library only.

## Dependencies

- **Python 3.8+** — standard library only, no pip install
- **~/.feeds/feeds.toml** — user preferences (default OPML path, hot/ignore topics)
- **~/.feeds/*.opml** — feed subscriptions
