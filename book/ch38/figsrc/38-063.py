import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians
from matplotlib.patches import Arc

s = 0.014
fig, ax = canvas(78)
O = (8, 7)
def pt(dist, ang): return (O[0] + dist*s*cos(radians(ang)), O[1] + dist*s*sin(radians(ang)))
A = O; B = pt(3000, 0); D = pt(4000, 30); C = pt(5000, 60)
poly(ax, [A, B, D], 'sujet'); poly(ax, [A, D, C], 'autre')
line(ax, [A, B, D, C, A], 'fixe', 1.2)
line(ax, [A, D], 'varie', 2.0, dash=True)
ax.add_patch(Arc(A, 22, 22, theta1=0, theta2=30, ec=COL['fixe'], lw=0.9, zorder=3))
ax.add_patch(Arc(A, 22, 22, theta1=30, theta2=60, ec=COL['fixe'], lw=0.9, zorder=3))
text(ax, A[0] + 18 * cos(radians(15)), A[1] + 18 * sin(radians(15)), '30°', 'fixe', 's')
text(ax, A[0] + 18 * cos(radians(45)), A[1] + 18 * sin(radians(45)), '30°', 'fixe', 's')
text(ax, (A[0] + B[0]) / 2, A[1] - 3.5, '3000 m', 'sujet', 's', weight='bold')
text(ax, (A[0] + D[0]) / 2 + 3.2, (A[1] + D[1]) / 2 - 3.2, '4000 m', 'varie', 's', rot=30, weight='bold')
text(ax, (A[0] + C[0]) / 2 - 3.2, (A[1] + C[1]) / 2 + 1.8, '5000 m', 'autre', 's', rot=60, weight='bold')
text(ax, 42, 11.5, '3 millions m²', 'sujet', 's', weight='bold')
text(ax, 40.5, 43, '5 millions m²', 'autre', 's', weight='bold')
text(ax, 73, 44, '3 + 5\n= 8 millions\nde m²', 'resultat', 's', weight='bold')
save(fig, '38-063')
