from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tabulate import tabulate

from .csv_reader import load_videos
from .reports import REPORTS


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args(argv)


def validate_files(paths: list[str]) -> list[Path]:
    validated: list[Path] = []

    for raw_path in paths:
        path = Path(raw_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {raw_path}")
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {raw_path}")
        validated.append(path)

    return validated


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    report_factory = REPORTS.get(args.report)
    if report_factory is None:
        print(f"Unknown report: {args.report}", file=sys.stderr)
        return 1

    try:
        files = validate_files(args.files)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    rows = report_factory().build(load_videos(files))
    print(tabulate(rows, headers="keys", tablefmt="github", floatfmt=".1f"))
    return 0
