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

fig, ax = canvas(70)
row(ax, 56, [('3 fois le prix', 'fixe', 28), ('plus 3', 'fixe', 16), ('égale 12', 'fixe', 22)], size='s')
arrow(ax, (44, 55), (44, 47), 'varie')
text(ax, 47, 51, 'avec le signe', 'varie', 's', ha='left')
row(ax, 38, [('3', 'fixe', 10), (r'$x$', 'sujet', 10), ('+ 3', 'fixe', 10), ('= 12', 'fixe', 14)])
r = row(ax, 22, [(r'$x^2$', 'sujet', 12), ('+ 4', 'fixe', 10), (r'$x$', 'sujet', 10), ('= 30', 'fixe', 14)])
arrow(ax, (r[0][0], 21.5), (r[2][0], 21.5), 'sujet', curve=0.7, both=True)
text(ax, (r[0][0] + r[2][0]) / 2, 12, 'le même nombre', 'sujet', 's')
save(fig, '23-017')
