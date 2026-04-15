# Accessibility

SwiftUI accessibility patterns for VoiceOver, Dynamic Type, and inclusive design.

## Accessibility Modifiers

### Labels and Hints

```swift
// Simple label
Image(systemName: "heart.fill")
    .accessibilityLabel("Favorite")

// Label with hint
Button(action: toggleFavorite) {
    Image(systemName: isFavorite ? "heart.fill" : "heart")
}
.accessibilityLabel(isFavorite ? "Remove from favorites" : "Add to favorites")
.accessibilityHint("Double tap to toggle")

// Combined label
HStack {
    Text("$")
    Text("99.99")
}
.accessibilityElement(children: .combine)
.accessibilityLabel("Price: 99 dollars and 99 cents")
```

### Hiding Decorative Elements

```swift
// Hide from VoiceOver
Image("decorative-background")
    .accessibilityHidden(true)
```

### Grouping Elements

```swift
// Combine children into single element
HStack {
    Image(systemName: "star.fill")
    Text("4.5")
    Text("(128 reviews)")
}
.accessibilityElement(children: .combine)

// Ignore children, provide custom label
VStack {
    Text("John Doe")
    Text("Software Engineer")
}
.accessibilityElement(children: .ignore)
.accessibilityLabel("John Doe, Software Engineer")
```

## Accessibility Traits

```swift
Text("Welcome")
    .accessibilityAddTraits(.isHeader)

// Multiple traits
Text("Important Notice")
    .accessibilityAddTraits([.isHeader, .isStaticText])
```

### Common Traits

| Trait | Use Case |
|-------|----------|
| `.isHeader` | Section headings |
| `.isButton` | Tappable elements |
| `.isLink` | Navigation links |
| `.isImage` | Images with meaning |
| `.isSelected` | Selected state |
| `.updatesFrequently` | Live data |

## Custom Actions

```swift
struct MessageRow: View {
    var body: some View {
        HStack {
            Text(message.content)
        }
        .accessibilityAction(named: "Delete") { onDelete() }
        .accessibilityAction(named: "Reply") { onReply() }
    }
}
```

## Dynamic Type

```swift
// Use built-in text styles (automatically scale)
Text("Headline").font(.headline)
Text("Body text").font(.body)

// Custom font with scaling
Text("Custom")
    .font(.custom("Avenir", size: 18, relativeTo: .body))

// Limit scaling range
Text("Limited")
    .dynamicTypeSize(.medium ... .xxxLarge)
```

### Scaled Metrics

```swift
struct ScaledView: View {
    @ScaledMetric(relativeTo: .body) var iconSize: CGFloat = 24

    var body: some View {
        Image(systemName: "star")
            .font(.system(size: iconSize))
    }
}
```

### Adaptive Layouts

```swift
struct AdaptiveCard: View {
    @Environment(\.dynamicTypeSize) var dynamicTypeSize

    var body: some View {
        if dynamicTypeSize.isAccessibilitySize {
            VStack(alignment: .leading) { content }
        } else {
            HStack { content }
        }
    }
}
```

## Reduce Motion

```swift
struct AnimatedView: View {
    @Environment(\.accessibilityReduceMotion) var reduceMotion

    func toggle() {
        if reduceMotion {
            isExpanded.toggle()
        } else {
            withAnimation(.spring()) {
                isExpanded.toggle()
            }
        }
    }
}
```

## VoiceOver Announcements

```swift
// Announce changes
UIAccessibility.post(
    notification: .announcement,
    argument: "Item added to cart"
)
```

## Testing Checklist

- [ ] All interactive elements have labels
- [ ] Reading order makes sense
- [ ] Headers marked correctly
- [ ] Text uses semantic styles
- [ ] Layouts adapt to larger sizes
- [ ] Reduce Motion respected
- [ ] Color not sole indicator
- [ ] Minimum contrast met (4.5:1)
