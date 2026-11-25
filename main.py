"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name to /output/entry.txt. The name is a
single line that implies a whole story in a glance: a divorce where
she walked out with the router and left the kids behind. The reader
fills in the rest — the narrator, stuck with the children and no
internet, staring at the network list. No network, no input files,
no secrets — the text is a constant below.
"""

import os

NAME = "SheTookTheRouterNotTheKids"

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate: 1 to 32 chars, not only whitespace."""
    if not 1 <= len(text) <= 32:
        raise ValueError(f"entry is {len(text)} characters, must be 1-32")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def write_entry() -> str:
    """Write the Wi-Fi name to the output path and return it."""
    validate(NAME)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(NAME)
    return NAME


if __name__ == "__main__":
    write_entry()
