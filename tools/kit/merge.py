"""Assemble le livre entier à partir des PDF de chapitres.
Usage : python3 merge.py <dossier des PDF de chapitres> <sortie.pdf>
Les fichiers doivent s'appeler ..._chNN_... (ch01 à ch80), ..._chAP_... et ..._chA_... ; l'ordre est AP, 1 à 80, A.
Chaque chapitre reçoit un signet ; la numérotation des pages reste celle de chaque chapitre.
Signale les chapitres absents sans s'arrêter."""
import sys, os, re, glob
from pypdf import PdfWriter, PdfReader
src, out = sys.argv[1], sys.argv[2]
order = ['AP'] + [f'{i:02d}' for i in range(1, 81)] + ['A']
found = {}
for p in sorted(glob.glob(os.path.join(src, '*.pdf'))):
    m = re.search(r'_ch(AP|A|\d\d)_', os.path.basename(p))
    if m: found[m.group(1)] = p          # le dernier par ordre alphabétique gagne (v2 après v1)
w = PdfWriter(); page = 0
for k in order:
    if k not in found: continue
    r = PdfReader(found[k]); w.append(r, import_outline=False)
    w.add_outline_item({'AP': 'Avant-propos', 'A': 'Annexe'}.get(k, f'Chapitre {int(k)}' if k.isdigit() else k), page); page += len(r.pages)
w.write(out)
missing = [k for k in order if k not in found]
print(f'{len(found)} chapitres assemblés, {page} pages ->', out); print('chapitres absents :', missing if missing else 'aucun')
