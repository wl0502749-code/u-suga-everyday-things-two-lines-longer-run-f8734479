#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of a queue to /output/entry.txt:
line 1 explains it to a 10-year-old in a single vivid sentence built
on one analogy; line 2 says what the analogy maps and what it leaves out.
"""

import os

ENTRY = (
    "A queue is a caterpillar made of people, shuffling forward one tiny step "
    "at a time because the head can only nibble one leaf at a time.\n"
    "It maps the slow shuffle and a front that serves one person at a time, "
    "but leaves out that people can leave, grumble, or swap places, which "
    "caterpillars never do.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
