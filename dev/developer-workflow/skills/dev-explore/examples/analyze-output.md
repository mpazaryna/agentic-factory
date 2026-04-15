# Example: Analyze Mode Output

This shows the expected output format for `codebase_analysis.md`.

---

# TaskFlow API - Codebase Analysis

> Modular Codebase Analysis - Last updated: 2025-11-20
> Detected Technologies: Node.js, TypeScript, Express, PostgreSQL, Redis, Jest

## Technology Detection Results

- **Project Type**: REST API with WebSocket support
- **Tech Stack**: Node.js 20, TypeScript 5.x, Express.js, PostgreSQL, Redis
- **Templates Applied**: base, typescript, jest-testing

## Quick Reference

### Primary Entry Points
| File | Purpose | Start Here For |
|------|---------|----------------|
| `src/index.ts` | Application bootstrap | Understanding app initialization |
| `src/api/index.ts` | Route registration | Adding new endpoints |
| `src/services/` | Business logic | Core functionality changes |

### Key Configuration Files
| File | Purpose |
|------|---------|
| `package.json` | Dependencies, scripts |
| `tsconfig.json` | TypeScript configuration |
| `.env.example` | Environment variables |
| `jest.config.cjs` | Test configuration |

## Project Overview

**TaskFlow API** is a Node.js REST API providing task management with real-time WebSocket notifications.

### Tech Stack Summary
- **Runtime**: Node.js 20.x
- **Language**: TypeScript 5.3 (strict mode)
- **Framework**: Express.js 4.18
- **Database**: PostgreSQL 15 with TypeORM
- **Caching**: Redis 7.x
- **Testing**: Jest + Supertest
- **Package Manager**: npm (package-lock.json detected)

### Installation & Setup
```bash
git clone <repo>
cd taskflow-api
npm install
cp .env.example .env  # Configure environment
npm run db:migrate    # Run migrations
npm run dev           # Start development server
npm test              # Run tests
```

## Directory Structure

```
taskflow-api/
├── src/
│   ├── index.ts              # App entry point
│   ├── api/                  # Route handlers
│   │   ├── auth.ts           # Auth endpoints
│   │   ├── tasks.ts          # Task CRUD
│   │   └── users.ts          # User management
│   ├── services/             # Business logic
│   │   ├── auth-service.ts   # Authentication
│   │   ├── task-service.ts   # Task operations
│   │   └── notification-service.ts
│   ├── middleware/           # Request processing
│   │   ├── auth-middleware.ts
│   │   └── error-middleware.ts
│   ├── models/               # TypeORM entities
│   │   ├── user.ts
│   │   └── task.ts
│   └── utils/                # Shared utilities
├── tests/                    # Test files
│   ├── unit/
│   └── integration/
├── migrations/               # Database migrations
└── config/                   # Configuration files
```

## File-by-File Breakdown

### Core Application Files

#### src/index.ts - Application Entry
- **Purpose**: Bootstrap Express app, connect to database, start server
- **Key Features**:
  - Database connection with retry logic
  - Middleware registration
  - WebSocket server initialization
  - Graceful shutdown handling
- **How to Modify**: Add new middleware or services in the initialization sequence

#### src/api/tasks.ts - Task Routes
- **Purpose**: HTTP endpoints for task CRUD operations
- **Endpoints**:
  - `GET /api/tasks` - List tasks with filtering
  - `POST /api/tasks` - Create task
  - `GET /api/tasks/:id` - Get single task
  - `PUT /api/tasks/:id` - Update task
  - `DELETE /api/tasks/:id` - Delete task
- **How to Modify**: Follow existing pattern for new endpoints

#### src/services/task-service.ts - Task Business Logic
- **Purpose**: Core task operations separated from HTTP layer
- **Key Methods**:
  - `createTask(data)` - Creates task with validation
  - `updateTask(id, data)` - Updates with ownership check
  - `getTasks(filter)` - Filtered list with pagination
- **Dependencies**: TaskRepository, NotificationService

## Architecture

### Request Flow

```mermaid
flowchart LR
    A[Client] --> B[Express Router]
    B --> C[Auth Middleware]
    C --> D[Route Handler]
    D --> E[Service Layer]
    E --> F[Repository]
    F --> G[(PostgreSQL)]
    E --> H[(Redis Cache)]
```

### Key Patterns
- **Repository Pattern**: Data access abstracted in repository classes
- **Service Layer**: Business logic isolated from HTTP concerns
- **Middleware Chain**: Auth, validation, error handling
- **Dependency Injection**: Services receive dependencies via constructor

## Testing

### Test Structure
```
tests/
├── unit/
│   ├── services/
│   │   ├── task-service.test.ts
│   │   └── auth-service.test.ts
│   └── utils/
└── integration/
    ├── api/
    │   ├── tasks.test.ts
    │   └── auth.test.ts
    └── setup.ts
```

### Test Commands
```bash
npm test              # Run all tests
npm run test:watch    # Watch mode
npm run test:cov      # Coverage report
npm run test:unit     # Unit tests only
npm run test:int      # Integration tests only
```

### Coverage Target
- Statements: 80%+
- Branches: 75%+
- Functions: 80%+

## Environment Configuration

### Required Variables
```bash
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/taskflow
DATABASE_SSL=false

# Redis
REDIS_URL=redis://localhost:6379

# Auth
JWT_SECRET=your-secret-key
JWT_EXPIRES_IN=15m
REFRESH_TOKEN_EXPIRES_IN=7d

# Server
PORT=3000
NODE_ENV=development
```

### Environment-Specific Settings
| Setting | Development | Production |
|---------|-------------|------------|
| `NODE_ENV` | development | production |
| `DATABASE_SSL` | false | true |
| `LOG_LEVEL` | debug | info |

## Key Insights & Recommendations

### Strengths
- Clean separation between API and business logic
- Comprehensive test coverage
- Type-safe with strict TypeScript
- Good error handling patterns

### Areas for Improvement
- Add request rate limiting
- Implement API versioning
- Add OpenAPI/Swagger documentation
- Consider adding health check endpoint

## Architecture Diagram

```mermaid
flowchart TB
    subgraph "Client Layer"
        A[Web Client]
        B[Mobile App]
    end

    subgraph "API Layer"
        C[Express Router]
        D[WebSocket Server]
    end

    subgraph "Service Layer"
        E[Auth Service]
        F[Task Service]
        G[Notification Service]
    end

    subgraph "Data Layer"
        H[(PostgreSQL)]
        I[(Redis)]
    end

    A --> C
    B --> C
    A --> D
    B --> D
    C --> E
    C --> F
    D --> G
    E --> H
    E --> I
    F --> H
    F --> I
    G --> I
```

---

*Generated by codebase-docs skill (analyze mode) - 2025-11-20*
