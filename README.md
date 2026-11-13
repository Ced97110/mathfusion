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

1. Produire le chapitre avec le kit, puis `python3 kit/web.py <racine> <dossier web> content/toc.json`.
2. Copier `<dossier web>/chNN.html` dans `public/chapters/` et `<dossier web>/toc.json` dans `content/`.
3. `npm run build`, puis déployer.

Les polices (Inter, Lora, Noto Sans Math) viennent de Google Fonts.
