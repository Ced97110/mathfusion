import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians, degrees, atan2, hypot
from matplotlib.patches import Arc

def wedge(ax, P, Q, R, r, role='varie'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))

al, be = 51.33, 69.20
AP, AB, s = 162.793, 150.0, 0.3
fig, ax = canvas(100)
A = (18, 56); B = (A[0] + AB*s, A[1]); P = (A[0] + AP*s*cos(radians(al)), A[1] + AP*s*sin(radians(al)))
poly(ax, [A, B, P], 'fixe')
line(ax, [A, B], 'fixe', 1.0); line(ax, [B, P], 'fixe', 1.0); line(ax, [A, P], 'sujet', 2.0)
wedge(ax, A, B, P, 6, 'fixe'); wedge(ax, B, A, P, 5, 'fixe'); wedge(ax, P, A, B, 5, 'resultat')
text(ax, A[0] - 3, A[1] - 3, 'A'); text(ax, B[0] + 3, B[1] - 3, 'B'); text(ax, P[0], P[1] + 3.5, 'P')
text(ax, A[0] + 14, A[1] + 4.5, '51,33°', 'fixe', 's')
text(ax, B[0] - 9, B[1] + 6, '69,20°', 'fixe', 's')
u = (A[0]-P[0], A[1]-P[1]); v = (B[0]-P[0], B[1]-P[1]); lu = hypot(*u); lv = hypot(*v)
bx, by = u[0]/lu + v[0]/lv, u[1]/lu + v[1]/lv; lb = hypot(bx, by)
text(ax, P[0] + 13*bx/lb, P[1] + 13*by/lb, '59,47°', 'resultat', 's', weight='bold')
text(ax, (A[0]+B[0])/2, A[1] - 4, 'AB = 150 m', 'fixe', 's')
text(ax, (A[0]+P[0])/2 - 3, (A[1]+P[1])/2 + 3, 'AP ≈ 162,8 m', 'sujet', 's', ha='right', weight='bold')
box(ax, 2, 36, 84, 9, 'resultat', label='angle en P : 180° − 51,33° − 69,20°', size='s')
box(ax, 2, 23, 84, 9, 'fixe', label='AP est en face de β = 69,20°', size='s')
box(ax, 2, 10, 84, 9, 'sujet', label='AP = 150 × 0,93483 ÷ 0,86136', size='s')
arrow(ax, (44, 36), (44, 32.2), 'varie'); arrow(ax, (44, 23), (44, 19.2), 'varie')
save(fig, '38-049')
