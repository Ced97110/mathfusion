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

fig, ax = canvas(72)
box(ax, 14, 58, 60, 9, 'sujet', True, r'$x^2-7x+12=0$')
arrow(ax, (44, 57.5), (44, 49.5), 'varie')
text(ax, 48, 53.5, r'produit 12, somme $-7$', 'varie', 's', ha='left')
box(ax, 14, 40, 60, 9, 'fixe', True, r'$(x-3)(x-4)=0$')
arrow(ax, (30, 39.5), (25, 31.5), 'varie')
arrow(ax, (58, 39.5), (63, 31.5), 'varie')
text(ax, 44, 35.5, 'produit nul', 'varie', 's')
box(ax, 8, 22, 34, 9, 'fixe', True, r'$x-3=0$')
box(ax, 46, 22, 34, 9, 'fixe', True, r'$x-4=0$')
arrow(ax, (25, 21.5), (25, 13.5), 'resultat')
arrow(ax, (63, 21.5), (63, 13.5), 'resultat')
box(ax, 8, 4, 34, 9, 'resultat', True, r'$x=3$')
box(ax, 46, 4, 34, 9, 'resultat', True, r'$x=4$')
save(fig, '23-030')
