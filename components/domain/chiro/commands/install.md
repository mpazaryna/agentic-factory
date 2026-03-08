---
description: Build Release and install to Applications
tags: [build, release, install]
---

# Build and Install Release

Build PAB in Release configuration and install to Applications folder.

```bash
./scripts/build-and-install.sh
```

**What this does:**
1. Cleans previous builds
2. Builds Release configuration
3. Copies app to `/Applications/`
4. Makes it ready for production use

**Location:** `scripts/build-and-install.sh`

**Notes:**
- This is the production build (optimized, no debug symbols)
- App will be installed as `Practice Assistant for Bodywork.app`
- May need to approve in System Settings if Gatekeeper blocks it

**Related:**
- `/build` - Development build (Debug configuration)
- `/test` - Run test suite before releasing
