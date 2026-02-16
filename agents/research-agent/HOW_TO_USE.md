# How to Use the Research Agent

## Quick Start

Invoke the agent for research tasks:

```
"Research the latest React 19 features"
"Fetch documentation from https://docs.python.org/3/library/asyncio.html"
"Gather information about PostgreSQL indexing strategies"
```

## What This Agent Does

The Research Agent systematically gathers information from the web and organizes it into structured markdown files. It:
- Fetches content from URLs or searches for topics
- Avoids duplication by checking existing files
- Creates clean, organized markdown in `ai_docs/research/`
- Provides summaries and key findings
- Suggests related topics for further research

## Research Workflow

### 1. Parse Your Request
The agent analyzes what you need:
- Direct URLs to specific documentation
- Topics requiring web search
- Multiple sources to compare

### 2. Check Existing Research
Before fetching, checks if you already have this information:
- Scans `ai_docs/research/` directory
- Reads file metadata for timestamps
- Skips files less than 24 hours old (unless forced)

### 3. Fetch Content
Retrieves information from the web:
- Uses WebFetch for direct URLs
- Uses WebSearch for topics
- Processes HTML into markdown

### 4. Organize and Structure
Creates well-formatted documents:
- Descriptive filenames (lowercase-with-hyphens.md)
- Metadata headers (source, timestamp, summary)
- Clear section hierarchy
- Preserved code examples

### 5. Save to Repository
Stores research in organized structure:
- Creates `ai_docs/research/` if needed
- Saves with consistent formatting
- Adds cross-references when relevant

### 6. Report Results
Provides summary of research session:
- Files created or updated
- Key findings from each source
- Suggestions for follow-up research

## Usage Examples

### Example 1: Research a Technology

```
User: "Research Next.js Server Components"

Agent: I'll research Next.js Server Components and save the findings...

**Research Summary**

**Topic**: Next.js Server Components
**Sources Processed**: 3
**Files Created**: 1
**Files Updated**: 0
**Files Skipped**: 0

### Files Created
- `ai_docs/research/nextjs-server-components.md` - Comprehensive guide to React Server Components in Next.js

### Key Findings
- Server Components render on the server, reducing client-side JavaScript
- Can directly access backend resources (databases, file system)
- Automatic code splitting and streaming support
- Different from Client Components which use 'use client' directive
- Best practices for data fetching and composition patterns

### Suggested Follow-up Research
- Next.js App Router architecture
- React Suspense boundaries
- Server Actions in Next.js
```

### Example 2: Fetch Specific Documentation

```
User: "Fetch the Stripe webhook documentation from https://stripe.com/docs/webhooks"

Agent: Fetching Stripe webhook documentation...

**Research Summary**

**Topic**: Stripe Webhooks
**Sources Processed**: 1
**Files Created**: 1
**Files Updated**: 0
**Files Skipped**: 0

### Files Created
- `ai_docs/research/stripe-webhooks.md` - Complete webhook integration guide

### Key Findings
- Webhooks deliver real-time event notifications
- Must verify webhook signatures for security
- Use Stripe CLI for local testing
- Handle idempotency to prevent duplicate processing
- Supports retry mechanism for failed webhooks
- Event types: payment_intent.succeeded, customer.created, etc.

### Code Examples Preserved
✅ Webhook signature verification (Node.js)
✅ Express endpoint setup
✅ Event handling patterns
✅ Testing with Stripe CLI

### Suggested Follow-up Research
- Stripe Payment Intents API
- Webhook event reference
- Testing webhooks in production
```

### Example 3: Comparative Research

```
User: "Research and compare authentication strategies: JWT vs Session-based"

Agent: Researching authentication strategies...

**Research Summary**

**Topic**: Authentication Strategies Comparison
**Sources Processed**: 5
**Files Created**: 1
**Files Updated**: 0
**Files Skipped**: 0

### Files Created
- `ai_docs/research/authentication-jwt-vs-sessions.md` - Detailed comparison with trade-offs

### Key Findings

**JWT (JSON Web Tokens)**
- Stateless, stored client-side
- Scales horizontally easily
- Cannot invalidate without additional infrastructure
- Larger payload sent with each request
- Good for: Microservices, mobile apps, distributed systems

**Session-Based**
- Stateful, stored server-side
- Easy to invalidate/revoke
- Smaller cookie payload
- Requires session store (Redis, database)
- Good for: Monolithic apps, admin panels, high-security contexts

**Hybrid Approaches**
- Refresh tokens with short-lived JWTs
- Session ID with JWT claims
- Best of both worlds for many use cases

### Suggested Follow-up Research
- OAuth 2.0 implementation
- Refresh token rotation strategies
- Redis session store setup
```

### Example 4: Building a Tech Stack Reference

```
User: "Research our tech stack: React, TypeScript, PostgreSQL, Docker"

Agent: Gathering comprehensive documentation for your tech stack...

**Research Summary**

**Topic**: Tech Stack Documentation
**Sources Processed**: 8
**Files Created**: 4
**Files Updated**: 0
**Files Skipped**: 0

### Files Created
- `ai_docs/research/react-best-practices.md` - React patterns and hooks
- `ai_docs/research/typescript-strict-mode.md` - TypeScript configuration guide
- `ai_docs/research/postgresql-performance.md` - Query optimization and indexing
- `ai_docs/research/docker-compose-development.md` - Docker development setup

### Key Findings

**React**
- Prefer functional components with hooks
- Use custom hooks for shared logic
- Implement error boundaries for reliability
- Code splitting with React.lazy()

**TypeScript**
- Enable strict mode for type safety
- Use interfaces for object shapes
- Leverage type inference
- Avoid 'any' type

**PostgreSQL**
- Index foreign keys and query columns
- Use EXPLAIN ANALYZE for optimization
- Connection pooling with pg-pool
- Regular VACUUM maintenance

**Docker**
- Multi-stage builds reduce image size
- Use .dockerignore to exclude files
- Compose for local development
- Health checks for container monitoring

### Suggested Follow-up Research
- React Server Components
- TypeScript generics advanced patterns
- PostgreSQL replication strategies
- Kubernetes for production deployment
```

