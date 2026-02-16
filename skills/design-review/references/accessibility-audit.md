# Accessibility Audit

Systematic accessibility review for WCAG 2.1 compliance.

## Quick Audit Checklist

### Perceivable
- [ ] Text has 4.5:1 contrast ratio (3:1 for large text)
- [ ] Images have alt text
- [ ] Video has captions
- [ ] Color is not the only indicator
- [ ] Content reflows at 400% zoom

### Operable
- [ ] All functions available via keyboard
- [ ] Focus indicator is visible
- [ ] No keyboard traps
- [ ] Touch targets are 44x44pt minimum
- [ ] Motion can be disabled

### Understandable
- [ ] Language is declared
- [ ] Labels are clear and descriptive
- [ ] Error messages explain how to fix
- [ ] Navigation is consistent

### Robust
- [ ] Valid HTML/semantic elements
- [ ] ARIA used correctly
- [ ] Works with screen readers
- [ ] Works at different text sizes

## Color Contrast

### WCAG Requirements

| Element | AA (minimum) | AAA (enhanced) |
|---------|--------------|----------------|
| Normal text (<18px) | 4.5:1 | 7:1 |
| Large text (≥18px bold, ≥24px) | 3:1 | 4.5:1 |
| UI components | 3:1 | — |
| Non-text (icons, charts) | 3:1 | — |

### Testing Tools
- **Web**: WebAIM Contrast Checker, Chrome DevTools
- **iOS**: Xcode Accessibility Inspector
- **Figma**: Stark plugin
- **General**: Contrast app (macOS)

### Common Failures
- Light gray text on white background
- Placeholder text with insufficient contrast
- Disabled states that are unreadable
- Focus indicators that blend in

## Screen Reader Testing

### VoiceOver (iOS/macOS)

**Enable**: Settings → Accessibility → VoiceOver

**Test Checklist**:
- [ ] All interactive elements are reachable
- [ ] Reading order makes logical sense
- [ ] Buttons and links announce their purpose
- [ ] Images announce descriptions
- [ ] Form fields announce labels
- [ ] Errors are announced
- [ ] Dynamic content changes are announced

**Common Issues**:
- Unlabeled buttons ("button" instead of "Submit")
- Images with no description or wrong description
- Form fields without associated labels
- Custom controls not announced correctly

### TalkBack (Android)

**Enable**: Settings → Accessibility → TalkBack

**Gestures**:
- Swipe right: Next element
- Swipe left: Previous element
- Double tap: Activate
- Swipe up then right: Next heading

### NVDA/JAWS (Windows)

**Quick Keys**:
- H: Next heading
- B: Next button
- F: Next form field
- T: Next table

## Keyboard Navigation

### Required Support

| Key | Expected Action |
|-----|-----------------|
| Tab | Move to next focusable element |
| Shift+Tab | Move to previous focusable element |
| Enter | Activate buttons, links |
| Space | Activate buttons, toggle checkboxes |
| Arrow keys | Navigate within components |
| Escape | Close modals, cancel |

### Test Checklist
- [ ] Can reach all interactive elements with Tab
- [ ] Focus order matches visual order
- [ ] Focus indicator is clearly visible
- [ ] No focus traps (can always Tab out)
- [ ] Skip links work (if present)
- [ ] Modal traps focus correctly
- [ ] Dropdown menus navigable with arrows

### Common Failures
- Custom buttons not focusable
- Hidden elements receiving focus
- Focus lost after modal closes
- Invisible focus indicators

## Touch Target Audit

### Minimum Sizes

| Platform | Minimum Size |
|----------|-------------|
| iOS (Apple HIG) | 44x44 pt |
| Android (Material) | 48x48 dp |
| Web (WCAG) | 44x44 CSS px |

### Test Method
1. Enable touch target visualization (dev tools)
2. Check all buttons, links, form controls
3. Verify spacing between targets (8px minimum)

### Common Failures
- Icon buttons without padding
- Close buttons in corners
- Links within paragraphs
- Form checkboxes/radios

## Dynamic Content

### Announcements
- [ ] Alerts are announced to screen readers
- [ ] Loading states communicate progress
- [ ] Error messages are announced
- [ ] Success confirmations are announced
- [ ] Page/view changes are announced

### Live Regions (Web)
```html
<div aria-live="polite">
  <!-- Content changes announced -->
</div>

<div aria-live="assertive">
  <!-- Urgent changes interrupt -->
</div>
```

### iOS Announcements
```swift
UIAccessibility.post(
    notification: .announcement,
    argument: "Item added to cart"
)
```

## Form Accessibility

### Labels
- [ ] Every input has a visible label
- [ ] Labels are programmatically associated
- [ ] Required fields are indicated
- [ ] Field format hints are provided

### Errors
- [ ] Error messages identify the field
- [ ] Error messages explain how to fix
- [ ] Errors are announced to screen readers
- [ ] Focus moves to first error

### Example (Web)
```html
<label for="email">Email address</label>
<input
  type="email"
  id="email"
  aria-describedby="email-error"
  aria-invalid="true"
>
<span id="email-error" role="alert">
  Please enter a valid email address
</span>
```

## Motion & Animation

### Reduce Motion Check
- [ ] `prefers-reduced-motion` is respected (web)
- [ ] `accessibilityReduceMotion` is respected (iOS)
- [ ] Essential animations still convey meaning
- [ ] Auto-playing content can be paused

### Implementation

**Web**:
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**iOS**:
```swift
@Environment(\.accessibilityReduceMotion) var reduceMotion

if !reduceMotion {
    withAnimation { /* ... */ }
}
```

## Audit Report Template

```markdown
# Accessibility Audit Report

**Product**: [Name]
**Date**: [Date]
**Auditor**: [Name]
**Standard**: WCAG 2.1 AA

## Summary
- Critical Issues: X
- Major Issues: X
- Minor Issues: X

## Critical Issues (Must Fix)
1. [Issue]: [Location]
   - Impact: [Who is affected]
   - Fix: [How to resolve]

## Major Issues (Should Fix)
...

## Minor Issues (Consider)
...

## Passed Criteria
- [List of passing checks]

## Testing Methodology
- Screen readers tested: VoiceOver, TalkBack
- Browsers tested: Chrome, Safari, Firefox
- Devices tested: iPhone 14, Pixel 7
```
