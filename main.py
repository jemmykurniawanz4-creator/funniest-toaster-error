"""Write the entry for 'The Funniest Toaster Error Message'.

Line choice: the joke is the toaster's deadpan defence — it did its job
perfectly and calmly blames the user's own browning setting. It reads
like a real appliance error, avoids the obvious toast puns, and lands
in a single read, well under the 120-character limit.
"""

from pathlib import Path

ENTRY_TEXT = "ERROR: I browned it exactly as requested. The request was the problem."
OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(ENTRY_TEXT) <= MAX_CHARS, "entry must be 1-120 characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
