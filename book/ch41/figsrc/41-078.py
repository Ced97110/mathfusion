import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Arc
fig, ax = canvas(66)
ox, oy, s = 8, 28, 9
P = lambda x, y: (ox + s * x, oy + s * y)
arrow(ax, P(0, 0), P(1, 3), 'fixe', lw=1.4)
arrow(ax, P(0, 0), P(4, 2), 'fixe', lw=1.4)
ax.add_patch(Arc((ox, oy), 30, 30, theta1=math.degrees(math.atan2(2, 4)), theta2=math.degrees(math.atan2(3, 1)), color=COL['sujet'], lw=2.0, zorder=4))
text(ax, ox + 12, oy + 28.5, r'$u$', 'fixe', 'm')
text(ax, ox + 38, oy + 19, r'$v$', 'fixe', 'm')
text(ax, ox + 33, oy + 25, r'$\theta=45^\circ$', 'sujet', 'l')
text(ax, 5, 13, r'$\theta$ est toujours entre $0^\circ$ et $180^\circ$', 'encre', 's', ha='left')
f = numberline(ax, 8, 78, 5, 0, 180, step=45, arrow_right=False)
ax.plot([f(45)], [5], marker='o', ms=4.5, color=COL['sujet'], zorder=6)
save(fig, '41-078')
