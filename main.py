#!/usr/bin/env python3
"""Childhood memory entry for make.fun.

Writes one single line — a warm, specific childhood memory about
blowing into a game cartridge until it worked — to entry.txt.
Python stdlib only, deterministic, no network, no secrets.
"""

import os
import sys

# Revised line: the same cartridge memory, tightened, with one small
# honest detail — a younger sibling watching — so it reads like
# something that truly happened, not a greeting card.
ENTRY = (
    "I blew into the cartridge until the game flickered on, then spent "
    "the whole summer pretending I had no idea why it worked while my "
    "little brother watched in awe."
)


def verify(line: str) -> None:
    """Gate: one line, 1-200 characters, stripped, valid UTF-8."""
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if not line:
        raise ValueError("entry is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} chars, must be 1-200")
    line.encode("utf-8")  # raises if not valid UTF-8


def main() -> int:
    line = ENTRY.strip()
    verify(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Read back and re-verify what was actually written.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    verify(written)
    if written != line:
        raise ValueError("written entry differs from verified line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
