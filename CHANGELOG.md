# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of Agentic Factory
- Three specialized agents for code quality, documentation, and work summarization
  - `quality-control-enforcer` - Reviews code for quality issues and incomplete implementations
  - `research-docs-fetcher` - Fetches and organizes web documentation
  - `work-completion-summarizer` - Summarizes completed work
- Command structure with `paz/` namespace for organization
  - Prime commands for understanding codebases (`mcp_dev.md`, `web_dev.md`)
  - Learning resources (`acb.md`)
  - Context rebuilding commands (`rebuild_context.md`, `rebuild_readme.md`)
  - Tool-specific documentation (`playwright.md`)
- Comprehensive template system for project analysis
  - Base codebase analysis template
  - Technology-specific templates (TypeScript, Cloudflare Worker, Jest, MCP Server)
  - Mobile development templates (iOS Swift, Android Kotlin)
- `CLAUDE.md` file for Claude Code guidance
- Comprehensive README with installation instructions
- Inspired By section crediting CCPlugins, ContextKit, and IndyDevDan
- `.claude/` directory with meta-tooling for toolkit maintenance
  - `add-agent.md` command for creating new agents
  - `add-template.md` command for creating new templates
  - `toolkit-consistency-reviewer` agent for validating toolkit structure
- Sophisticated deployment system for managing toolkit distribution
  - `deploy.sh` script for deploying components to projects
  - `sync.sh` script for updating deployed components
  - `projects.json` index for tracking project deployments
  - Support for selective component deployment
  - Automatic tracking of deployment status and timestamps

### Changed
- Organized commands and templates under `paz/` namespace to support multiple toolkit collections

### Fixed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Security
- N/A

## [0.1.0] - TBD

Initial pre-release version for community testing and feedback.

[Unreleased]: https://github.com/[username]/agentic-factory/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/[username]/agentic-factory/releases/tag/v0.1.0