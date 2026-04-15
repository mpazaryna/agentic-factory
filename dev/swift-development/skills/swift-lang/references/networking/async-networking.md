# Async Networking with URLSession

Modern networking patterns using Swift's async/await with URLSession.

## Basic GET Request

```swift
func fetchUser(id: Int) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, response) = try await URLSession.shared.data(from: url)

    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw NetworkError.invalidResponse
    }

    return try JSONDecoder().decode(User.self, from: data)
}
```

## POST Request with Body

```swift
func createUser(_ user: CreateUserRequest) async throws -> User {
    let url = URL(string: "https://api.example.com/users")!

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    request.httpBody = try JSONEncoder().encode(user)

    let (data, response) = try await URLSession.shared.data(for: request)

    guard let httpResponse = response as? HTTPURLResponse,
          (200...299).contains(httpResponse.statusCode) else {
        throw NetworkError.invalidResponse
    }

    return try JSONDecoder().decode(User.self, from: data)
}
```

## API Client Pattern

Structure your networking layer cleanly:

```swift
// MARK: - Error Types

enum NetworkError: Error {
    case invalidURL
    case invalidResponse
    case httpError(statusCode: Int)
    case decodingError(Error)
    case noData
}

// MARK: - API Client

actor APIClient {
    private let baseURL: URL
    private let session: URLSession
    private let decoder: JSONDecoder

    init(baseURL: URL, session: URLSession = .shared) {
        self.baseURL = baseURL
        self.session = session
        self.decoder = JSONDecoder()
        self.decoder.dateDecodingStrategy = .iso8601
    }

    func get<T: Decodable>(_ path: String) async throws -> T {
        let url = baseURL.appendingPathComponent(path)
        return try await request(URLRequest(url: url))
    }

    func post<Body: Encodable, Response: Decodable>(
        _ path: String,
        body: Body
    ) async throws -> Response {
        let url = baseURL.appendingPathComponent(path)

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONEncoder().encode(body)

        return try await self.request(request)
    }

    private func request<T: Decodable>(_ request: URLRequest) async throws -> T {
        let (data, response) = try await session.data(for: request)

        guard let httpResponse = response as? HTTPURLResponse else {
            throw NetworkError.invalidResponse
        }

        guard (200...299).contains(httpResponse.statusCode) else {
            throw NetworkError.httpError(statusCode: httpResponse.statusCode)
        }

        do {
            return try decoder.decode(T.self, from: data)
        } catch {
            throw NetworkError.decodingError(error)
        }
    }
}
```

## Usage with SwiftUI

Inject the client via Environment and call from views:

```swift
// App setup
@main
struct MyApp: App {
    let apiClient = APIClient(baseURL: URL(string: "https://api.example.com")!)

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(apiClient)
        }
    }
}

// View usage
struct UserListView: View {
    @Environment(APIClient.self) private var client
    @State private var users: [User] = []
    @State private var isLoading = false
    @State private var error: Error?

    var body: some View {
        List(users) { user in
            Text(user.name)
        }
        .overlay {
            if isLoading {
                ProgressView()
            }
        }
        .task {
            await loadUsers()
        }
    }

    private func loadUsers() async {
        isLoading = true
        defer { isLoading = false }

        do {
            users = try await client.get("/users")
        } catch {
            self.error = error
        }
    }
}
```

## Authentication

Add authentication headers:

```swift
actor AuthenticatedAPIClient {
    private let baseURL: URL
    private let session: URLSession
    private var token: String?

    func setToken(_ token: String) {
        self.token = token
    }

    private func authorizedRequest(_ request: URLRequest) -> URLRequest {
        var request = request
        if let token {
            request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        }
        return request
    }

    func get<T: Decodable>(_ path: String) async throws -> T {
        let url = baseURL.appendingPathComponent(path)
        let request = authorizedRequest(URLRequest(url: url))
        return try await self.request(request)
    }
}
```

## Retry Logic

Implement automatic retries for transient failures:

```swift
func fetchWithRetry<T: Decodable>(
    _ request: URLRequest,
    maxRetries: Int = 3,
    delay: TimeInterval = 1.0
) async throws -> T {
    var lastError: Error?

    for attempt in 0..<maxRetries {
        do {
            return try await self.request(request)
        } catch let error as NetworkError {
            lastError = error

            // Only retry on specific errors
            switch error {
            case .httpError(let code) where code >= 500:
                // Server error - retry
                break
            default:
                throw error // Don't retry client errors
            }
        }

        // Exponential backoff
        let backoff = delay * pow(2.0, Double(attempt))
        try await Task.sleep(for: .seconds(backoff))
    }

    throw lastError ?? NetworkError.invalidResponse
}
```

## Concurrent Requests

Fetch multiple resources in parallel:

