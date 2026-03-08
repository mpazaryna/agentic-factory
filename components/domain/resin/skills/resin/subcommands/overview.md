# Subcommand: Overview (no args)

Show platform overview with workflows and recent runs.

## Steps

1. Read `mill/workflows.yaml` for workflow registry
2. Scan `dat/helpinghands/raw/*/` for recent runs (last 5)
3. Format output

## Output Format

```
# Resin Platform

## Workflows

| Workflow | Description | Trigger |
|----------|-------------|---------|
| weekly-focus-queue | Extract and prioritize donors | resin run weekly-focus-queue {t}-{e} |
| annual-intelligence | Annual program assessment | resin run annual-intelligence {t}-{e} |
| enrichment | Enrich raw data | ./scripts/devops/cli enrich {t} |
| email-generation | Generate donor emails | cd workers/email && npx tsx scripts/run-local.ts |

## Recent Runs (helpinghands)

| Run ID | Workflow | Status | Duration |
|--------|----------|--------|----------|
| 2026-01-06-143052 | weekly-focus-queue | complete | 2m 34s |
| 2026-01-05-091522 | annual-intelligence | complete | 4m 12s |

## Quick Actions

- "resin status" - Detailed run history
- "resin specs" - List spec folders
- "resin pipeline weekly-focus-queue helpinghands-prod" - Run full pipeline
```

## Reading Workflows

```bash
cat mill/workflows.yaml
```

Parse the `workflows:` section and format as table.

## Scanning Recent Runs

```bash
# Find log.json files
find dat/helpinghands/raw -name "log.json" -type f 2>/dev/null | head -10
```

Or use Glob: `dat/helpinghands/raw/*/*/log.json`

Read each log.json, sort by `started_at` descending, show last 5.
