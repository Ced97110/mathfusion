import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
u = 11.0; ox, oy = 9, 10
P = lambda x, y: (ox + u * x, oy + u * y)
from matplotlib.patches import Arc
import math
arrow(ax, P(0, 0), P(6.7, 0), 'fixe'); arrow(ax, P(0, 0), P(0, 5.5), 'fixe')
ax.add_patch(Arc(P(0, 0), 2 * u, 2 * u, theta1=0, theta2=90, ec=COL['fixe'], lw=0.7, zorder=1))
al = math.atan2(4, 5); c, s = math.cos(al), math.sin(al)
line(ax, [P(0, 0), P(5, 4)], 'fixe', lw=0.7)
line(ax, [P(5, 4), P(5, 0)], 'fixe', dash=True, lw=0.7); line(ax, [P(5, 4), P(0, 4)], 'fixe', dash=True, lw=0.7)
arrow(ax, P(c, s), P(5, 4), 'varie', lw=1.3)
ax.add_patch(Arc(P(0, 0), 14, 14, theta1=0, theta2=38.66, ec=COL['varie'], lw=1.1, zorder=4))
disc(ax, *P(c, s), 1.1, 'sujet'); disc(ax, *P(5, 4), 1.4, 'resultat')
text(ax, 24, 11.5, r'$\alpha$ = 38,66°', 'varie', 's', ha='left')
text(ax, 11, 29, '(0,781 ; 0,625)', 'sujet', 's', ha='left')
text(ax, P(5, 4)[0], P(5, 4)[1] + 4.5, '(5 ; 4)', 'resultat', 'm')
text(ax, 45, 31, r'$\times$ 6,40', 'varie', 'm')
text(ax, P(5, 0)[0], oy - 4, '5', 'fixe', 's'); text(ax, ox - 3, P(0, 4)[1], '4', 'fixe', 's')
save(fig, '37-101')
