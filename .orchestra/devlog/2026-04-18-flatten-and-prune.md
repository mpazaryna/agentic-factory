---
created_on: 2026-04-18
commits: 0adb3cc
---

# Flatten to skills/ + agents/, Prune 78 → 34

## Overview

Restructured agentic-factory from a nested plugin-of-plugins layout into a clean flat library: `skills/`, `agents/`, `plugins/`. Cut 78 skills down to 34 by pruning unused, redundant, and project-specific content.

## Problem

The original structure had skills buried inside plugin subfolders (`orchestra/skills/`, `kairos/skills/`, etc.). This made the library hard to browse, caused name collisions, and duplicated plugin scaffolding across every domain. Skills like `goose`, `rss`, and `spike-driven-dev` had no real home.

## Solution

Moved everything to three top-level directories:

```
skills/     — 34 skills, flat, domain-prefixed
agents/     — eddie, lenny, monk, slim
plugins/    — focused curated subsets (cloudflare)
```

Applied domain prefixes to all skill names:

| Prefix | Domain |
|--------|--------|
| `orchestra-` | Knowledge base methodology |
| `kairos-` | Daily/weekly rhythm |
| `yoga-` | Yoga planning multi-agent |
| `cf-` | Cloudflare Workers platform |
| `swift-` | Swift/SwiftUI development |
| `feynman-` | Technical investigation |
| `dev-` | Developer tooling |
| `writing-` | Prose style |

## What Got Cut

- `goose`, `rss`, `rebuild-readme`, `spike-driven-dev` — no clear value
- All `clickup-*` skills — project-specific, not portable
- Duplicate scaffolding from each domain plugin folder
- `CONTEXT.md`, `PROJECT.md` — stale top-level docs

## Lessons

Name collisions surface immediately when flattening: `kickoff`, `shutdown`, `weekly-plan`, `conventions` existed in multiple domains. Domain prefixes resolved all of them. The flat layout also makes `/skills` discovery much cleaner — Claude sees all 34 at once rather than having to navigate nested plugin paths.
