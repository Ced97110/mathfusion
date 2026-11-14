import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import degrees, atan2
from matplotlib.patches import Arc

def wedge(P, Q, R, r, role='varie'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))

fig, ax = canvas(62)
# un seul triangle : une base, deux angles, un sommet
A, B, C = (5, 14), (31, 14), (23, 40)
poly(ax, [A, B, C], 'fixe'); line(ax, [A, B, C, A], 'fixe', 1.0)
line(ax, [A, B], 'encre', 2.4)
wedge(A, B, C, 5); wedge(B, A, C, 5)
disc(ax, C[0], C[1], 1.3, 'resultat'); text(ax, C[0] + 1, C[1] + 4, 'sommet', 'resultat', 's', weight='bold')
text(ax, 18, 8, '1 base + 2 angles', 'fixe', 's')
text(ax, 18, 56, 'un triangle', 'encre', 's', weight='bold')
# un pays : des triangles qui s'enchaînent à partir d'une seule base
n = 6
V = [(47 + i * 37 / (n - 1), 14 if i % 2 == 0 else 40) for i in range(n)]
for i in range(n - 2):
    a, b, c = V[i], V[i + 1], V[i + 2]
    poly(ax, [a, b, c], 'sujet'); line(ax, [a, b, c, a], 'sujet', 0.9)
line(ax, [V[0], V[1]], 'encre', 2.4)
text(ax, 66, 8, 'beaucoup, 1 seule base', 'sujet', 's')
text(ax, 66, 56, 'un pays entier', 'sujet', 's', weight='bold')
arrow(ax, (36, 27), (44, 27), 'varie', lw=1.4)
text(ax, 40, 31, 'répéter', 'varie', 's', weight='bold')
save(fig, '38-059')
