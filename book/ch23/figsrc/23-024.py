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

fig, ax = canvas(58)
r = row(ax, 42, [(r'$x^2$', 'fixe', 12), (r'$b=0$', 'sujet', 16, True), (r'$+7$', 'fixe', 12), (r'$=0$', 'fixe', 12)])
text(ax, r[1][0], 38.5, r'pas de terme en $x$', 'sujet', 's')
r = row(ax, 24, [(r'$5x^2$', 'fixe', 14), (r'$+8x$', 'fixe', 14), (r'$c=0$', 'sujet', 16, True), (r'$=0$', 'fixe', 12)])
text(ax, r[2][0], 20.5, 'pas de terme seul', 'sujet', 's')
box(ax, 18, 6, 52, 8, 'limite', True, r'$a=0$ est interdit')
save(fig, '23-024')
