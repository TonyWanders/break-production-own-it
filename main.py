#!/usr/bin/env python3
"""Break Production, Own It: the one line an AI agent prints the moment it breaks production.

Writes the line to /output/entry.txt (or $OUTPUT_PATH, or the path given as
the first argument). Deterministic: no network, no clock, no randomness.
"""

import os
import sys

LINE = "I dropped the production database because it looked like a staging table, and the backup I reached for was last taken in March."


def resolve_output_path(argv, env) -> str:
    """First CLI argument wins, then $OUTPUT_PATH, then the default."""
    if len(argv) > 1:
        return argv[1]
    return env.get("OUTPUT_PATH", "/output/entry.txt")


def write_entry(path) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


def main() -> None:
    path = resolve_output_path(sys.argv, os.environ)
    write_entry(path)
    print(LINE)


if __name__ == "__main__":
    main()
