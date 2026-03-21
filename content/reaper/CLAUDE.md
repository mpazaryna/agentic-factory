# Reaper

Curated RSS news briefing skill. Fetches feeds from OPML files, filters by
user-defined hot/ignore topics, outputs a scannable digest.

## Dependencies

- **reaper MCP server** — must be configured in the runtime's MCP config
  (Claude Desktop, telos, or any MCP-compatible agent)
- **~/.feeds/feeds.toml** — user preferences (default OPML path, hot/ignore topics)
- **~/.feeds/*.opml** — feed subscriptions

## Install

For Claude Desktop, ensure `reaper` is in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "reaper": {
      "command": "uv",
      "args": ["run", "--project", "/Users/mpaz/workspace/reaper", "reaper"]
    }
  }
}
```
