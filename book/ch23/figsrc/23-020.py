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

fig, ax = canvas(62)
data = [(46, r'$+4x$', r'$-30=0$', r'$b=4$', False), (28, r'$-3x$', r'$-1=0$', r'$b=-3$', False), (10, 'aucun terme', r'$-49=0$', r'$b=0$', True)]
for y, mid, tail, res, dash in data:
    row(ax, y, [(r'$x^2$', 'fixe', 10), (mid, 'sujet', 18, dash, 's' if dash else 'm'), (tail, 'fixe', 20)], x0=4)
    arrow(ax, (58, y + 4), (65, y + 4), 'resultat')
    box(ax, 66, y, 18, 8, 'resultat', True, res)
save(fig, '23-020')
