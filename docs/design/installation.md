# Installation & Deployment

> **Note:** This toolkit uses a project-based deployment system rather than global installation. Components are copied to individual projects as needed.

## Quick Start

1. Clone this repository:
```bash
git clone https://github.com/[username]/agentic-factory.git
cd agentic-factory
```

2. Add your project to the index:
```bash
./deploy.sh add-project my-app ~/path/to/my-app
```

3. Deploy components:
```bash
# Deploy everything
./deploy.sh deploy-all my-app

# Or deploy specific components
./deploy.sh deploy my-app agent:quality-control-enforcer
./deploy.sh deploy my-app template:paz/acb/typescript
```

## Deployment System

The toolkit includes sophisticated deployment scripts for managing components across multiple projects:

### **deploy.sh** - Main deployment tool
```bash
# Add a new project
./deploy.sh add-project <name> <path>

# Deploy specific components
./deploy.sh deploy <project> agent:<name>
./deploy.sh deploy <project> command:<path>
./deploy.sh deploy <project> template:<path>

# Deploy all components
./deploy.sh deploy-all <project>

# View projects and status
./deploy.sh list                    # List all projects
./deploy.sh status <project>        # Show deployment details
```

### **sync.sh** - Keep projects updated
```bash
# Sync a single project
./sync.sh my-app

# Sync all projects
./sync.sh all

# Check what needs updating
./sync.sh check
```

### **projects.json** - Project index
Maintains a registry of all your projects with:
- Project paths and names
- Deployed components tracking
- Last deployment timestamps
- Custom `.claude` directory locations

## Manual Installation (Alternative)

If you prefer manual copying:
```bash
# Copy specific files to your project's .claude directory
cp agentic-factory/agents/*.md your-project/.claude/agents/
cp -r agentic-factory/commands/paz your-project/.claude/commands/
cp agentic-factory/templates/paz/acb/*.md your-project/.claude/templates/
```