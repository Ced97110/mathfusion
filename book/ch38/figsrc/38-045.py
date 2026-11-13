import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

def arc(x, y, r, a, b, role, lw=1.0):
    ax.add_patch(Arc((x, y), 2 * r, 2 * r, theta1=a, theta2=b, color=COL[role], lw=lw, zorder=3))

fig, ax = canvas(72)
k = 0.4                                     # mm par mètre : AB = 150 m -> 60 mm
al, be = 51.33, 69.20
ta, tb = math.tan(math.radians(al)), math.tan(math.radians(be))
w = 150 * ta * tb / (ta + tb)               # 127,1 m
g = 12.0
A = (10.0, g); B = (A[0] + 150 * k, g)
H = (A[0] + w / ta * k, g)
P = (H[0], g + w * k)
line(ax, [(4, g), (84, g)], 'fixe', lw=0.7)
line(ax, [(4, P[1]), (84, P[1])], 'fixe', lw=0.7, dash=True)
poly(ax, [A, B, P], 'sujet')
line(ax, [H, P], 'resultat', lw=2.0)
line(ax, [(H[0] - 2.2, g), (H[0] - 2.2, g + 2.2), (H[0], g + 2.2)], 'fixe', lw=0.7)
arc(A[0], A[1], 8, 0, al, 'varie'); arc(B[0], B[1], 8, 180 - be, 180, 'varie')
text(ax, A[0] + 14, g + 4.2, '51,33°', 'varie', 's', weight='bold')
text(ax, B[0] - 14, g + 5.2, '69,20°', 'varie', 's', weight='bold')
text(ax, A[0] - 1, g - 3.5, 'A', 'sujet', 's')
text(ax, B[0] + 1, g - 3.5, 'B', 'sujet', 's')
text(ax, H[0], g - 3.5, 'H', 'resultat', 's')
text(ax, P[0], P[1] + 3.5, 'P', 'sujet', 's')
text(ax, H[0] - 2, (g + P[1]) / 2, 'w = PH', 'resultat', 'm', ha='right', weight='bold')
text(ax, (A[0] + B[0]) / 2 + 9, g - 7, '150 m', 'fixe', 's')
text(ax, 82, P[1] + 3.5, 'autre rive', 'fixe', 's', ha='right')
save(fig, '38-045')
