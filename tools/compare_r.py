"""Print a_dire next to the reader's answer for a blind set R0x (run inside book/chNN).

Usage: python3 ../../tools/compare_r.py R01 [R02 ...]
"""
from __future__ import annotations

import glob
import json
import sys


def main(sets: list[str]) -> None:
    key = json.load(open("private/key.json"))
    specs = {e["code"]: e for f in glob.glob("specs/L*.json") for e in json.load(open(f))}
    for t in sets:
        raw = json.load(open(f"blind/{t}/reponses.json"))
        items = raw if isinstance(raw, list) else [{"img": k, **v} for k, v in raw.items()]
        for x in items:
            img = (x.get("img") or x.get("image") or x.get("id")).replace(".png", "")
            code = key[f"{t}/{img}"]
            lu = x.get("idee") or x.get("reponse") or str(x)
            print(f"{code} | A: {specs[code]['a_dire'][:170]}\n        L: {lu[:230]}")


if __name__ == "__main__":
    main(sys.argv[1:])
