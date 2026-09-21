#!/usr/bin/env bash
set -euo pipefail

# Always download into <repo root>/tml-data, regardless of the caller's cwd.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
DEST_DIR="$REPO_ROOT/tml-data"

mkdir -p "$DEST_DIR"
curl -s 'https://stats.tennismylife.org/api/data-files' | jq -r '.files[] | "\(.url)\t\(.name)"' | while IFS=$'\t' read -r url name; do
    curl -sSL "$url" -o "$DEST_DIR/$name"
done
