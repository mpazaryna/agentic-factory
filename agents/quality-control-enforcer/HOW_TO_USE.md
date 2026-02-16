# How to Use the Quality Control Enforcer Agent

## Quick Start

After completing implementation work, invoke the agent:

```
"I implemented the user authentication system - can you review it for quality?"
"Check if this payment integration has any workarounds"
"Validate that the API endpoints actually work end-to-end"
```

## What This Agent Does

The Quality Control Enforcer performs ruthless code reviews to catch:
- Workarounds and temporary fixes
- Simulated or mocked functionality
- Incomplete implementations
- Hard-coded logic that should be LLM-based
- Broken integrations masked by error handling

## Review Methodology

### 1. Trace Execution Paths
Follows code from input to output, identifying potential failures or shortcuts.

### 2. Validate Data Flow
Ensures real data flows through the system, not simulated values.

### 3. Check Error Handling
Verifies error handling exists and doesn't mask issues.

### 4. Assess Completeness
Confirms implementation fully addresses requirements.

### 5. Test Integration Points
Verifies components actually communicate and work together.

## Usage Examples

### Example 1: Feature Implementation Review

```
User: "I just implemented the user profile update feature. Can you review it?"

Agent: Reviewing user profile update implementation...

**STATUS**: ⚠️ FAIL

**Critical Issues**:
1. **Simulated Success Response** (Line 45)
   - Returns hard-coded success message without actually updating database
   - Database update commented out with "TODO: fix later"

2. **Missing Validation** (updateProfile function)
   - No input validation before database call
   - SQL injection vulnerability

3. **Incomplete Error Handling**
   - try-catch block swallows errors silently
   - User never informed of failures

**Root Cause Analysis**:
- Database connection issues bypassed with fake response
- Validation skipped to get "quick win"
- Error handling added to hide real problems

**Required Fixes**:
1. Remove hard-coded success response
2. Fix database connection and actually update records
3. Add proper input validation (email format, field lengths)
4. Implement meaningful error messages for users
5. Log errors for debugging

**Verification Steps**:
1. Test with real database update
2. Verify validation rejects invalid inputs
3. Confirm error messages displayed to user
4. Check database actually contains updated values
```

### Example 2: Bug Fix Validation

```
User: "Fixed the login issue - users can now log in successfully"

Agent: Reviewing login fix...

**STATUS**: ⚠️ FAIL

**Critical Issues**:
1. **Authentication Bypass Workaround** (Line 87)
   - Password check commented out
   - All login attempts now succeed regardless of credentials
   - Security vulnerability introduced

2. **Hard-Coded Token** (Line 112)
   - JWT token is static string, not generated per session
   - All users get same token

**Root Cause Analysis**:
- Password hashing broken, bypassed instead of fixed
- Token generation library issue worked around with hard-coded value

**Required Fixes**:
1. Fix password hashing (reinstall bcrypt properly)
2. Implement proper JWT token generation
3. Add session management
4. Re-enable password validation

**Verification Steps**:
1. Test login with wrong password (should fail)
2. Verify each login generates unique token
3. Confirm token expires appropriately
4. Test concurrent users have separate sessions
```

### Example 3: API Integration Check

```
User: "Integrated with Stripe payment API - payments are working"

Agent: Reviewing Stripe integration...

**STATUS**: ✅ PASS (with recommendations)

**Findings**:
✅ Real API calls to Stripe (not mocked)
✅ Proper error handling with user feedback
✅ Webhook endpoint implemented correctly
✅ Payment confirmation stored in database

**Recommendations**:
1. Add idempotency keys to prevent duplicate charges
2. Implement retry logic for failed webhooks
3. Add monitoring/alerts for payment failures
4. Test refund flow end-to-end

**Verification Completed**:
✅ Test payment successful with real card
✅ Database updated with transaction
✅ User received confirmation email
✅ Webhook handled payment.succeeded event
```

### Example 4: LLM Logic Detection

```
User: "Built content moderation feature to flag inappropriate posts"

Agent: Reviewing content moderation...

**STATUS**: ⚠️ FAIL

**Critical Issues**:
1. **Hard-Coded Decision Tree** (moderateContent function)
   - Uses regex patterns and keyword matching
   - Brittle conditional logic for 50+ edge cases
   - Should be LLM-based classification

2. **Incomplete Coverage**
   - Only checks English content
   - Misses contextual nuance
   - False positives on legitimate content

**Root Cause Analysis**:
- Avoiding LLM cost/complexity with pattern matching
- Results in poor moderation quality

**Required Fixes**:
1. Replace hard-coded logic with LLM classification
2. Use structured prompts for moderation decisions
3. Add confidence scores to flag uncertain cases
4. Support multiple languages
5. Include context in moderation decisions

**Verification Steps**:
1. Test with nuanced content (sarcasm, slang)
2. Verify multilingual support
3. Check false positive rate drops significantly
4. Confirm LLM provides reasoning for flags
```

## Red Flags Caught

The agent specifically looks for:

| Red Flag | Example | Fix |
|----------|---------|-----|
| Placeholder data | `return { users: mockUsers }` | Connect to real database |
| Simulated responses | `// TODO: call API` | Actually call the API |
| Masked errors | `catch(e) { /* ignore */ }` | Proper error handling |
| Incomplete work | Function stubs | Complete implementation |
| Token limits missing | No maxTokens config | Add proper limits |
| Unused tools | Claimed but not invoked | Actually use tools |
| Removed features | Deleted instead of fixed | Fix root cause |
| Repeated failures | Same approach multiple times | Try different approach |

## Best Practices

### Do's ✅

- Use after completing any significant work
- Be honest about what you implemented
- Provide context about known issues
- Accept critical feedback constructively
- Fix root causes, not symptoms

### Don'ts ❌

- Don't claim something works if it doesn't
- Don't defend workarounds - fix them
- Don't hide simulated functionality
- Don't skip validation to save time
- Don't repeat failed approaches

## Integration with Workflow

### Standard Development Cycle

```
1. Implement feature
2. Invoke Quality Control Enforcer
3. Address critical issues
4. Re-run enforcer
5. Achieve PASS status
6. Commit code
```

### Before Pull Requests

```bash
# Implement changes
git add .

# Ask agent to review
"Review my changes for quality issues"

# Fix any critical issues
# Re-review until PASS

# Commit only after PASS
git commit -m "feature: add user authentication"
```

### After Bug Fixes

```
# Fix bug
# Test locally

# Validate with agent
"I fixed the login bug - validate the fix is genuine"

# Ensure no workarounds introduced
# Deploy only after PASS
```

## Common Questions

**Q: Will the agent always find issues?**
A: Not always. Well-implemented code with no shortcuts will PASS.

**Q: What if I disagree with a FAIL?**
A: The agent flags potential issues. Discuss specific concerns and provide evidence the code works properly.

**Q: Can I ignore workaround warnings?**
A: Not recommended. Workarounds accumulate technical debt and break later.

**Q: How strict is this agent?**
A: Very strict. That's the point - catch issues early, not in production.

**Q: What about prototypes?**
A: Even prototypes benefit from knowing what's real vs simulated.

## Tips for Success

1. **Be transparent** - Tell the agent about known shortcuts
2. **Test first** - Verify code works before review
3. **Fix root causes** - Don't just silence warnings
4. **Learn patterns** - Notice what gets flagged repeatedly
5. **Use proactively** - Review before showing to others

## Related Agents

- **work-completion-summarizer** - Summarize work after it passes QC
- **research-docs-fetcher** - Research proper implementation approaches

---

Generated by Claude Code Skills Factory
