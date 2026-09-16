#!/usr/bin/env python3
"""Validate the minimum structure of a source-aware research pack."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = (
    "Scope and assumptions",
    "Executive answer",
    "Verified findings",
    "Source ledger",
)
URL_PATTERN = re.compile(r"https?://\S+")
SOURCE_MARKER = re.compile(r"\[S\d+\]")


def validate(text: str) -> list[str]:
    errors: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^#+\s+{re.escape(heading)}\b", text, re.MULTILINE | re.IGNORECASE):
            errors.append(f"missing heading: {heading}")
    if not SOURCE_MARKER.search(text):
        errors.append("no source marker like [S1] found")
    ledger_start = re.search(r"^#+\s+Source ledger\b", text, re.MULTILINE | re.IGNORECASE)
    if ledger_start and not URL_PATTERN.search(text[ledger_start.end() :]):
        errors.append("source ledger contains no URL")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Markdown research pack")
    args = parser.parse_args()
    if not args.path.is_file():
        print(f"error: file not found: {args.path}", file=sys.stderr)
        return 2
    errors = validate(args.path.read_text(encoding="utf-8"))
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
