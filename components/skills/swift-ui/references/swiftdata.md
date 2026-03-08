# SwiftData

Modern data persistence for iOS 17+ and macOS 14+ using Swift-native patterns that integrate directly with SwiftUI views.

## Why SwiftData

SwiftData replaces Core Data's complexity with Swift-native syntax:
- `@Model` macro instead of `.xcdatamodeld` files
- `@Query` property wrapper for reactive data in views
- Direct SwiftUI integration (no ViewModel layer needed)
- Automatic CloudKit sync support

## Core Concepts

### @Model Macro

Define your data models as Swift classes:

```swift
import SwiftData

@Model
class Book {
    var title: String
    var author: String
    var dateAdded: Date
    var isRead: Bool

    // Relationships
    @Relationship(deleteRule: .cascade)
    var notes: [Note]

    // Computed properties work normally
    var displayTitle: String {
        "\(title) by \(author)"
    }

    init(title: String, author: String) {
        self.title = title
        self.author = author
        self.dateAdded = .now
        self.isRead = false
        self.notes = []
    }
}

@Model
class Note {
    var content: String
    var createdAt: Date
    var book: Book?

    init(content: String, book: Book? = nil) {
        self.content = content
        self.createdAt = .now
        self.book = book
    }
}
```

### Relationship Types

```swift
// One-to-many (default)
@Relationship var notes: [Note]

// Cascade delete (delete notes when book is deleted)
@Relationship(deleteRule: .cascade) var notes: [Note]

// Nullify (set note.book to nil when book deleted)
@Relationship(deleteRule: .nullify) var notes: [Note]

// Inverse relationship (automatic)
@Relationship(inverse: \Note.book) var notes: [Note]
```

### ModelContainer Setup

Configure at app launch:

```swift
@main
struct BookApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: [Book.self, Note.self])
    }
}
```

Custom configuration:

```swift
@main
struct BookApp: App {
    let container: ModelContainer

    init() {
        let schema = Schema([Book.self, Note.self])
        let config = ModelConfiguration(
            "Books",
            schema: schema,
            isStoredInMemoryOnly: false,
            cloudKitDatabase: .automatic
        )

        do {
            container = try ModelContainer(for: schema, configurations: config)
        } catch {
            fatalError("Failed to create container: \(error)")
        }
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(container)
    }
}
```

## SwiftUI Integration

### @Query Property Wrapper

Fetch data reactively in views:

```swift
struct BookListView: View {
    // Basic query - all books
    @Query private var books: [Book]

    var body: some View {
        List(books) { book in
            BookRowView(book: book)
        }
    }
}
```

### Filtered and Sorted Queries

```swift
struct BookListView: View {
    // Sorted by date
    @Query(sort: \Book.dateAdded, order: .reverse)
    private var books: [Book]

    // Filtered + sorted
    @Query(
        filter: #Predicate<Book> { $0.isRead == false },
        sort: \Book.title
    )
    private var unreadBooks: [Book]

    var body: some View {
        List(books) { book in
            BookRowView(book: book)
        }
    }
}
```

### Dynamic Queries

For queries that depend on view state:

```swift
struct AuthorBooksView: View {
    let authorName: String
    @Query private var books: [Book]

    init(authorName: String) {
        self.authorName = authorName

        let predicate = #Predicate<Book> { book in
            book.author == authorName
        }
        _books = Query(filter: predicate, sort: \Book.title)
    }

    var body: some View {
        List(books) { book in
            Text(book.title)
        }
        .navigationTitle(authorName)
    }
}
```

### CRUD Operations

Access ModelContext from environment:

```swift
struct BookListView: View {
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \Book.dateAdded, order: .reverse) private var books: [Book]

    var body: some View {
        NavigationStack {
            List {
                ForEach(books) { book in
                    BookRowView(book: book)
                }
                .onDelete(perform: deleteBooks)
            }
            .toolbar {
                Button("Add Book") {
                    addBook()
                }
            }
        }
    }

    private func addBook() {
        let book = Book(title: "New Book", author: "Unknown")
        modelContext.insert(book)
        // Auto-saves - no explicit save needed
    }

    private func deleteBooks(at offsets: IndexSet) {
        for index in offsets {
            modelContext.delete(books[index])
        }
    }
}
```

### Editing Models

Models are observable - changes automatically reflect in UI:

