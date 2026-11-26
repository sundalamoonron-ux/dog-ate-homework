#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why it
ate the homework, to /output/entry.txt.

The joke: the dog is the grader. It failed the homework, so it shredded
the evidence — quality control, not a crime. Setup -> punchline, one twist.
"""

import os

LINE = "I graded it first \u2014 it failed, so I shredded the evidence. That's quality control, not a crime."


def main() -> None:
    # Gate self-check: 1-200 chars, one line, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
