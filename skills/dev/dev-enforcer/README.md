# quality-control-enforcer

Review and validate implementation quality — catches workarounds, simulated data, incomplete implementations, and shortcuts.

## Quick Start

```
review this implementation for quality issues
check if the payment flow is genuinely working end-to-end
quality check the auth feature before we ship
does this actually work or is it faking it?
```

## What It Does

Acts as a zero-tolerance code reviewer focused on whether things genuinely work, not just whether they look correct.

**Review methodology:**
1. Traces execution paths from input to output
2. Validates that real data flows through the system (not mocked/hardcoded)
3. Checks error handling — flags try-catch blocks that hide real failures
4. Assesses completeness against the original requirement
5. Verifies integration points actually communicate

**Red flags it hunts for:**
- Placeholder or simulated responses
- Hard-coded conditional logic that should be LLM-driven
- Functionality removed instead of fixed
- Token limits not configured or passed
- Tools claimed to be used but never invoked
- The same failed approach repeated without learning

**Output format:**
- **Status**: PASS or FAIL with clear reasoning
- **Critical Issues**: each workaround or incomplete implementation
- **Root Cause Analysis**: the underlying problem for each issue
- **Required Fixes**: specific actions needed
- **Verification Steps**: how to confirm the fixes worked

## See Also

- `convention-auditor` — checks adherence to project conventions, not implementation quality
