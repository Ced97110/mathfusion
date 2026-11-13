import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians
from matplotlib.patches import Arc

s = 0.27
fig, ax = canvas(98)
A = (20, 17); B = (A[0] + 200*s, A[1])
def fromA(dist, ang): return (A[0] + dist*s*cos(radians(ang)), A[1] + dist*s*sin(radians(ang)))
P = fromA(269.459, 80); Q = fromA(347.362, 50)
for X in (P, Q):
    line(ax, [A, X], 'fixe', 0.8); line(ax, [B, X], 'fixe', 0.8)
line(ax, [P, Q], 'resultat', 1.2, dash=True)
line(ax, [A, B], 'sujet', 2.4)
def arcA(r, ang): ax.add_patch(Arc(A, 2*r, 2*r, theta1=0, theta2=ang, ec=COL['varie'], lw=1.0, zorder=3))
def arcB(r, ang): ax.add_patch(Arc(B, 2*r, 2*r, theta1=180 - ang, theta2=180, ec=COL['varie'], lw=1.0, zorder=3))
def lab(C, r, ang, s_): text(ax, C[0] + r*cos(radians(ang)), C[1] + r*sin(radians(ang)), s_, 'varie', 's', weight='bold')
arcA(11, 50); arcA(18, 80); arcB(11, 60); arcB(18, 95)
lab(A, 14.5, 22, '50°'); lab(A, 23, 70, '80°')
lab(B, 14.5, 156, '60°'); lab(B, 24, 103, '95°')
for p, n, dx, dy in ((A, 'A', -3, -3), (B, 'B', 3, -3)):
    disc(ax, p[0], p[1], 1.1, 'sujet'); text(ax, p[0] + dx, p[1] + dy, n, 'encre', 'm')
for p, n in ((P, 'P'), (Q, 'Q')):
    disc(ax, p[0], p[1], 1.1, 'fixe', fill=False); text(ax, p[0], p[1] + 3.5, n, 'encre', 'm')
text(ax, (A[0] + B[0]) / 2, A[1] - 5, 'base d = 200 m', 'sujet', 's', weight='bold')
text(ax, (P[0] + Q[0]) / 2, P[1] + 4.5, 'PQ ?', 'resultat', 's', weight='bold')
text(ax, 44, 3.5, '5 mesures : la base et 4 angles', 'varie', 's', weight='bold')
save(fig, '38-055')
