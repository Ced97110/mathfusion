import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians
from matplotlib.patches import Arc

s = 0.27
fig, ax = canvas(96)
O = (20, 15)
def pt(dist, ang): return (O[0] + dist*s*cos(radians(ang)), O[1] + dist*s*sin(radians(ang)))
A = O; B = (O[0] + 200*s, O[1]); P = pt(269.459, 80); Q = pt(347.362, 50)
poly(ax, [A, P, Q], 'resultat')
line(ax, [A, P, B, A], 'sujet', 1.3); line(ax, [A, Q, B], 'varie', 1.3)
line(ax, [A, B], 'fixe', 2.0)
line(ax, [P, Q], 'resultat', 1.4, dash=True)
ax.add_patch(Arc(A, 24, 24, theta1=50, theta2=80, ec=COL['resultat'], lw=0.9, zorder=3))
text(ax, A[0] + 8.6, A[1] + 17.6, '30°', 'resultat', 's', weight='bold')
for p, n, dx, dy in ((A, 'A', -3, -3), (B, 'B', 3, -3), (P, 'P', 0, 3.5), (Q, 'Q', 0, 3.5)):
    disc(ax, p[0], p[1], 1.0, 'encre'); text(ax, p[0] + dx, p[1] + dy, n, 'encre', 'm')
text(ax, (A[0] + B[0]) / 2, A[1] - 5, '200 m', 'fixe', 's')
text(ax, (A[0] + P[0]) / 2 - 3.5, (A[1] + P[1]) / 2, '269,5 m', 'sujet', 's', rot=80, weight='bold')
M = (A[0] + 0.8 * (Q[0] - A[0]), A[1] + 0.8 * (Q[1] - A[1]))
text(ax, M[0] - 2.8, M[1] + 3.2, '347,4 m', 'varie', 's', rot=50, weight='bold')
text(ax, (P[0] + Q[0]) / 2, P[1] + 4, 'PQ ?', 'resultat', 's', weight='bold')
text(ax, 55, 76, 'APQ', 'resultat', 's')
text(ax, 22, 3, 'triangle ABP', 'sujet', 's', weight='bold')
text(ax, 66, 3, 'triangle ABQ', 'varie', 's', weight='bold')
save(fig, '38-054')
