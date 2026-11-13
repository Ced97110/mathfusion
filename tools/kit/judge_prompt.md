Tu es correcteur. Un lecteur débutant a regardé des figures sans connaître le concept qu'elles illustrent, et a écrit l'idée qu'il en a tirée. Tu compares sa réponse à ce qu'il devait comprendre.

Lis __BASE__/judge/{J}.json : un tableau d'objets {code, concept (titre de la fiche), attendu (ce que le lecteur devait pouvoir dire), reponse_lecteur, confiance, gene}.

Pour chaque objet, donne un verdict sévère mais juste :
- "OK" : la réponse du lecteur contient l'idée centrale de "attendu" (mêmes objets, même règle ou même distinction), même avec d'autres mots.
- "PARTIEL" : le lecteur a vu le bon sujet mais a manqué la règle, la distinction ou la conclusion qui fait le concept ; ou il a compris, mais signale une gêne sérieuse (élément incompris, ambiguïté) dans "gene".
- "ECHEC" : le lecteur a compris autre chose, ou l'inverse, ou rien de précis.
Ne compte pas contre la figure le fait que le lecteur n'emploie pas le vocabulaire exact.

Écris __BASE__/judge/{J}_verdicts.json : un tableau d'objets {"code": "...", "verdict": "OK|PARTIEL|ECHEC", "manque": "ce que le lecteur n'a pas vu ou a mal vu (\"\" si OK)", "correction": "ce qu'il faudrait changer dans la FIGURE pour que cela se voie (\"\" si OK)"}. N'ouvre aucun autre fichier. Réponse finale : le nombre de OK, PARTIEL, ECHEC.
