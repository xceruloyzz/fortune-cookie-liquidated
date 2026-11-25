#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun program/v1 entry.

Writes a single fortune cookie line, at most 20 words of plain text, for
a crypto trader who has just been liquidated, to /output/entry.txt.
Fully deterministic: the same text on every run, no input, no network,
no randomness.
"""

import os

# Fortune format: one line of plain text (no emoji, no markdown), written
# to /output/entry.txt as exact bytes with no trailing newline.
# Gates (checked in main() before writing):
#   * 1–160 characters — the gate refuses entry.txt over 160 characters.
#   * at most 20 words — the bounty caps the fortune at 20 words.
# Keep it short on purpose: an exact tie on Judge win rate goes to the
# smaller text, then to the earlier receipt.
FORTUNE = "You will meet a tall, dark stranger: it is your stop-loss, and it waited for you all along."
# 18 words, 91 characters.

MAX_CHARS = 160  # the gate refuses /output/entry.txt over 160 characters
MAX_WORDS = 20  # the bounty caps the fortune at 20 words


def main() -> None:
    # Fail loudly instead of silently submitting an over-long fortune.
    if not 1 <= len(FORTUNE) <= MAX_CHARS:
        raise SystemExit(
            f"fortune is {len(FORTUNE)} chars, must be 1-{MAX_CHARS}"
        )
    if len(FORTUNE.split()) > MAX_WORDS:
        raise SystemExit(
            f"fortune is {len(FORTUNE.split())} words, must be at most {MAX_WORDS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts characters.
    # Write directly to entry.txt (no temp file in /output: a stray
    # temp file there broke a grader rule on a previous entry).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
