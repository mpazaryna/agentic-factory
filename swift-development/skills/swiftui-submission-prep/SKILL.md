---
name: swiftui-submission-prep
description: Reviews SwiftUI apps for App Store submission readiness by analyzing guidelines compliance, code quality, metadata, and testing coverage
---

# SwiftUI App Store Submission Preparation

This skill provides comprehensive analysis of SwiftUI-based iOS and macOS applications to ensure they meet Apple App Store Review Guidelines and submission requirements. It delivers detailed reports covering compliance, code quality, metadata readiness, and testing coverage.

## Capabilities

- **App Store Review Guidelines Compliance**: Thorough review against Apple's latest guidelines including privacy, permissions, in-app purchases, content policies, and prohibited functionality
- **SwiftUI Code Quality & Architecture**: Analysis of SwiftUI best practices, view composition, state management, data flow, performance patterns, and architectural decisions
- **Metadata Readiness**: Evaluation of App Store Connect metadata including app description, keywords, screenshots, privacy policy, and support information
- **Testing Coverage Assessment**: Review of edge cases, error handling, network conditions, device compatibility, and quality assurance gaps
- **Actionable Recommendations**: Prioritized list of required fixes, suggested improvements, and best practice enhancements

## Input Requirements

To perform a comprehensive review, provide:

### Code Access
- SwiftUI source code files (views, models, view models)
- Info.plist and entitlements files
- Configuration files (build settings, capabilities)
- Third-party dependencies list (Package.swift, Podfile, etc.)

### App Information
- App description and intended functionality
- Target platforms (iOS, iPadOS, macOS, visionOS versions)
- Key features and user workflows
- Monetization approach (free, paid, subscriptions, IAP)
- Categories and intended audience

### Current State
- Known issues or concerns
- Previous rejection reasons (if resubmitting)
- Development/testing environment details

## Output Format

The skill generates a **detailed submission readiness report** structured as:

### Executive Summary
- Overall readiness assessment (Ready / Needs Work / Not Ready)
- Critical blockers count
- High-priority issues count
- Estimated time to submission readiness

### Section 1: App Store Review Guidelines Compliance
For each guideline category:
- **Status**: Pass / Warning / Fail
- **Findings**: Specific compliance issues identified
- **Guidelines Referenced**: Exact guideline numbers (e.g., 2.1, 5.1.1)
- **Required Actions**: What must be fixed before submission
- **Risk Level**: Critical / High / Medium / Low

Key areas reviewed:
- Safety (1.x): Objectionable content, user-generated content, kids category
- Performance (2.x): App completeness, beta features, accurate metadata
- Business (3.x): Payments, subscriptions, in-app purchases, advertising
- Design (4.x): Copycats, extensions, widgets, Apple Watch
- Legal (5.x): Privacy, data collection, intellectual property

### Section 2: Code Quality & Architecture Review
- **SwiftUI Best Practices**: View composition, modifiers, state management
- **State Management**: @State, @Binding, @StateObject, @ObservedObject, @EnvironmentObject usage
- **Data Flow**: MVVM implementation, data consistency, update patterns
- **Performance**: View update efficiency, lazy loading, memory management
- **Accessibility**: VoiceOver support, Dynamic Type, accessibility identifiers
- **Code Organization**: File structure, naming conventions, reusability
- **Error Handling**: User-facing error messages, graceful failures
- **Deprecated APIs**: Usage of deprecated SwiftUI features

### Section 3: Metadata Readiness
- **App Name**: Length, trademark issues, clarity
- **Subtitle**: Effectiveness, keyword usage (30 characters)
- **Keywords**: Optimization, relevance, competition analysis
- **Description**: Clarity, feature highlights, compliance with guidelines
- **Screenshots**: Required sizes, messaging, compliance
- **Preview Video**: Quality, length, content appropriateness (if applicable)
- **Privacy Policy**: Accessibility, completeness, accuracy
- **Support URL**: Functionality, help content quality
- **Age Rating**: Accuracy based on content
- **App Category**: Primary and secondary selection appropriateness

