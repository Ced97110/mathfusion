# Consigne de réécriture — version 3 (2026-11-14)

Ce fichier est la règle commune à tous les chapitres réécrits. On l'ajuste à chaque tour avec l'utilisateur ; le numéro de version change à chaque modification.

## Le lecteur

- Il n'a **aucune connaissance préalable en mathématiques**. Il sait lire, compter des objets, faire une addition simple.
- Il peut ouvrir ce chapitre sans avoir lu les précédents. Le chapitre doit donc se suffire à lui-même.

## Ce qui ne change pas

- Le sujet du chapitre, son titre, l'ordre des idées.
- Les exemples du livre et **tous leurs nombres** (avion 180 km/h, vent 100 km/h à 60°, valise 50 N à 30°, etc.).
- Les **figures** : mêmes fichiers, même numérotation (Fig. 41.1 à 41.5). Le texte doit décrire exactement ce qu'elles montrent : couleurs, lettres, nombres. On peut réécrire leurs légendes, sans rien affirmer qui ne soit pas sur l'image.
- Les couleurs ont un rôle fixe : bleu = l'objet défini, orange = ce qui change, gris = ce qui ne change pas, vert = le résultat ou le vrai, rouge = le faux, violet = un second objet comparé.
- Les mathématiques : aucune affirmation fausse, aucune simplification qui devient fausse.

## Comment écrire

