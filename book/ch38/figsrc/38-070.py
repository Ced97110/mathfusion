import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians, degrees, atan2
from matplotlib.patches import Arc

def wedge(P, Q, R, r, role):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))
    return (a1 + d / 2)

s = 0.27
fig, ax = canvas(96)
O = (20, 15)
def pt(dist, ang): return (O[0] + dist*s*cos(radians(ang)), O[1] + dist*s*sin(radians(ang)))
A = O; B = (O[0] + 200*s, O[1]); P = pt(269.459, 80); Q = pt(347.362, 50)
line(ax, [A, B], 'fixe', 1.0)
line(ax, [A, P], 'sujet', 1.8); line(ax, [A, Q], 'sujet', 1.8)
line(ax, [B, P], 'autre', 1.8); line(ax, [B, Q], 'autre', 1.8)
line(ax, [P, Q], 'resultat', 2.6)
wedge(A, Q, P, 12, 'sujet'); m = wedge(B, Q, P, 14, 'autre')
text(ax, A[0] + 8.6, A[1] + 17.6, '30°', 'sujet', 's', weight='bold')
text(ax, B[0] + 20 * cos(radians(m)), B[1] + 20 * sin(radians(m)), '35°', 'autre', 's', weight='bold')
for p, n, dx, dy in ((A, 'A', -3, -3), (B, 'B', 3, -3), (P, 'P', 0, 3.5), (Q, 'Q', 0, 3.5)):
    disc(ax, p[0], p[1], 1.0, 'encre'); text(ax, p[0] + dx, p[1] + dy, n, 'encre', 'm')
text(ax, (A[0] + P[0]) / 2 - 3.5, (A[1] + P[1]) / 2, '269,5 m', 'sujet', 's', rot=80, weight='bold')
M = (A[0] + 0.8 * (Q[0] - A[0]), A[1] + 0.8 * (Q[1] - A[1]))
text(ax, M[0] - 2.8, M[1] + 3.2, '347,4 m', 'sujet', 's', rot=50, weight='bold')
N = (B[0] + 0.8 * (P[0] - B[0]), B[1] + 0.8 * (P[1] - B[1]))
text(ax, N[0] + 3.4, N[1] + 1.6, '306,4 m', 'autre', 's', rot=-60, weight='bold')
text(ax, (B[0] + Q[0]) / 2 + 3.6, (B[1] + Q[1]) / 2, '267,1 m', 'autre', 's', rot=85, weight='bold')
text(ax, (P[0] + Q[0]) / 2, P[1] + 4.2, 'PQ ≈ 176,5 m des deux côtés', 'resultat', 's', weight='bold')
text(ax, 24, 3.5, 'depuis A', 'sujet', 's', weight='bold')
text(ax, 66, 3.5, 'depuis B', 'autre', 's', weight='bold')
save(fig, '38-070')
