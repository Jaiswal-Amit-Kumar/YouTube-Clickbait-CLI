from __future__ import annotations

import csv
from pathlib import Path

from .models import Video


def load_videos(files: list[Path]) -> list[Video]:
    videos: list[Video] = []

    for file_path in files:
        with file_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                videos.append(
                    Video(
                        title=row["title"].strip(),
                        ctr=float(row["ctr"]),
                        retention_rate=float(row["retention_rate"]),
                    )
                )
    return videos
