import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Arc
fig, ax = canvas(64)
u = 34; ox, oy = 21, 6
c, s = math.cos(math.radians(30)), math.sin(math.radians(30))
R = lambda x, y: (ox + u * (c * x - s * y), oy + u * (s * x + c * y))
poly(ax, [(ox, oy), (ox + u, oy), (ox + u, oy + u), (ox, oy + u)], 'fixe', fill=False, lw=0.7)
poly(ax, [R(0, 0), R(1, 0), R(1, 1), R(0, 1)], 'sujet')
line(ax, [(ox - 6, oy), (ox + u + 8, oy)], 'fixe', lw=0.5)
ax.add_patch(Arc((ox, oy), 2 * 14, 2 * 14, theta1=0, theta2=30, color=COL['varie'], lw=1.1, zorder=4))
text(ax, ox + 18, oy + 3.4, '30°', 'varie', 's')
ax.add_patch(Circle(R(1, 0), 1.0, fc=COL['encre'], ec=COL['encre'], zorder=6))
ax.add_patch(Circle((ox + u, oy), 1.0, fc=COL['fixe'], ec=COL['fixe'], zorder=6))
text(ax, ox + u + 1, oy - 3.2, '(1, 0)', 'fixe', 's', ha='left')
text(ax, R(1, 0)[0] + 2, R(1, 0)[1] + 2, 'A', 'encre', 's', ha='left', weight='bold')
text(ax, 62, 44, 'carré de départ', 'fixe', 's', ha='left')
text(ax, 62, 36, 'carré tourné', 'sujet', 's', ha='left')
text(ax, 62, 29, 'aire 1', 'sujet', 's', ha='left')
text(ax, 62, 22, r'$\det=1$', 'sujet', 'm', ha='left')
text(ax, 62, 56, r'A $\approx$ (0,87 ; 0,5)', 'encre', 's', ha='left')
save(fig, '73-018')
