---
name: build-deck
description: Convert a Marp markdown presentation to editable PPTX. Use when the user wants to generate, build, or export a slide deck.
user-invocable: true
allowed-tools: Bash, Read, Glob
---

# /build-deck — Generate PPTX from Marp markdown

Convert a Marp `presentation.md` file to an editable `.pptx` file using the project's marp_to_pptx.py script.

## Usage

`/build-deck <deck-folder-name>` — e.g., `/build-deck investor-deck-v2`
`/build-deck all` — build all decks

## Instructions

1. If `$ARGUMENTS` is "all", find all `decks/*/presentation.md` files using Glob. Otherwise, resolve the deck folder:
   - Check `decks/$ARGUMENTS/presentation.md` exists
   - If not found, search `decks/*/presentation.md` for a partial match on the argument

2. For each deck, run the build script:
   ```
   python3 .claude/skills/build-deck/marp_to_pptx.py decks/<folder>/presentation.md decks/<folder>/presentation.pptx
   ```

3. If a `--template` flag is provided in arguments, pass it through:
   ```
   python3 .claude/skills/build-deck/marp_to_pptx.py decks/<folder>/presentation.md decks/<folder>/presentation.pptx --template decks/templates/<name>.pptx
   ```

4. Report results: number of slides parsed, output file path.

## Notes

- The script requires `python-pptx` (`pip install python-pptx`)
- Output is an editable PPTX with real text (not rasterized images)
- The PPTX is suitable for import into Google Slides for business team editing
- Template support is optional — when no template is provided, uses python-pptx defaults
- Code blocks are rendered in Courier New on a light gray background, truncated at 20 lines
- Marp directives like `<!-- _class: dark -->` produce dark-background slides
