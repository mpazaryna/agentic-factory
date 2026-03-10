---
name: resin
description: Platform orchestrator - discover workflows, check status, run pipelines
---

# Resin Platform Orchestrator

Central skill for the Resin platform. Discover workflows, check run status, and execute pipelines.

## Arguments

Parse `$ARGUMENTS` to determine the subcommand:

| Pattern | Action | Details |
|---------|--------|---------|
| (empty) | Show overview | [subcommands/overview.md](subcommands/overview.md) |
| `status [tenant]` | Show run history | [subcommands/status.md](subcommands/status.md) |
| `specs` | List spec folders | [subcommands/specs.md](subcommands/specs.md) |
| `pipeline <workflow> <tenant-env>` | Run full pipeline | [subcommands/pipeline.md](subcommands/pipeline.md) |
| `run <workflow> <tenant-env>` | Run extraction only | [subcommands/run.md](subcommands/run.md) |

Default tenant: `helpinghands`

## Quick Reference

### Discovery (read-only)

```
resin                     → Platform overview + recent runs
resin status              → Run history for default tenant
resin status helpinghands → Run history for specific tenant
resin specs               → List all spec folders with manifests
```

### Execution

```
resin pipeline weekly-focus-queue helpinghands-prod  → Full pipeline (extraction + enrichment + sync)
resin run weekly-focus-queue helpinghands-prod       → Extraction only
resin run 99-dev-test helpinghands-local             → Dev testing (requires local MCP)
```

## Key Files

| File | Purpose |
|------|---------|
| `mill/workflows.yaml` | Workflow registry (source of truth) |
| `mill/spec/*/manifest.json` | Spec folder manifests |
| `dat/{tenant}/raw/*/log.json` | Run metadata for status |
| `config/secrets/{tenant}/secrets.{env}` | Tenant credentials |

## Execution Strategy

New specs are developed in Claude Code, then graduate to Cloudflare Workers:

| Phase | Method | Cost |
|-------|--------|------|
| Development | This skill + `/run-specs` | $0 (Max sub) |
| Production | `workers/extraction/` → Cloudflare | $1-2/run |

See [diagrams/execution-flow.md](diagrams/execution-flow.md) for the full pipeline flow.

## Examples

- [examples/weekly-helpinghands.md](examples/weekly-helpinghands.md) - Full pipeline run
- [examples/discovery.md](examples/discovery.md) - Discovery commands

## Related

- `.claude/commands/run-specs.md` - Underlying extraction command
- `docs/guides/pipeline-execution.md` - Detailed pipeline documentation
- `docs/roadmap/resin-orchestrator.md` - Roadmap and strategy
