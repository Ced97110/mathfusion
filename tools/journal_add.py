"""Insert a chapter row and its note into book/JOURNAL.md.

Usage: python3 tools/journal_add.py "<table row>" "<note line>"
The row goes after the last line starting with "| 20", the note at the end.
"""
from __future__ import annotations

import sys
from pathlib import Path


def main(row: str, note: str) -> None:
    path = Path("book/JOURNAL.md")
    lines = path.read_text().rstrip("\n").split("\n")
    last = max(i for i, ln in enumerate(lines) if ln.startswith("| 20"))
    new = lines[: last + 1] + [row] + lines[last + 1 :] + [note]
    path.write_text("\n".join(new) + "\n")
    print("journal : ligne", last + 2, "et note ajoutées")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
