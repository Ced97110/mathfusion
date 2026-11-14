import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
c, r = (64, 38), 15
pts = [(c[0] + r * math.cos(math.pi - 2 * math.pi * k / 12), c[1] + r * math.sin(math.pi - 2 * math.pi * k / 12)) for k in range(12)]
for k, p in enumerate(pts):
    disc(ax, p[0], p[1], 2.4 if k == 0 else 1.7, 'resultat' if k == 0 else 'autre', label='0' if k == 0 else None, size='s')
ys = [12 + i * 9 for i in range(7)]
for y in ys:
    disc(ax, 12, y, 2.2, 'sujet')
    arrow(ax, (14.6, y), (pts[0][0] - 2.9, pts[0][1]), 'varie', lw=0.7)
text(ax, 12, 76, 'horloge à 7', 'sujet', 's'); text(ax, 64, 62, 'horloge à 12', 'autre', 's')
text(ax, 52, 8, 'tout va sur le 0', 'varie', 'm')
text(ax, 84, 8, 'ker f = G', 'limite', 's', ha='right')
save(fig, '48-182')
