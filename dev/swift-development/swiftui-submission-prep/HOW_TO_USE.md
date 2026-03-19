# How to Use This Skill

Hey Claude—I just added the "swiftui-submission-prep" skill. Can you review my SwiftUI app for App Store submission readiness?

## Example Invocations

**Example 1: Initial Submission Review**
```
Hey Claude—I just added the "swiftui-submission-prep" skill. Can you analyze my iOS fitness tracking app and tell me if it's ready for App Store submission? The app tracks workouts, uses HealthKit, and has a freemium model with in-app purchases.
```

**Example 2: Post-Rejection Analysis**
```
Hey Claude—I just added the "swiftui-submission-prep" skill. My app was rejected for guideline 2.1 (incomplete app information). Can you review the app metadata and Info.plist to identify what might have caused the rejection?
```

**Example 3: Focused Code Quality Review**
```
Hey Claude—I just added the "swiftui-submission-prep" skill. Can you specifically review the SwiftUI code architecture and state management patterns in my app? I want to ensure I'm following best practices before submission.
```

**Example 4: Metadata and Compliance Check**
```
Hey Claude—I just added the "swiftui-submission-prep" skill. Can you review my App Store Connect metadata, screenshots, and privacy policy to ensure everything is compliant with Apple's guidelines?
```

**Example 5: Pre-Submission Checklist**
```
Hey Claude—I just added the "swiftui-submission-prep" skill. I'm planning to submit tomorrow. Can you generate a comprehensive readiness report with a prioritized action items checklist?
```

## What to Provide

For the most comprehensive review, share:

### Essential Information
- **App description**: What does your app do? Who is it for?
- **Monetization model**: Free, paid, freemium, subscriptions, ads?
- **Target platforms**: iOS, iPadOS, macOS, visionOS? Which versions?
- **Key features**: Main functionality and user workflows

### Code and Configuration
- SwiftUI view files (especially main views and navigation structure)
- Info.plist file (usage description strings, capabilities)
- Entitlements file (if using special capabilities)
- Package dependencies (Package.swift or Podfile)
- Any files related to in-app purchases, subscriptions, or payments

### Metadata (if available)
- App Store Connect metadata (name, subtitle, description, keywords)
- Screenshots and preview videos
- Privacy policy URL
- Support URL and contact information

### Known Concerns (optional)
- Previous rejection reasons (if resubmitting)
- Specific guidelines you're unsure about
- Features you think might be risky

## What You'll Get

### Detailed Submission Readiness Report

A comprehensive report with these sections:

1. **Executive Summary**
   - Overall readiness status (Ready / Needs Work / Not Ready)
   - Count of critical, high, medium, and low priority issues
   - Estimated time to address issues

2. **App Store Review Guidelines Compliance**
   - Section-by-section analysis (Safety, Performance, Business, Design, Legal)
   - Specific guideline violations or warnings
   - Required actions with guideline references

3. **SwiftUI Code Quality & Architecture**
   - Best practices compliance
   - State management patterns
   - Performance considerations
   - Accessibility implementation
   - Deprecated API usage

4. **Metadata Readiness**
   - App name, subtitle, keywords analysis
   - Description compliance and effectiveness
   - Screenshot and preview requirements
   - Privacy policy and support URL validation

5. **Testing Coverage Assessment**
   - Device and version compatibility
   - Edge cases and error scenarios
   - Network condition handling
   - Accessibility testing recommendations

6. **Prioritized Action Items Checklist**
   - Critical blockers (must fix)
   - High priority (strongly recommended)
   - Medium priority (best practices)
   - Low priority (nice-to-have)

### Clear Next Steps

You'll know exactly:
- What must be fixed before submitting
- What should be tested
- What metadata needs updating
- How to reduce rejection risk

## Tips for Best Results

1. **Share Code Context**: Even if you can't share entire codebase, sharing key views and Info.plist helps identify issues

2. **Be Honest About Features**: Mention any features that might be borderline (e.g., user-generated content, health data, cryptocurrency)

3. **Mention Your Timeline**: If you have a launch deadline, mention it so the review can prioritize critical issues

4. **Previous Rejections**: If you've been rejected before, share the exact rejection reason from App Store Connect

5. **Ask Follow-Up Questions**: If any part of the report is unclear, ask for clarification or examples

## Common Use Cases

- **First-time submission**: Get a comprehensive pre-flight check
- **Resubmission after rejection**: Understand what went wrong and how to fix it
- **Major update**: Ensure new features don't introduce compliance issues
- **Guideline uncertainty**: Clarify whether a specific feature is allowed
- **Code quality audit**: Verify SwiftUI best practices before submission
- **Metadata optimization**: Improve discoverability while staying compliant

## What This Skill Does NOT Do

- Does not submit your app (you still use App Store Connect)
- Does not guarantee approval (Apple makes final decision)
- Does not execute or test your app (static analysis only)
- Does not scan compiled binary for private APIs (Xcode does this)
- Does not generate screenshots or metadata content

This skill helps you prepare and review—the actual submission is still your responsibility through App Store Connect.
