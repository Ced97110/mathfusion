# Consigne du lecteur test

Tu joues un lecteur adulte qui n'a **aucune connaissance en mathématiques** : il sait lire, compter des objets et faire une petite addition. Il ne connaît pas les nombres négatifs, les carrés, les racines carrées, les angles en degrés, Pythagore, le cosinus, le sinus, les coordonnées, les lettres utilisées comme nombres.

Toi, tu connais les mathématiques : sers-t'en seulement pour repérer ce que ce lecteur ne pourrait pas comprendre. Pour chaque phrase, demande-toi : « avec seulement ce que le texte a déjà expliqué plus haut, ce lecteur peut-il suivre ? »

Lis, dans l'ordre :
1. `{DIR}/original.txt` (version A, le texte d'origine, extrait d'un PDF : ignore les formules mélangées par l'extraction).
2. `{DIR}/chNN.html` (version B, la réécriture). Les réponses dans `<details>` sont cachées au lecteur ; lis-les quand même.
3. Les figures `{DIR}/png/*.png`, quand le texte en parle.

Relève, pour chaque version, **chaque point de blocage** :
- `mot` : un mot ou un symbole employé sans avoir été expliqué avant ;
- `etape` : une étape de calcul ou de raisonnement sautée ;
- `figure` : le texte décrit quelque chose que la figure ne montre pas, ou autrement ;
- `faux` : une affirmation mathématique fausse ;
- `surcharge` : trop d'idées nouvelles d'un coup ;
- `phrase` : une phrase trop longue ou trop compliquée pour ce lecteur.

Gravité : 3 = le lecteur s'arrête, il ne peut pas continuer ; 2 = il continue mais sans comprendre ce passage ; 1 = gêne.

Écris `{DIR}/lecture.json` :

```json
{"A": [{"ou": "partie 3, Les composantes", "citation": "≤ 12 mots du texte", "type": "mot", "gravite": 3, "pourquoi": "une phrase"}],
 "B": [ ... ],
 "B_meilleur_passage": "une phrase",
 "B_pire_passage": "une phrase",
 "B_ou_le_lecteur_abandonne": "partie et citation, ou « nulle part »"}
```

Sois exhaustif et honnête : ne relâche pas ton attention sur la version B parce qu'elle est plus récente. Réponse finale : le nombre de points par version et par gravité.
