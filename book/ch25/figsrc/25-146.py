import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax, c, r, a0, a1, role, lw=1.0):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
fig, ax = canvas(55)
ox, oy, u = 8, 12, 9
arrow(ax, (ox, oy-3), (ox, oy+36), 'fixe', lw=0.6)
Q = (ox+4*u, oy+3*u)
line(ax, [(ox, oy), (Q[0], oy)], 'fixe', lw=1.2); line(ax, [(Q[0], oy), Q], 'fixe', lw=1.2, dash=True)
arrow(ax, (ox, oy), Q, 'sujet', lw=1.8)
arc(ax, (ox, oy), 10, 0, 36.87, 'varie', 1.4)
text(ax, ox+15, oy+3.5, 'direction', 'varie', 's')
text(ax, ox+18, oy-3.5, 'avance 4', 'fixe', 's'); text(ax, Q[0]+9, oy+13, 'monte 3', 'fixe', 's')
text(ax, 64, 46, r'$\tan = 3/4 = 0{,}75$', 'sujet', 'm')
text(ax, 64, 38.5, r'$\arctan\,0{,}75$', 'resultat', 'm')
text(ax, 64, 31.5, r'$\approx 36{,}87°$', 'resultat', 'm')
save(fig, '25-146')
