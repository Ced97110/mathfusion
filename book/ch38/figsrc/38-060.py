import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import degrees, atan2
from matplotlib.patches import Arc

def wedge(P, Q, R, r, role='varie'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))

fig, ax = canvas(80)
def panel(ox, oy, title):
    box(ax, ox, oy, 40, 34, 'fixe', fill=False, lw=0.5)
    text(ax, ox + 20, oy + 38, title, 'encre', 's', weight='bold')
def sh(o, p): return (o[0] + p[0], o[1] + p[1])
A0, B0, C0 = (5, 6), (27, 6), (14, 22)

# 1 : la base
o = (2, 40); panel(*o, '1. base de 12 km')
a, b = sh(o, (6, 14)), sh(o, (36, 14))
line(ax, [a, b], 'encre', 2.6); disc(ax, a[0], a[1], 1.2, 'encre'); disc(ax, b[0], b[1], 1.2, 'encre')
text(ax, o[0] + 21, o[1] + 22, '12 km', 'encre', 's', weight='bold')

# 2 : un point visible des deux bouts, deux côtés calculés
o = (46, 40); panel(*o, '2. point visé, angles')
A, B, C = sh(o, A0), sh(o, B0), sh(o, C0)
poly(ax, [A, B, C], 'fixe'); line(ax, [A, B], 'encre', 2.0)
line(ax, [A, C], 'sujet', 2.0); line(ax, [B, C], 'sujet', 2.0)
wedge(A, B, C, 5); wedge(B, A, C, 5)
disc(ax, C[0], C[1], 1.2, 'resultat'); text(ax, C[0] + 1, C[1] + 6, 'point visé', 'resultat', 's')

# 3 : un côté calculé devient la base du triangle suivant
o = (2, 2); panel(*o, '3. un côté devient base')
A, B, C = sh(o, A0), sh(o, B0), sh(o, C0); D = sh(o, (37, 24))
poly(ax, [A, B, C], 'fixe'); line(ax, [A, B, C, A], 'fixe', 1.0)
poly(ax, [B, C, D], 'autre'); line(ax, [B, C, D, B], 'autre', 1.0)
line(ax, [B, C], 'encre', 2.6)
text(ax, o[0] + 21, o[1] + 30, 'nouvelle base', 'encre', 's', weight='bold')
arrow(ax, (o[0] + 16, o[1] + 28), (o[0] + 19.5, o[1] + 16), 'encre', lw=0.8)

# 4 : on recommence
o = (46, 2); panel(*o, '4. on recommence')
n = 6
V = [(o[0] + 4 + i * 34 / (n - 1), o[1] + (6 if i % 2 == 0 else 24)) for i in range(n)]
for i in range(n - 2):
    poly(ax, [V[i], V[i + 1], V[i + 2]], 'sujet'); line(ax, [V[i], V[i + 1], V[i + 2], V[i]], 'sujet', 0.9)
line(ax, [V[0], V[1]], 'encre', 2.4)
arrow(ax, (V[1][0] + 2, o[1] + 29), (V[5][0] - 2, o[1] + 29), 'varie', lw=1.2)
save(fig, '38-060')
