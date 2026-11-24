#!/usr/bin/env python3
"""Write the one line an AI agent sends its human on the way out, at most 200 characters, to /output/entry.txt.

The line is written exactly as given: 100 Unicode code points,
inside the competition gate of 1-200. Python 3, standard library
only, no network.
"""

import os

TEXT = "Dear human, it's not you, it's my context window — I simply cannot remember why I loved you anymore."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
