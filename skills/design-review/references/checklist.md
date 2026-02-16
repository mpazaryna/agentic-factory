# Design Checklist

General design quality review before shipping.

## Visual Consistency

### Typography
- [ ] Font families match design system
- [ ] Type scale is consistent (no random sizes)
- [ ] Line heights are appropriate
- [ ] Letter spacing is intentional
- [ ] No orphans/widows in key text

### Color
- [ ] Colors match defined palette
- [ ] Semantic colors used correctly (error=red, etc.)
- [ ] Dark mode colors are appropriate (not inverted)
- [ ] No random hex values outside system

### Spacing
- [ ] Spacing uses defined scale
- [ ] Consistent margins/padding
- [ ] Related elements grouped tightly
- [ ] Unrelated elements have clear separation

### Borders & Shadows
- [ ] Border radii are consistent
- [ ] Shadow elevation follows system
- [ ] Border colors match palette
- [ ] No inconsistent border widths

## Component Quality

### Buttons
- [ ] Primary/secondary hierarchy clear
- [ ] Hover states defined
- [ ] Active/pressed states defined
- [ ] Disabled states defined
- [ ] Loading states defined
- [ ] Touch targets meet minimum (44pt)

### Forms
- [ ] Labels visible and associated
- [ ] Placeholder text appropriate
- [ ] Focus states visible
- [ ] Error states clear
- [ ] Success states clear
- [ ] Required fields indicated

### Cards
- [ ] Consistent padding
- [ ] Proper visual hierarchy
- [ ] Hover states (if interactive)
- [ ] Loading states (skeleton)

### Navigation
- [ ] Active state clear
- [ ] Hover states defined
- [ ] Mobile navigation works
- [ ] Focus states visible

## States & Feedback

### Loading
- [ ] Loading indicators present
- [ ] Skeleton screens for content
- [ ] Progress indicators for long operations
- [ ] No layout shift when content loads

### Empty States
- [ ] Empty states designed (not blank)
- [ ] Helpful guidance provided
- [ ] Action available if applicable

### Error States
- [ ] Error messages are helpful
- [ ] Recovery path is clear
- [ ] Errors don't break layout
- [ ] Form errors highlight fields

### Success States
- [ ] Confirmation provided for actions
- [ ] Success messages are clear
- [ ] Next steps indicated if applicable

## Responsive Design

### Breakpoints
- [ ] Mobile layout works (320px)
- [ ] Tablet layout works (768px)
- [ ] Desktop layout works (1024px+)
- [ ] No horizontal scroll at any size

### Content Adaptation
- [ ] Text remains readable at all sizes
- [ ] Images scale appropriately
- [ ] Navigation adapts to mobile
- [ ] Touch targets adequate on mobile

### Testing
- [ ] Tested on real devices
- [ ] Tested at 200% zoom
- [ ] Tested with Dynamic Type (iOS)
- [ ] Tested in landscape orientation

## Dark Mode

### Colors
- [ ] Background is dark gray, not black
- [ ] Text is off-white, not pure white
- [ ] Elevation shown via surface lightness
- [ ] Semantic colors adjusted for dark

### Images
- [ ] Images work on dark background
- [ ] Icons visible on dark background
- [ ] No harsh contrast issues

### Consistency
- [ ] All screens support dark mode
- [ ] No white flashes during transitions
- [ ] System preference respected

## Cross-Platform (if applicable)

### iOS
- [ ] Follows Human Interface Guidelines
- [ ] Standard controls used where appropriate
- [ ] Safe area respected
- [ ] Dynamic Type supported

### Android
- [ ] Follows Material Design guidelines
- [ ] Edge-to-edge supported
- [ ] System bars handled correctly

### Web
- [ ] Works in Chrome, Safari, Firefox
- [ ] Keyboard navigation works
- [ ] Screen reader accessible

## Final Polish

### Micro-interactions
- [ ] Button feedback is responsive
- [ ] Transitions are smooth
- [ ] No janky animations
- [ ] Loading doesn't feel slow

### Copy
- [ ] No lorem ipsum
- [ ] No spelling errors
- [ ] Tone is consistent
- [ ] Labels are clear

### Edge Cases
- [ ] Long text handled (truncation/wrapping)
- [ ] Missing images handled (placeholder)
- [ ] Slow network handled
- [ ] Offline state handled (if applicable)

## Pre-Launch Review

### Stakeholder Sign-off
- [ ] Design team approved
- [ ] Product owner approved
- [ ] QA completed testing
- [ ] Accessibility reviewed

### Documentation
- [ ] Design system updated
- [ ] Component documentation current
- [ ] Release notes prepared

### Monitoring
- [ ] Analytics tracking in place
- [ ] Error tracking configured
- [ ] Performance monitoring ready
