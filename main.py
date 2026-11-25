"""One Word From Grandma — the single word a grandma would text about AI.

The word is "Doohickey": the word grandmothers reach for when a gadget
does something they cannot name. Faced with AI, grandma does not explain
it, she labels it the way she labels every mysterious box with blinking
lights in her house — a doohickey. Warm, baffled, and one word long.

This program prints the word to stdout and writes it to /output/entry.txt,
the path the make.fun harness reads. Python standard library only; the
output is fully deterministic.
"""

import os

WORD = "Doohickey"
OUTPUT_PATH = "/output/entry.txt"

# The brief's gate, enforced here before anything is written out.
# The judge reads the file exactly as written, so the word must survive
# on its own: one token, no hidden whitespace, no extra characters.
assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
assert WORD == WORD.strip(), "no leading or trailing whitespace"
assert not any(ch.isspace() for ch in WORD), "no whitespace anywhere"
assert len(WORD.split()) == 1, "exactly one word, no spaces inside"
assert WORD.isalpha(), "letters only, no punctuation tricks"
assert all(ord(ch) >= 32 for ch in WORD), "no control characters"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
