"""The Meeting That Should Have Been One Line.

One-sentence entry for the make.fun bounty of the same name: the whole
meeting -- approval, deadline, and source -- compressed into a single
line, because it was all in the email from this morning that nobody
opened.

The program writes the entry verbatim (95 characters, no trailing
newline) to /output/entry.txt and echoes it to stdout.
"""

import os
import sys

ENTRY = "It's approved, it's due Friday, and it's all in the email from this morning that nobody opened."
OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write ENTRY to path, creating the parent directory if needed.

    Returns True on success. On failure the error is reported to stderr
    and False is returned, so the caller can still echo the entry.
    """
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError as exc:
        sys.stderr.write(f"error: could not write {path}: {exc}\n")
        return False
    return True


def main():
    write_entry()
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
