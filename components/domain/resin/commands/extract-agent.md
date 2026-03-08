---
name: Extract Agent
allowed-tools: Task, Bash, Read, Glob, Write
description: Run extraction workflow using Claude Code subagents (free on Max, parallel, desktop/dev)
---

# Extract Agent

Runs a spec workflow using parallel Claude Code subagents. Free on Max plan. Best for desktop/dev use.

## Arguments

$ARGUMENTS - Two arguments: `<workflow> <tenant-env>`
- **workflow**: The spec folder name (e.g., "fundraising-intelligence", "99-dev-test")
- **tenant-env**: Tenant and environment in format `{tenant}-{env}` (e.g., "helpinghands-prod", "pow-local")

Example: `fundraising-intelligence pow-prod`

## Flow

```
/extract-agent fundraising-intelligence pow-prod
       |
1. Parse arguments, derive MCP endpoint and secrets path
       |
2. Get repo root, validate secrets file exists
       |
3. Read manifest.json to get expected specs
       |
4. Resolve org-context from tenants.json → ../resin-knowledge
       |
5. Generate sequential run ID (YYYY-MM-DD-NNN)
       |
6. Create output dir: dat/{tenant}/extraction/{workflow}/{RUN_ID}/
       |
7. Phase 1: Run all spec-executors in parallel (SINGLE message)
       |
8. Verify which output JSON files were created
       |
9. Gate check: respect manifest synthesis gating rules
       |
10. Phase 2: Run synthesis (if gate passed)
       |
11. Phase 3: Run prioritization (if synthesis passed and manifest has it)
       |
12. Write log.json with "engine": "agent"
       |
13. Report results with next-step suggestions
```

## Execution Steps

Parse the arguments to extract `workflow` and `tenant-env`, then:

**Parse tenant-env argument:**
- Split on the LAST hyphen: `helpinghands-prod` → tenant=`helpinghands`, env=`prod`
- Split on the LAST hyphen: `pow-local` → tenant=`pow`, env=`local`

**Expand env shorthand:**
- `prod` → `production`
- `dev` → `develop`
- `local` → `local`
- If already full name (`production`, `develop`), keep as-is

**Derive MCP endpoint:**
- For `production`: `https://{tenant}.joebouchard.workers.dev/mcp`
- For `develop`: `https://{tenant}-dev.joebouchard.workers.dev/mcp`
- For `local`: `http://localhost:8787/mcp`

### Step 1: Get Repo Root

**CRITICAL**: Always derive the absolute repo root path first.

```bash
git rev-parse --show-toplevel
```

Store as `REPO_ROOT`.

### Step 2: Validate Secrets

Check the secrets file exists:
```bash
ls {REPO_ROOT}/secrets/{tenant}/secrets.{envName}
```

Where `{envName}` is the expanded environment name (e.g., `production`, `develop`, `local`).

If the file doesn't exist, report an error and stop.

### Step 3: Read Manifest

Read `{REPO_ROOT}/mill/spec/{workflow}/manifest.json` and extract:
- `specs[]` - array of spec objects with `spec_file` field
- `synthesis` - synthesis configuration including gating rules

### Step 4: Resolve Org-Context

Read `{REPO_ROOT}/tenants.json` to find the tenant entry:
```json
{
  "tenants": {
    "pow": {
      "name": "Protect Our Winters",
      "org_context": "orgs/protect-our-winters/org-context.json"
    }
  }
}
```

Then resolve the org-context file:
1. Build path: `{REPO_ROOT}/../resin-knowledge/{org_context}`
2. Read and parse the JSON file
3. Store the parsed object and the org name

If the tenant isn't in tenants.json or the file doesn't exist, warn but continue without org-context.

### Step 5: Generate Sequential Run ID

Generate a run ID in format `YYYY-MM-DD-NNN`:

```bash
# Get today's date
TODAY=$(date +%Y-%m-%d)

# List existing run dirs for today
ls -d {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/${TODAY}-* 2>/dev/null | sort
```

- If no dirs exist for today, use `{TODAY}-001`
- Otherwise parse the max sequence number and increment: if max is `003`, next is `004`
- Pad to 3 digits

Store as `RUN_ID`.

### Step 6: Create Output Directory and Capture Start Time

```bash
mkdir -p {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{RUN_ID}
date -u +%Y-%m-%dT%H:%M:%SZ
```

Store the ISO timestamp as `started_at`.

### Step 7: Phase 1 - Run Spec Executors (Parallel)

For EACH spec in `manifest.specs[]`, spawn a `spec-executor` Task agent IN PARALLEL using a SINGLE message with multiple Task tool calls.

**CRITICAL**: Send ALL spec-executor tasks in a SINGLE message to run them in parallel.

**CRITICAL**: Use ABSOLUTE PATHS in all prompts.

Each prompt MUST include the org-context section (if available).

**Prompt template for each spec:**

```
Task(subagent_type="spec-executor", prompt="
Run spec: {REPO_ROOT}/mill/spec/{workflow}/{spec.spec_file}
Tenant: {tenant}
Environment: {envName}
Output to: {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{RUN_ID}

IMPORTANT: All paths above are ABSOLUTE. Write output files to the exact path specified.

MCP Authentication:
- Endpoint: {derived_endpoint}
- Read {REPO_ROOT}/secrets/{tenant}/secrets.{envName} to get the API_KEY value
- Use the API_KEY as Bearer authentication for all MCP calls

## Organization Context

You are analyzing data for {org_name}. Use the following org-specific definitions and thresholds instead of generic defaults.

```json
{org_context_json}
```

IMPORTANT: Use these org-specific tier definitions, dollar thresholds, staff assignments, fiscal year, and Salesforce field names when segmenting donors, writing SOQL queries, and generating output. Do not use generic thresholds.
")
```

