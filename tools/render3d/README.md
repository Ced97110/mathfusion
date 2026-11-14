# Rendu 3D réaliste (Blender Cycles)

Pour une fiche dont le concept est à trois dimensions. Utilisé pour 41-123.

1. `python3 scene.py scene.json` : géométrie exacte (nombres de la fiche seulement), caméra parallèle.
2. `/Applications/Blender.app/Contents/MacOS/Blender -b -P render2.py -- scene.json $PWD/out.png 96` (Blender 5.2.4 LTS, environ 2 min).
3. `python3 check2.py scene.json out.png` : sommets à 1 px de la projection numpy, sommets dessinés, w incliné ≥ 15°.
4. Recadrer sur fond blanc et copier l'image et les points dans `book/chNN/figsrc/<code>.render.png|json` ;
   le script `figsrc/<code>.py` pose les textes avec `figstyle.py`, sans Blender.

Couleurs : arêtes en émission pure (pixel = couleur du rôle, vue « Standard », pas AgX).
