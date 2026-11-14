"""Rewrite batches/Lxx.txt of a chapter with a larger batch size (same format as pipe.setup).

Usage: python3 tools/rebatch.py book/chNN 30
A last batch smaller than 8 cards is merged into the previous one.
"""
from __future__ import annotations

import glob
import json
import os
import sys


def main(base: str, size: int) -> None:
    sys.path.insert(0, base)
    from pipe import plain  # type: ignore[import-not-found]

    cards = json.load(open(f"{base}/fiches.json"))
    lots = [cards[i : i + size] for i in range(0, len(cards), size)]
    if len(lots) > 1 and len(lots[-1]) < 8:
        tail = lots.pop()
        lots[-1] = lots[-1] + tail
    for old in glob.glob(f"{base}/batches/L*.txt"):
        os.remove(old)
    for bi, lot in enumerate(lots, 1):
        out = []
        for f in lot:
            out.append(
                f"=== FICHE {f['code']} ===\nTITRE (le concept) : {plain(f['title'])}\n"
                f"PASSAGE DU LIVRE : {plain(f['passage'])}"
            )
            for k in "123456":
                r = f["rub"][k]
                out.append(f"{k}. {r['label']}. " + "\n   ".join(plain(p) for p in r["paras"] if p))
            out.append("")
        open(f"{base}/batches/L{bi:02d}.txt", "w").write("\n".join(out))
    print(base, "| lots", [len(b) for b in lots])


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
