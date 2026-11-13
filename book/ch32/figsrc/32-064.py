import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9):
    n = 24
    pts = [pol(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw=lw)

fig, ax = canvas(76)
cx, cy, r = 30, 40, 22
disc(ax, cx, cy, r, 'sujet', fill=False)
line(ax, [(6, cy), (56, cy)], 'fixe'); line(ax, [(cx, 14), (cx, 66)], 'fixe')
xt = cx + r
line(ax, [(xt, 14), (xt, 66)], 'fixe', dash=True)
line(ax, [(cx - 1.2 * r, cy - 0.9 * r), (cx + 1.1 * r, cy + 0.825 * r)], 'varie', lw=1.2)
line(ax, [(xt, cy), (xt, cy + 0.75 * r)], 'sujet', lw=1.4)
Px, Py = cx + 0.8 * r, cy + 0.6 * r
disc(ax, Px, Py, 1.3, 'resultat'); disc(ax, 2 * cx - Px, 2 * cy - Py, 1.3, 'resultat'); disc(ax, xt, cy + 0.75 * r, 1.3, 'varie')
text(ax, 27.5, 37.2, '$O$', 'fixe', 's')
text(ax, Px - 3, Py + 3, '$P$', 'resultat', 'm'); text(ax, 2 * cx - Px - 2.5, 2 * cy - Py - 2.5, '$Q$', 'resultat', 'm')
text(ax, xt + 3.5, cy + 0.75 * r - 3.5, '$T$', 'varie', 'm')
text(ax, xt + 1.5, 44, '$k$ = 0,75', 'sujet', 's', ha='left')
box(ax, 58, 26, 28, 9, 'resultat', label='P : 36,87°', size='s')
box(ax, 58, 15, 28, 9, 'resultat', label='Q : 216,87°', size='s')
box(ax, 58, 4, 28, 9, 'fixe', label='écart : 180°', size='s')
save(fig, '32-064')
