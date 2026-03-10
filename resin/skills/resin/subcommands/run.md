# Subcommand: run <workflow> <tenant-env>

Run extraction only (no enrichment or sync).

## Arguments

- `workflow` - Spec folder name (e.g., `weekly-focus-queue`)
- `tenant-env` - Tenant and environment (e.g., `helpinghands-prod`)

## What It Does

Invokes the `/run-specs` command which:

1. Reads `mill/spec/{workflow}/manifest.json`
2. Spawns spec-executors for each spec (parallel)
3. Runs synthesis if all specs pass
4. Runs prioritization if synthesis passes
5. Writes outputs to `dat/{tenant}/raw/{workflow}/{run_id}/`

## Execution

Simply invoke the underlying command:

```
/run-specs {workflow} {tenant}-{env}
```

## Output

```
## Extraction Complete

**Workflow**: weekly-focus-queue
**Tenant**: helpinghands (prod)
**Run ID**: 2026-01-08-143052

### Specs
| Spec | Status |
|------|--------|
| 01-lapse-risk | ✅ Complete |
| 02-upgrade | ✅ Complete |
| 03-stewardship | ✅ Complete |
| 04-pipeline | ✅ Complete |
| 05-event | ✅ Complete |
| 06-recurring | ✅ Complete |

### Synthesis
✅ 99-queue-synthesis complete

### Prioritization
✅ 100-prioritization-senior complete
✅ 100-prioritization-manager complete
✅ 100-prioritization-frontline complete

### Output
dat/helpinghands/raw/weekly-focus-queue/2026-01-08-143052/

### Next Steps
To complete the pipeline:
- Run enrichment: ./scripts/devops/cli enrich helpinghands
- Run sync: ./scripts/devops/cli sync all helpinghands
- Or use: resin pipeline weekly-focus-queue helpinghands-prod
```

## When to Use

| Use Case | Command |
|----------|---------|
| Full pipeline (extraction + enrichment + sync) | `resin pipeline ...` |
| Extraction only (debugging, partial runs) | `resin run ...` |
| Re-run just enrichment | `./scripts/devops/cli enrich {tenant}` |
| Re-run just sync | `./scripts/devops/cli sync all {tenant}` |

## Available Workflows

Check `mill/workflows.yaml` or run `resin specs` for available workflows.
