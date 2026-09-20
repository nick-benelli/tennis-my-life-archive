#!/usr/bin/env python3
"""Organize raw CSVs from tml-data/ into the structured data/ folder.

Layout produced:
    data/atp/ATP_Database.csv, atp_rankings_*.csv   (top-level ATP reference files)
    data/atp/atp/                                   (top tier tour: YYYY.csv, atp_quali/, etc.)
    data/atp/challenger/                             (challenger tour)
    data/wta/wta/                                    (WTA tour, leaves room for a future data/wta/itf/)

Run with --dry-run to preview the moves without touching the filesystem.
Pass --delete-source to remove tml-data/ once every file has been moved.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
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
ATP_TOUR_FILE = re.compile(
    r"^(\d{4}|atp_matches_amateur|ongoing_tourneys)\.csv$"
)


def destination_for(path: Path) -> Path | None:
    """Return the destination path for a file/dir relative to tml-data, or None if unrecognized."""
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Show planned moves without moving anything")
    parser.add_argument("--delete-source", action="store_true", help="Delete tml-data/ after a successful move")
    args = parser.parse_args()

    if not SOURCE_DIR.is_dir():
        raise SystemExit(f"Source directory not found: {SOURCE_DIR}")

    unrecognized: list[Path] = []
    moved = 0

    for entry in sorted(SOURCE_DIR.iterdir()):
        dest = destination_for(entry)
        if dest is None:
            unrecognized.append(entry)
            continue

        print(f"{entry.relative_to(REPO_ROOT)} -> {dest.relative_to(REPO_ROOT)}")
        if not args.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(entry), str(dest))
        moved += 1

    if unrecognized:
        print("\nUnrecognized files/folders left in place (not moved):")
        for entry in unrecognized:
            print(f"  {entry.relative_to(REPO_ROOT)}")

    print(f"\n{moved} item(s) {'would be' if args.dry_run else ''} moved.")

    if args.delete_source and not args.dry_run:
        if unrecognized:
            print("Skipping tml-data/ deletion: unrecognized files remain.")
        else:
            shutil.rmtree(SOURCE_DIR)
            print(f"Deleted {SOURCE_DIR.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
