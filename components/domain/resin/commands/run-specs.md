---
name: Run Specs
allowed-tools: Task, Bash, Read, Glob, Write
description: Run all specs in a folder using spec-executor and synthesis-executor subprocesses
---

# Run Specs

Orchestrates spec execution based on the manifest, with synthesis gating and execution logging.

## Arguments

$ARGUMENTS - Two arguments: `<folder> <tenant-env>`
- **folder**: The spec folder name (e.g., "99-dev-test")
- **tenant-env**: Tenant and environment in format `{tenant}-{env}` (e.g., "helpinghands-prod", "resin-prod")

Example: `99-dev-test helpinghands-prod`

## Flow

```
/run-specs 99-dev-test helpinghands-prod
       ↓
1. Read manifest.json to get expected specs
       ↓
2. Generate timestamped run folder + capture started_at
       ↓
3. Phase 1: Run all spec-executors in parallel
       ↓
4. Verify outputs: Check which files were created
       ↓
5. Gate check: ALL specs completed?
       ↓
6. Phase 2: Run synthesis (only if ALL specs passed)
       ↓
7. Phase 3: Run prioritization for each worker_type (only if synthesis passed)
       ↓
8. Write log.json (execution log)
       ↓
9. Report results
```

## Execution Steps

Parse the arguments to extract `folder` and `tenant-env`, then:

**Parse tenant-env argument:**
- Split on the last hyphen: `helpinghands-prod` → tenant=`helpinghands`, env=`production`
- Split on the last hyphen: `helpinghands-dev` → tenant=`helpinghands`, env=`develop`
- Split on the last hyphen: `helpinghands-local` → tenant=`helpinghands`, env=`local`

**Derive MCP endpoint:**
- For production: `https://{tenant}-prod.joebouchard.workers.dev/mcp`
- For develop: `https://{tenant}-dev.joebouchard.workers.dev/mcp`
- For local: `http://localhost:8787/mcp`

### Step 1: Read Manifest

Read `mill/spec/{folder}/manifest.json` and extract:
- `specs[]` - array of spec objects with `spec_file` field
- `synthesis.spec_file` - the synthesis spec filename

### Step 2: Get Repo Root, Generate Run ID, and Capture Start Time

**CRITICAL**: Always derive the absolute repo root path first. This ensures all agents write to the correct location regardless of their working directory.

```bash
# Get absolute repo root (run this FIRST)
git rev-parse --show-toplevel

# Get RUN_ID
date +%Y-%m-%d-%H%M%S

# Get started_at (ISO format, UTC)
date -u +%Y-%m-%dT%H:%M:%SZ
```

Result:
- `REPO_ROOT = /Users/mpaz/workspace/joe/resin-platform` (or wherever the repo is cloned)
- `RUN_ID = 2025-12-08-143052`
- `started_at = 2025-12-08T14:30:52Z`

Output folder: `{REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/`

**IMPORTANT**:
- Use Bash `date` command to get real timestamps. Do not estimate or generate timestamps without running the command.
- Always use REPO_ROOT as an absolute path prefix in all agent prompts to prevent path confusion.

### Step 3: Validate Tenant and Create Output Directory

Validate the tenant exists by checking for the secrets file:
```bash
ls {REPO_ROOT}/config/secrets/{tenant}/secrets.{env}
```

If the file doesn't exist, report an error and stop.

Then create the output directory using the absolute path:
```bash
mkdir -p {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}
```

### Step 4: Phase 1 - Run Analysis Specs (Parallel)

For EACH spec in `manifest.specs[]`, spawn a spec-executor agent IN PARALLEL using a SINGLE message with multiple Task tool calls.

**CRITICAL**: Send ALL spec-executor tasks in a SINGLE message to run them in parallel.

**CRITICAL**: Use ABSOLUTE PATHS in all prompts. This prevents agents from writing to wrong directories.

Each prompt MUST include:
1. The absolute REPO_ROOT path
2. Explicit instructions for finding the API token