```swift
struct BookDetailView: View {
    @Bindable var book: Book

    var body: some View {
        Form {
            TextField("Title", text: $book.title)
            TextField("Author", text: $book.author)
            Toggle("Read", isOn: $book.isRead)
        }
        // Changes auto-save
    }
}
```

## Advanced Patterns

### Background Operations

For heavy operations, use a background context:

```swift
func importBooks(_ data: [BookData]) async {
    let container = modelContext.container

    await Task.detached {
        let backgroundContext = ModelContext(container)

        for item in data {
            let book = Book(title: item.title, author: item.author)
            backgroundContext.insert(book)
        }

        try? backgroundContext.save()
    }.value
}
```

### Predicates

Build complex queries:

```swift
// Simple comparison
#Predicate<Book> { $0.isRead == true }

// String contains
#Predicate<Book> { $0.title.contains("Swift") }

// Multiple conditions
#Predicate<Book> { book in
    book.isRead == false && book.author == "Apple"
}

// Date comparison
#Predicate<Book> { $0.dateAdded > Date.now.addingTimeInterval(-86400 * 7) }
```

### Fetch Descriptors

For more control over fetches:

```swift
func fetchRecentBooks() throws -> [Book] {
    var descriptor = FetchDescriptor<Book>(
        predicate: #Predicate { $0.isRead == false },
        sortBy: [SortDescriptor(\Book.dateAdded, order: .reverse)]
    )
    descriptor.fetchLimit = 10

    return try modelContext.fetch(descriptor)
}
```

### Testing Setup

Use in-memory store for tests:

```swift
@MainActor
class BookTests: XCTestCase {
    var container: ModelContainer!
    var context: ModelContext!

    override func setUp() {
        let config = ModelConfiguration(isStoredInMemoryOnly: true)
        container = try! ModelContainer(for: Book.self, configurations: config)
        context = container.mainContext
    }

    func testAddBook() {
        let book = Book(title: "Test", author: "Author")
        context.insert(book)

        let books = try! context.fetch(FetchDescriptor<Book>())
        XCTAssertEqual(books.count, 1)
    }
}
```

## Migration

SwiftData handles lightweight migrations automatically. For complex migrations:

```swift
enum BookSchemaV1: VersionedSchema {
    static var versionIdentifier = Schema.Version(1, 0, 0)
    static var models: [any PersistentModel.Type] { [Book.self] }

    @Model
    class Book {
        var title: String
        var author: String
    }
}

enum BookSchemaV2: VersionedSchema {
    static var versionIdentifier = Schema.Version(2, 0, 0)
    static var models: [any PersistentModel.Type] { [Book.self] }

    @Model
    class Book {
        var title: String
        var author: String
        var isbn: String? // New field
    }
}

enum BookMigrationPlan: SchemaMigrationPlan {
    static var schemas: [any VersionedSchema.Type] {
        [BookSchemaV1.self, BookSchemaV2.self]
    }

    static var stages: [MigrationStage] {
        [migrateV1toV2]
    }

    static let migrateV1toV2 = MigrationStage.lightweight(
        fromVersion: BookSchemaV1.self,
        toVersion: BookSchemaV2.self
    )
}
```

## Anti-Patterns

- **Don't use ViewModels** - @Query + @Environment(\.modelContext) is the pattern
- **Don't manually refresh** - SwiftData is reactive; UI updates automatically
- **Don't fetch in onAppear** - Use @Query instead
- **Don't ignore relationships** - Define them properly for cascade behavior
- **Don't store large blobs** - Use file references for images/documents

## Quick Reference

| Task | Pattern |
|------|---------|
| Define model | `@Model class MyModel { }` |
| Fetch in view | `@Query var items: [MyModel]` |
| Access context | `@Environment(\.modelContext) var context` |
| Insert | `context.insert(item)` |
| Delete | `context.delete(item)` |
| Edit | `@Bindable var item` + direct mutation |
| Filter | `@Query(filter: #Predicate { ... })` |
| Sort | `@Query(sort: \MyModel.date)` |

## References

- Adapted from [awesome-swift-claude-code-subagents](https://github.com/sanghun0724/awesome-swift-claude-code-subagents) by sanghun0724
- Apple SwiftData Documentation
- WWDC23: Meet SwiftData, Model your schema with SwiftData
