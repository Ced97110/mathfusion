import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(58)
xs = (14, 44, 74); ys = (40, 28, 16)
x_ = {1: 2, 2: 1, 3: 3}; sg = {1: 2, 2: 3, 3: 1}
for c in range(3):
    for i in range(3): disc(ax, xs[c], ys[i], 3.2, 'fixe', label=str(i + 1), size='s')
for i in (1, 2, 3):
    arrow(ax, (xs[0] + 3.6, ys[i - 1]), (xs[1] - 3.6, ys[x_[i] - 1]), 'sujet', lw=1.1)
    arrow(ax, (xs[1] + 3.6, ys[x_[i] - 1]), (xs[2] - 3.6, ys[sg[x_[i]] - 1]), 'varie', lw=1.1)
text(ax, 29, 49, r'$x = \tau_3$', 'sujet', 'm'); text(ax, 59, 49, r'$\sigma$', 'varie', 'l')
text(ax, 44, 55, r'$\sigma \circ x = \tau_2$', 'resultat', 'l')
box(ax, 4, 2, 80, 8, 'resultat', label=r'1→3, 2→2, 3→1 : c’est bien $\tau_2$', size='m')
save(fig, '44-238')
