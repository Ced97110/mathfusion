import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
import math
fig, ax = canvas(68)
cx, cy, R = 22, 40, 13
V = [(cx, cy + R), (cx - R * math.cos(math.radians(30)), cy - R / 2), (cx + R * math.cos(math.radians(30)), cy - R / 2)]
poly(ax, V, 'sujet')
def shrink(p, q, d):
    L = math.dist(p, q); return (p[0] + (q[0] - p[0]) * d / L, p[1] + (q[1] - p[1]) * d / L)
for i in range(3):
    p, q = V[i], V[(i + 1) % 3]
    arrow(ax, shrink(p, q, 5.5), shrink(q, p, 5.5), 'varie', lw=1.1, curve=-0.0)
for i, v in enumerate(V): disc(ax, v[0], v[1], 3.2, 'sujet', label=str(i + 1))
text(ax, cx, 18, 'tiers de tour du triangle', 'sujet', 's')
xs = [54, 66, 78]; yy = 40
for i in range(3): disc(ax, xs[i], yy, 3.2, 'autre', label=str(i + 1))
arrow(ax, (xs[0] + 3.8, yy + 1), (xs[1] - 3.8, yy + 1), 'varie', curve=-0.0)
arrow(ax, (xs[1] + 3.8, yy + 1), (xs[2] - 3.8, yy + 1), 'varie')
arrow(ax, (xs[2] - 1, yy - 3.8), (xs[0] + 1, yy - 3.8), 'varie', curve=-0.45)
text(ax, 66, 18, 'permutation de 1, 2, 3', 'autre', 's')
arrow(ax, (37, 40), (48, 40), 'resultat', lw=1.2, both=True)
text(ax, 44, 6, r'$D_3=S_3$', 'resultat', 'xl', weight='bold')
save(fig, '44-214')
