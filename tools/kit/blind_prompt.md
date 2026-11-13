Tu es un lecteur débutant en mathématiques. Tu testes des figures d'un livre. Pour chaque figure, tu dois dire quelle idée elle enseigne, en ne regardant QUE l'image et le court « cas concret » que le lecteur a lu juste avant.

Règles strictes : n'ouvre aucun autre fichier que ceux du dossier __BASE__/blind/{T}/ . Ne cherche pas la réponse ailleurs (pas de recherche dans d'autres dossiers). Le test n'a de valeur que si tu réponds à partir de l'image.

1. Lis __BASE__/blind/{T}/cas.txt (une ligne par image).
2. Pour chaque image img01.png, img02.png, … du dossier : ouvre-la avec l'outil Read, regarde-la, puis écris :
   - "idee" : en une ou deux phrases, l'idée mathématique que la figure veut faire comprendre (ce que tu dirais à un ami : « cette figure montre que… »). Sois précis : dis la règle ou la distinction, pas seulement le sujet.
   - "confiance" : "haute", "moyenne" ou "basse".
   - "gene" : ce qui t'a gêné pour comprendre (élément dont tu ne vois pas le sens, texte ambigu, entassement, vide, flèche peu claire), ou "" s'il n'y a rien.
3. Écris le résultat dans __BASE__/blind/{T}/reponses.json : un objet JSON { "img01": {"idee": "...", "confiance": "...", "gene": "..."}, ... } avec une entrée par image.
Réponse finale : seulement le nombre d'images traitées.
