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

fig, ax = canvas(86)
box(ax, 14, 72, 60, 9, 'sujet', True, r'$x^2-3x-1=0$')
arrow(ax, (44, 71.5), (44, 62.5), 'varie')
text(ax, 48, 67, r'comme $(x+p)(x+q)$', 'varie', 's', ha='left')
box(ax, 4, 52, 38, 9, 'sujet', True, r'$p+q=-3$')
box(ax, 46, 52, 38, 9, 'sujet', True, r'$pq=-1$')
text(ax, 44, 47, r'seul couple : 1 et $-1$', 'fixe', 's')
arrow(ax, (23, 51.5), (23, 43.5), 'fixe')
arrow(ax, (65, 51.5), (65, 43.5), 'fixe')
box(ax, 4, 34, 38, 9, 'limite', True, r'$1+(-1)=0$')
box(ax, 46, 34, 38, 9, 'resultat', True, r'$1\times(-1)=-1$')
arrow(ax, (23, 33.5), (23, 25.5), 'limite')
box(ax, 4, 16, 80, 9, 'limite', True, r"0 n'est pas $-3$ : aucun couple")
save(fig, '23-032')
