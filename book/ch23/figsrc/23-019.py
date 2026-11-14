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

fig, ax = canvas(60)
row(ax, 46, [(r'$a$', 'sujet', 10), (r'$x^2$', 'fixe', 10)], x0=4)
text(ax, 28, 50, r'$a$ multiplie $x^2$', 'sujet', 's', ha='left')
r = row(ax, 28, [('1', 'sujet', 8, True), (r'$x^2$', 'fixe', 10), (r'$+4x-30=0$', 'fixe', 28, False, 's')], x0=4)
text(ax, r[0][0], 24.5, 'non écrit', 'sujet', 's')
arrow(ax, (56, 32), (64, 32), 'resultat')
box(ax, 66, 28, 18, 8, 'resultat', True, r'$a=1$')
row(ax, 10, [('5', 'sujet', 8), (r'$x^2$', 'fixe', 10), (r'$+8x=0$', 'fixe', 28, False, 's')], x0=4)
arrow(ax, (56, 14), (64, 14), 'resultat')
box(ax, 66, 10, 18, 8, 'resultat', True, r'$a=5$')
save(fig, '23-019')
