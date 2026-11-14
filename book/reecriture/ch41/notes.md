# Notes de réécriture, chapitre 41 — version 2 (consigne v2)

## Erreurs de l'original corrigées (règle 15)
- **Morceau manquant de Pythagore** (démonstration, bloc facultatif) : c'est −2(u1 v1 + u2 v2), pas le seul terme −2 u1 v1. Le texte nomme maintenant les deux termes et leur somme.
- **Produit vectoriel « n'existe que dans l'espace »** : remplacé par « il n'existe pas dans le plan ; en dehors des dimensions 3 et 7, il n'existe aucun produit de ce genre ».
- **Chapitre 76 : u1 v2 − u2 v1 « est l'aire »** : c'est l'aire au signe près ; le nombre peut être négatif, son signe dit le sens de rotation.
- **« Vérifions sur la figure » (Fig. 41.3)** : la figure ne porte aucun nombre. Le texte dit « vérifions avec les nombres de u et v », et la légende précise que la figure vaut pour deux vecteurs quelconques.
- **Règle de la main droite « visible sur la figure 41.5 »** : elle ne l'est pas. Le texte dit que seules les deux premières exigences se voient, et invite à faire le geste.
- (Déjà en v1.1) θ = 180° : ‖u − v‖ = ‖u‖ + ‖v‖.

## Ce qui a changé depuis la version 1.1
- **Figures nouvelles (règle 11)**, dessinées par `tools/reecriture/fig41.py` (A à E inchangées) :
  - 41.F : axe gradué, 5 − 8 = −3 (rappel des nombres négatifs).
  - 41.G : cercle de rayon 1, points à 60° et 120°, cos 60° = 0,5 et cos 120° = −0,5.
  - 41.H : vecteur de A(5, 7) à B(18, 13), écarts 13 et 6.
  - 41.I : parallélépipède sur u = ⟨2, 0, 0⟩, v = ⟨1, 2, 0⟩, w = ⟨1, 1, 3⟩ (base, hauteur, arêtes cachées en pointillés). Projection isométrique exacte, vue depuis la direction (−1, 1, 1) : la vue habituelle de `iso()` posait la pointe de v sur une arête. La flèche u, cachée, est en pointillés ; la hauteur est tracée depuis un point intérieur de la face du haut (depuis la pointe de w, elle tombait sur la flèche u).
  - 41.J : effet 1, triangle O / bout de a / bout de r, angles 60° et 120° (pourquoi 180° − 60°).
  - 41.K : effet 2, direction vraie 93,69° et réponse de l'arctangente −86,31°, séparées d'un demi-tour.
  - 41.L : sac porté à hauteur constante, force verticale et déplacement horizontal à angle droit.
