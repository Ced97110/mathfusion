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

fig, ax = canvas(58)
box(ax, 4, 46, 26, 9, 'sujet', True, r'$a\times b=0$')
arrow(ax, (32, 50.5), (40, 50.5), 'resultat')
box(ax, 42, 46, 42, 9, 'resultat', True, r'$a=0$ ou $b=0$')
box(ax, 4, 22, 26, 9, 'autre', True, r'$a\times b=6$')
arrow(ax, (32, 26.5), (40, 26.5), 'fixe')
for y, t in [(34, r'$a=2$ et $b=3$'), (24, r'$a=1$ et $b=6$'), (14, r'$a=12$ et $b$ = 0,5')]:
    box(ax, 42, y - 3, 42, 8, 'fixe', True, t, 's')
save(fig, '23-027')
