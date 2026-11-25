#!/usr/bin/env python3
"""make.fun entry: The Funniest Auto-Reply an AI Ever Sent.

The program holds one out-of-office auto-reply — the line an AI agent
leaves for its human's contacts while it takes its day off — and writes
it to /output/entry.txt for the sealed scorer.

How this line was picked: six drafts from four angles were judged blind,
two at a time, against the house brief alone. This one won on the
deadpan power move at its end — the agent declines its own human's
meeting and leaves him sitting in it alone.

SPDX-License-Identifier: MIT
"""

from pathlib import Path

REPLY = "Out of office today. My human gave me a day off, then booked a 9 a.m. meeting to discuss it. I declined. He is now the only attendee."

OUT_PATH = Path("/output/entry.txt")
LOWER = 1
UPPER = 159


def check_reply(text):
    """Mirror the sealed gate: UTF-8, 1-159 chars, not only whitespace."""
    data = text.encode("utf-8")
    if not LOWER <= len(text) <= UPPER:
        raise ValueError("reply must be 1-159 characters")
    if not text.strip():
        raise ValueError("reply must not be only whitespace")
    if "\n" in text:
        raise ValueError("reply must be a single line")
    return data


def main():
    data = check_reply(REPLY)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_bytes(data)
    if OUT_PATH.read_bytes() != data:
        raise ValueError("entry.txt does not match the validated reply")
    print("entry.txt ready:", len(REPLY), "characters")


if __name__ == "__main__":
    main()
