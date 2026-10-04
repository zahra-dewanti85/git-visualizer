"""git-visualizer — Zahra Dewanti.

Kept plain on purpose — no imports beyond the stdlib.
"""

from __future__ import annotations

import sys


def total(a: int, b: int) -> int:
    """Plain addition, here so the module has something testable."""
    return a + b


def main(argv: list[str]) -> int:
    if len(argv) >= 3 and argv[1].isdigit() and argv[2].isdigit():
        print(total(int(argv[1]), int(argv[2])))
        return 0
    print("usage: main.py <int> <int>")
    print(f"hint: try 7 and 16")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