### Section 4: Testing Coverage Assessment
- **Device Compatibility**: Testing across iPhone, iPad, Mac (as applicable)
- **iOS Version Compatibility**: Minimum version testing, API availability
- **Edge Cases**: Empty states, maximum data, offline mode, permissions denied
- **Network Conditions**: Poor connectivity, offline, timeout handling
- **Error Scenarios**: Invalid input, server errors, authentication failures
- **Accessibility Testing**: VoiceOver navigation, Dynamic Type scaling
- **Performance Testing**: Launch time, memory usage, battery impact
- **Localization**: If supporting multiple languages

### Action Items Checklist
Prioritized list of tasks:
- [ ] **CRITICAL**: Must fix before submission
- [ ] **HIGH**: Strongly recommended, may cause rejection
- [ ] **MEDIUM**: Best practices, improves approval chances
- [ ] **LOW**: Nice-to-have improvements

## How to Use

Invoke this skill when preparing to submit your SwiftUI app to the App Store:

"Review my SwiftUI app for App Store submission readiness"

"Check if my iOS app complies with Apple's latest App Store Review Guidelines"

"Analyze my app's metadata and identify any compliance issues before submission"

"What testing gaps should I address before submitting to the App Store?"

## Best Practices

1. **Run Early and Often**: Don't wait until the last minute before submission. Run this review during development milestones.

2. **Keep Guidelines Updated**: Apple updates their guidelines regularly. Ensure the review references the latest version.

3. **Address Critical Issues First**: Focus on blockers that will definitely cause rejection before polishing lower-priority items.

4. **Test on Real Devices**: Simulator testing is insufficient. Test on actual devices across your supported hardware.

5. **Review Privacy Declarations**: Ensure Info.plist usage descriptions match your actual data collection and App Store Connect privacy declarations.

6. **Document Monetization**: If using in-app purchases or subscriptions, ensure StoreKit implementation follows guidelines and restore purchases functionality works.

7. **Prepare Rejection Response**: Have a plan for how you'll address feedback if rejected, including timeline estimates.

## Review Methodology

The skill follows this systematic approach:

1. **Code Analysis**: Reviews SwiftUI code for patterns that commonly cause rejections (incomplete features, placeholder content, developer-facing UI)

2. **Guideline Mapping**: Maps app functionality to specific App Store Review Guidelines to identify potential violations

3. **Metadata Validation**: Checks that all required metadata is complete, accurate, and compliant

4. **Testing Gap Analysis**: Identifies scenarios that should be tested but may not have been covered

5. **Risk Assessment**: Prioritizes findings based on likelihood of rejection and severity

## Limitations

- **No Automated Testing**: This is a static review; it doesn't execute the app or run automated tests
- **Binary Review Not Included**: Does not examine compiled binary for private API usage (Xcode does this)
- **Guideline Interpretation**: Some guidelines are subjective; final decision rests with Apple's review team
- **No Guarantee**: Passing this review doesn't guarantee App Store approval
- **Point-in-Time**: Guidelines change frequently; always verify against Apple's current documentation
- **Context-Dependent**: Some evaluations require understanding business model and target audience

## Key References

This skill references:
- **App Store Review Guidelines**: https://developer.apple.com/app-store/review/guidelines/
- **Human Interface Guidelines**: https://developer.apple.com/design/human-interface-guidelines/
- **SwiftUI Best Practices**: Apple's official documentation and WWDC sessions
- **App Store Connect Help**: Metadata requirements and submission process

## Common Rejection Reasons Covered

- Incomplete app information or placeholder content
- Missing privacy policy or usage description strings
- Inaccurate metadata or misleading screenshots
- Crashes or bugs encountered during review
- Broken links or non-functional features
- Improper use of Apple trademarks or design
- Missing restore purchases functionality (for IAP apps)
- Inadequate age rating for content
- Privacy violations or unauthorized data collection
- Minimum functionality not met

## Version Compatibility

This skill is optimized for:
- SwiftUI (iOS 14+, macOS 11+, latest SwiftUI features)
- Xcode 14+ projects
- App Store Review Guidelines (current as of skill generation date)

Always verify against Apple's latest guidelines at submission time.
