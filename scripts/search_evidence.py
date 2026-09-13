#!/usr/bin/env python3
"""Search refined research-method indexes for evidence snippets."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


INDEX_FILES = [
    "顶刊idea形成套路蒸馏.md",
    "博弈建模套路蒸馏.md",
    "实证方法套路蒸馏.md",
    "算法优化套路蒸馏.md",
    "顶刊写作套路蒸馏.md",
    "阶段性review与后续文献规划_2026-07-31.md",
]


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize(text: str) -> str:
    return text.casefold()


def find_hits(query: str, limit: int) -> list[tuple[str, int, str]]:
    root = project_root()
    index_dir = root / "references" / "evidence-indexes"
    terms = [normalize(t) for t in query.split() if t.strip()]
    hits: list[tuple[str, int, str]] = []
    for name in INDEX_FILES:
        path = index_dir / name
        if not path.exists():
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            hay = normalize(line)
            if all(term in hay for term in terms):
                hits.append((name, line_no, line.strip()))
                if len(hits) >= limit:
                    return hits
    return hits


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Search terms, separated by spaces")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    hits = find_hits(args.query, args.limit)
    if not hits:
        print("No hits found.")
        return 1
    for name, line_no, text in hits:
        print(f"{name}:{line_no}: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
