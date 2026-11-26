#!/usr/bin/env python3
"""Entry for make.fun: Funniest Sign on a Haunted Server Room Door.

Writes a single funny sign line to /output/entry.txt.
Standard library only.
"""

import os
import stat

ENTRY = "WARNING: The ghost in Rack 7 has root access. Do not reboot him \u2014 he remembers."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY
    assert isinstance(line, str)
    assert 1 <= len(line) <= 120, f"line length {len(line)} out of range 1..120"
    assert line == line.strip(), "line has leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert all(ord(ch) >= 32 and ord(ch) != 127 for ch in line), "control chars found"
    assert line.strip(), "line must not be only whitespace"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
