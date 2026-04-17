# View Composition

Building clean, reusable SwiftUI views with proper modifier ordering and composition.

## View Structure

### Basic Pattern

```swift
struct FeatureCard: View {
    // MARK: - Properties
    let title: String
    let subtitle: String
    let iconName: String

    // MARK: - Environment
    @Environment(\.colorScheme) private var colorScheme

    // MARK: - State
    @State private var isPressed = false

    // MARK: - Body
    var body: some View {
        HStack(spacing: 16) {
            iconView
            textContent
            Spacer()
            chevron
        }
        .padding()
        .background(cardBackground)
        .clipShape(RoundedRectangle(cornerRadius: 12))
        .contentShape(Rectangle())
    }

    // MARK: - Subviews
    private var iconView: some View {
        Image(systemName: iconName)
            .font(.title2)
            .foregroundStyle(.accent)
            .frame(width: 44, height: 44)
            .background(Color.accentColor.opacity(0.1))
            .clipShape(Circle())
    }

    private var textContent: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(title)
                .font(.headline)
            Text(subtitle)
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
    }

    private var chevron: some View {
        Image(systemName: "chevron.right")
            .font(.caption.weight(.semibold))
            .foregroundStyle(.tertiary)
    }

    private var cardBackground: some View {
        RoundedRectangle(cornerRadius: 12)
            .fill(Color(uiColor: .secondarySystemBackground))
    }
}
```

## Modifier Ordering

Order matters. The general pattern:

```swift
Text("Hello")
    // 1. Content modifiers (font, color)
    .font(.headline)
    .foregroundStyle(.primary)

    // 2. Layout modifiers (padding, frame)
    .padding()
    .frame(maxWidth: .infinity, alignment: .leading)

    // 3. Background/border
    .background(Color.blue)
    .clipShape(RoundedRectangle(cornerRadius: 8))

    // 4. Effects (shadow, opacity)
    .shadow(radius: 4)

    // 5. Gestures/interactions
    .onTapGesture { }

    // 6. Animation
    .animation(.default, value: someValue)
```

### Common Mistakes

```swift
// Wrong: padding after background
Text("Hello")
    .background(Color.blue)
    .padding()  // Blue box doesn't include padding

// Right: padding before background
Text("Hello")
    .padding()
    .background(Color.blue)  // Blue box includes padding
```

## Custom View Modifiers

### Creating Modifiers

```swift
struct CardStyle: ViewModifier {
    let cornerRadius: CGFloat

    func body(content: Content) -> some View {
        content
            .padding()
            .background(Color(uiColor: .secondarySystemBackground))
            .clipShape(RoundedRectangle(cornerRadius: cornerRadius))
            .shadow(color: .black.opacity(0.1), radius: 8, y: 4)
    }
}

extension View {
    func cardStyle(cornerRadius: CGFloat = 12) -> some View {
        modifier(CardStyle(cornerRadius: cornerRadius))
    }
}

// Usage
Text("Content")
    .cardStyle()
```

### Conditional Modifiers

```swift
extension View {
    @ViewBuilder
    func `if`<Content: View>(
        _ condition: Bool,
        transform: (Self) -> Content
    ) -> some View {
        if condition {
            transform(self)
        } else {
            self
        }
    }
}

// Usage
Text("Hello")
    .if(isHighlighted) { view in
        view.foregroundStyle(.accent)
    }
```

## ViewBuilder Patterns

### Custom Containers

```swift
struct Section<Content: View>: View {
    let title: String
    @ViewBuilder let content: () -> Content

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text(title)
                .font(.headline)
                .foregroundStyle(.secondary)

            content()
        }
    }
}

// Usage
Section(title: "Settings") {
    Toggle("Notifications", isOn: $notifications)
    Toggle("Dark Mode", isOn: $darkMode)
}
```

### Generic Views

```swift
struct ItemList<Item: Identifiable, Content: View>: View {
    let items: [Item]
    @ViewBuilder let content: (Item) -> Content

    var body: some View {
        LazyVStack(spacing: 8) {
            ForEach(items) { item in
                content(item)
            }
        }
    }
}
```

## Preview Patterns

```swift
#Preview {
    FeatureCard(
        title: "Notifications",
        subtitle: "Manage your alerts",
        iconName: "bell.fill"
    )
    .padding()
}

#Preview("Dark Mode") {
    FeatureCard(
        title: "Notifications",
        subtitle: "Manage your alerts",
        iconName: "bell.fill"
    )
    .padding()
    .preferredColorScheme(.dark)
}

#Preview("Large Text") {
    FeatureCard(
        title: "Notifications",
        subtitle: "Manage your alerts",
        iconName: "bell.fill"
    )
    .padding()
    .environment(\.sizeCategory, .accessibilityExtraLarge)
}
```

## Component Organization

### File Structure

```
Views/
├── Components/
│   ├── Buttons/
│   │   ├── PrimaryButton.swift
│   │   └── SecondaryButton.swift
│   ├── Cards/
│   │   ├── FeatureCard.swift
│   │   └── ProfileCard.swift
│   └── Inputs/
│       ├── SearchField.swift
│       └── FormField.swift
├── Screens/
│   ├── Home/
│   │   ├── HomeView.swift
│   │   └── HomeViewModel.swift
│   └── Settings/
│       ├── SettingsView.swift
│       └── SettingsViewModel.swift
└── Shared/
    ├── ViewModifiers/
    └── Extensions/
```

### Naming Conventions

```swift
// Views end with View or descriptive name
struct ProfileView: View { }
struct FeatureCard: View { }
struct PrimaryButton: View { }

// ViewModels end with ViewModel
class ProfileViewModel: ObservableObject { }

// Modifiers describe what they do
struct CardStyle: ViewModifier { }
struct ShimmerEffect: ViewModifier { }
```

## Best Practices

1. **Extract Subviews** - If body exceeds ~20 lines, extract computed properties
2. **Use Semantic Colors** - `Color.primary`, not `Color.black`
3. **Prefer Built-in Components** - Use `List`, `Form`, `NavigationStack` over custom
4. **Document Complex Views** - Add comments for non-obvious logic
5. **Test with Previews** - Multiple previews for different states/configurations