```
Task(subagent_type="spec-executor", prompt="
Run spec: {REPO_ROOT}/mill/spec/{folder}/{spec.spec_file}
Tenant: {tenant}
Environment: {env}
Output to: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}

IMPORTANT: All paths above are ABSOLUTE. Write output files to the exact path specified.

MCP Authentication:
- Endpoint: {derived_endpoint} (production=https://{tenant}-prod.joebouchard.workers.dev/mcp, develop=https://{tenant}-dev.joebouchard.workers.dev/mcp, local=http://localhost:8787/mcp)
- Read {REPO_ROOT}/config/secrets/{tenant}/secrets.{env} to get the API_KEY value
- Use the API_KEY as Bearer authentication for all MCP calls
")
```

Example for helpinghands-local running 99-dev-test with 4 specs (REPO_ROOT=/Users/mpaz/workspace/joe/resin-platform) - send ONE message with FOUR Task calls:
```
Task(subagent_type="spec-executor", prompt="Run spec: /Users/mpaz/workspace/joe/resin-platform/mill/spec/99-dev-test/01-donor-counts.md. Tenant: helpinghands. Environment: local. Output to: /Users/mpaz/workspace/joe/resin-platform/dat/helpinghands/raw/99-dev-test/2025-12-08-143052. IMPORTANT: Output path is ABSOLUTE - write files there exactly. MCP: endpoint=http://localhost:8787/mcp, API_KEY from /Users/mpaz/workspace/joe/resin-platform/config/secrets/helpinghands/secrets.local")
Task(subagent_type="spec-executor", prompt="Run spec: /Users/mpaz/workspace/joe/resin-platform/mill/spec/99-dev-test/02-gift-summary.md. Tenant: helpinghands. Environment: local. Output to: /Users/mpaz/workspace/joe/resin-platform/dat/helpinghands/raw/99-dev-test/2025-12-08-143052. IMPORTANT: Output path is ABSOLUTE - write files there exactly. MCP: endpoint=http://localhost:8787/mcp, API_KEY from /Users/mpaz/workspace/joe/resin-platform/config/secrets/helpinghands/secrets.local")
Task(subagent_type="spec-executor", prompt="Run spec: /Users/mpaz/workspace/joe/resin-platform/mill/spec/99-dev-test/03-recurring-donors.md. Tenant: helpinghands. Environment: local. Output to: /Users/mpaz/workspace/joe/resin-platform/dat/helpinghands/raw/99-dev-test/2025-12-08-143052. IMPORTANT: Output path is ABSOLUTE - write files there exactly. MCP: endpoint=http://localhost:8787/mcp, API_KEY from /Users/mpaz/workspace/joe/resin-platform/config/secrets/helpinghands/secrets.local")
Task(subagent_type="spec-executor", prompt="Run spec: /Users/mpaz/workspace/joe/resin-platform/mill/spec/99-dev-test/04-revenue-by-quarter.md. Tenant: helpinghands. Environment: local. Output to: /Users/mpaz/workspace/joe/resin-platform/dat/helpinghands/raw/99-dev-test/2025-12-08-143052. IMPORTANT: Output path is ABSOLUTE - write files there exactly. MCP: endpoint=http://localhost:8787/mcp, API_KEY from /Users/mpaz/workspace/joe/resin-platform/config/secrets/helpinghands/secrets.local")
```

### Step 5: Verify Outputs

After all spec-executors complete, check which output files exist:

```bash
ls {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/*.json 2>/dev/null | grep -v log.json
```

Build two lists:
- **specs_completed**: spec names whose JSON output files exist (e.g., ["01-donor-counts", "02-gift-summary"])
- **specs_missing**: spec names whose JSON output files are missing

### Step 6: Gate Check

**ALL specs must complete for synthesis to run.** No partial synthesis is allowed.

```
IF specs_missing is empty:
    gate_passed = true → Proceed to synthesis
ELSE:
    gate_passed = false → Report failure, list missing specs, SKIP synthesis
```

### Step 7: Phase 2 - Run Synthesis (if gate passed)

If gate check passed, spawn synthesis-executor with ABSOLUTE paths:

```
Task(subagent_type="synthesis-executor", prompt="Run spec: {REPO_ROOT}/mill/spec/{folder}/99-synthesis.md. Source folder: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}. IMPORTANT: All paths are ABSOLUTE - read from and write to the exact paths specified.")
```

Set `synthesis_status`:
- `"complete"` if synthesis ran successfully
- `"skipped"` if gate check failed
- `"failed"` if synthesis encountered an error

