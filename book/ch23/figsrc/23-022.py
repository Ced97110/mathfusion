import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def row(ax, y, items, x0=None, h=8, gap=2, size='m'):
    tot = sum(it[2] for it in items) + gap * (len(items) - 1)
    x = (W - tot) / 2 if x0 is None else x0
    out = []
    for it in items:
        lab, role, w = it[0], it[1], it[2]
        dash = len(it) > 3 and it[3]
        sz = it[4] if len(it) > 4 else size
        box(ax, x, y, w, h, role, True, lab, sz, dash=dash)
        out.append((x + w / 2, x, w)); x += w + gap
    return out

fig, ax = canvas(66)
row(ax, 52, [(r'$x^2+4x$', 'fixe', 26), ('=', 'fixe', 8), ('30', 'varie', 12)])
arrow(ax, (44, 51), (44, 43), 'varie')
text(ax, 48, 47, 'on retire 30 des deux côtés', 'varie', 's', ha='left')
row(ax, 34, [(r'$x^2+4x-30$', 'fixe', 38), (r'$=0$', 'sujet', 12)])
arrow(ax, (44, 33), (44, 25), 'fixe')
box(ax, 19, 16, 50, 8, 'limite', True, r'$x=3$ : $9+12-30=-9$', 's')
text(ax, 44, 9, r'$-9\neq0$ : pas une solution', 'limite', 's')
save(fig, '23-022')
