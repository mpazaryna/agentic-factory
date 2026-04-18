---
created_on: 2026-04-18
commits: 2af09a9, a5553e8
---

# Focused Plugin: cloudflare

## Overview

Built a focused `cloudflare` plugin at `plugins/cloudflare/` — a curated subset of the five `cf-*` skills packaged for standalone installation.

## Motivation

Not every Claude Code user needs all 34 skills. Someone working on Cloudflare Workers wants `cf-workers`, `cf-hono`, `cf-kv`, etc. without pulling in orchestra, kairos, yoga, and everything else. A focused plugin solves this.

## Structure

```
plugins/cloudflare/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── cf-workers/
│   ├── cf-workers-ai/
│   ├── cf-hono/
│   ├── cf-kv/
│   └── cf-durable-objects/
└── README.md
```

Skills are physically copied from `skills/` into `plugins/cloudflare/skills/`. The plugin scanner requires files to live under the plugin root — symlinks don't work.

## The "Anthropic Tax"

The plugin system requires skills to live inside the plugin's own directory. When skills already exist in `skills/`, building a focused plugin means copying them in. This duplication is unavoidable — it's the cost of distribution.

For the all-in-one case (`skills@agentic-factory`), `skills/` itself is the plugin and no duplication is needed. For focused plugins, pay the tax.

## Install

```
/plugin marketplace add mpaz/agentic-factory
/plugin install cloudflare@agentic-factory
```

## marketplace.json

Both plugins registered in `.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    { "name": "cloudflare", "source": "./plugins/cloudflare" },
    { "name": "skills",     "source": "./skills" }
  ]
}
```

## Lesson

Focused plugins are straightforward once the tax is understood. The pattern: copy skills in, add `plugin.json`, add README, register in marketplace. Future candidates: `orchestra`, `kairos`, `swift`.
