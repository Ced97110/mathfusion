"""Report fix/F*_textes.json into specs/*.json (run inside book/chNN)."""
import glob
import json

upd: dict = {}
for f in sorted(glob.glob("fix/F*_textes.json")):
    upd.update(json.load(open(f)))
done = set()
for sp in sorted(glob.glob("specs/L*.json")):
    entries = json.load(open(sp))
    new = []
    for e in entries:
        if e["code"] in upd:
            e = {**e, **upd[e["code"]]}
            done.add(e["code"])
        new.append(e)
    json.dump(new, open(sp, "w"), ensure_ascii=False, indent=1)
missing = set(upd) - done
print(f"{len(done)} entrées mises à jour ; codes absents des specs : {sorted(missing)}")
