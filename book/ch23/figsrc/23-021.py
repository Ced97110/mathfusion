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
row(ax, 50, [(r'$x^2$', 'fixe', 10), (r'$+4x$', 'fixe', 14), (r'$-30$', 'sujet', 14)], x0=4)
arrow(ax, (44, 54), (56, 54), 'resultat')
box(ax, 58, 50, 26, 8, 'resultat', True, r'$c=-30$')
text(ax, 44, 46, r'pour 50, seul $c$ change', 'varie', 's')
row(ax, 34, [(r'$x^2$', 'fixe', 10), (r'$+4x$', 'fixe', 14), (r'$-50$', 'varie', 14)], x0=4)
arrow(ax, (44, 38), (56, 38), 'resultat')
box(ax, 58, 34, 26, 8, 'resultat', True, r'$c=-50$')
row(ax, 14, [(r'$x^2$', 'fixe', 10, True), (r'$+4x$', 'fixe', 14, True), (r'$c$', 'sujet', 14)], x0=4)
arrow(ax, (44, 18), (56, 18), 'resultat')
box(ax, 58, 14, 26, 8, 'resultat', True, r'$x=0$ : reste $c$', 's')
save(fig, '23-021')
