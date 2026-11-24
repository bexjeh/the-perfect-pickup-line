#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6.

Deterministic, offline, no randomness, no timestamps.
Prints the line to stdout and writes it to line.txt inside
MAKEFUN_OUTPUT_DIR (fallback ".").
"""

import os

LINE = (
    "My smartwatch just logged my heart rate as a workout, "
    "and all I did was walk over here to talk to you."
)

# The entry must be exactly one line: enforce it rather than assume it.
assert "\n" not in LINE and "\r" not in LINE


def main() -> None:
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "line.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
