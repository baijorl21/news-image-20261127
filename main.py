#!/usr/bin/env python3
"""Deliver the prepared news artwork to the requested output folder."""

from pathlib import Path
import os
import shutil


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    destination_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination_dir / source.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
