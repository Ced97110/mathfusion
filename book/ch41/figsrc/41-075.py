import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Arc
fig, ax = canvas(84)
ox, oy, s = 14, 30, 9
P = lambda x, y: (ox + s * x, oy + s * y)
text(ax, 44, 79, r'$u\cdot v=\|u\|\,\|v\|\cos\theta$', 'sujet', 'l')
arrow(ax, P(0, 0), P(1, 3), 'sujet', lw=1.4)
arrow(ax, P(0, 0), P(4, 2), 'autre', lw=1.4)
ax.add_patch(Arc((ox, oy), 28, 28, theta1=math.degrees(math.atan2(2, 4)), theta2=math.degrees(math.atan2(3, 1)), color=COL['varie'], lw=1.5, zorder=4))
text(ax, ox + 33, oy + 24, r'$\theta=45^\circ$', 'varie', 'm')
text(ax, ox + 12, oy + 29, r'$\|u\|=\sqrt{10}$', 'sujet', 's')
text(ax, ox + 41, oy + 5, r'$\|v\|=\sqrt{20}$', 'autre', 's')
box(ax, 3, 4, 26, 14, 'fixe', label='$\\|u\\|\\|v\\|$\n$\\approx14{,}14$')
text(ax, 33.5, 11, r'$\times$', 'encre', 'xl')
box(ax, 38, 4, 26, 14, 'varie', label='$\\cos\\theta$\n$\\approx0{,}7071$')
text(ax, 68, 11, '=', 'encre', 'xl')
box(ax, 72, 4, 14, 14, 'resultat', label='$u\\cdot v$\n$=10$')
save(fig, '41-075')
