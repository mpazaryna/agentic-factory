# Example: Discovery Commands

## Platform Overview

**Command:**
```
resin
```

**Output:**
```
# Resin Platform

## Workflows

| Workflow | Description | Trigger |
|----------|-------------|---------|
| weekly-focus-queue | Extract and prioritize donors | resin run weekly-focus-queue {t}-{e} |
| annual-intelligence | Annual program assessment | resin run annual-intelligence {t}-{e} |
| enrichment | Enrich raw data | ./scripts/devops/cli enrich {t} |
| email-generation | Generate donor emails | cd workers/email && npx tsx scripts/run-local.ts |
| sync | Upload to R2 | ./scripts/devops/cli sync all {t} |

## Recent Runs (helpinghands)

| Run ID | Workflow | Status | Duration |
|--------|----------|--------|----------|
| 2026-01-08-143052 | weekly-focus-queue | complete | 2m 34s |
| 2026-01-07-091522 | annual-intelligence | complete | 4m 12s |
| 2026-01-06-103045 | 99-dev-test | complete | 45s |

## Quick Actions

- "resin status" - Detailed run history
- "resin specs" - List spec folders
- "resin pipeline weekly-focus-queue helpinghands-prod" - Run full pipeline
```

---

## Run Status

**Command:**
```
resin status helpinghands
```

**Output:**
```
# Run History: helpinghands

## Recent Runs

### 2026-01-08-143052 - weekly-focus-queue
- **Status**: complete
- **Duration**: 2m 34s
- **Specs**: 6/6 complete
- **Synthesis**: complete
- **Prioritization**: 3/3 complete (senior, manager, frontline)
- **Cost**: $0.63
- **Output**: dat/helpinghands/raw/weekly-focus-queue/2026-01-08-143052/

### 2026-01-07-091522 - annual-intelligence
- **Status**: partial (5/8 specs)
- **Duration**: 4m 12s
- **Missing**: 06-capacity-analysis, 07-board-participation, 08-institutional
- **Cost**: $0.89
- **Output**: dat/helpinghands/raw/annual-intelligence/2026-01-07-091522/

### 2026-01-06-103045 - 99-dev-test
- **Status**: complete
- **Duration**: 45s
- **Specs**: 4/4 complete
- **Cost**: $0.12
- **Output**: dat/helpinghands/raw/99-dev-test/2026-01-06-103045/
```

---

## List Specs

**Command:**
```
resin specs
```

**Output:**
```
# Spec Folders

| Folder | Specs | Synthesis | Description |
|--------|-------|-----------|-------------|
| weekly-focus-queue | 6 + 2 | 99-queue-synthesis.md | Weekly donor extraction |
| annual-intelligence | 8 + 1 | 99-synthesis.md | Annual program assessment |
| 99-dev-test | 4 + 2 | 99-synthesis.md | Development testing |

## Spec Details

### weekly-focus-queue
- 01-lapse-risk-candidates - Donors in 11-14 month lapse risk window
- 02-major-donor-recovery - Lapsed major donors with engagement signals
- 03-new-donor-stewardship - First-time donors in 30-day window
- 04-upgrade-opportunities - Donors showing upgrade trajectory
- 05-pipeline-progression - Stalled opportunities
- 06-event-followup - Recent event attendees
- 99-queue-synthesis - Score and filter candidates
- 100-prioritization - Generate role-specific plans

### 99-dev-test
- 01-donor-counts - Basic donor metrics
- 02-giving-summary - Giving totals by fiscal year
- 03-top-donors - Top donors by lifetime value
- 04-recent-gifts - Recent gift activity
- 99-synthesis - Combine test outputs
- 100-prioritization - Test prioritization
```
