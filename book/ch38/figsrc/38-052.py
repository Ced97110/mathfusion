import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, tan, radians, degrees, atan2, hypot
from matplotlib.patches import Arc

def wedge(ax, P, Q, R, r, role='varie'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))

fig, ax = canvas(104)
# --- rivière : A, B, P, H (échelle 0,3 mm par mètre) ---
al, be, s = 51.33, 69.20, 0.3
A = (8, 56); B = (A[0] + 150*s, A[1])
P = (A[0] + 162.793*s*cos(radians(al)), A[1] + 162.793*s*sin(radians(al))); H = (P[0], A[1])
poly(ax, [A, B, P], 'fixe')
line(ax, [A, B, P, A], 'fixe', 1.0)
line(ax, [P, H], 'sujet', 1.8, dash=False)
wedge(ax, A, B, P, 6, 'fixe'); wedge(ax, B, A, P, 5, 'fixe'); wedge(ax, P, A, B, 4, 'fixe')
disc(ax, H[0], H[1], 1.1, 'varie'); text(ax, H[0], H[1] - 3.5, 'H', 'varie', 's', weight='bold')
text(ax, A[0] + 11, A[1] + 3.5, 'α', 'fixe', 's'); text(ax, B[0] - 7, B[1] + 5, 'β', 'fixe', 's')
text(ax, (A[0] + B[0]) / 2 - 3, A[1] - 6.5, '150 m', 'fixe', 's')
text(ax, H[0] + 3, (A[1] + P[1]) / 2, 'w', 'sujet', 'm', weight='bold')
line(ax, [(P[0] + 1, P[1] - 3), (63, P[1] - 3)], 'fixe', 0.6)
text(ax, 64.5, P[1] - 3, '180° − α − β', 'varie', 's', ha='left', weight='bold')
text(ax, 58, 76, 'rivière :\nH entre A et B', 'encre', 's', ha='left', weight='bold')
# --- montagne : A, B, S, H (échelle 0,012 mm par mètre) ---
a2, b2, s2 = 18.0, 21.25, 0.012
hh = 1975.55
AH = hh / tan(radians(a2)); BH = hh / tan(radians(b2))
A2 = (6, 12); B2 = (A2[0] + 1000*s2, 12); H2 = (A2[0] + AH*s2, 12); S2 = (H2[0], 12 + hh*s2)
poly(ax, [A2, B2, S2], 'fixe')
line(ax, [A2, H2], 'fixe', 0.8)
line(ax, [A2, B2, S2, A2], 'fixe', 1.0)
line(ax, [S2, H2], 'sujet', 1.8)
wedge(ax, A2, B2, S2, 6, 'fixe'); wedge(ax, B2, A2, S2, 2.2, 'fixe'); wedge(ax, S2, A2, B2, 10, 'fixe')
disc(ax, H2[0], H2[1], 1.1, 'varie'); text(ax, H2[0], H2[1] - 3.5, 'H', 'varie', 's', weight='bold')
text(ax, A2[0] + 8.2, A2[1] + 1.6, 'α', 'fixe', 's')
line(ax, [(B2[0] + 3*cos(radians(100)), B2[1] + 3*sin(radians(100))), (B2[0] - 3, B2[1] + 10)], 'fixe', 0.6)
text(ax, B2[0] - 3, B2[1] + 12, '180° − β', 'fixe', 's')
line(ax, [(S2[0] - 10, S2[1] - 3.2), (S2[0] - 9, S2[1] + 8)], 'fixe', 0.6)
text(ax, S2[0] - 9, S2[1] + 10, 'β − α', 'varie', 's', weight='bold')
text(ax, (A2[0] + B2[0]) / 2, A2[1] - 6.5, '1000 m', 'fixe', 's')
text(ax, S2[0] + 2.5, (12 + S2[1]) / 2, 'h', 'sujet', 'm', ha='left', weight='bold')
text(ax, 8, 40, 'montagne : H après B', 'encre', 's', ha='left', weight='bold')
save(fig, '38-052')
