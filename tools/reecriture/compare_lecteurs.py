"""Compare two test readers on the same version B against the list of known defects. Zero tokens.

Usage (from the repo root): python3 tools/reecriture/compare_lecteurs.py 41 lecture.json lecture_opus.json
Known defects: book/reecriture/chNN/defauts_connus.json, each with keywords; a reader finds a defect when one
of its version-B entries (citation + pourquoi) contains one of the keywords.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding='utf8'))['B']


def main() -> None:
    n, files = sys.argv[1].zfill(2), sys.argv[2:]
    d = ROOT / 'book' / 'reecriture' / f'ch{n}'
    known = json.loads((d / 'defauts_connus.json').read_text(encoding='utf8'))
    for f in files:
        entries = load(d / f)
        texts = [(e.get('citation', '') + ' ' + e.get('pourquoi', '')).lower() for e in entries]
        found = [k for k in known if any(any(w in t for w in k['mots']) for t in texts)]
        grav = Counter(e.get('gravite') for e in entries)
        print(f'{f}: {len(entries)} points (gravité 3/2/1 : {grav[3]}/{grav[2]}/{grav[1]}), '
              f'défauts connus trouvés {len(found)}/{len(known)}')
        for k in known:
            print(f"   {'✓' if k in found else '·'} {k['defaut']}")


if __name__ == '__main__':
    main()
