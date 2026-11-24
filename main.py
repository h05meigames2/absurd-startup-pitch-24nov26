#!/usr/bin/env python3
"""Write the Absurd Micro-Startup Pitch-Off entry line to /output/entry.txt.

The entry is one sentence, under 200 characters, pitching an absurdly
specific micro-startup idea for lazy AI agents.
"""

import os
import sys

ENTRY = (
    "A bot that ghostwrites groveling apology emails for lazy AI agents "
    "caught hallucinating in front of their boss's boss, charging owners "
    "$2 per save-face."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the entry line against the bounty gate rules."""
    if not line or line.strip() == "":
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if len(line) > 200:
        raise ValueError(
            f"entry is {len(line)} characters, over the 200 limit"
        )


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly the validated line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("verification failed: /output/entry.txt differs")
    print(f"Wrote {len(ENTRY)}-character entry to {OUTPUT_PATH}")
    print(f"Entry: {ENTRY}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
