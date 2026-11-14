import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians, degrees, atan2, hypot
from matplotlib.patches import Arc

def wedge(ax, P, Q, R, r, role='varie'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))

al = 51.33; s = 0.2
fig, ax = canvas(66)

def tri(x0, AP, wtxt, aptxt):
    A = (x0, 14); P = (x0 + AP*s*cos(radians(al)), 14 + AP*s*sin(radians(al))); H = (P[0], 14)
    poly(ax, [A, H, P], 'fixe')
    line(ax, [A, H], 'fixe', 1.0); line(ax, [A, P], 'varie', 2.0); line(ax, [H, P], 'sujet', 2.0)
    wedge(ax, A, H, P, 6, 'fixe')
    d = 2.4
    line(ax, [(H[0] - d, 14), (H[0] - d, 14 + d), (H[0], 14 + d)], 'fixe', 0.7)
    text(ax, A[0] + 11, A[1] + 3, '51,33°', 'fixe', 's')
    text(ax, (A[0] + P[0])/2 - 3, (A[1] + P[1])/2 + 3, 'AP', 'varie', 'm', weight='bold')
    text(ax, H[0] + 3, (14 + P[1])/2, 'w', 'sujet', 'm', weight='bold')
    text(ax, (A[0] + H[0])/2 + 2, 7.5, aptxt, 'varie', 's', weight='bold')
    text(ax, (A[0] + H[0])/2 + 2, 3, wtxt, 'sujet', 's', weight='bold')
    return A, H, P

tri(5, 162.8, 'w = 127,1 m', 'AP = 162,8 m')
tri(50, 200.0, 'w = 156,2 m', 'AP = 200 m')
text(ax, 44, 56.5, r'$w = AP \times \sin\alpha$ : même angle, même relation', 'encre', 's')
text(ax, 44, 62, 'sin 51,33° = 0,78076 dans les deux cas', 'fixe', 's')
save(fig, '38-050')
