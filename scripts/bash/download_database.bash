#!/usr/bin/env bash
set -euo pipefail

# Thin wrapper: the real logic (and the skip-if-unchanged check) lives in
# tennis_my_life_archive.download, so it isn't duplicated here.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"
uv run python -m tennis_my_life_archive.download
