# State Management

SwiftUI property wrappers and data flow patterns for clean state management.

## Property Wrappers Overview

| Wrapper | Owner | Use Case |
|---------|-------|----------|
| `@State` | View | Simple local state |
| `@Binding` | Parent | Two-way connection to parent state |
| `@StateObject` | View | Reference type owned by view |
| `@ObservedObject` | Parent | Reference type passed from parent |
| `@EnvironmentObject` | App/Scene | Shared dependency injection |
| `@Environment` | SwiftUI | System values (colorScheme, etc.) |
| `@AppStorage` | UserDefaults | Persistent simple values |
| `@SceneStorage` | Scene | Scene-specific persistence |

## @State

Local value type state owned by the view.

```swift
struct CounterView: View {
    @State private var count = 0
    @State private var isAnimating = false

    var body: some View {
        VStack {
            Text("\(count)")
                .font(.largeTitle)
                .scaleEffect(isAnimating ? 1.2 : 1.0)

            Button("Increment") {
                withAnimation(.spring(response: 0.3)) {
                    count += 1
                    isAnimating = true
                }
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
                    withAnimation {
                        isAnimating = false
                    }
                }
            }
        }
    }
}
```

**Rules**:
- Always mark `private`
- For value types (Int, String, Bool, struct)
- View owns the source of truth

## @Binding

Two-way connection to state owned elsewhere.

```swift
struct ToggleRow: View {
    let title: String
    @Binding var isOn: Bool

    var body: some View {
        HStack {
            Text(title)
            Spacer()
            Toggle("", isOn: $isOn)
                .labelsHidden()
        }
    }
}

// Usage
struct SettingsView: View {
    @State private var notificationsEnabled = true

    var body: some View {
        ToggleRow(
            title: "Notifications",
            isOn: $notificationsEnabled  // Pass binding
        )
    }
}
```

**Creating Bindings**:

```swift
// From @State
$count

// Constant binding (for previews)
.constant(true)

// Custom binding
Binding(
    get: { viewModel.isEnabled },
    set: { viewModel.isEnabled = $0 }
)
```

## @StateObject vs @ObservedObject

### @StateObject (Owner)

```swift
class ItemViewModel: ObservableObject {
    @Published var items: [Item] = []
    @Published var isLoading = false

    func loadItems() async {
        isLoading = true
        items = await api.fetchItems()
        isLoading = false
    }
}

struct ItemListView: View {
    @StateObject private var viewModel = ItemViewModel()

    var body: some View {
        List(viewModel.items) { item in
            ItemRow(item: item)
        }
        .task {
            await viewModel.loadItems()
        }
    }
}
```

### @ObservedObject (Passed In)

```swift
struct ItemDetailView: View {
    @ObservedObject var viewModel: ItemDetailViewModel

    var body: some View {
        // Uses viewModel passed from parent
    }
}

// Parent creates and passes
struct ParentView: View {
    @StateObject private var detailVM = ItemDetailViewModel()

    var body: some View {
        ItemDetailView(viewModel: detailVM)
    }
}
```

**Rule**: Use `@StateObject` when the view creates/owns the object. Use `@ObservedObject` when passed from a parent.

## @EnvironmentObject

Dependency injection for shared state.

```swift
// Define the object
class AppState: ObservableObject {
    @Published var user: User?
    @Published var isLoggedIn = false
}

// Inject at app level
@main
struct MyApp: App {
    @StateObject private var appState = AppState()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(appState)
        }
    }
}

// Use anywhere in hierarchy
struct ProfileView: View {
    @EnvironmentObject var appState: AppState

    var body: some View {
        if let user = appState.user {
            Text("Hello, \(user.name)")
        }
    }
}
```

## @Environment

System-provided values.

```swift
struct AdaptiveView: View {
    @Environment(\.colorScheme) var colorScheme
    @Environment(\.dynamicTypeSize) var dynamicTypeSize
    @Environment(\.horizontalSizeClass) var horizontalSizeClass
    @Environment(\.dismiss) var dismiss
    @Environment(\.openURL) var openURL

    var body: some View {
        VStack {
            if colorScheme == .dark {
                // Dark mode content
            }

            Button("Close") {
                dismiss()
            }
        }
    }
}
```

### Custom Environment Values

```swift
// Define key
private struct ThemeKey: EnvironmentKey {
    static let defaultValue = Theme.standard
}

// Extend Environment
extension EnvironmentValues {
    var theme: Theme {
        get { self[ThemeKey.self] }
        set { self[ThemeKey.self] = newValue }
    }
}

// Usage
struct ThemedView: View {
    @Environment(\.theme) var theme

    var body: some View {
        Text("Themed")
            .foregroundStyle(theme.primaryColor)
    }
}

// Set value
ContentView()
    .environment(\.theme, .dark)
```

## @AppStorage

Persistent storage backed by UserDefaults.

```swift
struct SettingsView: View {
    @AppStorage("hasCompletedOnboarding") var hasCompletedOnboarding = false
    @AppStorage("preferredTheme") var preferredTheme = "system"
    @AppStorage("notificationsEnabled") var notificationsEnabled = true

    var body: some View {
        Form {
            Toggle("Notifications", isOn: $notificationsEnabled)

            Picker("Theme", selection: $preferredTheme) {
                Text("System").tag("system")
                Text("Light").tag("light")
                Text("Dark").tag("dark")
            }
        }
    }
}
```

## Preferred Pattern: No ViewModels

> **Important:** This project does NOT use ViewModels. See `references/architecture.md` for the full rationale.

Instead of MVVM, use:
- `@State` with ViewState enums for local view state
- `@Environment` for service injection
- `@Query` for SwiftData (handles fetching, observation, UI updates automatically)
- `.task(id:)` and `.onChange()` for side effects

```swift
struct ProfileView: View {
    @Environment(UserService.self) private var userService

    enum ViewState {
        case loading
        case loaded(User)
        case error(String)
    }

    @State private var viewState: ViewState = .loading

    var body: some View {
        switch viewState {
        case .loading:
            ProgressView()
        case .loaded(let user):
            ProfileContent(user: user)
        case .error(let message):
            ErrorView(message: message)
        }
    }
    .task { await loadUser() }

    private func loadUser() async {
        do {
            let user = try await userService.fetchCurrentUser()
            viewState = .loaded(user)
        } catch {
            viewState = .error(error.localizedDescription)
        }
    }
}
```

## Data Flow Best Practices

1. **Single Source of Truth** - Each piece of state has one owner
2. **Unidirectional Flow** - Parent passes down, child calls actions up
3. **No ViewModels** - Use @State + @Environment instead
4. **Avoid Deep Nesting** - Use @Environment for deeply shared services
5. **Prefer Value Types** - Use structs for models when possible
6. **Split Large Views** - Extract subviews, not ViewModels
