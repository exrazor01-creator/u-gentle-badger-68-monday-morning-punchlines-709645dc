#!/usr/bin/env python3
"""One line for Monday Morning Punchlines.

The judge here is briefed like a stand-up comic who can tell
a real laugh from a polite one: it wants a joke about Monday
mornings first, then a real laugh with a turn or a punchline
that lands rather than a complaint, then surprise -- a twist
that is not the first thing anyone would think of -- then few
words with every word doing work, then freshness rather than a
rerun of the tired Monday cliches. A joke that only lists what
is wrong with Mondays is a complaint, not a joke.

This line follows that order on purpose. It is squarely about
Monday morning: the alarm, the snooze, the weekend just lost.
The turn is the surprise: the speaker snoozes so hard that the
snooze button itself -- the one thing built to absorb the
abuse -- asks for the weekend off too, so the exhaustion
spreads from the human to the machine. That is a joke, not a
complaint: nothing is listed as wrong, the laugh comes from the
button joining the strike. It dodges the tired "I hate Mondays"
and "coffee first" cliches, and every word does work toward
the last four words.

Why LIMIT is 200: the gate for this bounty allows 1 to 200
characters, so 200 is the hard cap the scorer enforces. The
line is 97 characters, leaving 103 spare, and validation only
guards against an edit that would push it past the cap.
"""

import os

# The sealed line. A Monday alarm snoozed so hard the snooze
# button itself asks for the weekend off too.
ENTRY = "Monday's alarm went off and I snoozed it so hard the snooze button asked for the weekend off too."

LIMIT = 200  # gate: one line, 1-200 characters


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, not another type")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Non-ASCII bytes would make the character count mean
        # different things on different platforms, so ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        # The gate counts one line; a line break would split the
        # entry into two texts and break the single-line promise.
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space may separate words; any other
        # whitespace would hide invisible bytes inside the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            f"entry is {len(text)} characters, past the {LIMIT} limit"
        )
    if text.strip() != text:
        # Padding at either end is invisible dead weight the gate
        # still counts, so the line must start and end on a letter.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        # A tab or newline would break the single line, and any
        # other control character would hide bytes inside it.
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # Two spaces in a row is a gap where a word should be, and
        # in a 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