### Step 8: Phase 3 - Run Prioritization (if synthesis passed)

If synthesis completed successfully, check if `manifest.prioritization` exists. If it does, spawn prioritization agents for each worker type IN PARALLEL.

Read `manifest.prioritization.worker_types` array (e.g., `["senior", "manager", "frontline"]`).

**CRITICAL**: Send ALL prioritization tasks in a SINGLE message to run them in parallel.

**CRITICAL**: Use ABSOLUTE PATHS in all prompts.

```
Task(subagent_type="synthesis-executor", prompt="
Run spec: {REPO_ROOT}/mill/spec/{folder}/100-prioritization.md
Worker type: senior
Source folder: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}
Input file: 99-synthesis.json

IMPORTANT: All paths are ABSOLUTE - read from and write to the exact paths specified.

Read the synthesis JSON and generate a role-specific action plan for a SENIOR worker (Development Director / CDO).
Focus on: Strategic decisions, board communication, resource allocation, 12-24 month horizon.
Output files: 100-prioritization-senior.md and 100-prioritization-senior.json
")

Task(subagent_type="synthesis-executor", prompt="
Run spec: {REPO_ROOT}/mill/spec/{folder}/100-prioritization.md
Worker type: manager
Source folder: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}
Input file: 99-synthesis.json

IMPORTANT: All paths are ABSOLUTE - read from and write to the exact paths specified.

Read the synthesis JSON and generate a role-specific action plan for a MANAGER worker (Development Manager / Major Gifts Officer).
Focus on: Campaign execution, team coordination, donor portfolio management, 3-12 month horizon.
Output files: 100-prioritization-manager.md and 100-prioritization-manager.json
")

Task(subagent_type="synthesis-executor", prompt="
Run spec: {REPO_ROOT}/mill/spec/{folder}/100-prioritization.md
Worker type: frontline
Source folder: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}
Input file: 99-synthesis.json

IMPORTANT: All paths are ABSOLUTE - read from and write to the exact paths specified.

Read the synthesis JSON and generate a role-specific action plan for a FRONTLINE worker (Development Associate / Gift Officer).
Focus on: Daily donor interactions, task completion, data entry, 1-4 week horizon.
Output files: 100-prioritization-frontline.md and 100-prioritization-frontline.json
")
```

Set `prioritization_status`:
- `"complete"` if all worker types completed successfully
- `"skipped"` if synthesis failed or prioritization not in manifest
- `"partial"` if some worker types failed
- `"failed"` if all worker types failed

Track `prioritization_completed` array with worker types that succeeded.

### Step 9: Write log.json

