# PRD: Integration Test Harness for Plugin Skills

**Objective:** Establish a repeatable methodology for integration-testing factory plugins against real project conditions, improving skill quality through real-world feedback loops.

## Success Criteria

- [ ] Test repo exists with realistic project scaffolding (CONTEXT.md, .env, source code, git history)
- [ ] clickup plugin fully tested: all 5 skills (open, investigate, agent, close, conventions) validated against real ClickUp tickets
- [ ] At least 3 measurable skill improvements promoted back to agentic-factory
- [ ] Integration test methodology documented and repeatable for other plugins
- [ ] Test scenarios captured in the repo for regression testing

## Context

The agentic-factory is an authoring workspace — skills are written and structured here, but they cannot be fully validated without real project context. A skill like `/open` requires a ClickUp API key, a CONTEXT.md with project conventions, actual source code to navigate, and real tickets to fetch. Testing in the factory catches structural issues (bad frontmatter, missing files) but not behavioral issues (wrong API call, poor output format, missed edge cases).

The Skills 2.0 article describes a five-step iterative loop: (1) find a hard task, (2) iterate until Claude succeeds, (3) extract the winning approach into a skill, (4) expand test coverage, (5) version like code. Steps 2-4 require integration context.

## Approach

### Phase 1: Test Repo Setup

Create a dedicated test repo with:
- Realistic project structure (src/, tests/, docs/)
- `CONTEXT.md` with build commands, directory structure, conventions, ADR locations
- `.env` with `CLICKUP_API_KEY`
- Git history with branches and commits
- A few known ClickUp tickets in different states (to do, in progress, complete)
- Install clickup plugin from the marketplace: `/plugin install clickup@agentic-factory`

### Phase 2: Test Scenarios

For each skill, define and execute:

**`/open <task-id>`**
- Happy path: ticket exists, clear description, no blockers
- Edge: ticket has no description
- Edge: ticket is already in progress
- Edge: search query instead of task ID
- Verify: status changes to "in progress", branch created, evaluation checklist presented

**`/investigate <task-id>`**
- Happy path: ticket with open questions
- Edge: ticket is fully specified (nothing to investigate)
- Edge: ticket references ADRs that don't exist
- Verify: status NOT changed, no branch created, structured analysis returned

**`/agent <task-id>`**
- Happy path: small, clear ticket with bounded scope
- Edge: ambiguous ticket (should escalate, not proceed)
- Edge: build fails during implementation
- Verify: runs in forked context, posts plan to ClickUp, creates PR, updates status

**`/close <task-id>`**
- Happy path: work complete, UAT passed
- Edge: UAT found issues (should loop back)
- Edge: no doc changes needed
- Verify: PR created, merge confirmed, status set to complete

**`conventions` (background)**
- Verify: Claude references correct status flow when working on ClickUp tickets
- Verify: comment templates match expected format
- Verify: does NOT appear in `/` menu (user-invocable: false)

### Phase 3: Improve and Promote

For each failure or suboptimal output:
1. Fix the skill in the test project's installed copy
2. Re-test until passing
3. Copy the improved SKILL.md back to agentic-factory
4. Commit with reference to the test scenario that drove the change

### Phase 4: Document

Capture in the test repo:
- `tests/` folder with scenario descriptions and expected outputs
- `RESULTS.md` with pass/fail per scenario
- Improvement changelog: what changed and why

## Materials

| Material | Location | Status |
|----------|----------|--------|
| Test repo with project scaffolding | TBD (new repo) | Not Started |
| clickup plugin installed | test repo .claude/ | Not Started |
| Test scenarios for 5 skills | test repo tests/ | Not Started |
| Skill improvements | agentic-factory pm/clickup/ | Not Started |
| Process documentation | test repo README.md | Not Started |

## References

- Skills 2.0 iterative loop: start with hard task, iterate, extract, expand tests, version
- ADR-004 (Skills 2.0 migration): documents current skill structure and frontmatter decisions
- Orchestra methodology: test repo could use .orchestra/ for its own work tracking

## Notes

- Start with clickup as the first plugin to test — it has the most complex skills (API calls, git operations, forked context)
- The methodology should generalize to any plugin: create test repo, install plugin, run scenarios, improve, promote
- Consider whether the test repo pattern itself becomes a skill (/scaffold-test-repo)
