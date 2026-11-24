#!/usr/bin/env python3
"""Houseplant Out-of-Office entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Deterministic, self-contained, stdlib only.
"""

import os

ENTRY = "Out of office: ignored since March, alive purely out of spite. Your email? Filed under compost."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
