---
name: compose-guide
description: Compose a guide from UAT walkthrough files into a single handbook. Use when UAT files have been updated and guides need recomposing, or when generating guides for handoff. Supports markdown composition and styled PDF generation.
---

# Compose Guide

Compose handbooks from UAT walkthrough files. Extracts `## Walkthrough` sections from `docs/uat/` files, stitches them into cohesive guides, and optionally generates styled PDFs.

## How It Works

All mechanical work is handled by `scripts/compose-guide.py`. This skill tells you when and how to invoke it.

### Commands

```bash
# Compose one guide
uv run scripts/compose-guide.py getting-started

# Compose one guide + PDF
uv run scripts/compose-guide.py getting-started --pdf

# Compose all guides
uv run scripts/compose-guide.py --all

# Compose all guides + PDFs
uv run scripts/compose-guide.py --all --pdf

# Show which UAT IDs aren't in any guide
uv run scripts/compose-guide.py --coverage

# List available guides
uv run scripts/compose-guide.py
```

### Dependencies

Dependencies are declared inline in the script via PEP 723. `uv run` handles them automatically — no manual install needed.

## When to Invoke This Skill

### As an agent completing a programming task

If you updated any `docs/uat/*.md` file (added or changed a `## Walkthrough` section), recompose affected guides:

1. Read `docs/guides/manifest.json`
2. Find which guides include the UAT ID you changed
3. Run `uv run scripts/compose-guide.py <guide-name>` for each affected guide

### As a human

Use `/compose-guide getting-started --pdf` to manually compose and generate a PDF for sharing.

### Coverage audit

Run `uv run scripts/compose-guide.py --coverage` to find UAT IDs not included in any guide. This surfaces features that were added but never documented in a guide.

## Resources

| File | Role |
|------|------|
| `scripts/compose-guide.py` | Composition + PDF script |
| `docs/guides/manifest.json` | Guide definitions — source of truth |
| `docs/guides/guide-style.css` | PDF styling |
| `docs/guides/composed/` | Output directory (fully regenerable) |
| `docs/guides/primary/` | Hand-written guides (never touched) |
| `docs/uat/*.md` | Source walkthrough files |

## Manifest Structure

`docs/guides/manifest.json` defines all guides:

```json
{
  "output_dir": "composed",
  "source_dir": "../uat",
  "guides": [
    {
      "name": "getting-started",
      "title": "Getting Started",
      "description": "Core workflow: create an item, generate a report...",
      "ids": ["201", "301", "302", "302-02", "305", "306", "1204"]
    }
  ]
}
```

Each guide has a `name` (used for filename), `title`, `description`, and ordered `ids` array referencing UAT file IDs.

## Composition Rules

- Walkthroughs are extracted **verbatim** — no rewriting, no AI embellishment
- Image paths are rewritten for the output directory depth (`../screenshots/` → `../../screenshots/`)
- UAT H1 titles are cleaned: "201 — Create a New Record" → "Create a New Record"
- The `## Walkthrough` heading is stripped — the step heading replaces it
- `docs/guides/composed/` is fully regenerable — everything in it can be deleted and rebuilt

## See Also

- `ADR-023` — UAT documentation and guide composition (full architecture)
- `CLAUDE.md` → "After Completing a Task" — workflow trigger for recomposition
