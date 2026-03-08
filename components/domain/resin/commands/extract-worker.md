---
name: Extract Worker
allowed-tools: Bash, Read, Glob
description: Run extraction workflow using TypeScript worker (Anthropic SDK, production-grade, API cost)
---

# Extract Worker

Launches the TypeScript extraction worker as a background process and monitors it to completion. Uses the Anthropic SDK ($2-7/run). Best for production use.

## Arguments

$ARGUMENTS - Two arguments: `<workflow> <tenant-env>`
- **workflow**: The spec folder name (e.g., "fundraising-intelligence", "99-dev-test")
- **tenant-env**: Tenant and environment in format `{tenant}-{env}` (e.g., "helpinghands-prod", "pow-local")

Example: `fundraising-intelligence pow-prod`

## Flow

```
/extract-worker fundraising-intelligence pow-prod
       |
1. Parse arguments (same convention as extract-agent)
       |
2. Get repo root, validate spec folder and secrets exist
       |
3. Predict next run ID to know where output will land
       |
4. Launch worker in background (npm run extract)
       |
5. Report launch immediately with expected output path
       |
6. Monitor: poll for JSON files appearing in output dir
       |
7. Detect completion: log.json appears
       |
8. Report: run_id, duration, specs, tokens, cost
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

### Step 1: Get Repo Root

```bash
git rev-parse --show-toplevel
```

Store as `REPO_ROOT`.

### Step 2: Validate Prerequisites

Check that the spec folder and secrets file exist:

```bash
ls {REPO_ROOT}/mill/spec/{workflow}/manifest.json
ls {REPO_ROOT}/secrets/{tenant}/secrets.{envName}
```

If either is missing, report the error and stop.

### Step 3: Predict Next Run ID

The TS worker generates its own run ID. Predict it so we know where to monitor:

```bash
TODAY=$(date +%Y-%m-%d)
ls -d {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/${TODAY}-* 2>/dev/null | sort
```

- If no dirs exist for today, predicted ID is `{TODAY}-001`
- Otherwise parse max sequence and increment
- Store as `PREDICTED_RUN_ID`

The predicted output path is: `{REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{PREDICTED_RUN_ID}/`

### Step 4: Launch Worker in Background

**CRITICAL**: Full extraction runs take 12-18 minutes. The Bash tool has a 10-minute max timeout. Use `run_in_background: true`.

```bash
cd {REPO_ROOT}/workers/extraction && npm run extract -- --spec {workflow} --tenant {tenant} --env {envName} 2>&1
```

Launch this with `Bash(run_in_background=true)`.

Store the background task ID.

### Step 5: Report Launch

Immediately tell the user:

```
Worker launched in background!

Workflow: {workflow}
Tenant: {tenant} ({envName})
Expected output: dat/{tenant}/extraction/{workflow}/{PREDICTED_RUN_ID}/

Monitoring for completion... (typical runtime: 12-18 min for full workflows, 2-5 min for dev-test)

I'll check progress every ~30 seconds and report when done.
```

### Step 6: Monitor Progress

Poll every ~30 seconds to check for output files appearing:

```bash
ls {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{PREDICTED_RUN_ID}/*.json 2>/dev/null | wc -l
```

**Race condition handling**: If the predicted output directory doesn't appear within 60 seconds:
1. Re-scan for any new directory that appeared for today:
   ```bash
   ls -dt {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/$(date +%Y-%m-%d)-* 2>/dev/null | head -1
   ```
2. Update the monitored path to the actual directory the worker created

On each poll, briefly report progress if new files appeared (e.g., "3/8 specs complete...").

Also check if the background process has exited:
- Use `TaskOutput(task_id, block=false)` to check background process status without blocking

### Step 7: Detect Completion

The worker writes `log.json` as its final output. Watch for it:

```bash
ls {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{ACTUAL_RUN_ID}/log.json 2>/dev/null
```

When `log.json` appears, the run is complete.

### Step 8: Report Results

Read `log.json` and extract key metrics:

```bash
# Read the log
cat {REPO_ROOT}/dat/{tenant}/extraction/{workflow}/{ACTUAL_RUN_ID}/log.json
```

Report a summary:

```
Extraction complete!

Engine: worker (TypeScript / Anthropic SDK)
Run ID: {run_id}
Tenant: {tenant} ({environment})
Duration: {duration} seconds
Output: dat/{tenant}/extraction/{workflow}/{run_id}/

Specs: {completed}/{total}
- [status for each spec with duration if available]

Synthesis: {status}
Prioritization: {status}

Token Usage: {input_tokens} input / {output_tokens} output
Estimated Cost: ${cost}

Next steps:
- Sync to R2: ./scripts/devops/cli sync all {tenant}
- Run with subagents: /extract-agent {workflow} {tenant}-{env}
- View results: ls dat/{tenant}/extraction/{workflow}/{run_id}/
```

### Error Handling

If the background process exits with an error (non-zero exit code):

1. Read the background task output for error details
2. Check the daily log file for diagnostics:
   ```bash
   tail -20 {REPO_ROOT}/logs/{tenant}/$(date +%Y-%m-%d).jsonl 2>/dev/null
   ```
3. Report the error with context:
   ```
   Worker failed!

   Error: {error message from process output}

   Recent logs:
   {last few log entries}

   To debug:
   - Check full logs: logs/{tenant}/{date}.jsonl
   - Try with local MCP: /extract-worker {workflow} {tenant}-local
   - Use subagent engine: /extract-agent {workflow} {tenant}-{env}
   ```

## Output Structure

Same as extract-agent — both engines produce identical output structure:

```
dat/{tenant}/extraction/{workflow}/{RUN_ID}/
├── log.json                        <- Execution metadata (includes token usage)
├── 01-spec-name.json
├── 01-spec-name.md
├── ...
├── 99-synthesis.json
├── 99-synthesis.md
└── ...
```

## Example Usage

```
# Run fundraising intelligence for Protect Our Winters (production)
/extract-worker fundraising-intelligence pow-prod

# Run dev test against local MCP
/extract-worker 99-dev-test helpinghands-local

# Run against develop environment
/extract-worker fundraising-intelligence helpinghands-dev
```

## Differences from /extract-agent

| Aspect | /extract-agent | /extract-worker |
|--------|---------------|-----------------|
| Engine | Claude Code subagents | TypeScript + Anthropic SDK |
| Cost | Free (Max plan) | $2-7 per run |
| Runtime | Variable (parallel agents) | 12-18 min (sequential) |
| Best for | Desktop/dev, iteration | Production, consistency |
| Org-context | Injected via prompt | Auto-discovered from tenants.json |
| Token tracking | Not available | Full token + cost tracking |
