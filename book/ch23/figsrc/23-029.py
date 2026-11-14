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
box(ax, 4, 70, 56, 8, 'sujet', True, r'$a\neq0$ et $b\neq0$')
arrow(ax, (32, 69.5), (32, 62.5), 'fixe')
box(ax, 4, 54, 56, 8, 'varie', True, r'supposons $a\times b=0$')
arrow(ax, (32, 53.5), (32, 46.5), 'varie')
text(ax, 36, 50, r'on divise par $a$', 'varie', 's', ha='left')
box(ax, 4, 38, 56, 8, 'limite', True, r'$b=0$ contredit $b\neq0$')
arrow(ax, (32, 37.5), (32, 30.5), 'resultat')
box(ax, 4, 22, 56, 8, 'resultat', True, r'donc $a\times b\neq0$')
for i, t in enumerate(['5 × (−3) = −15', '4 × 0,5 = 2', '−2 × (−6) = 12']):
    box(ax, 3 + i * 28, 4, 26, 8, 'resultat', True, t, 's')
save(fig, '23-029')
