#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why it
ate the homework, to /output/entry.txt.
"""

import os

LINE = "I graded it first \u2014 it failed, so I shredded the evidence. That's quality control, not a crime."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