### Example 5: Avoiding Duplicate Research

```
User: "Research TypeScript best practices"

Agent: Checking existing research...

**Research Summary**

**Topic**: TypeScript Best Practices
**Sources Processed**: 0
**Files Created**: 0
**Files Updated**: 0
**Files Skipped**: 1

### Files Skipped
- `ai_docs/research/typescript-best-practices.md` - Created 3 hours ago (fresh)

**Note**: Research file exists and is recent. To force refresh, request:
"Re-research TypeScript best practices and update the existing file"

**Quick Summary of Existing Research**:
- Covers strict mode configuration
- Type inference patterns
- Generic usage examples
- Common pitfalls to avoid
- Integration with React/Node.js

Would you like me to:
1. Summarize the existing research
2. Research a specific TypeScript subtopic
3. Force refresh the existing file
```

### Example 6: Incremental Research

```
User: "Add OAuth 2.0 research to our authentication documentation"

Agent: Checking for existing authentication research...

**Research Summary**

**Topic**: OAuth 2.0 Integration
**Sources Processed**: 3
**Files Created**: 1
**Files Updated**: 1
**Files Skipped**: 0

### Files Created
- `ai_docs/research/oauth2-implementation.md` - Complete OAuth 2.0 guide

### Files Updated
- `ai_docs/research/authentication-strategies.md` - Added OAuth 2.0 section and cross-reference

### Key Findings
- OAuth 2.0 has multiple grant types (authorization code, client credentials, etc.)
- Authorization code flow most common for web apps
- Use PKCE for public clients (SPAs, mobile)
- Requires registration with OAuth provider
- Handle token refresh automatically
- Store tokens securely (httpOnly cookies or secure storage)

### Cross-References Added
✅ Linked OAuth guide from authentication strategies doc
✅ Added comparison with JWT and session-based auth

### Suggested Follow-up Research
- OpenID Connect (OIDC)
- Social login integrations (Google, GitHub)
- Token refresh patterns
```

## Research Patterns

### Pattern 1: Before Starting a Feature

```bash
# Research before implementation
"Research Stripe checkout integration"
"Gather WebSocket real-time communication docs"

# Implement with reference
# ai_docs/research/ has everything you need
```

### Pattern 2: Learning New Technology

```bash
# Systematic learning
"Research GraphQL basics"
"Research GraphQL schema design"
"Research GraphQL resolvers and data loading"
"Research GraphQL error handling"

# Build knowledge progressively
```

### Pattern 3: Troubleshooting

```bash
# When stuck, research solutions
"Research PostgreSQL connection pool exhaustion"
"Gather Redis memory optimization strategies"
"Research Docker container networking issues"

# Solutions saved for future reference
```

### Pattern 4: Team Onboarding

```bash
# Build comprehensive docs
"Research our entire tech stack"
"Gather best practices for each technology"
"Research common gotchas and pitfalls"

# New team members have instant reference
```

## Best Practices

### Do's ✅

- Be specific about what you want to research
- Provide URLs when you have specific sources
- Let the agent check for existing research
- Build a research library incrementally
- Use research files during implementation
- Update research periodically

### Don'ts ❌

- Don't fetch the same documentation repeatedly
- Don't ignore existing research files
- Don't research too broadly (break into topics)
- Don't forget to reference research during coding
- Don't skip organizing research files

## Integration with Workflow

### Standard Development Cycle

```
1. Get feature request
2. Research relevant technologies
3. Review generated research files
4. Implement using documented patterns
5. Reference research during code review
```

### Building a Knowledge Base

```bash
# Start of project
mkdir -p ai_docs/research

# Ongoing research
"Research [technology] as needed"

# Result: Growing library of technical documentation
ls ai_docs/research/
# authentication-strategies.md
# nextjs-server-components.md
# postgresql-indexing.md
# react-performance.md
# stripe-webhooks.md
# ...
```

## Tips for Success

1. **Be Specific**: "Research JWT refresh token rotation" vs "Research authentication"
2. **Provide Context**: "Research OAuth for our React SPA" vs "Research OAuth"
3. **Use URLs**: Direct links get better, more accurate results
4. **Build Incrementally**: Research subtopics rather than huge topics at once
5. **Reference Often**: Use `cat ai_docs/research/[topic].md` during development
6. **Keep Fresh**: Re-research key topics periodically for updates

## Common Questions

**Q: Where are research files saved?**
A: In `ai_docs/research/` directory by default.

**Q: Can I change the output directory?**
A: Yes, edit the agent definition to use your preferred location.

**Q: Will the agent research the same topic twice?**
A: No, it checks for existing files and skips recent ones (< 24 hours old).

**Q: How do I force a refresh?**
A: Request explicitly: "Re-research [topic] and update the file"

**Q: Can I research multiple topics at once?**
A: Yes: "Research React hooks, TypeScript generics, and PostgreSQL transactions"

**Q: What if a URL is behind a paywall?**
A: The agent will report fetch failures and suggest alternatives.

## Related Agents

- **quality-control-enforcer** - Validate implementation against researched best practices
- **work-completion-summarizer** - Summarize research findings in reports

---

Generated by Claude Code Skills Factory
