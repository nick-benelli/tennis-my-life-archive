"""Download raw CSV data files published by the TML stats API."""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

from tennis_my_life_archive.layout import SOURCE_DIR, destination_for

API_URL = "https://stats.tennismylife.org/api/data-files"


def _already_archived(name: str, size: int) -> bool:
    """Check whether name is already archived with a matching file size."""
    archived = destination_for(Path(name))
    if archived is None or not archived.is_file():
        return False
    return archived.stat().st_size == size


def download_data_files(
    dest_dir: Path = SOURCE_DIR, api_url: str = API_URL
) -> list[Path]:
    """Download new/changed files from the TML API into dest_dir.

    Files already archived (see tennis_my_life_archive.layout) with a
    matching size are skipped, since the API doesn't provide a checksum.
    """
    dest_dir.mkdir(parents=True, exist_ok=True)

    request = urllib.request.Request(
        api_url, headers={"User-Agent": "tennis-my-life-archive"}
    )
    with urllib.request.urlopen(request) as response:
        payload = json.load(response)

    downloaded: list[Path] = []
    for entry in payload["files"]:
        name = entry["name"]
        if _already_archived(name, entry["size"]):
            continue

        target = dest_dir / name
        print(f"{name} <- {entry['url']}")
        urllib.request.urlretrieve(entry["url"], target)
        downloaded.append(target)

    return downloaded


if __name__ == "__main__":
    download_data_files()
