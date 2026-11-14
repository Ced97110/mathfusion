# Niveau « Vent de travers » — prompt à lancer dans une session neuve (2026-11-14)

Premier exemple rempli du modèle commun `book/reecriture/prompt_illustration.md` (v1). Toute amélioration du prompt se fait d'abord dans le modèle.

Planifie en une page un niveau jouable sur l'addition de vecteurs : un Cessna 172S vole avec le vent mesuré dans `data/vent_travers.json`, aucun nombre inventé. Le joueur ne règle que le cap. Il gagne en atteignant la piste plein est. Boucle : prédire, agir, observer, expliquer. Mets à l'épreuve mon hypothèse que la fausse idée est « les vitesses s'additionnent ». Vérifie-la d'abord avec une question posée avant de jouer à 3 débutants, sur une maquette papier. Construis en vue de dessus 2D. Ne passe à la 3D que si un test montre qu'elle aide. Enregistre chaque tentative en JSON. Épreuves : (1) Vitest compare chaque valeur affichée à la formule du triangle des vents, à 1e-6 près, et la mesure réelle est recalculée par la méthode de la FAA à 0,1° près ; (2) un vrai téléphone Android tient 50 images par seconde ou plus pendant 10 s, avec Playwright ralenti seulement comme garde-fou ; (3) 2 lecteurs sur 3 ratent la question d'avant et réussissent la question jumelle (la barque) d'après. Si une épreuve ne peut pas être faite, arrête-toi et dis laquelle.

## Contexte pour la session

- Stack prévue : Next.js (le site existant), React Three Fiber, drei, Rapier (seulement pour détecter l'arrivée), KaTeX, tactile d'abord, boîtes grises avant tout décor.
- Calcul provisoire à refaire et tester : cap 083,6°, vitesse sol 131,1 kt, dérive 13,3 NM/h au sud si le joueur pointe plein est.
- Convention : le vent météo « vient du » 316° ; il pousse vers 136°.
- Disque presque plein : `df -h` avant toute installation.
- Sources : POH Cessna 172S (befa.org, Rev. 4, Fig. 4-3, p. 103) ; radiosondage De Bilt 06260 (University of Wyoming).
