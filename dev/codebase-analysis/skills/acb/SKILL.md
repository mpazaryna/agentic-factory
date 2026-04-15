---
name: acb
description: "Analyze Codebase — modular, template-driven codebase analysis that detects project type and generates comprehensive codebase_analysis.md. Use when the user wants a full codebase analysis, architecture overview, or onboarding document."
argument-hint: "<folder-path>"
allowed-tools: Bash, Read, Write
disable-model-invocation: false
---

# Analyze Codebase (Modular Templates)

Follow the Workflow for the `FOLDER_PATH` then Report the completed work.

## Variables

FOLDER_PATH: $ARGUMENTS

## Workflow

If no `FOLDER_PATH` is provided, STOP immediately and ask the user to provide it.

### Step 1: Project Detection & Template Loading

1. Scan for key indicator files in the target directory
2. Load base analysis template from `${CLAUDE_SKILL_DIR}/templates/base.md`
3. Load technology-specific templates based on detection
4. Merge templates into comprehensive analysis structure

### Step 2: Technology Detection Logic

Detect project types by scanning for these files:
- **MCP Server**: `package.json` contains `@modelcontextprotocol/sdk`
- **Next.js**: `next.config.js` or `next.config.ts` exists
- **Cloudflare Worker**: `wrangler.toml` or `wrangler.jsonc` exists
- **React App**: `package.json` contains `react`
- **TypeScript**: `tsconfig.json` exists
- **Jest Testing**: `jest.config.js` or `jest.config.cjs` exists
- **iOS App**: `Package.swift` or `*.xcodeproj` exists
- **Python**: `requirements.txt` or `pyproject.toml` exists

### Step 3: Template Integration

**Base Template**: Always include `${CLAUDE_SKILL_DIR}/templates/base.md`

**Technology Templates** (include if detected):
- MCP Server → `${CLAUDE_SKILL_DIR}/templates/mcp-server.md`
- Cloudflare Workers → `${CLAUDE_SKILL_DIR}/templates/cloudflare-worker.md`
- TypeScript → `${CLAUDE_SKILL_DIR}/templates/typescript.md`
- Jest → `${CLAUDE_SKILL_DIR}/templates/jest-testing.md`
- iOS → `${CLAUDE_SKILL_DIR}/templates/ios-swift.md`
- Android → `${CLAUDE_SKILL_DIR}/templates/android-kotlin.md`

### Step 4: Execute Comprehensive Analysis

Using the merged template structure, analyze:
1. Project Overview
2. Technology-Specific Analysis
3. Directory Structure Analysis
4. File-by-File Breakdown
5. Architecture Deep Dive
6. Testing Analysis
7. Deployment Analysis
8. Technology Stack Breakdown
9. Visual Architecture Diagram
10. Key Insights & Recommendations

### Step 5: Create Analysis Document

Create `codebase_analysis.md` with detected technologies, integration analysis, and tech-specific recommendations.