- **Rappels ajoutés ou complétés** : angle droit (dans « angle et degré ») ; rapport et barre « / » (dans « cosinus et sinus ») ; valeurs lues à la calculatrice en degrés (cos, sin, tan⁻¹, cos⁻¹) ; nombres négatifs avec règle des signes, division de deux négatifs et soustraction d'un négatif ; cosinus et sinus d'un angle plus grand que 90° (cercle de rayon 1, coordonnées définies avant usage) ; carré d'une racine carrée ; produit de deux racines carrées (√10 × √20 = √200) ; **loi des cosinus** (encadré sur le parcours principal, avec exemple chiffré) ; carré d'une différence et d'une somme (dans la démonstration) ; notation sin² θ et sin² θ + cos² θ = 1 avec exemple.
- **Section « Multiplier deux vecteurs » coupée en deux** (définition / ce que mesure le produit scalaire) ; l'arccosinus est défini en gras au moment où il sert (45° obtenu par cos⁻¹ à la calculatrice).
- **Une lettre = un objet (règle 13)** :
  - a (flèche de l'avion) / a (composante) : signalé au lecteur ; la flèche est toujours appelée « la flèche a de l'avion ».
  - v (vent) puis v (autres vecteurs) : signalé deux fois (partie 3, « Le vecteur » et « Multiplier deux vecteurs »).
  - u1, u2 (composantes) puis u1, u2 (parties de la projection) : les parties s'appellent maintenant p et q (partie 3 et effet 4), avec une phrase qui le dit.
  - x, y de l'identité (x − y)² : remplacés par m et n (nombres), pour ne pas croiser les axes.
  - r de « sa norme r » (partie 5) supprimé.
- **Produit mixte** : écrit w ⋅ (u × v), base construite sur u et v, comme dans l'effet 6 et la figure 41.I. Le texte signale que l'original écrit u ⋅ (v × w), base sur v et w.
- **Étapes ajoutées** : exemple chiffré avant A(x1, y1) → B(x2, y2) et lecture des indices ; a i expliqué (50 i = ⟨50, 0⟩) avant la section sur la multiplication ; carré d'une fraction ; passage a / ‖v‖ = cos θ → a = ‖v‖ cos θ refait avec 50 / 100 = 0,5 ; « isoler » remplacé par la division des deux côtés, refaite avec les nombres ; simplification de ‖u‖ montrée sur 3 × 10 / (3 × 5) ; passage de ‖v‖ à ‖v‖² dans la projection, avec √20 × √20 = 20 ; lecture de proj_v u ; sin θ = 2 / √5 lu sur la figure 41.5 (côté opposé 2) au lieu de passer par sin² + cos² ; règle de lecture des indices du produit vectoriel, composante par composante ; annulation des six termes expliquée paire par paire ; développements de Lagrange écrits ; mise en facteur montrée sur 6 − 6 × 0,25 ; produit mixte : pourquoi la hauteur vaut ‖w‖ cos φ ; cos(α − β) : produit scalaire écrit, puis exemple ; effet 2 : pourquoi mesurer depuis l'est, pourquoi 90° ± 40°, pourquoi ajouter 180° ; effet 3 : normes et √2 × √41 = √82 détaillés ; effet 5 : le déplacement de la valise est horizontal, donc l'angle force/déplacement vaut 30°.
- **Mots** : « quadrilatère » remplacé par « figure à quatre côtés droits » ; « parallèles » expliqué ; « pente » expliquée en une phrase ; « axe » expliqué ; « grandeur » n'est plus employé pour l'objet vecteur ; « le point ⋅ se lit scalaire » corrigé en « u ⋅ v se lit u scalaire v » ; les renvois au « manuel source » supprimés ; séparateur « ; » expliqué ; valeur absolue déplacée après le rappel des négatifs et définie en gras ; en partie 5, « linéaire », « réflexion », « partie réelle », « coordonnées polaires », « courbes paramétrées », « algèbres de Lie » remplacés par une phrase simple ; « les huit règles vues plus haut » situées dans le bloc facultatif.
- Légende de la Fig. 41.2 : le pied de la flèche verte n'a pas de lettre ; le texte dit « le point de l'axe x situé juste sous V ».
- Termes nouveaux en gras : angle droit, rapport, coordonnées, valeur absolue, arccosinus.

## Nombres nouveaux hors des « À vous »
- Rappels : 6 / 3 = 2 ; (−6) / (−3) = 2 ; ⟨1, 1⟩ et ⟨−1, −1⟩ (même rapport 1) ; loi des cosinus avec côtés 3 et 4 et angle 60° : 9 + 16 − 12 = 13, √13 ≈ 3,606 ; (5 − 2)² = 9 et (5 + 2)² = 49 ; 3 × 10 / (3 × 5) = 2 ; 6 − 6 × 0,25 = 6 × (1 − 0,25) ; sin² 60° ≈ 0,75, cos² 60° = 0,25 ; cos(α − β) avec α = 90°, β = 30°.
- Valeurs de calculatrice pour les angles de l'original : cos 50° ≈ 0,642788, sin 50° ≈ 0,766044, cos 130° ≈ −0,642788, sin 130° ≈ 0,766044 ; cos 90° = 0 ; sin 60 = 0,8660254… ; √10 ≈ 3,162, √20 ≈ 4,472, 3,162 × 4,472 ≈ 14,14.
- Étapes intermédiaires tirées de l'original : A(5, 7) → B(18, 13) avancé en partie 3 (il venait de l'effet 5) ; OH = √10 × cos 45° ≈ 2,236 ; (−6,428)² ≈ 41,32, 99,586² ≈ 9 917,37, somme ≈ 9 958,69 ; rapport 99,586 / (−6,428) ≈ −15,49 ; √82 ≈ 9,055 ; u ⋅ v = 2 pour la figure 41.5 ; règle de commutativité vérifiée sur ⟨2, 5⟩ et ⟨7, −1⟩ (nombres d'un « À vous »).
- Repris de la v1.1 : 2v = ⟨100 ; 173,20⟩, −v, |−2| × 100 ; produit scalaire de ⟨1, 3⟩ et ⟨4, 2⟩ avant la formule ; vérification d'aire et de Lagrange ; détails de l'effet 1 et de l'effet 5.

## Inchangé
- Ordre des idées, six parties, exemples et nombres du livre, figures 41.1 à 41.5 et 41.A à 41.E. Rien n'est coupé. Les blocs « Pour aller plus loin » gardent le même contenu qu'en v1.1.
- Points de lecteurs non traités (gravité 1, choix) : le mot « vecteur » figure dans le titre avant sa définition ; la règle de la main droite n'a pas de figure (geste à faire) ; partie 5 garde quelques noms de chapitres (quaternions, modules, déterminant) présentés comme annonces.
