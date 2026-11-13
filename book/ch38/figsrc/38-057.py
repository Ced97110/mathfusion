import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians
from matplotlib.patches import Arc

s = 0.17
fig, ax = canvas(88)
A = (16, 30)
def pt(dist, ang): return (A[0] + dist*s*cos(radians(ang)), A[1] + dist*s*sin(radians(ang)))
P = pt(269.459, 80); Q = pt(347.362, 50)
poly(ax, [A, P, Q], 'fixe')
line(ax, [A, P], 'sujet', 2.0); line(ax, [A, Q], 'sujet', 2.0)
line(ax, [P, Q], 'varie', 2.0, dash=True)
ax.add_patch(Arc(A, 18, 18, theta1=50, theta2=80, ec=COL['resultat'], lw=1.1, zorder=3))
text(ax, A[0] + 6.5, A[1] + 14, '30°', 'resultat', 's', weight='bold')
arrow(ax, (A[0] + 11*cos(radians(66)), A[1] + 11*sin(radians(66))), ((P[0] + Q[0]) / 2 - 2, P[1] - 1.5), 'fixe', both=True)
text(ax, 44, 55, 'en face', 'fixe', 's', rot=0)
for p, n, dx, dy in ((A, 'A', -3, -3), (P, 'P', 0, 3.5), (Q, 'Q', 0, 3.5)):
    disc(ax, p[0], p[1], 1.0, 'encre'); text(ax, p[0] + dx, p[1] + dy, n, 'encre', 'm')
text(ax, (A[0] + P[0]) / 2 - 3.5, (A[1] + P[1]) / 2, '269,5 m', 'sujet', 's', rot=80, weight='bold')
M = (A[0] + 0.8 * (Q[0] - A[0]), A[1] + 0.8 * (Q[1] - A[1]))
text(ax, M[0] + 3, M[1] - 3, '347,4 m', 'sujet', 's', rot=50, weight='bold')
text(ax, (P[0] + Q[0]) / 2, P[1] + 4.5, 'PQ ?', 'varie', 's', weight='bold')
box(ax, 2, 14, 84, 9, 'limite', label='× sinus : le côté en face de 30° est inconnu', size='s')
box(ax, 2, 2, 84, 9, 'resultat', label='✓ cosinus : deux côtés et l’angle entre eux', size='s')
save(fig, '38-057')
