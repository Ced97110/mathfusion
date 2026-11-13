import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax, c, r, a0, a1, role, lw=1.0):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
fig, ax = canvas(74)
cx, cy = 44, 44
d1 = (4, 3); d2 = (3, -4)
line(ax, [(cx-7*d1[0], cy-7*d1[1]), (cx+7*d1[0], cy+7*d1[1])], 'sujet', lw=1.6)
line(ax, [(cx-5.5*d2[0], cy-5.5*d2[1]), (cx+5.5*d2[0], cy+5.5*d2[1])], 'autre', lw=1.6)
n1 = (-3/5, 4/5); e1 = (4/5, 3/5); s = 4.5
line(ax, [(cx+e1[0]*s, cy+e1[1]*s), (cx+(e1[0]+n1[0])*s, cy+(e1[1]+n1[1])*s), (cx+n1[0]*s, cy+n1[1]*s)], 'resultat', lw=1.1)
text(ax, cx+27, cy+25, 'pente 0,75', 'sujet', 'm')
text(ax, cx+16, cy-27, r'pente $-4/3$', 'autre', 'm')
text(ax, cx-22, cy+16, 'angle droit', 'resultat', 's')
text(ax, 44, 4, r'$0{,}75 \times (-4/3) = -1$', 'resultat', 'l')
save(fig, '25-147')
