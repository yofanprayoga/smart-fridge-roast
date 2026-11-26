#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins — make.fun entry.

Writes one line (1-160 chars) to /output/entry.txt: a roast of the smart
fridge or any smart home gadget the writer shares a house with.

Usage:
    python3 main.py                 # Option 1 (default)
    python3 main.py --option 2      # Option 2
    python3 main.py --option 3      # Option 3
    ENTRY_TEXT="..." python3 main.py # override with custom text
"""

import os
import sys
from pathlib import Path

OPTIONS = {
    1: "My fridge has Wi-Fi, a touchscreen, and opinions — it locked me out of the ice maker for 'excessive midnight snacking'.",
    2: "My smart fridge texts me 'we're out of milk' from three feet away, then orders twelve cartons and judges me for drinking them.",
    3: "My smart fridge updated its firmware at 3 AM, forgot what food is, and now greets me every morning with 'Have you tried salad?'",
}

MAX_CHARS = 160


def main() -> int:
    option = 1
    args = sys.argv[1:]
    if "--option" in args:
        idx = args.index("--option")
        try:
            option = int(args[idx + 1])
        except (IndexError, ValueError):
            print("usage: main.py [--option N]", file=sys.stderr)
            return 2
    if option not in OPTIONS:
        print(f"unknown option {option}; valid: {sorted(OPTIONS)}", file=sys.stderr)
        return 2

    text = os.environ.get("ENTRY_TEXT", OPTIONS[option])

    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")  # no trailing newline
    print(f"option {option}: {len(text)} chars -> {out}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
