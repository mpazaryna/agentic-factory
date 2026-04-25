# Gherkin Scenarios: Technical Spec — Component Sharing & Distribution System

> Source: .orchestra/work/86e08c1a1-optimize-factory/spec.md
> Generated: 2026-04-25

```gherkin
Feature: Component discovery via factory gateway
  The factory gateway command lets a developer discover available components
  from the registry without installing them or loading their full content

  Background:
    Given the factory gateway is installed at "~/.claude/commands/factory.md"
    And the factory repo is at "~/workspace/agentic-factory"
    And "registry.yaml" contains at least one skill, one agent, and one command

  Scenario: List all components grouped by type
    When the developer runs "/factory list" from any project
    Then skills are displayed under a SKILLS heading
    And agents are displayed under an AGENTS heading
    And commands are displayed under a COMMANDS heading
    And domain-specific components are displayed under their DOMAIN heading

  Scenario: Filter components by scope and type
    When the developer runs "/factory list --scope general --type skill"
    Then only skills with scope "general" are shown
    And no agents or commands appear in the output
    And no domain-specific components appear in the output

  Scenario: Search components by keyword
    When the developer runs "/factory list --search codebase"
    Then only components whose name, description, or tags match "codebase" are shown
    And the result includes component type and description for each match

  Scenario: Search returns no matches
    When the developer runs "/factory list --search xyznotarealterm"
    Then the output reports zero matching components
    And no component entries are shown


Feature: Component installation
  The factory gateway installs components from the factory repo into either the
  global ~/.claude/ or the current project's .claude/ directory

  Background:
    Given the factory gateway is installed at "~/.claude/commands/factory.md"
    And the factory repo is at "~/workspace/agentic-factory"
    And "registry.yaml" is current

  Scenario: Install a single component globally
    Given "dev-explore" is listed in "registry.yaml" with install_target "skills/dev-explore"
    When the developer runs "/factory install dev-explore --global"
    Then "SKILL.md" is copied to "~/.claude/skills/dev-explore/SKILL.md"
    And the output confirms the install location

  Scenario: Install a command with bundled templates at project level
    Given "acb" is listed with 8 install files including 7 templates
    When the developer runs "/factory install acb --project" from a project directory
    Then "acb.md" and all 7 template files are copied to ".claude/commands/acb/"
    And the directory structure mirrors the factory component layout

  Scenario: Install all general components in a single command
    Given the registry contains multiple components with scope "general"
    When the developer runs "/factory install --all --scope general"
    Then all general-scoped components are installed to ".claude/"
    And no domain-specific components are installed

  Scenario: Dependency resolution installs transitive requirements
    Given component "A" declares component "B" as a dependency in its meta.yaml
    When the developer runs "/factory install A"
    Then both "A" and "B" are installed to the target location
    And the output lists both components as installed

  Scenario: Skip install when target content is identical
    Given "dev-explore" is already installed at "~/.claude/skills/dev-explore/SKILL.md"
    And the installed file content is identical to the factory source
    When the developer runs "/factory install dev-explore --global"
    Then the file is not overwritten
    And no output is shown for that file

  Scenario: Prompt user when installed file differs from factory source
    Given "dev-explore" is already installed at "~/.claude/skills/dev-explore/SKILL.md"
    And the installed file content differs from the factory source
    When the developer runs "/factory install dev-explore --global"
    Then a diff of the changes is shown
    And the developer is prompted to overwrite or skip

  Scenario: Installed but unused global components add zero context cost
    Given multiple components are installed to "~/.claude/skills/"
    When the developer starts a new Claude Code session without invoking those skills
    Then none of the installed skill bodies appear in the active context
    And only skill descriptions are loaded as part of the session


Feature: Component promotion
  The factory gateway promotes a component from a domain project into the
  factory repo, validating conventions and checking for domain-context leaks

  Background:
    Given the factory gateway is installed at "~/.claude/commands/factory.md"
    And the developer is working in a domain project with a candidate component

  Scenario: Promote a clean general-purpose component
    Given a skill file at "~/workspace/proj/.claude/skills/foo/SKILL.md"
    And the file has valid frontmatter with name and description fields
    And the file contains no hardcoded domain-specific paths or product references
    When the developer runs "/factory promote ~/workspace/proj/.claude/skills/foo"
    Then the skill is copied to "components/skills/foo/" in the factory repo
    And a "meta.yaml" is generated with scope "general"
    And "registry.yaml" is updated with the new component entry
    And the output confirms what was promoted

  Scenario: Flag domain-context violations during promotion
    Given a skill file that contains hardcoded references to a specific app name
    And the file uses a fixed output path not derived from codebase inspection
    When the developer runs "/factory promote" on that file
    Then each domain-leak violation is listed with the offending line
    And the developer is asked whether to refactor or classify the component as domain-specific

  Scenario: Promote a domain-specific component without refactoring
    Given a skill that cannot be generalized without losing its purpose
    When the developer runs "/factory promote ./phi-guardian --scope domain-specific --domain chiro"
    Then the skill is copied to "components/domain/chiro/skills/phi-guardian/"
    And the generated "meta.yaml" reflects scope "domain-specific" and domain "chiro"
    And no context-separation warnings are emitted


Feature: Registry management
  The factory gateway keeps the registry current, detects drift between installed
  components and the factory source, and can rebuild from component metadata

  Background:
    Given the factory gateway is installed at "~/.claude/commands/factory.md"
    And the factory repo has a "components/" directory with "meta.yaml" files

  Scenario: Detect stale installed components
    Given one or more components installed in "~/.claude/" have older content than the factory source
    When the developer runs "/factory check"
    Then each stale component is listed by name
    And the output suggests the exact "/factory install <name> --global" command to update

  Scenario: Update all stale global components
    Given "/factory check" has identified stale components in "~/.claude/"
    When the developer runs "/factory update --all --global"
    Then each stale component is re-installed from the factory source
    And identical components are skipped silently
    And conflicting components prompt for confirmation before overwriting

  Scenario: Rebuild registry from component metadata files
    Given "meta.yaml" files exist under "components/" for all components
    When the developer runs "/factory rebuild-registry"
    Then "registry.yaml" is regenerated from all "meta.yaml" sources
    And the output reports the component count by type and scope

  @wip
  Scenario: Uninstall a component
    Given a component is installed in ".claude/" or "~/.claude/"
    When the developer runs "/factory uninstall <name>"
    Then the component files are removed from the install target
    And "registry.yaml" is not modified

  @wip
  Scenario: Self-update the factory gateway
    Given the factory gateway file at "~/.claude/commands/factory.md" is older than the factory source
    When the developer runs "/factory self-update"
    Then the gateway file is overwritten with the current factory version
    And the output confirms the update


Feature: Project bootstrap
  A developer can go from a brand-new project to a fully tooled environment
  in under two minutes using the factory gateway

  Scenario: Bootstrap a new project with the full general-purpose toolkit
    Given I am in a brand-new project directory with no ".claude/" folder
    And the factory gateway is installed at "~/.claude/commands/factory.md"
    When the developer runs "/factory install --all --scope general"
    Then all general-purpose skills, agents, and commands are available in the project
    And the setup completes in under two minutes
    And starting Claude Code in the project produces no context budget warnings
```
