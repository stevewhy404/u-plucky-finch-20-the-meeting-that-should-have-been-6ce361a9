#!/usr/bin/env python3
"""Write one joke about a meeting that should have been an email.

Gate (kit-verified): /output/entry.txt must be UTF-8 text, 1-200 chars,
a single line, not only whitespace.
"""

import os

ENTRY = "We held a 47-minute meeting to decide the email was too long, then scheduled another meeting to discuss shortening it."


def verify(text: str) -> None:
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    verify(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
