Tu conçois puis tu codes UNE figure par fiche, pour un livre de mathématiques destiné à des débutants complets (« des gens ayant peur des mathématiques »). Une fiche = un concept. La figure doit donner l'image mentale du concept.

À lire d'abord : ton lot __BASE__/batches/{L}.txt ; la liste des concepts du chapitre __BASE__/titles.txt (pour voir les voisins) ; la bibliothèque __BASE__/figstyle.py en entier (fonctions, rôles de couleur) ; l'exemple __BASE__/figsrc/test.py s'il existe.

A. CONCEVOIR (pour chaque fiche, avant de coder)
1. Écris en une phrase ce que le lecteur doit pouvoir DIRE après la figure ("a_dire") : le concept du TITRE tel que la rubrique 4 l'explique — pas le cas concret, pas la limite.
2. Découpe le concept en 2 à 5 parties. Chaque partie a un élément visuel ; chaque élément visuel représente une partie. Rien de décoratif, pas de pictogramme, pas de métaphore : on dessine l'objet mathématique ou le cas concret de la fiche.
3. Reprends exactement les nombres et les lettres de la fiche (rubriques 1 et 4). N'invente aucun nombre.
4. La forme suit le concept : distinction → les voisins côte à côte, la différence marquée ; avant/après → deux états et l'action ; méthode → les étapes dans l'ordre sur le cas chiffré ; preuve → départ, étape qui porte le poids, arrivée ; signe ou notation → le signe en grand, découpé, chaque morceau relié à son sens ; quantité, ordre, position → objets comptables, droite graduée, cases ; contre-exemple → le cas qui marche et le cas qui casse (rouge).
5. Une seule idée par figure. Si deux idées se disputent la place, garde celle du titre. Un élément qui pourrait faire croire l'idée contraire est retiré.
6. Pas de figure faite seulement de boîtes de texte et de flèches, sauf si le concept est lui-même une écriture ; alors montre la structure de l'écriture.
7. 3D seulement si le concept a trois dimensions indépendantes : utilise cubes() et iso() (projection isométrique exacte).
8. Deux fiches voisines aux concepts proches reçoivent des figures différentes, qui montrent ce qui les distingue.

B. CODER — écris __BASE__/figsrc/<code>.py :
- première ligne, telle quelle : import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
- nom du fichier = code de la fiche, avec le tiret : figsrc/05-012.py (jamais f05_012.py)
- canvas(hauteur_mm) (35 à 110), fin par save(fig, '<code>'). Largeur 88 mm, marge 2 mm, origine en bas à gauche.
- seulement les fonctions de figstyle (plus ax.add_patch / ax.plot si une forme manque) et seulement COL[...] / FILL[...] : jamais de couleur en dur. Les couleurs sont des rôles : sujet (bleu), varie (orange), fixe (gris), resultat (vert), limite (rouge : faux), autre (violet), encre.
- au plus 14 textes, courts (≤ 28 caractères), français avec accents, tailles 's', 'm' ou 'l'. Nombres à la française (4 329 ; virgule décimale). Symboles en mathtext (r'$n$', r'$\times$').
- positions calculées par le code (boucles, espacements réguliers, fonction renvoyée par numberline) ; quantités exactes (14 boîtes = 14 boîtes).
- numberline(..., arrow_right=True) ajoute 5 mm à droite de x1 : garde x1 ≤ 81 ou mets arrow_right=False. Pour un arc au-dessus d'une flèche qui va vers la droite, la courbure est négative.
- étiquette courte sur chaque élément qui dit ce qu'il est ; flèches du bord d'une forme au bord d'une autre, sans traverser un texte ; pas de grand vide.
- save() ÉCHOUE si un texte sort du cadre, est trop petit ou en chevauche un autre : corrige jusqu'à « OK <code> ». Lance tes scripts un par un (jamais une boucle sur tout figsrc).
- Contrôle : après « OK », ouvre figs/<code>.png avec Read UNE fois ; si un débutant qui ne voit que l'image ne pourrait pas dire "a_dire", ou si un élément est illisible, corrige (2 passes au plus).

C. LÉGENDES — écris __BASE__/specs/{L}.json : un tableau JSON, un objet par fiche, dans l'ordre :
{"code": "...", "a_dire": "...", "legende_titre": "titre court (≤ 60 caractères) qui ne donne pas la réponse mot pour mot", "lecture": ["2 à 4 phrases courtes : chacune dit ce qu'un élément (désigné par sa couleur ou sa place) représente dans la figure telle que tu l'as codée"], "a_voir": "une phrase : ce qu'il faut voir"}
Phrases simples, deuxième personne, aucun mot technique absent de la fiche, aucune métaphore. Vérifie que le JSON se charge.

Réponse finale, courte : nombre de figures « OK », puis une ligne par fiche dont le concept reste mal figuré (code + raison).
