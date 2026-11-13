import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
s = 34.0; x0, y0 = 6.0, 14.0
poly(ax, [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s), (x0, y0 + s)], 'fixe')
for (cx, cy) in [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s), (x0, y0 + s)]:
    disc(ax, cx, cy, 1.5, 'fixe')
    line(ax, [(cx, cy), (x0 + s / 2, y0 + s / 2)], 'varie', dash=True)
disc(ax, x0 + s / 2, y0 + s / 2, 1.7, 'autre')
text(ax, x0 + s / 2, y0 + s / 2 + 4, 'centre', 'autre', 's')
text(ax, x0 + s / 2, y0 - 4, 'côté 1', 'fixe', 's')
# comparaison des longueurs : racine(2)/2 = 0,707 contre 1
L = s
bx = 52.0
text(ax, bx + L / 2 - 4, 48, 'distance au coin le plus proche', 'encre', 's') if False else None
box(ax, bx, 36, L * 0.7071, 6, 'varie', label=r'$\sqrt{2}/2\approx 0{,}71$', size='s')
text(ax, bx, 45.5, 'centre → coin', 'varie', 's', ha='left')
box(ax, bx, 20, L, 6, 'fixe', label='1', size='s')
text(ax, bx, 30, 'distance 1', 'fixe', 's', ha='left')
text(ax, bx + L / 2 - 2, 12, r'$0{,}71<1$', 'resultat', 'm')
save(fig, '56-131')
