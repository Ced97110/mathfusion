"""Affiche le numéro du prochain chapitre à faire (le premier sans fichier dans content/toc.json), ou rien si tout est fait.
Ordre : 1 à 80, puis AP (avant-propos), puis A (annexe)."""
import json, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
toc = {str(c['key']): c for c in json.load(open(f'{root}/content/toc.json'))}
for k in [str(i) for i in range(1, 81)] + ['AP', 'A']:
    if not toc.get(k, {}).get('file'): print(k); break
