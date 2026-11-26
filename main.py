#!/usr/bin/env python3
"""Entry for make.fun: Funniest Sign on a Haunted Server Room Door.

Writes a single funny sign line to /output/entry.txt.
Standard library only.
"""

import os
import stat

ENTRY = "WARNING: The ghost in Rack 7 has root access. Do not reboot him \u2014 he remembers."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Check the sign line is a single clean line; return it unchanged."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 120, f"line length {len(text)} out of range 1..120"
    assert text == text.strip(), "line has leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(ch) >= 32 and ord(ch) != 127 for ch in text), "control chars found"
    assert text.strip(), "line must not be only whitespace"
    return text


def main() -> None:
    line = validate(ENTRY)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
