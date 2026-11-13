import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
X0, X1, ys, vals = 22, 66, [46, 32, 18], [2, 3, 7]
text(ax, X0, 60, r'$S$', 'sujet', 'l'); text(ax, X1, 60, r'$T$', 'autre', 'l')
for y, v in zip(ys, vals): disc(ax, X0, y, 3.5, 'sujet', label=str(v)); disc(ax, X1, y, 3.5, 'autre', label=str(v))
for i in range(3):
    for j in range(i, 3):
        p, q = (X0, ys[i]), (X1, ys[j]); d = math.hypot(q[0]-p[0], q[1]-p[1]); ux, uy = (q[0]-p[0])/d, (q[1]-p[1])/d
        arrow(ax, (p[0]+3.8*ux, p[1]+3.8*uy), (q[0]-3.8*ux, q[1]-3.8*uy), 'varie' if i == 0 else 'sujet', lw=0.9)
text(ax, X0, 53.5, 'plusieurs liens', 'varie', 's')
box(ax, 10, 2, 68, 8, 'resultat', label='relation = ensemble de liens', size='s')
save(fig, '42-261')