If org-context was not resolved, omit the "Organization Context" section entirely.

### Step 8: Verify Outputs

After all spec-executors complete, check which output files exist:

```bash
ls {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{RUN_ID}/*.json 2>/dev/null
```

Build two lists:
- **specs_completed**: spec names whose JSON output files exist
- **specs_missing**: spec names whose JSON output files are missing

### Step 9: Gate Check (Flexible Synthesis Gating)

Read the manifest's synthesis configuration:
- `requires_all_specs` (boolean, default `true`)
- `minimum_specs_required` (number, default = total spec count)

Apply gating logic (matches TS worker `main.ts:448-454`):

```
IF requires_all_specs is true (or not set):
    gate_passed = (specs_missing is empty)
ELSE:
    gate_passed = (len(specs_completed) >= minimum_specs_required)
```

### Step 10: Phase 2 - Run Synthesis (if gate passed)

If gate check passed, spawn synthesis-executor with ABSOLUTE paths AND org-context:

```
Task(subagent_type="synthesis-executor", prompt="
Run spec: {REPO_ROOT}/mill/spec/{workflow}/{manifest.synthesis.spec_file}
Source folder: {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{RUN_ID}

IMPORTANT: All paths are ABSOLUTE - read from and write to the exact paths specified.

## Organization Context

You are analyzing data for {org_name}. Use the following org-specific definitions and thresholds instead of generic defaults.

```json
{org_context_json}
```

IMPORTANT: Use these org-specific tier definitions, dollar thresholds, staff assignments, fiscal year, and Salesforce field names when analyzing data and generating the synthesis report.
")
```

Set `synthesis_status`:
- `"complete"` if synthesis ran successfully
- `"skipped"` if gate check failed
- `"failed"` if synthesis encountered an error

### Step 11: Phase 3 - Run Prioritization (if synthesis passed)

If synthesis completed successfully AND `manifest.prioritization` exists, spawn prioritization agents for each worker type IN PARALLEL in a SINGLE message.

Read `manifest.prioritization.worker_types` array (e.g., `["senior", "manager", "frontline"]`).

```
Task(subagent_type="synthesis-executor", prompt="
Run spec: {REPO_ROOT}/mill/spec/{workflow}/100-prioritization.md
Worker type: {worker_type}
Source folder: {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{RUN_ID}
Input file: 99-synthesis.json

IMPORTANT: All paths are ABSOLUTE - read from and write to the exact paths specified.

Read the synthesis JSON and generate a role-specific action plan for a {WORKER_TYPE_UPPER} worker.
Output files: 100-prioritization-{worker_type}.md and 100-prioritization-{worker_type}.json

## Organization Context

You are analyzing data for {org_name}. Use the following org-specific definitions and thresholds.

```json
{org_context_json}
```
")
```

Set `prioritization_status`:
- `"complete"` if all worker types completed successfully
- `"skipped"` if synthesis failed or prioritization not in manifest
- `"partial"` if some worker types failed
- `"failed"` if all worker types failed

### Step 12: Write log.json

Capture completion time:
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
```

Calculate `duration_seconds` = completed_at - started_at.

Write `{REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{RUN_ID}/log.json`:

```json
{
  "run_id": "{RUN_ID}",
  "engine": "agent",
  "tenant": "{tenant}",
  "environment": "{envName}",
  "workflow": "{workflow}",
  "started_at": "{ISO timestamp}",
  "completed_at": "{ISO timestamp}",
  "duration_seconds": 0,
  "org_context_source": "{tenants.json org_context path or null}",
  "specs_expected": ["01-retention-metrics", "02-revenue-analysis"],
  "specs_completed": ["01-retention-metrics", "02-revenue-analysis"],
  "specs_missing": [],
  "gate_passed": true,
  "gate_rule": "minimum_specs_required: 6",
  "synthesis_status": "complete",
  "prioritization_status": "skipped",
  "prioritization_worker_types": [],
  "prioritization_completed": []
}
```

### Step 13: Report Results

**If all phases completed:**
```
Run complete!

Engine: agent (Claude Code subagents)
Run ID: {RUN_ID}
Tenant: {tenant} ({envName})
Output: dat/{tenant}/extraction/{workflow}/{RUN_ID}/

Specs: N/N completed
- [completed/missing status for each spec]

Synthesis: Complete / Skipped / Failed
Prioritization: Complete / Skipped / N/A

Next steps:
- Sync to R2: ./scripts/devops/cli sync all {tenant}
- Run with TS worker: /extract-worker {workflow} {tenant}-{env}
- View results: ls dat/{tenant}/extraction/{workflow}/{RUN_ID}/
```

**If gate check failed (synthesis skipped):**
```
Run incomplete - synthesis skipped

Specs: M/N completed (gate requires {gate_rule})
[list each spec with status]

Synthesis: Skipped ({reason})

To retry: /extract-agent {workflow} {tenant}-{env}
```

## Output Structure

```
dat/{tenant}/extraction/{workflow}/{RUN_ID}/
├── log.json                        <- Execution metadata
├── 01-spec-name.json
├── 01-spec-name.md
├── 02-spec-name.json
├── 02-spec-name.md
├── ...
├── 99-synthesis.json               <- If synthesis ran
├── 99-synthesis.md
├── 100-prioritization-senior.json  <- If prioritization ran
├── 100-prioritization-senior.md
└── ...
```

## Example Usage

```
# Run fundraising intelligence for Protect Our Winters (production)
/extract-agent fundraising-intelligence pow-prod

# Run dev test against local MCP
/extract-agent 99-dev-test helpinghands-local

# Run against develop environment
/extract-agent fundraising-intelligence helpinghands-dev
```
