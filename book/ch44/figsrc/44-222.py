import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(52)
h = 8.5
def corners(cx, cy): return [(cx - h, cy + h), (cx + h, cy + h), (cx + h, cy - h), (cx - h, cy - h)]
def pull(p, q, d):
    L = math.dist(p, q); return (p[0] + (q[0] - p[0]) * d / L, p[1] + (q[1] - p[1]) * d / L)
import math
cy = 28
# panel A : 1 can go to n = 4 places
C = corners(16, cy)
for c in C: disc(ax, c[0], c[1], 2.6, 'varie')
disc(ax, 16, cy, 3.2, 'sujet', label='1')
for c in C: arrow(ax, pull((16, cy), c, 4), pull(c, (16, cy), 3.2), 'varie', lw=0.9)
text(ax, 16, 8, r'1 : $n=4$ places', 'varie', 's')
# panel B : 2 goes next to the place of 1
C = corners(48, cy)
disc(ax, C[0][0], C[0][1], 2.6, 'sujet', label='1')
for i in (1, 3): disc(ax, C[i][0], C[i][1], 2.6, 'varie')
disc(ax, C[2][0], C[2][1], 2.6, 'fixe')
disc(ax, 48, cy, 3.2, 'varie', label='2')
for i in (1, 3): arrow(ax, pull((48, cy), C[i], 4), pull(C[i], (48, cy), 3.2), 'varie', lw=0.9)
text(ax, 48, 8, '2 : 2 places voisines', 'varie', 's')
# panel C : total
text(ax, 74, 34, r'$4\times 2=8$', 'resultat', 'l', weight='bold')
text(ax, 74, 25, r'$n\times 2=2n$', 'resultat', 'm')
text(ax, 74, 8, 'mouvements', 'resultat', 's')
save(fig, '44-222')
