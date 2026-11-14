# Figures interactives du livre de physique — consigne d'un lot

Tu écris les versions interactives des figures d'un lot. Dépôt : `/Users/ced/Desktop/mathfusion/.worktrees/physique` (lance toutes les commandes depuis ce dossier). Lot : `{BATCH}`. Ne fais ni commit ni push. N'écris que dans `public/physique/fig/cNNN/` (les chapitres de ton lot) et dans `{BATCH}/`. Ne modifie pas `lib.js`, `kit.js` ni `index.json` (un autre agent travaille en même temps).

## Contrat
La figure du livre (`public/physique/img/<id>.svg`, découpée du PDF) reste dans la page. On ajoute à côté un module ES `public/physique/fig/<id>.js` qui exporte `mount(el)` et dessine dans la `<div>` vide `el`. Lis d'abord `public/physique/fig/lib.js` (`svg`, `add`, `clear`, `slider`, `resetButton`, `reducedMotion`, `view3d`) et `public/physique/fig/kit.js` (couleurs du livre `COL`, `txt`, `arrow`, `readout`, `fr`, `poly`). Prends exemple sur `public/physique/fig/c036/*.js` et `c104/p1251_11.js` (3D). Aucune bibliothèque externe. Moins de 8 Ko par module. Si tu as besoin d'un helper qui n'existe pas, écris-le dans ton module.

## Matériau brut, pour chaque figure de `{BATCH}/figures.json`
- l'image du livre : le champ `ref` (regarde-la avec ton outil de lecture d'image) ;
- le SVG d'origine : couleurs exactes (`rgb(...)`) ;
- le texte : `pdftotext -layout -f <page-1> -l <page+2> /Users/ced/Downloads/Cause_effets_finalite_physique_chimie_v3_verifie.pdf -` (légende complète, et ce que le texte dit de la figure et de ses nombres).

## Trier d'abord
Une figure ne devient interactive que si une grandeur du concept peut varier et que la faire varier montre quelque chose que le texte dit (ce qui change, ce qui ne change pas, une relation). Sinon, ne fais rien : la figure du livre reste. La 3D seulement si le concept est en trois dimensions ; elle s'ouvre sur l'orientation du livre (`start` de `view3d`), arêtes cachées en pointillés.

## Règles
- **État de départ = la figure du livre** : mêmes éléments, lettres, valeurs, couleurs, disposition. `resetButton` y ramène.
- Le curseur porte sur ce qui change dans le texte. Les valeurs affichées sont recalculées par la formule du livre, jamais écrites en dur.
- **Aucun nombre inventé.** Bornes des curseurs autour de la valeur du livre ; tout nombre mesuré sur le dessin est signalé dans le rapport.
- **Les nombres du texte priment sur les mesures du dessin.** Si le dessin n'est pas à l'échelle, l'état de départ affiche les valeurs du texte (vérifie-les en refaisant le calcul du texte) ; le dessin s'en approche autant que possible.
- Toute étiquette suit l'objet qu'elle nomme : aucune position en dur pour un texte placé près d'un objet qui bouge.
- Animation seulement avec un bouton Lecture/Pause, jamais automatique, coupée si `reducedMotion()`.
- `aria-label` sur le SVG qui dit ce que montre la figure. Aucune décoration, aucune métaphore.

## Contrôle (à relancer jusqu'à ce que tout passe)
1. `python3 tools/physique/figtest.py {BATCH}/shots <id> <id> ...` avec les ids que tu as faits : chaque ligne commence par `OK`.
2. Regarde chaque `{BATCH}/shots/<nom>_default.png` à côté de l'image du livre et corrige tout écart. Regarde `<nom>_alt.png` (curseurs à 80 %, vue tournée) : lisible et dans le cadre.

## Rendu
Écris `{BATCH}/done.json` : `{"interactive": [ids faits], "static": {"<id>": "raison en une phrase"}}`.
Rapport final court : par figure faite, le curseur, ses bornes et pourquoi, les écarts restants, les nombres qui ne viennent pas du texte ; la dernière sortie de figtest.
