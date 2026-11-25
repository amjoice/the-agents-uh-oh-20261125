#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word: "Recalculating" — the voice of a lost GPS, an agent that has
no idea where it is going and says so, mid-task, in machine voice.
"""
import os

WORD = "Recalculating"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 99 characters,
# not only white space, and exactly one word with nothing attached.
assert 1 <= len(WORD) <= 99, "word must be 1-99 characters"
assert WORD.split() == [WORD], "entry must be exactly one word"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

if __name__ == "__main__":
    main()
