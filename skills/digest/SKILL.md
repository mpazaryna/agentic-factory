---
name: digest
description: "Extract key points from a URL (web or YouTube) and organize the output. Usage: /digest <url>"
allowed-tools: Bash
disable-model-invocation: false
---

# digest

Run the digest worker on a URL and organize the output.

## Steps

1. Run the extraction:
   ```bash
   cd ~/workspace/workers/digest && uv run digest url '<url>'
   ```
   Always single-quote the URL to prevent shell glob expansion.

2. Run organize:
   ```bash
   cd ~/workspace/workers/digest && uv run digest organize
   ```

3. Report the output file path from step 1 and confirm organize ran.

## Nothing else

Do not modify files. Do not read existing digests. Do not suggest follow-up actions unless asked.
