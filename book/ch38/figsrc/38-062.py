import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import degrees, atan2
from matplotlib.patches import Arc

def wedge(P, Q, R, r, role='varie'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))

fig, ax = canvas(62)
V = [(8 + i * 18, 18 if i % 2 == 0 else 46) for i in range(5)]
tris = [(V[i], V[i + 1], V[i + 2]) for i in range(3)]
for t in tris:
    poly(ax, list(t), 'fixe')
edges = {(0, 1), (1, 2), (0, 2), (1, 3), (2, 3), (2, 4), (3, 4)}      # 7 côtés au total
for i, j in sorted(edges):
    if (i, j) != (0, 2):
        line(ax, [V[i], V[j]], 'sujet', 1.6)
line(ax, [V[0], V[2]], 'encre', 2.8)
for k, (a, b, c) in enumerate(tris):
    r = 2.6 + 1.3 * k
    wedge(a, b, c, r); wedge(b, a, c, r); wedge(c, a, b, r)
text(ax, 26, 11.5, 'base mesurée au ruban', 'encre', 's', weight='bold')
text(ax, 22, 3.5, '6 côtés calculés', 'sujet', 's', weight='bold')
text(ax, 62, 3.5, 'angles mesurés', 'varie', 's', weight='bold')
save(fig, '38-062')
