"""Download raw CSV data files published by the TML stats API."""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEST_DIR = REPO_ROOT / "tml-data"
API_URL = "https://stats.tennismylife.org/api/data-files"


def download_data_files(
    dest_dir: Path = DEST_DIR, api_url: str = API_URL
) -> list[Path]:
    """Fetch the TML data-files listing and download each file into dest_dir."""
    dest_dir.mkdir(parents=True, exist_ok=True)

    request = urllib.request.Request(
        api_url, headers={"User-Agent": "tennis-my-life-archive"}
    )
    with urllib.request.urlopen(request) as response:
        payload = json.load(response)

    downloaded: list[Path] = []
    for entry in payload["files"]:
        target = dest_dir / entry["name"]
        print(f"{entry['name']} <- {entry['url']}")
        urllib.request.urlretrieve(entry["url"], target)
        downloaded.append(target)

    return downloaded


if __name__ == "__main__":
    download_data_files()
