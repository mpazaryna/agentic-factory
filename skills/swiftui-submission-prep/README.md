# SwiftUI App Store Submission Prep

**Version:** 1.0.0
**Type:** Prompt-based skill (no Python required)
**Focus:** iOS/macOS SwiftUI app review for App Store compliance

## Overview

This Claude skill provides comprehensive pre-submission review of SwiftUI-based apps for Apple App Store readiness. It analyzes your app against four critical dimensions:

1. **App Store Review Guidelines Compliance** - Ensures adherence to Apple's latest submission policies
2. **SwiftUI Code Quality & Architecture** - Reviews best practices and patterns
3. **Metadata Readiness** - Validates App Store Connect information completeness
4. **Testing Coverage** - Identifies gaps in QA and edge case handling

## What This Skill Does

- Reviews code, configuration, and metadata for compliance issues
- Maps app features to specific App Store Review Guidelines
- Identifies common rejection reasons before submission
- Generates prioritized action items checklist
- Provides clear, actionable recommendations
- Delivers detailed readiness report with risk assessment

## When to Use This Skill

- **Pre-submission review**: Before uploading to App Store Connect
- **Post-rejection analysis**: Understanding why an app was rejected
- **Major updates**: Ensuring new features don't introduce compliance issues
- **Code quality audit**: Verifying SwiftUI best practices
- **Metadata optimization**: Improving discoverability while staying compliant

## Installation

### For Claude Desktop (macOS/Windows)
1. Download `swiftui-submission-prep.zip`
2. Drag and drop the ZIP file into Claude Desktop
3. Skill will be automatically installed and available

### For Claude Code (CLI)
```bash
# Copy skill folder to Claude skills directory
cp -r swiftui-submission-prep ~/.claude/skills/

# Or install from this directory
ln -s "$(pwd)/swiftui-submission-prep" ~/.claude/skills/
```

### For Claude Apps (Browser)
1. Use the `skill-creator` skill to import `swiftui-submission-prep.zip`
2. Follow the import wizard
3. Skill will be available in your current project

## Quick Start

After installation, invoke the skill:

```
Hey Claude—I just added the "swiftui-submission-prep" skill. Can you review my SwiftUI app for App Store submission readiness?
```

### What to Provide

For best results, share:
- App description and key features
- SwiftUI source files (especially main views)
- Info.plist and entitlements
- App Store Connect metadata (name, description, keywords, screenshots)
- Monetization details (IAP, subscriptions, ads)
- Known issues or concerns

### What You'll Get

A comprehensive report with:
- Overall readiness status (Ready / Needs Work / Not Ready)
- Compliance analysis by guideline section
- Code quality assessment
- Metadata validation
- Testing gap analysis
- Prioritized action items checklist (Critical → Low)

## Example Use Cases

**Example 1: First-Time Submission**
```
Hey Claude—I just added the "swiftui-submission-prep" skill. Can you analyze my productivity app? It uses CloudKit for sync, has in-app purchases for premium features, and targets iOS 16+.
```

**Example 2: Rejection Investigation**
```
Hey Claude—I just added the "swiftui-submission-prep" skill. My app was rejected for guideline 2.1 (incomplete app). Can you review the Info.plist and metadata to find the issue?
```

**Example 3: Code Quality Focus**
```
Hey Claude—I just added the "swiftui-submission-prep" skill. Can you specifically review my SwiftUI state management and architecture patterns before I submit?
```

## Files Included

```
swiftui-submission-prep/
├── SKILL.md                    # Main skill definition with review methodology
├── HOW_TO_USE.md              # Detailed usage examples and invocations
├── sample_input.json          # Example app data structure
├── expected_output.json       # Sample readiness report format
└── README.md                  # This file
```

## Key Features

### Comprehensive Guidelines Coverage

Reviews against all major guideline categories:
- **Safety (1.x)**: Content, UGC, kids apps
- **Performance (2.x)**: Completeness, beta testing, metadata accuracy
- **Business (3.x)**: Payments, IAP, subscriptions, advertising
- **Design (4.x)**: Copycats, extensions, widgets
- **Legal (5.x)**: Privacy, data collection, IP

### SwiftUI-Specific Analysis

- State management patterns (@State, @Binding, @StateObject, etc.)
- View composition and reusability
- Performance optimization (lazy loading, update efficiency)
- Accessibility implementation (VoiceOver, Dynamic Type)
- SwiftUI best practices compliance
- Deprecated API detection

### Prioritized Action Items

All findings are categorized:
- **Critical**: Must fix before submission (will cause rejection)
- **High**: Strongly recommended (likely to cause rejection)
- **Medium**: Best practices (improves approval chances)
- **Low**: Nice-to-have improvements

## Requirements

- SwiftUI-based app (iOS 14+, macOS 11+, or newer)
- App Store submission intent
- Access to app code, configuration, and metadata

## Limitations

- **Static analysis only**: Does not execute or compile your app
- **No binary inspection**: Does not scan for private API usage (Xcode does this)
- **Guideline interpretation**: Some guidelines are subjective; Apple makes final decision
- **No approval guarantee**: Passing this review doesn't guarantee App Store approval
- **Point-in-time**: Guidelines change frequently; always verify current Apple documentation

## Best Practices

1. **Run early**: Don't wait until submission day
2. **Address critical issues first**: Focus on blockers before polish
3. **Test on real devices**: Simulator is insufficient
4. **Keep guidelines current**: Reference Apple's latest documentation
5. **Prepare demo accounts**: For apps with authentication or paid features
6. **Document privacy**: Ensure Info.plist descriptions match reality

## Common Rejection Reasons Detected

- Incomplete app information
- Missing or inadequate privacy policy
- Inaccurate metadata or screenshots
- Missing usage description strings (Info.plist)
- Broken restore purchases functionality
- Crashes or non-functional features
- Privacy violations
- Improper age rating
- Placeholder or developer-facing content

## References

This skill is based on:
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- SwiftUI best practices from Apple documentation
- App Store Connect submission requirements

## Version History

**1.0.0** (2025-12-12)
- Initial release
- Comprehensive guideline compliance review
- SwiftUI code quality analysis
- Metadata validation
- Testing coverage assessment
- Prioritized action items

## Support

For questions or improvements to this skill:
1. Review the SKILL.md for detailed methodology
2. Check HOW_TO_USE.md for invocation examples
3. Examine sample_input.json and expected_output.json for format guidance

## License

This skill is provided as-is for use with Claude AI. Modify and distribute freely.

---

**Note**: This skill provides analysis and recommendations. The actual App Store submission must be done through App Store Connect. Always verify findings against Apple's current guidelines, as they change frequently.
