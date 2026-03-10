# PRD Examples: Good vs. Problematic

## Example 1: Email-to-CRM Sync Feature

### ✅ GOOD PRD

```markdown
# PRD: Auto-Sync CRM from Email

## Problem Statement
Sales reps spend 30 minutes daily manually updating deal status in CRM, copying information from emails.
This causes data staleness (deals out of sync by 1-3 days), errors (wrong amounts entered), and frustration.
We lose visibility into real-time deal status, impacting forecast accuracy.

## Goals

### User Goals
- Sales reps: Spend <5 min/day on CRM updates (save 25+ min)
- Sales reps: Have confidence that CRM reflects current deal status
- Sales managers: See real-time deal status without chasing reps for updates

### Business Goals
- Reduce manual data entry errors by 80%
- Improve forecast accuracy (compare actual vs. predicted close dates)
- Increase rep satisfaction (less busywork)

## Success Metrics
- CRM sync latency: <2 min from email to CRM (currently 30 min manual)
- Rep adoption: 80% of team using sync within 4 weeks
- Data accuracy: 95%+ match between email and CRM for synced fields
- Time saved: avg 25 min/rep/day measured via time tracking survey

## User Stories
- As a sales rep, I want deal updates in emails to auto-sync to CRM so I don't waste time copying data
- As a sales manager, I want real-time deal visibility so I can spot at-risk deals early
- As a finance analyst, I want accurate deal data so I can forecast revenue confidently

## Requirements
- Detect deal updates in email subjects and bodies
- Extract deal fields: name, amount, close date, stage
- Match emails to existing CRM records using fuzzy matching
- Sync matched records back to CRM within 2 minutes
- Log all sync actions and flag conflicts for manual review
- Notify rep if email data conflicts with current CRM data

## Non-Goals
- Not integrating with Salesforce API (only reading email)
- Not handling custom CRM fields in v1 (only standard fields)
- Not providing historical sync (only forward from launch)

## Acceptance Criteria
- ✓ System syncs 95%+ of emails with valid deal info
- ✓ Sync latency measured at <2 min (p95)
- ✓ Zero data loss or duplication in UAT
- ✓ Reps can pause sync per email if needed
- ✓ Conflicts flagged with suggested resolution
- ✓ 80% adoption in pilot team within 4 weeks
```

### ❌ PROBLEMATIC VERSION (Before Revision)

```markdown
# PRD: Improve CRM Sync

## Problem
Users want better CRM sync. The current process is manual and slow.

## Goals
- Improve efficiency
- Better data quality
- User satisfaction

## Success Metrics
- Users are happy
- No bugs
- System is fast

## User Stories
- As a user, I want to sync data
- As a manager, I want better visibility
- As an analyst, I want accurate data

## Requirements
- Build an auto-sync feature
- Use machine learning for smart matching
- Integrate with CRM API
- Make it fast and scalable
```

**Problems with the bad version:**
- Problem statement is vague ("users want better CRM sync"—why?)
- Success metrics are unmeasurable ("users are happy", "no bugs")
- User stories don't describe concrete behavior
- Requirements focus on solutions, not needs
- No acceptance criteria
- No scope boundaries

---

## Example 2: Dashboard Analytics Feature

### ✅ GOOD PRD

```markdown
# PRD: Sales Dashboard – Real-Time Pipeline Analytics

## Problem Statement
Sales managers spend 2+ hours weekly compiling pipeline reports from disparate sources (Salesforce, emails,
spreadsheets). By the time the report is assembled, data is stale. Managers can't spot trends (deals slipping,
reps underperforming) until end-of-month reviews—too late to course-correct.

## Goals

### User Goals
- Sales managers see current pipeline status without manual work
- Spot at-risk deals within hours, not weeks
- Identify top-performing reps and replicate their tactics

### Business Goals
- Reduce month-end forecast surprises (increase forecast accuracy by 20%)
- Enable faster deal recovery (intervene on slipping deals 2+ weeks earlier)
- Improve rep coaching quality (data-driven conversations)

## Success Metrics
- Dashboard load time: <3 sec on typical data (~1K deals)
- Adoption: 90% of managers accessing dashboard weekly by week 4
- Forecast accuracy: 20% improvement in predicted vs. actual close rates
- Manager satisfaction: 4/5 stars in feedback survey

## User Stories
- As a sales manager, I want to see pipeline by stage/rep so I can prioritize coaching
- As a VP of Sales, I want to see trends (win rate, deal velocity, forecast health) so I can adjust targets
- As a sales rep, I want to see my personal metrics so I understand how I compare

## Requirements
- Real-time data from Salesforce (synced every 15 min)
- Pipeline view: deals grouped by stage, rep, and probability
- Drill-down capability: click a stage to see deals
- Trend charts: deal velocity, win rate, avg deal size over 90 days
- Filters: date range, rep, deal size, industry
- Export: users can download report as CSV/PDF

## Non-Goals
- Not predicting deal close probability in v1 (AI model deferred to v2)
- Not integrating with email/calendar to infer engagement level
- Not building custom dashboard builder (fixed dashboard for v1)

## Acceptance Criteria
- ✓ Dashboard displays current deal data synced <15 min from Salesforce
- ✓ Load time <3 sec for 1K deals
- ✓ All filters work without lag
- ✓ Charts render accurately (spot checks against source data)
- ✓ 90% of managers adopt by week 4
- ✓ Export produces valid CSV/PDF
```

