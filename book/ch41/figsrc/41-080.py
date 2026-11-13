import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Arc
fig, ax = canvas(66)
ox, oy, s = 12, 8, 17
P = lambda x, y: (ox + s * x, oy + s * y)
O, U, V = P(0, 0), P(1, 3), P(4, 2)
poly(ax, [O, U, V], 'fixe')
arrow(ax, O, U, 'sujet', lw=1.6)
arrow(ax, O, V, 'autre', lw=1.6)
arrow(ax, V, U, 'varie', lw=1.6)
ax.add_patch(Arc(O, 22, 22, theta1=math.degrees(math.atan2(2, 4)), theta2=math.degrees(math.atan2(3, 1)), color=COL['resultat'], lw=1.6, zorder=4))
text(ax, O[0] - 2.5, O[1] - 2, r'$O$', 'encre', 'm')
text(ax, U[0] - 2.5, U[1] + 2.5, r'$U$', 'sujet', 'm')
text(ax, V[0] + 3, V[1] - 1, r'$V$', 'autre', 'm')
text(ax, O[0] + 17, O[1] + 18, r'$\theta=45^\circ$', 'resultat', 'm')
text(ax, 3, 36, r'$u=\langle1,3\rangle$' + '\n' + r'longueur $\sqrt{10}$', 'sujet', 's', ha='left')
text(ax, 58, 16, r'$v=\langle4,2\rangle$' + '\n' + r'longueur $\sqrt{20}$', 'autre', 's')
text(ax, 62, 58, r'$u-v=\langle-3,1\rangle$' + '\n' + r'face à $\theta$ ; carré $=10$', 'varie', 's')
save(fig, '41-080')
