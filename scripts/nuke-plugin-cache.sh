#!/usr/bin/env bash
# Clears all agentic-factory plugin cache from Claude Code.
# Run from any terminal. After running, reinstall via:
#   /plugin marketplace add mpaz/agentic-factory
#   /plugin install <name>@agentic-factory

set -euo pipefail

PLUGIN_DIR="$HOME/.claude/plugins"
MARKETPLACE="agentic-factory"

echo "Nuking agentic-factory plugin cache..."

# 1. Cached plugin versions
if [ -d "$PLUGIN_DIR/cache/$MARKETPLACE" ]; then
  rm -rf "$PLUGIN_DIR/cache/$MARKETPLACE"
  echo "  ✓ Cleared cache/$MARKETPLACE"
else
  echo "  - No cache/$MARKETPLACE found"
fi

# 2. Marketplace clone (pulled from GitHub)
if [ -d "$PLUGIN_DIR/marketplaces/$MARKETPLACE" ]; then
  rm -rf "$PLUGIN_DIR/marketplaces/$MARKETPLACE"
  echo "  ✓ Cleared marketplaces/$MARKETPLACE"
else
  echo "  - No marketplaces/$MARKETPLACE found"
fi

# 3. Strip agentic-factory entries from installed_plugins.json
INSTALLED="$PLUGIN_DIR/installed_plugins.json"
if [ -f "$INSTALLED" ]; then
  python3 - <<'PYEOF'
import json, sys, os

path = os.path.expanduser("~/.claude/plugins/installed_plugins.json")
with open(path) as f:
    data = json.load(f)

removed = [k for k in data if "@agentic-factory" in k]
for k in removed:
    del data[k]

with open(path, "w") as f:
    json.dump(data, f, indent=4)

if removed:
    print(f"  ✓ Removed from installed_plugins.json: {', '.join(removed)}")
else:
    print("  - No agentic-factory entries in installed_plugins.json")
PYEOF
fi

# 4. Strip agentic-factory from known_marketplaces.json
KNOWN="$PLUGIN_DIR/known_marketplaces.json"
if [ -f "$KNOWN" ]; then
  python3 - <<'PYEOF'
import json, os

path = os.path.expanduser("~/.claude/plugins/known_marketplaces.json")
with open(path) as f:
    data = json.load(f)

if "agentic-factory" in data:
    del data["agentic-factory"]
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print("  ✓ Removed agentic-factory from known_marketplaces.json")
else:
    print("  - agentic-factory not in known_marketplaces.json")
PYEOF
fi

echo ""
echo "Done. To reinstall:"
echo "  /plugin marketplace add mpaz/agentic-factory"
echo "  /plugin install orchestra@agentic-factory"
