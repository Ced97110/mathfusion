import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(56)
xs = (14, 44, 74); ys = (40, 28, 16)
t1 = {1: 1, 2: 3, 3: 2}; t3 = {1: 2, 2: 1, 3: 3}
for c in range(3):
    for i in range(3): disc(ax, xs[c], ys[i], 3.2, 'fixe', label=str(i + 1), size='s')
for i in (1, 2, 3):
    p = (xs[0] + 3.6, ys[i - 1] - (0 if t1[i] == i else (3.6 * (ys[i - 1] - ys[t1[i] - 1]) / 30)))
    arrow(ax, (xs[0] + 3.6, ys[i - 1]), (xs[1] - 3.6, ys[t1[i] - 1]), 'sujet', lw=1.1)
    arrow(ax, (xs[1] + 3.6, ys[i - 1]), (xs[2] - 3.6, ys[t3[i] - 1]), 'varie', lw=1.1)
text(ax, 29, 48.5, r'$\tau_1$', 'sujet', 'l'); text(ax, 59, 48.5, r'$\tau_3$', 'varie', 'l')
box(ax, 4, 2, 80, 8, 'resultat', label=r'$\tau_3 \circ \tau_1$ : 1→2, 2→3, 3→1 = $\sigma$', size='m')
save(fig, '44-234')