---

## Example 3: API Rate Limiting Feature

### ✅ GOOD PRD

```markdown
# PRD: API Rate Limiting to Prevent Abuse

## Problem Statement
Public APIs are experiencing requests from automated bots and scraping tools, consuming 40% of our compute.
Legitimate users experience timeouts during bot traffic spikes. We need rate limiting to protect service stability
and ensure fair resource allocation.

## Goals

### User Goals
- Legitimate API users: Consistent response times regardless of bot traffic
- API users building integrations: Clear guidance on rate limits and retry strategy

### Business Goals
- Reduce compute costs by 30% (by blocking abusive traffic)
- Improve API reliability (reduce timeout errors for real users)
- Enable tier-based monetization (free tier, pro tier with higher limits)

## Success Metrics
- P95 API response time: <100ms (currently 300-500ms during bot peaks)
- Compute cost reduction: 30% drop in usage from baseline
- Error rate for legitimate users: <1% (down from 5% due to timeouts)
- Adoption of rate-limit headers: 80% of integrations respect headers

## User Stories
- As a legitimate API user, I want consistent response times so my integration is reliable
- As an integration developer, I want clear rate limits and retry guidance so I can build resilient code
- As a billing manager, I want usage tiers so I can monetize the API fairly

## Requirements
- Implement per-IP rate limiting (requests/minute)
- Return HTTP 429 with Retry-After header
- Provide rate limit headers in responses (X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset)
- Free tier: 100 requests/min per IP
- Pro tier: 1,000 requests/min per IP
- Spike allowance: Allow burst of +20% for 30 seconds (graceful degradation)
- Log all rate limit violations for abuse detection

## Non-Goals
- Not building a dashboard to monitor API usage in v1 (defer to v2)
- Not implementing JWT-based rate limiting per user (IP-based only for v1)
- Not white-listing known good bots (manual process for now)

## Acceptance Criteria
- ✓ Free tier APIs reject requests >100/min with 429 status
- ✓ Pro tier APIs reject requests >1,000/min with 429 status
- ✓ 429 response includes Retry-After header
- ✓ Rate limit headers present in all successful responses
- ✓ Burst window (+20% for 30s) functions as designed
- ✓ Load test with 2x normal traffic shows 30% reduction in compute cost
- ✓ Zero legitimate user 429 errors in canary deployment
```

---

## Pattern Comparison

| Dimension | ✅ Good | ❌ Problematic |
|-----------|--------|------------------|
| **Problem** | Specific pain (users spend 30 min/day on X) | Generic ("improve efficiency") |
| **Metrics** | Measurable with targets (25 min saved, 95% sync) | Aspirational ("happy users", "no bugs") |
| **Stories** | User behavior ("I want X so I can Y") | System capability ("build X feature") |
| **Requirements** | What must be true ("sync in <2 min") | How to build it ("use ML", "scale it") |
| **Scope** | Clear boundaries (non-goals listed) | Everything is in scope |
| **Criteria** | Testable conditions (checkboxes) | Subjective ("works well") |

---

## Red Flags to Catch & Fix

### 🚩 "We need machine learning"
**Red flag:** Solution-first thinking without clear problem.
**Fix:** Ask "What do reps currently do to find at-risk deals?" and "Why is it hard?"

### 🚩 "Scale it to millions of users"
**Red flag:** Premature optimization; confusing constraint with goal.
**Fix:** Ask "How many users in v1?" and "What's the growth projection?"

### 🚩 "Make it intuitive"
**Red flag:** Unmeasurable success criteria.
**Fix:** Ask "What would an 'intuitive' onboarding look like?" and define metrics (time to first sync, errors, etc.)

### 🚩 "Improve data quality"
**Red flag:** Vague goal with no metric.
**Fix:** Ask "How is quality measured today?" and "What's the target?" (95% accuracy? 99%?)

---

## Using These Examples

When working with customers or teams:
1. Share the **good example** as a target state
2. Review their draft against the **pattern comparison table**
3. Use red flags to highlight vague language and push for specificity
4. Iterate until their PRD meets the ✅ good standards
