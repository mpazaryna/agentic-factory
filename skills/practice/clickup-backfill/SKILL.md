---
name: clickup-backfill
description: "Ensure every .orchestra/work/ item has a corresponding ClickUp ticket. Creates missing tickets and writes the ID back into the PRD frontmatter. Use when backfilling a repo's work items into ClickUp."
allowed-tools: Read, Glob, Edit, Bash
argument-hint: "<repo-name (optional — defaults to current repo)>"
disable-model-invocation: false
---

# ClickUp Backfill

Scan all work items in `.orchestra/work/` and ensure each has a corresponding ClickUp ticket. Create missing tickets and write the ID back into the PRD frontmatter. Do not modify ticket status.

## Step 1 — Resolve Credentials

Read the ClickUp API key:

```bash
grep 'api_key:' ~/.config/workspace/bench/config.yaml | awk '{print $2}'
```

If not found, check `CLICKUP_API_KEY` env var. If neither exists, stop and tell the user.

## Step 2 — Resolve List ID

Find the `clickupListId` for this repo:

1. Determine the repo name — use `$ARGUMENTS` if provided, otherwise infer from the current directory name
2. Read `config/projects/<repo-name>.json` (relative to BENCH_ROOT, typically `../..` from `apps/web/` or the monorepo root)
3. Extract `clickupListId` from the JSON

If no `clickupListId` is configured for this repo, stop and tell the user which field to add to `config/projects/<repo-name>.json`.

## Step 3 — Scan Work Items

Use Glob to find all work item folders:

```
.orchestra/work/*/
```

Skip `TEMPLATES` and any folder starting with `.`.

For each folder, find the primary document in this order: `prd.md`, `spec.md`, `README.md`, first `.md` file found.

Read the frontmatter of the primary document and extract:
- `ticket` — existing ClickUp ID (if present, skip this item)
- `title` — work item title (or extract from the first `# Heading` in the file)
- `status` — current status

## Step 4 — Identify Missing Tickets

Build two lists:
- **Already linked**: work items with a `ticket` field in frontmatter
- **Missing**: work items with no `ticket` field, or where the ticket field is empty

Report the count of each before proceeding.

## Step 5 — Create Missing Tickets

For each work item in the Missing list:

1. Extract the title and a short description (first non-heading paragraph of the PRD, or the Objective section if present)
2. Create a ClickUp task:

```bash
curl -s -X POST "https://api.clickup.com/api/v2/list/<LIST_ID>/task" \
  -H "Authorization: <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "<title>",
    "description": "<description>"
  }'
```

3. Extract the `id` field from the response
4. Write the ticket ID back into the primary document's frontmatter:
   - If frontmatter exists: add or update the `ticket:` line
   - If no frontmatter: prepend a frontmatter block with `ticket`, `status`, and `created_on`

## Step 6 — Report

Print a summary table:

| Work Item | Action | Ticket ID |
|-----------|--------|-----------|
| folder-name | already linked | 86eXXXXXX |
| folder-name | created | 86eYYYYYY |
| folder-name | created | 86eZZZZZZ |

State how many tickets were created and how many were already linked. Do not modify ClickUp status.
