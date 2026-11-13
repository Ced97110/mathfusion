"""Affiche le numéro du prochain chapitre à faire (le premier sans fichier dans content/toc.json et sans dossier book/chNN, pour ne pas reprendre un chapitre en cours dans une autre session), ou rien si tout est fait.
Ordre : 1 à 80, puis AP (avant-propos), puis A (annexe)."""
import json, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
toc = {str(c['key']): c for c in json.load(open(f'{root}/content/toc.json'))}
for k in [str(i) for i in range(1, 81)] + ['AP', 'A']:
    d = f'{root}/book/ch{int(k):02d}' if k.isdigit() else f'{root}/book/ch{k}'
    if not toc.get(k, {}).get('file') and not os.path.isdir(d): print(k); break
