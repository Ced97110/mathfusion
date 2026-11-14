# Contrôle des figures interactives — consigne d'un lot

Tu compares des figures interactives à la figure du livre de physique dont elles partent. Lot : `{BATCH}`. N'écris que `{BATCH}/check.json`. Ne modifie aucun autre fichier.

Pour chaque id de `{BATCH}/done.json` (liste `interactive`) :
- `ref` dans `{BATCH}/figures.json` : la figure du livre (image) ; son champ `page` : page du PDF ;
- `{BATCH}/shots/<id avec / remplacé par _>_default.png` : la version interactive dans son état de départ ;
- `{BATCH}/shots/<même nom>_alt.png` : la même après avoir déplacé le curseur (et tourné la vue 3D) ;
- la légende : `pdftotext -layout -f <page> -l <page+1> /Users/ced/Downloads/Cause_effets_finalite_physique_chimie_v3_verifie.pdf -` (cherche la ligne « Fig. … — » qui suit la figure ; elle peut manquer : regarde alors le texte autour).

Regarde les trois images avec ton outil de lecture d'image. Réponds à quatre questions, en phrases courtes :
1. Chaque élément de la figure du livre (objet, lettre, flèche, courbe, valeur) est-il dans l'état de départ, à la même place relative et de la même couleur ? Liste ce qui manque ou diffère.
2. Les nombres écrits dans la version interactive sont-ils compatibles avec la légende et le texte ? Liste tout nombre absent du livre.
3. Dans l'état modifié, ce qui change correspond-il à ce que dit le texte, et la figure reste-t-elle lisible et dans le cadre ?
Règle : si le dessin du livre n'est pas à l'échelle des nombres de son texte, la version interactive suit le texte. Une forme différente du dessin n'est alors pas un écart, à condition que les nombres affichés soient ceux du texte ; vérifie-les en refaisant le calcul du texte.
4. Verdict : `OK` si rien ne manque et rien n'est faux ; `ECART` sinon.

Écris `{BATCH}/check.json` : `{"<id>": {"verdict": "OK" | "ECART", "ecarts": ["…"]}}` avec une entrée par id. Vérifie à la fin que le nombre d'entrées égale le nombre d'ids.
