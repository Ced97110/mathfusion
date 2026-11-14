import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import json
from PIL import Image

# Rendu Blender Cycles (vue parallèle exacte, azimut 330°, élévation 25° : w incliné de 28° à l'écran).
# Ici, seulement l'image réduite et les positions des sommets projetés,
# pour poser les textes sans Blender.
HERE = os.path.dirname(os.path.abspath(__file__))
img = Image.open(os.path.join(HERE, '41-123.render.png'))
pts = json.load(open(os.path.join(HERE, '41-123.render.json')))
PW, PH = pts['size']
X0, Y_TOP, IW = 0.0, 46.0, W  # l'image (recadrée, fond blanc) occupe toute la largeur
IH = IW * PH / PW
mm = lambda p: (X0 + p[0] * IW / PW, Y_TOP - p[1] * IH / PH)

fig, ax = canvas(54)
ax.imshow(img, extent=(X0, X0 + IW, Y_TOP - IH, Y_TOP), zorder=1, interpolation='antialiased')
cx = {n: sum(mm(p)[0] for p in pts[n]) / len(pts[n]) for n in ('parallelogramme', 'carton', 'parallelepipede')}

text(ax, cx['parallelogramme'], 50, 'parallélogramme', 'fixe', 's')
text(ax, cx['carton'], 50, 'carton', 'autre', 's')
text(ax, cx['parallelepipede'], 50, 'parallélépipède', 'sujet', 's')
text(ax, cx['parallelogramme'], 14, '1 face, plate', 'fixe', 's')
text(ax, cx['carton'], 14, '6 faces', 'autre', 's')
text(ax, cx['carton'], 9, 'en rectangle', 'autre', 's')
text(ax, cx['carton'], 4, 'arêtes droites', 'autre', 's')
text(ax, cx['parallelepipede'], 14, '6 faces', 'sujet', 's')
text(ax, cx['parallelepipede'], 9, 'en parallélogramme', 'sujet', 's')
text(ax, cx['parallelepipede'], 4, 'arêtes inclinées', 'sujet', 's')

a = {k: mm(v) for k, v in pts['anchors'].items()}
line(ax, [a['h_top'], a['h_foot']], 'fixe', lw=0.9, dash=True)
text(ax, a['h_top'][0] + 1.8, (a['h_top'][1] + a['h_foot'][1]) / 2, '3', 'fixe', 's', weight='bold')
text(ax, a['u'][0] + 0.5, a['u'][1] - 2.4, r'$u$', 'encre', 's')
text(ax, a['v'][0] - 2.2, a['v'][1] - 0.6, r'$v$', 'encre', 's')
text(ax, a['w'][0] - 2.2, a['w'][1] + 0.6, r'$w$', 'encre', 's')
save(fig, '41-123')
