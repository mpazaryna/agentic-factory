# Subcommand: specs

List all spec folders with manifest information.

## Steps

1. Glob `mill/spec/*/manifest.json`
2. Read each manifest
3. Format with spec counts and descriptions

## Output Format

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

## manifest.json Structure

```json
{
  "name": "Weekly Focus Queue",
  "folder": "weekly-focus-queue",
  "description": "Extract and prioritize donors for weekly outreach",
  "specs": [
    { "spec_file": "01-lapse-risk.md" },
    { "spec_file": "02-upgrade.md" }
  ],
  "synthesis": {
    "spec_file": "99-synthesis.md",
    "requires_all_specs": true
  },
  "prioritization": {
    "spec_file": "100-prioritization.md",
    "worker_types": ["senior", "manager", "frontline"]
  }
}
```
