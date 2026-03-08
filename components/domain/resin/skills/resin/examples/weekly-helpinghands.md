# Example: Weekly HelpingHands Pipeline

## Command

```
resin pipeline weekly-focus-queue helpinghands-prod
```

## What Happens

### 1. Argument Parsing

```
workflow = weekly-focus-queue
tenant = helpinghands
env = prod
```

### 2. Prerequisites Check

- ✅ `mill/spec/weekly-focus-queue/manifest.json` exists
- ✅ `config/secrets/helpinghands/secrets.production` exists
- ✅ MCP endpoint `https://helpinghands.joebouchard.workers.dev/mcp` responds

### 3. Extraction Stage

Runs `/run-specs weekly-focus-queue helpinghands-prod`

**Output:**
```
dat/helpinghands/raw/weekly-focus-queue/2026-01-08-143052/
├── 01-lapse-risk-candidates.json
├── 01-lapse-risk-candidates.md
├── 02-upgrade-candidates.json
├── 02-upgrade-candidates.md
├── 03-new-donor-retention.json
├── 03-new-donor-retention.md
├── 04-major-gift-pipeline.json
├── 04-major-gift-pipeline.md
├── 05-recurring-health.json
├── 05-recurring-health.md
├── 06-event-engagement.json
├── 06-event-engagement.md
├── 99-queue-synthesis.json
├── 99-queue-synthesis.md
├── 100-prioritization-senior.json
├── 100-prioritization-manager.json
├── 100-prioritization-frontline.json
└── log.json
```

### 4. Enrichment Stage

Runs `./scripts/devops/cli enrich helpinghands`

**Output:**
```
dat/helpinghands/enriched/
├── dashboard-data.json
├── focus-queue.json
└── staff/
    ├── sarah-johnson.json
    ├── jennifer-martinez.json
    └── michael-chen.json
```

### 5. Sync Stage

Runs `./scripts/devops/cli sync all helpinghands`

**Uploads to R2:**
- `dashboard-data.json` → `helpinghands-data` bucket
- `focus-queue.json` → `helpinghands-data` bucket

### 6. Success Report

```
## Pipeline Complete

**Workflow**: weekly-focus-queue
**Tenant**: helpinghands (prod)
**Run ID**: 2026-01-08-143052

### Stages
| Stage | Status | Duration |
|-------|--------|----------|
| Extraction | ✅ Complete | 2m 45s |
| Enrichment | ✅ Complete | 38s |
| Sync | ✅ Complete | 12s |

**Total Duration**: 3m 35s

### Outputs
- **Extraction**: dat/helpinghands/raw/weekly-focus-queue/2026-01-08-143052/
- **Enriched**: dat/helpinghands/enriched/
- **Dashboard**: R2 synced

### Metrics
- Specs executed: 6/6
- Donors in focus queue: 47
- Prioritization plans: 3 (senior, manager, frontline)

### Next Steps
1. Review focus queue in dashboard
2. Check prioritization plans by role
3. Generate emails using workers/email/
```

## Alternative: Local Development

```
resin pipeline 99-dev-test helpinghands-local
```

**Prerequisites:**
- Start local MCP server: `cd workers/mcp/resin && npm run dev`
- Uses `config/secrets/helpinghands/secrets.local`

## Alternative: Extraction Only

```
resin run weekly-focus-queue helpinghands-prod
```

Runs extraction without enrichment or sync. Useful for debugging or partial runs.
