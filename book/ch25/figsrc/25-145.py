import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax, c, r, a0, a1, role, lw=1.0):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
fig, ax = canvas(66)
ox, oy, u = 12, 10, 8
arrow(ax, (ox-4, oy), (ox+38, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy-3), (ox, oy+52), 'fixe', lw=0.8)
P = (ox+3*u, oy+4*u)
poly(ax, [(ox, oy), (P[0], oy), P], 'sujet')
line(ax, [(ox, oy), P], 'sujet', lw=1.6)
line(ax, [(P[0], oy), P], 'fixe', lw=1.2); line(ax, [(ox, oy), (P[0], oy)], 'fixe', lw=1.2)
disc(ax, P[0], P[1], 1.3, 'sujet')
arc(ax, (ox, oy), 9, 0, 53.13, 'varie', 1.4)
text(ax, ox+13, oy+4.5, 'angle', 'varie', 's')
text(ax, ox+12, oy-3.2, '3', 'fixe', 's'); text(ax, P[0]+3, oy+16, '4', 'fixe', 's')
text(ax, ox+7, oy+22, '5', 'sujet', 's')
text(ax, 64, 52, r'$y/x = 4/3$', 'sujet', 'm'); text(ax, 64, 45, r'$\approx 1{,}333$', 'resultat', 'm')
text(ax, 64, 30, r'angle $\approx 53{,}13°$', 'varie', 'm')
text(ax, 64, 22, 'distance 5 + angle', 'resultat', 's')
save(fig, '25-145')
