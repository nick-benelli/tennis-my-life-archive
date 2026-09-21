"""Shared knowledge of where archived TML data files belong on disk."""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = REPO_ROOT / "tml-data"
DEST_DIR = REPO_ROOT / "data"

ATP_TOP_DIR = DEST_DIR / "atp"
ATP_TOUR_DIR = ATP_TOP_DIR / "atp"
ATP_CHALLENGER_DIR = ATP_TOP_DIR / "challenger"
WTA_TOP_DIR = DEST_DIR / "wta"
WTA_TOUR_DIR = WTA_TOP_DIR / "wta"

# Reference/database files that aren't tied to a single tour year.
ATP_TOP_LEVEL_FILES = re.compile(r"^(ATP_Database|atp_rankings_.*)\.csv$")
CHALLENGER_FILE = re.compile(r"^(\d{4}_challenger|challenger_ongoing_tourneys)\.csv$")
WTA_FILE = re.compile(r"^(\d{4}_wta|wta_ongoing_tourneys)\.csv$")
ATP_TOUR_FILE = re.compile(r"^(\d{4}|atp_matches_amateur|ongoing_tourneys)\.csv$")


def destination_for(path: Path) -> Path | None:
    """Return the archived destination for a file/dir, or None if unrecognized."""
    name = path.name

    if path.is_dir():
        if name == "atp_quali":
            return ATP_TOUR_DIR / name
        return None

    if ATP_TOP_LEVEL_FILES.match(name):
        return ATP_TOP_DIR / name
    if CHALLENGER_FILE.match(name):
        return ATP_CHALLENGER_DIR / name
    if WTA_FILE.match(name):
        return WTA_TOUR_DIR / name
    if ATP_TOUR_FILE.match(name):
        return ATP_TOUR_DIR / name

    return None
