#!/usr/bin/env python3
"""Write the phone's last words for the make.fun bounty.

The entry is one line, in the phone's own voice, at 1 percent battery:
the phone spent its last percent on this farewell instead of the alarm
that would have woken its owner, and the punch lands on the last words.
"""

import os

ENTRY = (
    "I could have spent my last percent on your alarm. "
    "I spent it on this sentence instead. Sleep well."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
