# Subcommand: status [tenant]

Show detailed run history for a tenant.

## Arguments

- `tenant` - Optional, defaults to `helpinghands`

## Steps

1. Parse tenant from args (default: `helpinghands`)
2. Glob `dat/{tenant}/raw/*/*/log.json`
3. Read each log.json and sort by `started_at` descending
4. Show last 10 runs with details

## Output Format

```
# Run History: helpinghands

## Recent Runs

### 2026-01-06-143052 - weekly-focus-queue
- **Status**: complete
- **Duration**: 2m 34s
- **Specs**: 6/6 complete
- **Synthesis**: complete
- **Output**: dat/helpinghands/raw/weekly-focus-queue/2026-01-06-143052/

### 2026-01-05-091522 - annual-intelligence
- **Status**: partial (5/8 specs)
- **Duration**: 4m 12s
- **Missing**: 06-capacity-analysis, 07-board-participation
- **Output**: dat/helpinghands/raw/annual-intelligence/2026-01-05-091522/
```

## log.json Structure

Each run produces a `log.json` with:

```json
{
  "run_id": "2026-01-06-143052",
  "tenant": "helpinghands",
  "spec_folder": "weekly-focus-queue",
  "started_at": "2026-01-06T14:30:52Z",
  "completed_at": "2026-01-06T14:33:26Z",
  "duration_ms": 154000,
  "specs_expected": ["01-lapse-risk", "02-upgrade", ...],
  "specs_completed": ["01-lapse-risk", "02-upgrade", ...],
  "specs_missing": [],
  "gate_passed": true,
  "synthesis_status": "complete",
  "prioritization_status": "complete",
  "token_usage": {
    "input_tokens": 85000,
    "output_tokens": 25000,
    "api_calls": 10
  },
  "cost": {
    "estimated_cost_usd": 0.63
  }
}
```

## Key Fields

| Field | Description |
|-------|-------------|
| `gate_passed` | All required specs completed |
| `synthesis_status` | complete, skipped, or failed |
| `specs_missing` | Array of failed/missing spec names |
| `cost.estimated_cost_usd` | API cost for the run |
