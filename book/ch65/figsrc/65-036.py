import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
P = {1: (44, 58), 2: (22, 26), 3: (66, 26)}
edges = [(1, 2), (1, 3), (2, 3)]
for a, b in edges:
    (xa, ya), (xb, yb) = P[a], P[b]
    L = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
    ux, uy = (xb - xa) / L, (yb - ya) / L
    line(ax, [(xa + 3.6 * ux, ya + 3.6 * uy), (xb - 3.6 * ux, yb - 3.6 * uy)], 'varie', lw=1.2)
lab = {(1, 2): (27.5, 46, r'$r_1-r_2$'), (1, 3): (60.5, 46, r'$r_1-r_3$'), (2, 3): (44, 21, r'$r_2-r_3$')}
for e, (x, y, s) in lab.items():
    box(ax, x - 9, y - 3, 18, 6, 'varie', label=s, size='s')
for k, (x, y) in P.items():
    disc(ax, x, y, 3.6, 'sujet', label=r'$r_%d$' % k, size='s')
text(ax, 44, 11, r'$D=(r_1-r_2)(r_1-r_3)(r_2-r_3)$', 'sujet', 'm', weight='bold')
text(ax, 44, 4.5, '3 paires = 3 facteurs', 'fixe', 's')
save(fig, '65-036')
