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

fig, ax = canvas(84)
box(ax, 4, 70, 44, 9, 'fixe', True, r'$x(x+4)=30$')
arrow(ax, (26, 69.5), (26, 55.5), 'varie')
text(ax, 30, 62.5, '1 développer', 'varie', 's', ha='left')
box(ax, 4, 46, 44, 9, 'fixe', True, r'$x^2+4x=30$')
arrow(ax, (26, 45.5), (26, 31.5), 'varie')
text(ax, 30, 38.5, '2 retirer 30 des deux côtés', 'varie', 's', ha='left')
box(ax, 4, 22, 44, 9, 'sujet', True, r'$x^2+4x-30=0$')
arrow(ax, (26, 21.5), (26, 13.5), 'varie')
text(ax, 30, 17.5, r'3 ranger : $x^2$, $x$, seul', 'varie', 's', ha='left')
for i, t in enumerate([r'$a=1$', r'$b=4$', r'$c=-30$']):
    box(ax, 3 + i * 16, 4, 14, 8, 'resultat', True, t, 's')
save(fig, '23-025')
