import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians, degrees, atan2
from matplotlib.patches import Arc

def wedge(P, Q, R, r, role='fixe'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))

al, s = 51.33, 0.35
fig, ax = canvas(80)
A = (16, 30); B = (A[0] + 150*s, A[1])
H = (A[0] + 101.717*s, A[1]); P = (H[0], A[1] + 127.1*s)
poly(ax, [A, B, P], 'fixe')
line(ax, [A, P], 'fixe', 1.0); line(ax, [B, P], 'fixe', 1.0)
line(ax, [P, H], 'sujet', 2.2)
line(ax, [A, H], 'varie', 2.6); line(ax, [H, B], 'autre', 2.6)
d = 2.2
line(ax, [(H[0] - d, A[1]), (H[0] - d, A[1] + d), (H[0], A[1] + d)], 'fixe', 0.7)
wedge(A, B, P, 6); wedge(B, A, P, 4)
text(ax, A[0] + 13, A[1] + 3.5, '51,33°', 'fixe', 's')
text(ax, B[0] - 10.5, B[1] + 6.5, '69,20°', 'fixe', 's')
text(ax, H[0] - 2.5, A[1] + 20, 'w = 127,1 m', 'sujet', 's', ha='right', weight='bold')
brace(ax, A[0], H[0], A[1] - 2, 'varie', depth=1.8); brace(ax, H[0] + 0.4, B[0], A[1] - 2, 'autre', depth=1.8)
text(ax, (A[0] + H[0]) / 2, A[1] - 11, 'w / tan 51,33°\n= 101,7 m', 'varie', 's', weight='bold')
text(ax, (H[0] + B[0]) / 2 + 3, A[1] - 11, 'w / tan 69,20°\n= 48,3 m', 'autre', 's', weight='bold')
brace(ax, A[0], B[0], A[1] - 18, 'resultat', depth=1.8)
text(ax, (A[0] + B[0]) / 2, A[1] - 26, '101,7 + 48,3 = 150 m = AB', 'resultat', 's', weight='bold')
save(fig, '38-067')
