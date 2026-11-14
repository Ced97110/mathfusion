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
box(ax, 4, 58, 50, 9, 'sujet', True, r'$a\times b=0$ et $a\neq0$')
arrow(ax, (29, 57.5), (29, 49.5), 'varie')
text(ax, 33, 53.5, r'on divise par $a$', 'varie', 's', ha='left')
box(ax, 4, 40, 50, 9, 'fixe', True, r'$b=0\div a$')
arrow(ax, (29, 39.5), (29, 31.5), 'varie')
text(ax, 33, 35.5, '0 divisé par non nul : 0', 'varie', 's', ha='left')
box(ax, 4, 22, 50, 9, 'resultat', True, r'$b=0$')
box(ax, 3, 4, 26, 8, 'resultat', True, r'$0\times7=0$', 's')
box(ax, 31, 4, 54, 8, 'limite', True, r'$5\times(-3)=-15\neq0$', 's')
save(fig, '23-028')
