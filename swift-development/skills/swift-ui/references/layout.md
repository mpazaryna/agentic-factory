# Layout Patterns

SwiftUI layout system: stacks, grids, geometry, and responsive patterns.

## Stack Layouts

### VStack, HStack, ZStack

```swift
// Vertical stack
VStack(alignment: .leading, spacing: 12) {
    Text("Title")
        .font(.headline)
    Text("Subtitle")
        .font(.subheadline)
        .foregroundStyle(.secondary)
}

// Horizontal stack
HStack(spacing: 16) {
    Image(systemName: "star.fill")
    Text("Featured")
    Spacer()
    Text("→")
}

// Layered stack
ZStack(alignment: .bottomTrailing) {
    Image("photo")
        .resizable()
        .aspectRatio(contentMode: .fill)

    Text("New")
        .padding(8)
        .background(.red)
        .foregroundStyle(.white)
        .clipShape(Capsule())
        .padding(8)
}
```

### Alignment

```swift
VStack(alignment: .leading) { }  // Leading edge
VStack(alignment: .center) { }   // Center (default)
VStack(alignment: .trailing) { } // Trailing edge

HStack(alignment: .top) { }      // Top edge
HStack(alignment: .center) { }   // Center (default)
HStack(alignment: .bottom) { }   // Bottom edge
HStack(alignment: .firstTextBaseline) { } // Text baseline
```

## LazyStacks

For large lists—only renders visible items.

```swift
ScrollView {
    LazyVStack(spacing: 16) {
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
    .padding()
}

// With pinned headers
ScrollView {
    LazyVStack(spacing: 0, pinnedViews: [.sectionHeaders]) {
        ForEach(sections) { section in
            Section {
                ForEach(section.items) { item in
                    ItemRow(item: item)
                }
            } header: {
                SectionHeader(title: section.title)
            }
        }
    }
}
```

## Grid Layouts

### LazyVGrid

```swift
let columns = [
    GridItem(.flexible()),
    GridItem(.flexible()),
    GridItem(.flexible())
]

ScrollView {
    LazyVGrid(columns: columns, spacing: 16) {
        ForEach(items) { item in
            GridCell(item: item)
        }
    }
    .padding()
}
```

### Adaptive Grid

```swift
let columns = [
    GridItem(.adaptive(minimum: 150, maximum: 200))
]

// Automatically fits as many columns as possible
LazyVGrid(columns: columns, spacing: 16) {
    ForEach(items) { item in
        GridCell(item: item)
    }
}
```

### Fixed Size Grid

```swift
let columns = [
    GridItem(.fixed(100)),
    GridItem(.fixed(100)),
    GridItem(.flexible())  // Takes remaining space
]
```

### Grid (iOS 16+)

```swift
Grid(alignment: .leading, horizontalSpacing: 12, verticalSpacing: 8) {
    GridRow {
        Text("Name")
            .gridColumnAlignment(.trailing)
        Text("John Doe")
    }
    GridRow {
        Text("Email")
        Text("john@example.com")
    }
    Divider()
        .gridCellColumns(2)  // Span all columns
    GridRow {
        Text("Status")
        Text("Active")
            .foregroundStyle(.green)
    }
}
```

## Frame and Alignment

```swift
// Fixed size
Text("Fixed")
    .frame(width: 200, height: 100)

// Flexible with max
Text("Flexible")
    .frame(maxWidth: .infinity, alignment: .leading)

// Ideal size
Image(systemName: "star")
    .frame(idealWidth: 44, idealHeight: 44)

// Min/max constraints
Text("Constrained")
    .frame(minWidth: 100, maxWidth: 300)
```

## GeometryReader

Access parent size and safe areas.

```swift
struct ResponsiveCard: View {
    var body: some View {
        GeometryReader { geometry in
            VStack {
                if geometry.size.width > 500 {
                    // Wide layout
                    HStack {
                        leadingContent
                        trailingContent
                    }
                } else {
                    // Narrow layout
                    VStack {
                        leadingContent
                        trailingContent
                    }
                }
            }
            .frame(width: geometry.size.width, height: geometry.size.height)
        }
    }
}
```

### Safe Area

```swift
GeometryReader { geometry in
    VStack {
        Text("Top safe area: \(geometry.safeAreaInsets.top)")
        Text("Bottom safe area: \(geometry.safeAreaInsets.bottom)")
    }
}
```

## Layout Priorities

Control which views shrink/grow first.

```swift
HStack {
    Text("Important")
        .layoutPriority(1)  // Resists compression

    Text("This text can be truncated if needed")
        .lineLimit(1)
        .layoutPriority(0)  // Default, will truncate first
}
```

## Spacers and Dividers

```swift
HStack {
    Text("Left")
    Spacer()           // Pushes apart
    Text("Right")
}

HStack {
    Text("A")
    Spacer(minLength: 20)  // At least 20pt
    Text("B")
}

VStack {
    Text("Above")
    Divider()          // Horizontal line
    Text("Below")
}
```

## Padding

```swift
// All edges
Text("Padded")
    .padding()         // System default (~16pt)
    .padding(20)       // Custom amount

// Specific edges
Text("Padded")
    .padding(.horizontal, 16)
    .padding(.vertical, 8)
    .padding(.top, 24)
    .padding(.leading, 12)

// Edge set
Text("Padded")
    .padding([.top, .bottom], 16)
```

## Safe Area

```swift
// Ignore safe area
Image("hero")
    .ignoresSafeArea()

// Ignore specific edges
Color.blue
    .ignoresSafeArea(edges: .top)

// Add to safe area
VStack {
    content
}
.safeAreaInset(edge: .bottom) {
    BottomBar()
}
```

## Responsive Layout Patterns

### Adaptive Stack

```swift
struct AdaptiveStack<Content: View>: View {
    @Environment(\.horizontalSizeClass) var sizeClass
    let content: () -> Content

    var body: some View {
        if sizeClass == .compact {
            VStack(content: content)
        } else {
            HStack(content: content)
        }
    }
}
```

### ViewThatFits (iOS 16+)

```swift
ViewThatFits(in: .horizontal) {
    // Try full layout first
    HStack {
        Image(systemName: "star.fill")
        Text("Favorites")
        Text("View all your favorites")
    }

    // Fall back to compact
    HStack {
        Image(systemName: "star.fill")
        Text("Favorites")
    }

    // Final fallback
    Image(systemName: "star.fill")
}
```

## Container Relative Frame (iOS 17+)

```swift
ScrollView(.horizontal) {
    HStack {
        ForEach(items) { item in
            ItemCard(item: item)
                .containerRelativeFrame(.horizontal, count: 3, spacing: 16)
        }
    }
}
```

## Best Practices

1. **Avoid Hardcoded Sizes** - Use `.frame(maxWidth: .infinity)` over fixed widths
2. **Use Lazy Stacks** - For lists over ~20 items
3. **Minimize GeometryReader** - Can cause layout issues if overused
4. **Test Size Classes** - Preview in compact and regular widths
5. **Support Dynamic Type** - Layouts should adapt to larger text
