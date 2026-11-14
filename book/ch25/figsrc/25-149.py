import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax, c, r, a0, a1, role, lw=1.0):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
fig, ax = canvas(62)
ox, oy, u = 14, 10, 24
arrow(ax, (ox-4, oy), (ox+38, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy-3), (ox, oy+46), 'fixe', lw=0.8)
A = (ox+u, oy); B = (ox+u, oy+u)
line(ax, [A, B], 'fixe', lw=1.0, dash=True)
arrow(ax, (ox, oy), A, 'autre', lw=1.6)
arrow(ax, (ox, oy), B, 'sujet', lw=1.8)
arc(ax, (ox, oy), 14, 0, 45, 'varie', 1.5)
text(ax, ox+19, oy+4.5, '45°', 'varie', 's')
text(ax, ox+12, oy-3.5, r'$a = 1$', 'autre', 's'); text(ax, A[0]+6, oy+12, r'$b = 1$', 'fixe', 's')
text(ax, B[0]-5, B[1]+3.5, r'$1 + i$', 'sujet', 's')
text(ax, 63, 50, r'$\tan = b/a = 1$', 'sujet', 'm')
text(ax, 63, 42, 'rotation de 45°', 'varie', 'm')
text(ax, 63, 34, r'agrandit de $\sqrt{2}$', 'resultat', 'm')
text(ax, ox+u/2-4.5, oy+u/2+4.5, r'longueur $\sqrt{2}$', 'resultat', 's', rot=45)
save(fig, '25-149')