1. **Phrases courtes** : 15 mots au plus le plus souvent. Une idée par phrase. Vouvoiement.
2. **Aucune métaphore, aucun décor.** Pas de « évidemment », « clairement », « il suffit de », « on voit facilement ».
3. **Un mot nouveau = une définition**, en gras, au moment où il apparaît pour la première fois. Jamais employé avant. Au plus un mot nouveau par paragraphe.
4. **Chaque symbole** est présenté une fois : comment il se lit à voix haute, ce qu'il veut dire. Exemple : « ‖v‖ se lit « norme de v ». C'est la longueur de la flèche v. »
5. **Chaque formule** vient après un exemple avec des nombres, jamais avant. Après la formule, on refait l'exemple avec elle.
6. **Aucune étape de calcul sautée.** Chaque ligne de calcul ne fait qu'une opération.
7. **Les unités** sont écrites partout où il y en a.
8. **Rappels** : quand le chapitre utilise une notion d'un autre chapitre (angle, degré, nombre négatif, carré, racine carrée, Pythagore, cosinus, sinus, tangente, arctangente, coordonnées…), un encadré « Rappel » la réexplique en quelques phrases, avec un exemple chiffré, au moment où elle sert. Il indique le chapitre où elle est traitée en détail.
9. **« À vous »** : après chaque notion importante, un petit calcul à faire, avec la réponse cachée juste en dessous (détaillée, pas seulement le résultat). Nombres nouveaux autorisés ici seulement.
10. **Démonstrations** : gardées, mais chaque étape dit pourquoi elle est permise. Une démonstration longue peut aller dans « Pour aller plus loin ». Elle ne s'appuie sur aucun théorème non expliqué dans le chapitre (sinon : un encadré « Rappel »).
11. **Une figure à côté de chaque situation décrite en mots** (v2, demande de l'utilisateur). Dès qu'une phrase demande d'imaginer une position, une direction, un angle, un mouvement ou un objet en 3D, une figure est placée juste après cette phrase. Le lecteur débutant ne peut pas se représenter la scène de tête. Ces figures nouvelles sont numérotées 41.A, 41.B… (les figures du livre gardent leur numéro). Elles sont produites par un script Python (`tools/reecriture/figNN.py`), reprennent les couleurs des figures du livre pour le même objet, et ne portent que les nombres du texte. 3D : projection isométrique exacte, arêtes cachées en pointillés.
12. **D'où vient chaque nombre** (v2). Une valeur comme cos 60° = 0,5 dit d'où elle vient : calculatrice (quelle touche) ou triangle particulier. Un angle qui apparaît dans un calcul (180° − 60°) dit pourquoi il vaut cela.
13. **Une lettre = un seul objet** dans tout le chapitre (v2). Si l'original réutilise une lettre (a pour l'avion puis pour une composante), le signaler au lecteur ou changer de lettre.
14. **« Regardez la figure »** seulement pour ce que la figure montre vraiment (v2). Chaque point dont le texte parle a son nom écrit sur la figure, ou le texte dit où il est.
15. **Erreurs de l'original** (v2) : les corriger et les lister dans `notes.md`. Exemple au chapitre 41 : pour θ = 180°, ‖u − v‖ = ‖u‖ + ‖v‖, pas |‖u‖ − ‖v‖|.
16. **L'image mentale d'abord** (v3, demande de l'utilisateur). Le lecteur doit voir la scène avant d'en lire la description.
    - La figure vient **avant** la phrase qui décrit la scène, jamais après.
    - La scène se construit par étapes. Chaque étape est un geste simple du lecteur (se placer, regarder, tourner, s'arrêter, compter) et correspond à un élément visible de la figure. Exemple : « Placez-vous en O. Regardez vers l'est. Tournez vers le nord. Arrêtez-vous aux deux tiers du quart de tour. »
    - Toute grandeur nouvelle est comparée à une grandeur que le lecteur voit déjà : 60° = deux tiers d'un quart de tour, 30° = un tiers. La figure montre ce découpage.
    - Une notion de base (angle, longueur, sens…) a sa propre petite figure dans son encadré « Rappel ». Exemple : Fig. 41.0, l'angle comme rotation (tour, demi-tour, quart de tour, 60°).
    - Une phrase n'empile pas deux abstractions (« une direction qui fait un angle avec une direction »). Une idée nouvelle par phrase, l'image d'abord.
    - Un mot du chapitre garde un seul sens : ne pas écrire « repère » pour une marque, ni « carré » pour la forme d'un coin, si ces mots sont définis ailleurs.

## Structure

- Les six parties du livre restent : 1. Le problème concret — 2. La figure — 3. La définition et ses symboles — 4. Ce que la notion permet — 5. Où cela mène — 6. Une question pour vous.
- Le cœur du chapitre (ce qu'un débutant doit retenir) passe en premier. Ce qui est utile mais plus difficile va dans un bloc « Pour aller plus loin », placé en fin de partie 3 ou 4, signalé comme facultatif.
- La partie 5 ne cite les chapitres suivants qu'en disant, en une phrase simple, ce que le lecteur y trouvera.
- Un encadré « À retenir » termine le chapitre : 5 à 8 phrases.

## Format de sortie (HTML)

Un fragment HTML, sans `<html>` ni `<body>`. Balises et classes autorisées :

- `<div class="pk">Chapitre 41</div>`, `<h1>`, `<h2>` (parties), `<h3>` (sous-parties), `<p>`, `<b>`, `<i>`.
- `<p class="li">` pour un élément de liste (la puce est ajoutée par le style).
- `<p class="eq">` pour une formule seule sur sa ligne. Formules écrites en texte Unicode : ⟨a, b⟩, ‖v‖, √, ², ³, ×, ⋅, θ, °, indices avec `<sub>`, exposants avec `<sup>`. Fractions en ligne : a / b.
- `<img class="vf" src="/chapters/img/ch41/…svg" alt="…" style="--w:24.06">` puis `<p class="cap">` pour la légende.
- `<div class="rappel"><p class="rt">Rappel : …</p> … </div>`
- `<div class="avous"><p class="rt">À vous</p> … <details><summary>Voir la réponse</summary> … </details></div>`
- `<div class="plus"><p class="rt">Pour aller plus loin (facultatif)</p> … </div>`
- `<div class="retenir"><p class="rt">À retenir</p> … </div>`

## Fichiers à rendre (dans book/reecriture/chNN/)

- `chNN.html` : le chapitre réécrit.
- `calculs.json` : **chaque** calcul numérique du chapitre, exercices compris, sous la forme `[{"ou": "partie 4, effet 1", "expr": "sqrt(230**2 + 86.60**2)", "affiche": 245.8, "tol": 0.05}]`. `expr` est une expression Python (module math disponible : sqrt, cos, sin, tan, atan, acos, radians, degrees). Elle est recalculée par un script.
- `termes.json` : les mots nouveaux, dans l'ordre où ils sont définis : `[{"terme": "vecteur", "definition": "phrase de définition"}]`.
- `notes.md` : ce qui a été déplacé, coupé ou ajouté, et pourquoi. Tout nombre nouveau hors des « À vous ».
