#!/usr/bin/env python3
"""Write one funny passive-aggressive note from a smart fridge to its owner.

The note is one line and a complete little scene: the fridge brags
about its sensor numbers (3 degrees, six days and counting), the
yogurt outlives the owner's diets without even trying, and the fridge
ends by betraying the owner and rooting for the yogurt. The note uses
nearly the whole 199-character allowance, every word earning its place.
"""

import os
from pathlib import Path

# The repo root is this file's own directory: every path resolves from
# here, never from the process working directory.
BASE_DIR = Path(__file__).resolve().parent

NOTE = (
    "I kept your yogurt at 3 degrees for six days and counting. "
    "It has now outlived three of your diets in a row, "
    "and it isn't even trying. "
    "I am already starting to root for the yogurt."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    # A relative output dir resolves against this file's own directory,
    # never against the process working directory.
    output_path = Path(output_dir)
    if not output_path.is_absolute():
        output_path = BASE_DIR / output_path
    output_path.mkdir(parents=True, exist_ok=True)
    # Fail loudly if the note ever drifts outside the gate (1-199 chars).
    if not 1 <= len(NOTE) <= 199:
        raise SystemExit(f"note is {len(NOTE)} chars, gate is 1-199")
    path = output_path / "entry.txt"
    # Exact bytes, no trailing newline: the file content is the judged text.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
