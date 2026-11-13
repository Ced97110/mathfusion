import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(55)
text(ax, 44, 50, '$0/8 = 0$', 'resultat', 'l')
disc(ax, 20, 28, 13, 'sujet')
import math as _m
for k in range(8):
    a = _m.radians(k * 45 + 22.5)
    line(ax, [(20, 28), (20 + 13 * _m.cos(a), 28 + 13 * _m.sin(a))], 'sujet')
text(ax, 20, 9, 'couper en 8 parts', 'sujet', 's')
arrow(ax, (35, 28), (53, 28), 'varie'); text(ax, 44, 33, 'prendre 0', 'varie', 's')
disc(ax, 68, 28, 13, 'fixe', fill=False)
text(ax, 68, 28, '0', 'resultat', 'xl')
text(ax, 68, 9, 'assiette vide', 'resultat', 's')
save(fig, '06-020')