```swift
func fetchDashboard() async throws -> Dashboard {
    async let user: User = client.get("/me")
    async let posts: [Post] = client.get("/posts")
    async let notifications: [Notification] = client.get("/notifications")

    return try await Dashboard(
        user: user,
        posts: posts,
        notifications: notifications
    )
}
```

## Streaming with AsyncSequence

For large downloads or server-sent events:

```swift
func downloadLargeFile(from url: URL) async throws {
    let (bytes, response) = try await URLSession.shared.bytes(from: url)

    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw NetworkError.invalidResponse
    }

    let totalSize = httpResponse.expectedContentLength
    var downloadedSize: Int64 = 0

    for try await byte in bytes {
        // Process byte
        downloadedSize += 1

        // Update progress
        let progress = Double(downloadedSize) / Double(totalSize)
        await MainActor.run {
            self.downloadProgress = progress
        }
    }
}
```

## Request Cancellation

Tasks are automatically cancelled when views disappear:

```swift
struct UserDetailView: View {
    let userId: Int
    @State private var user: User?

    var body: some View {
        Group {
            if let user {
                UserContent(user: user)
            } else {
                ProgressView()
            }
        }
        .task {
            // This task is automatically cancelled if view disappears
            user = try? await fetchUser(id: userId)
        }
    }
}
```

Manual cancellation:

```swift
class SearchViewModel: ObservableObject {
    @Published var results: [SearchResult] = []
    private var searchTask: Task<Void, Never>?

    func search(_ query: String) {
        // Cancel previous search
        searchTask?.cancel()

        searchTask = Task {
            // Debounce
            try? await Task.sleep(for: .milliseconds(300))

            guard !Task.isCancelled else { return }

            do {
                let results: [SearchResult] = try await client.get("/search?q=\(query)")
                await MainActor.run {
                    self.results = results
                }
            } catch {
                // Handle error
            }
        }
    }
}
```

## URLSession Configuration

Custom configurations for different needs:

```swift
// Default (for most requests)
let defaultSession = URLSession.shared

// Background transfers (continues when app is suspended)
let backgroundConfig = URLSessionConfiguration.background(
    withIdentifier: "com.app.background"
)
backgroundConfig.sessionSendsLaunchEvents = true
let backgroundSession = URLSession(configuration: backgroundConfig)

// Ephemeral (no caching, no cookies)
let ephemeralConfig = URLSessionConfiguration.ephemeral
let ephemeralSession = URLSession(configuration: ephemeralConfig)

// Custom timeouts
let customConfig = URLSessionConfiguration.default
customConfig.timeoutIntervalForRequest = 30
customConfig.timeoutIntervalForResource = 60
let customSession = URLSession(configuration: customConfig)
```

## Error Handling Best Practices

```swift
enum APIError: LocalizedError {
    case networkError(URLError)
    case serverError(statusCode: Int, message: String?)
    case decodingError(Error)
    case unauthorized
    case notFound

    var errorDescription: String? {
        switch self {
        case .networkError(let error):
            return "Network error: \(error.localizedDescription)"
        case .serverError(let code, let message):
            return "Server error \(code): \(message ?? "Unknown")"
        case .decodingError:
            return "Failed to parse response"
        case .unauthorized:
            return "Please log in again"
        case .notFound:
            return "Resource not found"
        }
    }
}

func handleResponse(_ response: HTTPURLResponse, data: Data) throws {
    switch response.statusCode {
    case 200...299:
        return // Success
    case 401:
        throw APIError.unauthorized
    case 404:
        throw APIError.notFound
    case 500...599:
        let message = try? JSONDecoder().decode(ErrorResponse.self, from: data).message
        throw APIError.serverError(statusCode: response.statusCode, message: message)
    default:
        throw APIError.serverError(statusCode: response.statusCode, message: nil)
    }
}
```

## Quick Reference

| Task | Pattern |
|------|---------|
| GET request | `try await URLSession.shared.data(from: url)` |
| POST request | `try await URLSession.shared.data(for: request)` |
| Parallel requests | `async let a = ...; async let b = ...` |
| Cancellation | `.task { }` auto-cancels; or `task.cancel()` |
| Retry | Loop with `Task.sleep` for backoff |
| Streaming | `URLSession.shared.bytes(from: url)` |
| Auth header | `request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")` |

## Anti-Patterns

- **Don't block the main thread** - Always use async/await, never synchronous requests
- **Don't ignore cancellation** - Check `Task.isCancelled` in long operations
- **Don't hardcode URLs** - Use a configurable base URL
- **Don't skip error handling** - Handle all HTTP status codes appropriately
- **Don't retain strong references** - Use `[weak self]` in closures if needed

## References

- Adapted from [awesome-swift-claude-code-subagents](https://github.com/sanghun0724/awesome-swift-claude-code-subagents) by sanghun0724
- Apple URLSession Documentation
- WWDC21: Use async/await with URLSession
