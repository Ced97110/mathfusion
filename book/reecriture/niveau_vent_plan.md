# Niveau « Vent de travers » — plan (v2, 2026-11-14)

État : niveau 2D en boîtes grises construit le 2026-11-14, page `/niveau/vent-de-travers/` (non liée depuis le menu). Reste : la question 1 aux 3 débutants, le test Android, la question 2 après le jeu.

Tiré de `niveau_vent_prompt.md` (modèle `prompt_illustration.md` v1), puis approfondi. Chapitre 41, addition de deux vecteurs.

## Nombres vérifiés (calculés depuis `data/vent_travers.json`, testés par Vitest)

| Grandeur | Valeur | Calcul |
|---|---|---|
| Vitesse air (POH, Fig. 4-3) | 119 kt | mesure |
| Vent (De Bilt, 1222 m) | vient du 316°, 9,5 m/s = 18,467 kt | 9,5 × 3600 / 1852 |
| Composante de travers | 13,284 kt vers le sud | W · sin(316° − 090°) |
| Composante arrière | 12,828 kt | −W · cos(316° − 090°) |
| Cap à prendre | 083,59° | 090° − asin(13,284 / 119) |
| Vitesse sol avec ce cap | 131,08 kt | somme des deux vecteurs |
| Si le joueur pointe 090° | route 095,75°, vitesse sol 132,50 kt, dérive 13,28 NM/h au sud | somme des deux vecteurs |
| Réponse de la fausse idée | 137,47 kt, plein est | 119 + 18,467 |

## Étape 0 — la fausse idée (avant tout code)

Feuille à imprimer : `book/reecriture/niveau_vent_feuille.html` (v2). Deux questions jumelles de même structure (vent ou courant à 46° de la direction pointée), chacune en deux parties : où (a) et à quelle vitesse (b). Penser à voix haute ; noter les mots exacts.

Règles fixées avant le test (chances de les remplir en répondant au hasard, calcul exact) :
- Hypothèse confirmée si au moins 2 personnes sur 3 choisissent A en 1a et A en 1b : 25/729 = 3,4 %.
- Épreuve 3 réussie si au moins 2 personnes sur 3 font au moins une erreur à la question 1, puis réussissent 2a et 2b : 2,7 %.

La version 1 (une question, « 2 sur 3 ») laissait 26 % de chances au hasard.

## Le niveau (vue de dessus 2D)

- Fait : `app/niveau/vent-de-travers/` (page, carte, molette, vue du seuil) ; logique dans `lib/niveau_vent.js` (testée). Distance au seuil retenue : une heure de vol avec le bon cap (131,08 NM), comme la question papier ; à changer dans `DUREE_CONCEPTION_H`.
- Prédiction : le joueur touche la carte ; après le vol, la page affiche la distance entre sa prédiction et le point réel (pas de verdict juste/faux : aucune tolérance mesurée pour une prédiction).
- Rendu SVG dans le site Next.js. Pas de React Three Fiber (concept en 2D), pas de Rapier (l'arrivée se calcule exactement : `ecartAuSeuilM`).
- Couleurs : bleu = vecteur avion, violet = vecteur vent, vert = vecteur somme, orange = le cap réglé, gris = carte et piste, rouge = la prédiction fausse.
- Seul réglage : le cap, au dixième de degré. **Le cap est bloqué dès le départ** : un test montre qu'un joueur qui vise sans cesse la piste arrive à moins de 93 m sans additionner les vecteurs.
- Boucle : prédire (tracer l'arrivée), agir (choisir le cap), observer (trace réelle à côté de la prédiction), expliquer (triangle bleu + violet = vert, formule en KaTeX).
- Gagné si l'avion passe à moins de 350 ft (106,68 m) de l'axe au seuil : largeur du couloir d'approche finale, « usually 700 feet » (AIM, FAA). À une heure de vol (131,08 NM), seul le cap 083,6° gagne ; 083,5° et 083,7° perdent. **La distance au seuil reste un choix de conception à fixer.**
- Chaque tentative en JSON : `{horodatage, cap_deg, prediction_xy, arrivee_xy, route_deg, vitesse_sol_kt, ecart_seuil_m, gagne}`, gardé dans le navigateur et téléchargeable.

## Épreuves

1. **Vitest** — 18 tests verts (`npm test`).
   - `lib/vent.test.js` : chaque valeur comparée à la formule du triangle des vents à 1e-6.
   - `lib/vent.proprietes.test.js` : exemple résolu publié par la FAA (PHAK FAA-H-8083-25C, p. 16-14 et 16-15 : route 090°, vent du 045° à 40 kt, 120 kt → cap 076°, 88 kt), à ±0,5 ; propriétés sur 10 000 cas tirés au hasard (fast-check) ; tolérance d'arrivée ; poursuite.
   - Limite : la FAA trace au rapporteur et donne des degrés entiers. La vérification « à 0,1° près par la méthode FAA » du prompt n'est pas possible avec cette source ; la précision 1e-6 vient de la loi des cosinus et des propriétés.
2. **Téléphone Android réel** : ouvrir `/niveau/vent-de-travers/?fps=1` ; en mode `fps`, un vol dure 10 s et le bilan affiche les images par seconde (moyenne et minimum). Garde-fou fait dans Chrome avec processeur ralenti ×4 : 60,0 en moyenne, minimum 59,5, sur 10,0 s (`tools/niveau/test_vent.mjs`, 36/36). Exigence : 50 images par seconde ou plus pendant 10 s (cible plus dure : 60 sur un téléphone d'entrée de gamme), mesure avec le débogage à distance de Chrome. Playwright ralenti seulement en garde-fou. **À faire par toi.**
3. **Transfert** : la barque, avec la mesure réelle `data/barque_riviere.json` (Delaware à Trenton, USGS, 2026-10-15, 314 m, 0,52 m/s). **À faire par toi, avec 3 personnes.**

## Ordre

0. Feuille, question 1 (toi, 3 débutants) → 1. `lib/vent.js` + Vitest (fait) → 2. niveau 2D en boîtes grises, cap bloqué (fait) → 3. test Android → 4. question 2 après le jeu → 5. décor, puis 3D seulement si un test montre qu'elle aide.
