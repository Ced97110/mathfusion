import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(70)
xs = (30, 50, 70); ys = (52, 33, 14)
t1 = {1: 1, 2: 3, 3: 2}; t3 = {1: 2, 2: 1, 3: 3}
for r, y in enumerate(ys):
    v = r + 1; pl = [v, t1[v], t3[t1[v]]]
    for c, x in enumerate(xs):
        poly(ax, pg(x, y, 6, 3), 'fixe')
        a = (90, 210, 330)[pl[c] - 1]; px, py = pol(x, y, 6, a); disc(ax, px, py, 1.9, 'resultat' if c == 2 else 'sujet')
    arrow(ax, (xs[0] + 8, y), (xs[1] - 8, y), 'sujet'); arrow(ax, (xs[1] + 8, y), (xs[2] - 8, y), 'varie')
    text(ax, 2, y, f'sommet {v}', 'sujet', 's', ha='left')
    text(ax, 83, y, f'{v}→{pl[2]}', 'resultat', 's')
text(ax, 30, 65, 'départ', 'sujet', 's'); text(ax, 50, 65, r'après $\tau_1$', 'sujet', 's'); text(ax, 70, 65, r'après $\tau_3$', 'varie', 's')
save(fig, '44-235')
