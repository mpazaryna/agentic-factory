---
name: Remarkable Notebook Extraction
description: Extract dated entries from a Remarkable PDF notebook into interstitial notes
source: original
collected: 2025-02-05
tags: [pkm, remarkable, capture, extraction, obsidian]
---

# Remarkable Notebook Extraction

Extract dated entries from a monthly Remarkable PDF notebook into interstitial notes.

**Incremental by design:** Safe to run repeatedly as you add to the notebook throughout the month. Already-extracted dates are skipped.

## Input

The user may specify:
- A PDF path (default: look for `YYYY-MM-daily.pdf` in vault root for current month)
- Specific dates to extract (default: all dated entries)

## Process

1. **Find the PDF**
   - If path provided, use it
   - Otherwise look for `{current-year}-{current-month}-daily.pdf` in vault root
   - Example: `2026-01-daily.pdf`

2. **Read and parse the PDF**
   - Read the PDF using the Read tool
   - Identify dated entries by looking for date patterns:
     - `M/DD/YY` (e.g., "1/10/26")
     - `YYYY-MM-DD` (e.g., "2026-01-25")
     - Day names with dates (e.g., "Sunday" near a date)
   - Look for hashtags on the date line (e.g., "1/20/26 #resin" or "1/20/26 #resin #chiro")
   - These become project tags on the interstitial

3. **Check for existing interstitials**
   - For each dated entry found, check if `50-log/interstitial/YYYY-MM-DD-*-*.md` exists with `source: remarkable`
   - If exists: skip (already extracted)
   - If not: include in extraction list

4. **For each NEW dated entry:**
   - Extract the date
   - Extract the content following that date until the next date or section break
   - Ask the user for a slug/title for that entry (or infer from content)
   - Create an interstitial note

5. **Create interstitial notes**

   Location: `50-log/interstitial/YYYY-MM-DD-HHMM-{slug}.md`

   Format:
   ```markdown
   ---
   tags: [interstitial, remarkable, {project-tags}]
   date: YYYY-MM-DD
   time: HH:MM
   source: remarkable
   ---

   {transcribed content}
   ```

   Project tags come from hashtags on the date line. If you write `1/20/26 #resin`, the interstitial gets `tags: [interstitial, remarkable, resin]`.

6. **Handle undated content**
   - Check if `YYYY-MM-remarkable.md` exists
   - If exists: ask user if they want to UPDATE it with new undated content
   - If not: create it with all undated content

7. **Report results**
   - List new interstitials created
   - List dates skipped (already extracted)
   - Note any entries that were unclear

## Example

User: `/remarkable`

Claude finds `2026-01-daily.pdf`, reads it, and identifies entries:

```
Found 3 dated entries in 2026-01-daily.pdf:

1. 1/10/26 - Content about single notebook approach
2. 1/20/26 #chiro - Content about Quick Assist, Hyzentra
3. 2026-01-25 #kairos - Discovery Engine TDD work

Create interstitial notes for these? [Y/n]
```

User confirms, Claude creates:
- `50-log/interstitial/2026-01-10-0900-single-notebook-approach.md` (tags: interstitial, remarkable)
- `50-log/interstitial/2026-01-20-0900-quick-assist-notes.md` (tags: interstitial, remarkable, chiro)
- `50-log/interstitial/2026-01-25-0900-discovery-engine-tdd.md` (tags: interstitial, remarkable, kairos)

## Notes

- Time defaults to 09:00 since Remarkable doesn't capture time
- User can override slug suggestions
- Entries without clear dates are flagged for manual review
- The `source: remarkable` frontmatter tag allows filtering/querying these notes later
- **Hashtag convention:** Write `#project` on the date line (e.g., "1/20/26 #resin") to auto-tag the interstitial
- Multiple tags work: "1/20/26 #resin #chiro" tags both projects
- If no hashtag, the entry gets just `[interstitial, remarkable]` tags
