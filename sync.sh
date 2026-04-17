#!/usr/bin/env bash
# Sync skills to ~/.claude/skills/
# Run after making changes to skills/

set -euo pipefail

SRC="$(dirname "$0")/skills/"
DEST="$HOME/.claude/skills/"

mkdir -p "$DEST"
rsync -av --delete "$SRC" "$DEST"

echo ""
echo "Synced to $DEST"
