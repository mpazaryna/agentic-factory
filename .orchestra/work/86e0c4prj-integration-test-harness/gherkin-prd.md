# Gherkin Scenarios: Integration Test Harness for Plugin Skills

> Source: .orchestra/work/86e0c4prj-integration-test-harness/prd.md
> Generated: 2026-04-26

```gherkin
Feature: Integration Test Harness Setup
  A dedicated test repository exists with realistic project scaffolding
  sufficient to exercise API calls, git operations, and plugin skills

  Scenario: Test repo scaffolded with realistic project structure
    Given no test repository exists
    When the tester creates a new repo following the harness setup guide
    Then the repo contains src/, tests/, and docs/ directories
    And a CONTEXT.md file describes build commands, directory structure, and ADR locations
    And a .env file contains a valid CLICKUP_API_KEY

  Scenario: Test repo has git history that simulates real project conditions
    Given the scaffolded test repo exists
    When the tester adds commits across multiple branches
    Then the repo has at least one main branch commit and one feature branch commit
    And git log shows realistic commit messages

  Scenario: clickup plugin installed from marketplace into test repo
    Given the test repo is scaffolded
    When the tester runs /plugin install clickup@agentic-factory inside the test repo
    Then the clickup plugin skills appear under .claude/skills/
    And all 5 skills are present: open, investigate, agent, close, conventions


Feature: /open Skill Validation
  The /open skill changes ticket status, creates a branch, and presents a checklist

  Background:
    Given the test repo is set up
    And the clickup plugin is installed
    And at least one ClickUp ticket exists in "to do" status

  Scenario: Open a ticket with a clear description
    Given a ticket with a complete description and no blockers
    When the tester runs /open <task-id> with that ticket ID
    Then the ticket status changes to "in progress"
    And a git branch is created named after the ticket
    And an evaluation checklist is presented to the tester

  Scenario: Open a ticket that has no description
    Given a ticket exists with an empty description field
    When the tester runs /open <task-id> with that ticket ID
    Then the skill surfaces a warning that the description is missing
    And does not proceed until the tester confirms or the ticket is updated

  Scenario: Open a ticket already in progress
    Given a ticket is already in "in progress" status
    When the tester runs /open <task-id> with that ticket ID
    Then the skill detects the existing status
    And informs the tester rather than silently duplicating the branch

  Scenario: Open with a search query instead of a task ID
    Given no explicit task ID is provided
    When the tester runs /open "keyword search string"
    Then the skill searches ClickUp for matching tasks
    And presents candidate matches for the tester to confirm before proceeding


Feature: /investigate Skill Validation
  The /investigate skill returns structured analysis without changing ticket state

  Background:
    Given the test repo is set up
    And the clickup plugin is installed

  Scenario: Investigate a ticket with open questions
    Given a ticket contains ambiguous requirements or missing context
    When the tester runs /investigate <task-id>
    Then the skill returns a structured analysis identifying the open questions
    And the ticket status is unchanged
    And no git branch is created

  Scenario: Investigate a fully specified ticket
    Given a ticket has complete acceptance criteria and no ambiguity
    When the tester runs /investigate <task-id>
    Then the skill returns a confirmation that no open questions were found
    And suggests proceeding directly to /open

  Scenario: Investigate a ticket referencing ADRs that do not exist
    Given a ticket references an ADR by name or number
    And that ADR does not exist in the .orchestra/adr/ folder
    When the tester runs /investigate <task-id>
    Then the skill flags the missing ADR as a blocker
    And lists it explicitly in the analysis output


Feature: /agent Skill Validation
  The /agent skill runs autonomously in a forked context and posts updates to ClickUp

  Background:
    Given the test repo is set up
    And the clickup plugin is installed

  Scenario: Agent executes a small clear ticket end to end
    Given a ticket has a clear description, bounded scope, and defined acceptance criteria
    When the tester runs /agent <task-id>
    Then the skill posts a plan comment to ClickUp before starting implementation
    And runs implementation in a forked context
    And creates a pull request on completion
    And updates the ticket status to reflect work in progress

  Scenario: Agent escalates rather than proceeding on an ambiguous ticket
    Given a ticket has missing or contradictory requirements
    When the tester runs /agent <task-id>
    Then the skill declines to proceed autonomously
    And returns a summary of what information is needed before execution can begin

  Scenario: Agent recovers or surfaces failure when the build breaks
    Given a ticket is clear and scoped
    When the tester runs /agent <task-id> and the build fails mid-implementation
    Then the skill surfaces the build error with context
    And does not create a pull request with broken code


Feature: /close Skill Validation
  The /close skill confirms UAT, creates a PR, merges, and sets terminal status

  Background:
    Given the test repo is set up
    And the clickup plugin is installed
    And a ticket is in "in progress" with a feature branch ready

  Scenario: Close a ticket after UAT passes
    Given the feature branch work is complete and UAT has passed
    When the tester runs /close <task-id>
    Then a pull request is created if one does not already exist
    And the PR is merged
    And the ticket status is set to complete

  Scenario: Close loops back when UAT finds issues
    Given UAT identified defects before merge
    When the tester runs /close <task-id> and reports UAT failure
    Then the skill does not merge the PR
    And surfaces the issues for remediation
    And leaves the ticket in "in progress" status

  Scenario: Close proceeds when no documentation changes are needed
    Given the feature has no public-facing or architectural impact
    When the tester runs /close <task-id>
    Then the skill skips the doc-update step
    And completes the close flow without prompting for doc changes


Feature: conventions Background Skill Validation
  The conventions skill is a background reference that shapes Claude's behavior
  without appearing in the user-invocable slash command menu

  Scenario: Conventions informs correct status transitions during ticket work
    Given the conventions skill is installed in the test repo
    When Claude is asked to work on a ClickUp ticket in any skill
    Then Claude references the correct status flow defined in conventions
    And does not apply incorrect status labels at any step

  Scenario: Comment templates match the expected format
    Given the conventions skill is installed
    When a skill posts a comment to ClickUp
    Then the comment format matches the template defined in conventions

  Scenario: Conventions skill does not appear in the slash command menu
    Given the conventions skill frontmatter sets user-invocable to false
    When the tester types / in Claude Code
    Then the conventions skill does not appear as a selectable command


Feature: Skill Improvement Promotion
  Failures and suboptimal outputs from integration testing drive improvements
  that are promoted back to the factory

  Background:
    Given integration testing has been run for at least one skill

  Scenario: A failing scenario drives a skill improvement
    Given a test scenario produced incorrect or missing output
    When the tester fixes the SKILL.md in the test repo's installed copy
    And re-runs the scenario until it passes
    Then the improved SKILL.md is copied back to agentic-factory
    And committed with a reference to the test scenario that drove the change

  Scenario: At least three measurable improvements are promoted
    Given integration testing has completed for all 5 clickup skills
    When the tester reviews all scenario results
    Then at least 3 distinct SKILL.md improvements have been committed to agentic-factory

  Scenario: Integration test methodology is captured for reuse
    Given the test repo exists with a populated tests/ folder and RESULTS.md
    When another developer wants to test a different plugin
    Then they can follow the same methodology without additional guidance
    And the process is documented in the test repo README.md
```
