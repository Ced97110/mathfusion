# mathfusion — « Des nombres aux structures », fiches illustrées

Ce dépôt contient deux choses :

- le **site** Next.js (export statique) qui affiche le livre : `app/`, `lib/`, `content/toc.json`, `public/chapters/chNN.html` ;
- l'**atelier** qui fabrique les chapitres : `tools/` (scripts et consignes) et `book/` (sources de chaque chapitre).

Le livre source est un PDF de 14 315 fiches en 82 chapitres (avant-propos, 1 à 80, annexe). Une fiche = un concept, six rubriques. Le travail : donner à chaque fiche **une figure** qui fait voir le concept, vérifiée par un lecteur qui ne voit que l'image.

Langue de travail et des réponses : français, phrases simples, sans métaphore.

## Avant de commencer

- Le PDF du livre doit être à `book/source/Des_nombres_aux_structures_fiches.pdf` (il n'est pas dans Git). S'il manque, s'arrêter et le demander.
- Outils nécessaires : Python 3 avec `matplotlib`, `numpy`, `pillow` ; Poppler (`pdftohtml`) ; Node.js. Vérifier avant de lancer ; s'il en manque un, le dire et s'arrêter.
- Chapitre à faire : celui demandé, sinon `python3 tools/next_chapter.py`.

## Règles de budget (prioritaires)

- L'utilisateur est sur un plan Ultra et ne veut pas dépasser 50 % d'utilisation hebdomadaire. Dix chapitres par session, enchaînés sans attendre (décision du 2026-11-12). Commit et push à la fin de chaque chapitre.
- Chaque sous-agent coûte environ 80 000 tokens au démarrage, quel que soit le travail : peu d'agents, gros lots.
- Tout ce qui est mécanique passe par les scripts (zéro token).
- Modèles des sous-agents : **Sonnet** pour concevoir et coder les figures, juger, corriger ; **Haiku** pour la lecture à l'aveugle. Pas d'Opus, sauf si la réussite au premier test tombe sous 75 % (le signaler dans le bilan avant de l'utiliser).
- Un seul tour de correction. Le superviseur ne commente pas chaque étape : une ligne au plus, bilan à la fin.

## Procédure pour un chapitre N

Toutes les commandes partent de la racine du dépôt, sauf mention contraire.

1. **Préparer.** `python3 tools/kit/pipe.py setup N book/source/Des_nombres_aux_structures_fiches.pdf book` crée `book/chNN/`, découpe les fiches, écrit `meta.json` et les lots `batches/Lxx.txt` (16 fiches par lot). Vérifier que la sortie n'annonce aucune anomalie.
2. **Figures.** Un sous-agent Sonnet par lot, tous lancés ensemble, avec la consigne : « Lis le fichier `<chemin absolu de book/chNN>/figure_prompt.md` et exécute exactement ses instructions, en remplaçant partout {L} par Lxx. » Chaque agent écrit `figsrc/<code>.py` et `specs/Lxx.json`.
3. **Contrôle.** Dans `book/chNN` : `python3 pipe.py check`. La sortie doit donner aucun échec, toutes les figures, aucune légende manquante. Corriger ce qui manque avant de continuer.
4. **Lecture à l'aveugle.** `python3 pipe.py blind`, puis un sous-agent Haiku par dossier `blind/Txx` : « Lis `<…>/blind_prompt.md` et exécute ses instructions en remplaçant {T} par Txx. Traite toutes les images. »
5. **Jugement.** `python3 pipe.py judgein`, puis un seul sous-agent Sonnet : « Lis `<…>/judge_prompt.md` et exécute ses instructions en remplaçant {J} par J1. Traite tous les objets et vérifie le nombre d'entrées. »
6. **Correction.** `python3 pipe.py fixin`, puis un seul sous-agent Sonnet (deux au-delà de 20 figures) : « Lis `<…>/fix_prompt.md` et exécute ses instructions en remplaçant {F} par F1. Lance tes scripts un par un. »
7. **Contrôle des corrections.** Préparer un jeu aveugle avec les seules figures corrigées (fonction `blind(codes, 'R')` de `pipe.py`), un sous-agent Haiku, puis comparer soi-même les réponses aux phrases « a_dire ». Pas d'agent juge pour une douzaine de lignes.
8. **Site.** `python3 tools/site.py`, puis `npm install` (si besoin) et `npm run build`. Le site doit se construire sans erreur et `content/toc.json` doit montrer le chapitre N comme fait.
9. **Journal.** Ajouter une entrée à `book/JOURNAL.md` : date, chapitre, nombre de fiches, réussies au premier test, réussies après correction, liste des figures encore partielles avec ce qui manque, tout nombre inventé par un agent, toute couleur du livre changée à cause des rôles.
10. **Commit et push.** Un commit « Chapitre N : <titre> (<n> fiches) » sur `main`, puis `git push`. Ne pas pousser si la construction du site a échoué.
11. **Bilan** en réponse finale : les chiffres du journal, en quelques lignes.

## Règles de fond

- La figure est le miroir du concept du titre : chaque partie du concept a un élément visuel, chaque élément représente une partie. Aucun décor, aucune métaphore, uniquement les nombres de la fiche.
- Couleurs à rôle fixe, dans les figures comme dans les rubriques : bleu = l'objet défini, orange = ce qui change, gris = ce qui ne change pas, vert = le résultat ou le vrai, rouge = le faux, violet = un second objet comparé.
- 3D seulement pour un concept à trois dimensions, en projection isométrique exacte (`cubes`, `iso` de `figstyle.py`).
- Le texte des fiches n'est jamais réécrit.

## Reprendre après un clone

Les dossiers `book/chNN` ne gardent dans Git que les sources (`fiches.json`, `meta.json`, `specs/`, `figsrc/`). Pour retravailler un chapitre : `python3 tools/kit/pipe.py adopt book/chNN`, puis dans ce dossier `python3 pipe.py check` régénère toutes ses figures.

## Repères mesurés

- Chapitres 1 à 4 (ancien réglage, Opus à la conception) : 82 à 91 % de réussite au premier test, environ 40 000 tokens par fiche.
- Chapitre 5 (réglage de cette procédure) : 94 % au premier test, 99 % après correction, environ 14 600 tokens par fiche.
- À partir du chapitre 42 (groupes, anneaux, Galois), les concepts sont plus abstraits : surveiller le taux de réussite.
