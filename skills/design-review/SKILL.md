---
name: design-review
description: Design audits and submission preparation. Use when reviewing designs for quality, checking accessibility compliance, or preparing for App Store submission.
---

# design-review

Systematic review and audit patterns for polishing designs before launch.

## Scope

This skill covers **review and submission**—the checklists, audits, and compliance checks needed before shipping. For implementation patterns, see `web-design` or `swift-ui`. For theory, see `design-principles`.

## Routing

Based on what you need reviewed, I'll reference the appropriate guide:

### App Store Submission
**When**: Preparing iOS/macOS app for App Store
**Reference**: `references/app-store.md`
- App Store Review Guidelines compliance
- Metadata readiness
- Common rejection reasons
- Submission checklist

### Accessibility Audit
**When**: Checking WCAG compliance, VoiceOver support
**Reference**: `references/accessibility-audit.md`
- WCAG 2.1 AA checklist
- Screen reader testing
- Color contrast verification
- Keyboard navigation audit

### Design Checklist
**When**: General design quality review
**Reference**: `references/checklist.md`
- Visual consistency audit
- Typography review
- Color system verification
- Component quality check

## Quick Audit

### Visual Consistency
- [ ] Typography scale is consistent
- [ ] Spacing uses defined scale
- [ ] Colors match system
- [ ] Border radii are consistent
- [ ] Shadows follow elevation system

### Accessibility Quick Check
- [ ] Color contrast meets 4.5:1 (text)
- [ ] Touch targets are 44pt minimum
- [ ] Focus states are visible
- [ ] Images have alt text
- [ ] Forms have labels

### App Store Quick Check
- [ ] No placeholder content
- [ ] No broken features
- [ ] Privacy policy accessible
- [ ] All permissions have usage strings
- [ ] Restore purchases works (if IAP)

## Review Methodology

1. **Systematic Pass** - Go through each checklist item
2. **Device Testing** - Test on real devices, not just simulators
3. **Edge Cases** - Empty states, error states, loading states
4. **Accessibility Testing** - VoiceOver/TalkBack, keyboard navigation
5. **Fresh Eyes** - Step away, return with fresh perspective

## Anti-Patterns

- Skipping device testing
- Ignoring accessibility until the end
- Not testing error states
- Rushing submission without checklist
- Assuming simulator = real device

## Related Skills

- **design-principles** - Theory behind good design
- **web-design** - Web implementation
- **swift-ui** - SwiftUI implementation
