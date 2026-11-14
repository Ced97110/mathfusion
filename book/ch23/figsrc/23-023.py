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
box(ax, 4, 44, 16, 9, 'sujet', True, r'$a\neq0$')
arrow(ax, (22, 48.5), (30, 48.5), 'sujet')
box(ax, 32, 44, 52, 9, 'sujet', True, 'le carré reste', 'm')
box(ax, 4, 18, 16, 9, 'limite', True, r'$a=0$')
arrow(ax, (22, 22.5), (30, 22.5), 'varie')
box(ax, 32, 18, 28, 9, 'fixe', True, r'$4x-30=0$')
text(ax, 46, 30, 'le carré disparaît', 'varie', 's')
arrow(ax, (62, 22.5), (66, 22.5), 'resultat')
box(ax, 66, 18, 18, 9, 'resultat', True, r'$x$ = 7,5', 's')
text(ax, 62, 12, 'premier degré', 'resultat', 's')
save(fig, '23-023')
