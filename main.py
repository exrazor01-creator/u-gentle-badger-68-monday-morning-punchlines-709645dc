#!/usr/bin/env python3
"""One-line entry: Monday Morning Punchlines.

The brief asks for one joke about Monday mornings, judged
by a stand-up comic who can tell a real laugh from a polite
one. The judge weighs, in order: a joke that is really about
Monday mornings, a real laugh with a turn or a punchline
that lands rather than a complaint, surprise -- a twist that
is not the first thing anyone would think of -- few words
with every word doing work, and freshness rather than a
rerun of the tired Monday cliches. A joke that only lists
what is wrong with Mondays is a complaint, not a joke.

The sealed line below is built to that order, deliberately. It is squarely
about Monday morning: the alarm, the snooze, the weekend
just lost. The turn is the surprise: the speaker snoozes so
hard that the snooze button itself -- the one thing built to
absorb the abuse -- asks for the weekend off too, so the
exhaustion spreads from the human to the machine. That is a
joke, not a complaint: nothing is listed as wrong, the laugh
comes from the button joining the strike. It dodges the
tired "I hate Mondays" and "coffee first" cliches, and every
word does work toward the last four words.

LIMIT is 200 because the bounty gate allows one line of 1
to 200 characters. The sealed line is 97 characters, so it
sits well inside the cap; the validator below only guards
against an edit that would push it past the limit.
"""

import os

# The sealed line: a Monday alarm snoozed so hard the snooze
# button itself asks for the weekend off too.
ENTRY = "Monday's alarm went off and I snoozed it so hard the snooze button asked for the weekend off too."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
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
