#!/usr/bin/env python3
"""Check a skill tree for machine-specific absolute paths."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TEXT_SUFFIXES = {".md", ".csv", ".json", ".py", ".yaml", ".yml", ".txt"}
ABSOLUTE_PATH = re.compile(
    r"(?:[A-Za-z]:[\\/]Users[\\/]|[A-Za-z]:[\\/]Documents[\\/]|/Users/|/home/|\\\\Users\\\\)",
    re.IGNORECASE,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    findings: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            findings.append(f"{path}: non-UTF-8 text file")
            continue
        for line_no, line in enumerate(lines, 1):
            if ABSOLUTE_PATH.search(line):
                findings.append(f"{path.relative_to(root)}:{line_no}: machine-specific absolute path")
    if findings:
        print("Portability issues found:")
        print("\n".join(findings))
        return 1
    print(f"Portable: scanned {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
