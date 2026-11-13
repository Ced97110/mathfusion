import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

def arc(x, y, r, a, b, role, lw=1.0):
    ax.add_patch(Arc((x, y), 2 * r, 2 * r, theta1=a, theta2=b, color=COL[role], lw=lw, zorder=3))

fig, ax = canvas(76)
k = 0.4
al, be = 51.33, 69.20
ta, tb = math.tan(math.radians(al)), math.tan(math.radians(be))
w = 150 * ta * tb / (ta + tb)
g = 16.0
A = (10.0, g); B = (A[0] + 150 * k, g)
P = (A[0] + w / ta * k, g + w * k)
line(ax, [(4, g), (84, g)], 'fixe', lw=0.7)
line(ax, [A, B], 'fixe', lw=2.0)
arrow(ax, A, (A[0] + (P[0] - A[0]) * 0.93, A[1] + (P[1] - A[1]) * 0.93), 'sujet')
arrow(ax, B, (B[0] + (P[0] - B[0]) * 0.93, B[1] + (P[1] - B[1]) * 0.93), 'sujet')
disc(ax, A[0], g, 1.3, 'sujet'); disc(ax, B[0], g, 1.3, 'sujet'); disc(ax, P[0], P[1], 1.3, 'sujet')
arc(A[0], A[1], 8, 0, al, 'varie'); arc(B[0], B[1], 8, 180 - be, 180, 'varie')
text(ax, A[0] + 14, g + 4.2, 'α = 51,33°', 'varie', 's', weight='bold')
text(ax, B[0] + 1, g + 12, 'β = 69,20°', 'varie', 's', weight='bold', ha='left')
text(ax, P[0], P[1] + 3.5, 'poteau P', 'sujet', 's')
brace(ax, A[0], B[0], g - 3, 'fixe', label='base AB : 150 m')
text(ax, A[0] - 3, g + 2.5, 'A', 'sujet', 's')
text(ax, B[0] + 3, g + 2.5, 'B', 'sujet', 's')
save(fig, '38-046')
