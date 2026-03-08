# Resin Skill

Central orchestrator for the Resin platform. Discover workflows, check status, and run pipelines.

## What It Does

The resin skill is your single entry point for platform operations:

- **Discovery**: See what workflows exist, check recent runs, list specs
- **Execution**: Run extraction pipelines, trigger enrichment and sync

## Quick Start

### In Claude Code

Ask Claude using natural language:

```
"show resin overview"
"show resin status for helpinghands"
"list resin specs"
"run resin pipeline weekly-focus-queue helpinghands-prod"
```

### Commands

| Command | Description |
|---------|-------------|
| `resin` | Platform overview with recent runs |
| `resin status [tenant]` | Detailed run history |
| `resin specs` | List all spec folders |
| `resin pipeline <workflow> <tenant-env>` | Full pipeline (extraction + enrichment + sync) |
| `resin run <workflow> <tenant-env>` | Extraction only |

## Pipeline Stages

When you run `resin pipeline`, three stages execute in sequence:

```
Salesforce → Extraction → Enrichment → R2 Sync → Dashboard
```

| Stage | What Happens |
|-------|--------------|
| **Extraction** | Queries Salesforce via MCP, runs specs, generates synthesis |
| **Enrichment** | Adds personas, templates, organizational context |
| **Sync** | Uploads to Cloudflare R2 for dashboard access |

## Available Workflows

| Workflow | Purpose | When to Run |
|----------|---------|-------------|
| `weekly-focus-queue` | Weekly donor outreach priorities | Every Monday |
| `annual-intelligence` | Full program health assessment | Quarterly |
| `99-dev-test` | Development testing | As needed |

## Requirements

- **MCP Access**: Tenant must have Salesforce configured via MCP
- **Secrets**: `config/secrets/{tenant}/secrets.{env}` must exist
- **For local dev**: MCP server must be running (`cd workers/mcp/resin && npm run dev`)

## Execution Strategy

```
Development:  Claude Code CLI (this skill)     → $0 with Max subscription
Production:   Cloudflare Workers (workers/extraction/)  → $1-2 per run
```

New specs are developed interactively using this skill, then graduate to autonomous Cloudflare Worker execution.

## Troubleshooting

### "Workflow not found"
Check that `mill/spec/{workflow}/manifest.json` exists.

### "Tenant not configured"
Check that `config/secrets/{tenant}/secrets.{env}` exists.

### "MCP health check failed"
For local: `cd workers/mcp/resin && npm run dev`
For production: `curl https://{tenant}.joebouchard.workers.dev/mcp/health`

## For Developers

See the subcommands folder for implementation details:
- `subcommands/overview.md` - How to build the overview
- `subcommands/status.md` - How to scan run history
- `subcommands/specs.md` - How to list specs
- `subcommands/pipeline.md` - Full pipeline execution
- `subcommands/run.md` - Extraction-only runs

## Related

- [Pipeline Execution Guide](../../../docs/guides/pipeline-execution.md)
- [Resin Orchestrator Roadmap](../../../docs/roadmap/resin-orchestrator.md)
- [ADR-019: Execution Nomenclature](../../../docs/adr/ADR-019-execution-nomenclature-reset.md)
