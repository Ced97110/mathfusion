import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians, degrees, atan2, hypot
from matplotlib.patches import Arc

def wedge(P, Q, R, r, role='fixe'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))

al, s = 51.33, 0.3
fig, ax = canvas(68)
A = (14, 16); B = (A[0] + 150*s, A[1])
P = (A[0] + 162.793*s*cos(radians(al)), A[1] + 162.793*s*sin(radians(al))); H = (P[0], A[1])
poly(ax, [A, B, P], 'fixe')
line(ax, [A, B], 'sujet', 2.2); line(ax, [B, P], 'fixe', 1.0); line(ax, [A, P], 'varie', 1.8)
line(ax, [P, H], 'resultat', 2.2)
d = 2.4
line(ax, [(H[0] - d, A[1]), (H[0] - d, A[1] + d), (H[0], A[1] + d)], 'fixe', 0.7)
wedge(A, B, P, 6); wedge(B, A, P, 5); wedge(P, A, B, 5, 'resultat')
text(ax, A[0] + 14, A[1] + 4.5, '51,33°', 'fixe', 's')
text(ax, B[0] - 9, B[1] + 6, '69,20°', 'fixe', 's')
u = (A[0]-P[0], A[1]-P[1]); v = (B[0]-P[0], B[1]-P[1]); lu = hypot(*u); lv = hypot(*v)
bx, by = u[0]/lu + v[0]/lv, u[1]/lu + v[1]/lv; lb = hypot(bx, by)
line(ax, [(P[0] + 1.5, P[1] - 4.2), (P[0] + 6, P[1] - 1)], 'resultat', 0.6)
text(ax, P[0] + 7, P[1] - 1, '59,47°', 'resultat', 's', ha='left', weight='bold')
text(ax, (A[0] + B[0]) / 2, A[1] - 4.5, 'AB = 150 m', 'sujet', 's', weight='bold')
text(ax, (A[0] + P[0]) / 2 - 3, (A[1] + P[1]) / 2 + 3, 'AP ≈ 162,8 m', 'varie', 's', ha='right', weight='bold')
text(ax, H[0] - 2.5, A[1] + 13, 'w ≈ 127,1 m', 'resultat', 's', ha='right', weight='bold')
text(ax, 44, 4, 'angles aigus : H est entre A et B', 'fixe', 's')
save(fig, '38-066')
