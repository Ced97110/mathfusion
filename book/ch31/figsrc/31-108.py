import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(56)
data = [(0, 1, 1), (90, 0, 0), (180, 1, 1), (270, 0, 2)]
base, unit = 14, 11
for i, (a, l, r) in enumerate(data):
    x0 = 3 + i * 21.5
    box(ax, x0, 6, 20, 38, 'resultat' if l == r else 'limite')
    line(ax, [(x0 + 2, base), (x0 + 18, base)], 'fixe')
    for j, (v, role) in enumerate(((l, 'sujet'), (r, 'varie'))):
        bx = x0 + 3 + j * 8
        if v: ax.add_patch(Rectangle((bx, base), 6, v * unit, ec=COL[role], fc=FILL[role], lw=0.8, zorder=3))
        text(ax, bx + 3, base + v * unit + 2.4, str(v), role, 's')
    text(ax, x0 + 10, 9.8, f'{a}°', 'encre', 's')
text(ax, 24, 51, 'cos² x', 'sujet', 's'); text(ax, 62, 51, '1 − sin x', 'varie', 's')
save(fig, '31-108')