**Capture `completed_at`** using Bash:
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
```

Calculate `duration_seconds` = completed_at - started_at (in seconds).

**IMPORTANT**: Use Bash `date` command to get the actual completion time. Do not hallucinate timestamps.

Write `log.json` to the output folder using the Write tool:

**File**: `{REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/log.json`

**Content**:
```json
{
  "run_id": "{RUN_ID}",
  "tenant": "{tenant}",
  "environment": "{env}",
  "folder": "{folder}",
  "started_at": "{ISO timestamp}",
  "completed_at": "{ISO timestamp}",
  "duration_seconds": {number},
  "specs_expected": ["01-donor-counts", "02-gift-summary", "03-recurring-donors", "04-revenue-by-quarter"],
  "specs_completed": ["01-donor-counts", "02-gift-summary", "03-recurring-donors", "04-revenue-by-quarter"],
  "specs_missing": [],
  "gate_passed": true,
  "synthesis_status": "complete",
  "prioritization_status": "complete",
  "prioritization_worker_types": ["senior", "manager", "frontline"],
  "prioritization_completed": ["senior", "manager", "frontline"]
}
```

### Step 9: Report Results

**If all phases completed:**
```
✅ Analysis complete!

Run ID: {RUN_ID}
Tenant: {tenant}
Output: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/

Specs: 4/4 completed
- ✅ 01-donor-counts
- ✅ 02-gift-summary
- ✅ 03-recurring-donors
- ✅ 04-revenue-by-quarter

Synthesis: ✅ Complete
Executive summary: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/99-synthesis.md

Prioritization: ✅ Complete (3 worker types)
- ✅ senior: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/100-prioritization-senior.md
- ✅ manager: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/100-prioritization-manager.md
- ✅ frontline: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/100-prioritization-frontline.md

Run log: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/log.json
```

**If specs failed (synthesis & prioritization skipped):**
```
❌ Analysis incomplete - synthesis skipped

Run ID: {RUN_ID}
Tenant: {tenant}
Output: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/

Specs: 3/4 completed
- ✅ 01-donor-counts
- ❌ 02-gift-summary (missing)
- ✅ 03-recurring-donors
- ✅ 04-revenue-by-quarter

Synthesis: ⏭️ Skipped (requires all specs)
Prioritization: ⏭️ Skipped (requires synthesis)

Run log: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/log.json

To retry, re-run /run-specs {folder} {tenant}-{env}
```

**If synthesis passed but prioritization failed:**
```
⚠️ Analysis partially complete

Run ID: {RUN_ID}
Tenant: {tenant}
Output: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/

Specs: 4/4 completed
Synthesis: ✅ Complete

Prioritization: ⚠️ Partial (1/3 worker types)
- ✅ senior
- ❌ manager (failed)
- ❌ frontline (failed)

Run log: {REPO_ROOT}/dat/{tenant}/raw/{folder}/{RUN_ID}/log.json
```

## Output Structure

After execution, the output folder contains:

```
dat/helpinghands/raw/99-dev-test/2025-12-08-143052/
├── log.json                        ← Execution metadata (includes cost tracking)
├── 01-donor-counts.json
├── 01-donor-counts.md
├── 02-gift-summary.json
├── 02-gift-summary.md
├── 03-recurring-donors.json
├── 03-recurring-donors.md
├── 04-revenue-by-quarter.json
├── 04-revenue-by-quarter.md
├── 99-synthesis.json
├── 99-synthesis.md
├── 100-prioritization-senior.json   ← Role-specific action plans
├── 100-prioritization-senior.md
├── 100-prioritization-manager.json
├── 100-prioritization-manager.md
├── 100-prioritization-frontline.json
└── 100-prioritization-frontline.md
```

Output is organized by tenant at the top level: `dat/{tenant}/raw/{folder}/{RUN_ID}/`

## Example Usage

```
# Run specs against local MCP server (requires npm run dev in workers/mcp/resin)
/run-specs 99-dev-test helpinghands-local

# Run specs against helpinghands develop environment
/run-specs 99-dev-test helpinghands-develop

# Run specs against helpinghands production
/run-specs 99-dev-test helpinghands-production
```

## Available Tenants

Tenants are auto-discovered from `config/secrets/` folder structure.

To list available tenants:
```bash
ls config/secrets/*/secrets.* | sed 's|config/secrets/||;s|/secrets\.| |' | grep -v template
```

Current tenants:
- `helpinghands-production` - Helping Hands production
- `helpinghands-develop` - Helping Hands dev/sandbox
- `helpinghands-local` - Helping Hands local development (requires MCP server running)
- `resin-production` - Resin dev server (Joe's sandbox)
- `resin-develop` - Resin dev environment

## MCP Authentication

**Single source of truth: Deployment secrets**

Everything is derived from the `{tenant}-{env}` argument:
1. Parse argument: `helpinghands-local` → tenant=`helpinghands`, env=`local`
2. Derive endpoint: `http://localhost:8787/mcp`
3. Read secrets: `config/secrets/helpinghands/secrets.local` → `API_KEY=xxx`
4. Use API_KEY as Bearer token for MCP calls

**Endpoint derivation:**
- production: `https://{tenant}-prod.joebouchard.workers.dev/mcp`
- develop: `https://{tenant}-dev.joebouchard.workers.dev/mcp`
- local: `http://localhost:8787/mcp`

This eliminates all configuration files - the same secrets file used for Cloudflare deployment is also used for agent authentication.

The key principle: Be explicit about where agents should find credentials. Don't rely on agents to "figure it out."

## Why This Pattern?

- **Manifest-driven**: Knows exactly what specs to expect
- **Gated synthesis**: Won't synthesize on insufficient data
- **Clear reporting**: Shows exactly what succeeded/failed
- **Timestamped runs**: Each execution isolated, never overwrites
- **Parallel execution**: All specs run simultaneously
- **Execution logging**: `log.json` enables debugging and future R2 integration
