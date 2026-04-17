# swift-ui

SwiftUI implementation patterns for building polished iOS/macOS apps — views, state, layout, animation, and architecture.

## Quick Start

```
build a list view with navigation to a detail screen
how should I manage state for this form?
implement a spring animation on this button
set up SwiftData with relationships for my model
do I need a ViewModel here or can I use @State?
```

## What It Does

Background knowledge skill — loads the appropriate SwiftUI reference based on what you're building.

| Topic | When to use |
|-------|-------------|
| **View Composition** | Building views, applying modifiers, custom view modifiers, ViewBuilder |
| **State Management** | @State, @Binding, @StateObject, @Observable, Environment, data flow patterns |
| **Layout** | VStack/HStack/ZStack, LazyStacks, LazyGrids, GeometryReader, adaptive layouts |
| **Animation** | Implicit/explicit animation, transitions, spring animations, gesture-driven motion |
| **Accessibility** | VoiceOver, Dynamic Type, accessibility traits and actions |
| **Architecture** | Views as pure state expressions, Environment for DI, `.task(id:)` — no MVVM required |
| **SwiftData** | @Model, @Query, ModelContainer/ModelContext, relationships, predicates, migrations |

The architecture reference explicitly covers when you do NOT need a ViewModel (the default should be `@State` + Environment, not a separate ViewModel layer).

## File Structure

`references/` contains one file per topic:

```
references/
  views.md         accessibility.md
  state.md         architecture.md
  layout.md        swiftdata.md
  animation.md
  components/
```

## See Also

- `swift-lang` — Swift language internals (macros, concurrency, generics, testing)
