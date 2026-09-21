"""Organize raw CSVs from tml-data/ into the structured data/ folder.

Layout produced:
    data/atp/ATP_Database.csv, atp_rankings_*.csv   (top-level ATP reference
                                                     files)
    data/atp/atp/                                   (top tier tour: YYYY.csv,
                                                     atp_quali/, etc.)
    data/atp/challenger/                             (challenger tour)
    data/wta/wta/                                    (WTA tour, leaves room for
                                                      a future data/wta/itf/)
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from tennis_my_life_archive.layout import REPO_ROOT, SOURCE_DIR, destination_for


def organize_files(dry_run: bool = False) -> tuple[int, list[Path]]:
    """Move recognized files from tml-data/ into data/, reporting progress.

    Returns the number of items moved (or that would be moved) and the list
    of unrecognized paths left behind.
    """
    unrecognized: list[Path] = []
    moved = 0

    for entry in sorted(SOURCE_DIR.iterdir()):
        dest = destination_for(entry)
        if dest is None:
            unrecognized.append(entry)
            continue

        print(f"{entry.relative_to(REPO_ROOT)} -> {dest.relative_to(REPO_ROOT)}")
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(entry), str(dest))
        moved += 1

    return moved, unrecognized


def main() -> None:
    """CLI entry point: parse args and organize tml-data/ into data/."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned moves without moving anything",
    )
    parser.add_argument(
        "--delete-source",
        action="store_true",
        help="Delete tml-data/ after a successful move",
    )
    args = parser.parse_args()

    if not SOURCE_DIR.is_dir():
        raise SystemExit(f"Source directory not found: {SOURCE_DIR}")

    moved, unrecognized = organize_files(dry_run=args.dry_run)

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
