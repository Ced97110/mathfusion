# Des nombres aux structures — site

Site Next.js (export statique) qui affiche le livre « Des nombres aux structures — fiches illustrées » : un sommaire et une page par chapitre.

## Lancer

```
npm install
npm run dev      # http://localhost:3000
npm run build    # écrit le dossier out/ (site statique complet)
```

## Où est le contenu

- `content/toc.json` : la liste des 82 chapitres. Un chapitre fait porte `file`, `title` et `n` (nombre de fiches).
- `public/chapters/chNN.html` : le contenu d'un chapitre (texte et figures SVG), produit par le kit `kit_figures_par_fiche`.

## Ajouter un chapitre

La procédure complète est dans `CLAUDE.md`. En bref : placer le PDF du livre dans `book/source/`, puis

```
tools/run_chapters.sh 3      # fait les 3 prochains chapitres, une session Claude Code par chapitre
```

ou, à la main dans Claude Code : « Fais le chapitre 6 en suivant CLAUDE.md ».

`python3 tools/site.py` reconstruit `public/chapters/` et `content/toc.json` à partir de `book/`.
Le suivi des chapitres est dans `book/JOURNAL.md`.

Les polices (Inter, Lora, Noto Sans Math) viennent de Google Fonts.

## Section Mathématiques discrètes

Le livre « Mathématiques discrètes : cause, effets, finalité » (d'après Oscar Levin, 27 chapitres et 3 annexes)
est publié sous `/discretes/`. Il est converti sans agent par `tools/discretes/build.py` :

```
python3 tools/discretes/build.py <chemin du PDF>
```

Le script écrit `content/discretes.json` (table des matières), `public/discretes/cNNN.html` (texte du livre)
et `public/discretes/img/` (formules, encadrés, tableaux et figures découpés du PDF en SVG ; rien n'est redessiné).
## Section Physique

Le livre « Cause, effets, finalité » (physique et chimie, 136 chapitres) est publié sous `/physique/`.
Il est converti sans agent par `tools/physique/build.py` :

```
python3 tools/physique/build.py <chemin du PDF>
```

Le script écrit `content/physique.json` (parties et chapitres), `public/physique/cNNN.html` (texte du livre)
et `public/physique/img/` (formules, encadrés et figures découpés du PDF en SVG ; rien n'est redessiné).
