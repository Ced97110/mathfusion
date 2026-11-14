# Prompt des illustrations jouables — version 1 (2026-11-14)

Modèle commun à toutes les illustrations jouables du livre. On l'améliore à chaque tour avec l'utilisateur, jusqu'à un résultat de qualité ; le numéro de version change à chaque modification, et chaque changement note sa raison dans le journal en bas.

Pour l'utiliser : remplir les champs `{…}` à partir du chapitre, puis lancer le prompt dans une session neuve.

## Champs à remplir

| Champ | Ce qu'il faut | Exemple (chapitre 41) |
|---|---|---|
| `{CHAPITRE}` | numéro et titre | 41, Les vecteurs du plan et de l'espace |
| `{CONCEPT}` | une seule notion du chapitre | l'addition de deux vecteurs |
| `{CAS_REEL}` | une situation réelle où la notion décide du résultat | un Cessna 172S vole avec un vent de travers |
| `{DONNEES}` | fichier de mesures réelles, avec leurs sources | `data/vent_travers.json` (POH Cessna 172S ; radiosondage De Bilt) |
| `{REGLAGE}` | la seule variable que le joueur contrôle : la variable du concept | le cap |
| `{BUT}` | ce qui fait gagner, et qui exige d'appliquer la notion | atteindre la piste plein est |
| `{FAUSSE_IDEE}` | l'idée fausse que le niveau doit battre (hypothèse à vérifier) | « les vitesses s'additionnent » |
| `{FORMULE}` | la formule exacte qui sert de vérité aux tests | triangle des vents : cap = route − asin(vent de travers / vitesse air) |
| `{REFERENCE}` | une source extérieure qui recalcule la mesure réelle | méthode du *Pilot's Handbook of Aeronautical Knowledge* (FAA), à 0,1° près |
| `{TRANSFERT}` | un cas nouveau, jamais vu dans le niveau, avec une mesure réelle | une barque traverse une rivière (courant mesuré à une station) |
| `{DIMENSION}` | 2D ou 3D : 3D seulement si le concept est en trois dimensions (CLAUDE.md) | 2D, vue de dessus |

## Le prompt

> Planifie en une page une illustration jouable du chapitre {CHAPITRE} sur {CONCEPT} : {CAS_REEL}, avec les mesures de {DONNEES}, aucun nombre inventé. Le joueur ne règle que {REGLAGE}. Il gagne en {BUT}. Boucle : prédire, agir, observer, expliquer. Mets à l'épreuve mon hypothèse que la fausse idée est {FAUSSE_IDEE} : vérifie-la d'abord avec une question posée avant de jouer à 3 débutants, sur une maquette papier. Construis en {DIMENSION} ; ne passe à la 3D que si le concept est en 3D ou qu'un test montre qu'elle aide. Enregistre chaque tentative en JSON. Épreuves : (1) Vitest compare chaque valeur affichée à {FORMULE}, à 1e-6 près, et la mesure réelle est recalculée par {REFERENCE} ; (2) un vrai téléphone Android tient 50 images par seconde ou plus pendant 10 s, avec Playwright ralenti seulement comme garde-fou ; (3) 2 lecteurs sur 3 ratent la question d'avant et réussissent la question jumelle ({TRANSFERT}) d'après. Si une épreuve ne peut pas être faite, arrête-toi et dis laquelle.

## Règles fixes (valables pour toutes les illustrations)

- Stack : le site Next.js existant ; React Three Fiber et drei seulement si 3D ; Rapier seulement pour une collision réelle, jamais pour remplacer un calcul exact ; KaTeX pour les formules ; tactile d'abord ; boîtes grises avant tout décor.
- Couleurs à rôle fixe du livre : bleu = l'objet défini, orange = ce qui change, gris = ce qui ne change pas, vert = le résultat, rouge = le faux, violet = un second objet.
- Image mentale d'abord (consigne de réécriture, règle 16) : le joueur voit la scène avant toute phrase qui la décrit.
- Chaque mesure réelle garde sa source, sa date, son unité et sa convention (exemple : le vent météo « vient du » 316°, il pousse vers 136°).
- Disque presque plein : `df -h` avant toute installation.
- L'épreuve 3 demande trois vraies personnes : un modèle ne peut pas la faire passer.

## Exemples remplis

- Chapitre 41 : `book/reecriture/niveau_vent_prompt.md`.

## Journal des versions

- v1 (2026-11-14) : tiré du plan « Vent de travers » approfondi (deepen-prompt). Pas encore lancé.
