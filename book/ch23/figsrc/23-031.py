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

fig, ax = canvas(74)
box(ax, 4, 62, 38, 9, 'resultat', True, r'$(x-3)(x-4)=0$', 's')
arrow(ax, (44, 66.5), (52, 66.5), 'resultat')
box(ax, 54, 62, 30, 9, 'resultat', True, 'un facteur vaut 0', 's')
box(ax, 4, 32, 38, 9, 'limite', True, r'$(x-3)(x-4)=2$', 's')
arrow(ax, (44, 36.5), (52, 36.5), 'limite')
for y, t in [(46, 'facteurs 1 et 2'), (36, 'facteurs 4 et 0,5'), (26, "d'autres couples")]:
    box(ax, 54, y, 30, 7.5, 'fixe', True, t, 's')
text(ax, 69, 21, 'une équation par couple', 'fixe', 's')
arrow(ax, (23, 31.5), (23, 13.5), 'varie')
box(ax, 4, 4, 80, 9, 'resultat', True, r'ramener à 0 : $x^2-7x+10=0$')
save(fig, '23-031')
