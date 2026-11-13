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

fig, ax = canvas(46)
r = row(ax, 24, [(r'$x^2$', 'sujet', 22), (r'$+4x$', 'sujet', 22), (r'$-30$', 'sujet', 22)], gap=3, h=9)
for (cx, _, _), a, e in zip(r, ['$a$', '$b$', '$c$'], ['exposant 2', 'exposant 1', r'sans $x$']):
    text(ax, cx, 37, a, 'resultat', 'm')
    text(ax, cx, 20, e, 'fixe', 's')
text(ax, 44, 14, 'même équation, autre ordre', 'autre', 's')
row(ax, 2, [(r'$-30$', 'autre', 22), (r'$+4x$', 'autre', 22), (r'$+x^2$', 'autre', 22)], gap=3, h=9)
save(fig, '23-026')
