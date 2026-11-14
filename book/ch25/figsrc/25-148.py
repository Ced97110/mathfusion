import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax, c, r, a0, a1, role, lw=1.0):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
fig, ax = canvas(72)
cx, cy, r = 40, 36, 20
arc(ax, (cx, cy), r, 0, 360, 'fixe', 0.8)
arc(ax, (cx, cy), r, 0, 40, 'varie', 2.2); arc(ax, (cx, cy), r, 40, 90, 'autre', 2.2)
pt = lambda a, k=r: (cx+k*math.cos(math.radians(a)), cy+k*math.sin(math.radians(a)))
for a, role in ((0, 'sujet'), (40, 'varie'), (90, 'resultat')):
    disc(ax, *pt(a), 1.5, role)
text(ax, pt(0, r+3)[0], cy-4, r'$0° = 360°$', 'sujet', 's', ha='left')
text(ax, *pt(20, r+8), r'$+40°$', 'varie', 's')
text(ax, *pt(40, r+5), r'$40°$', 'varie', 's')
text(ax, *pt(68, r+8), r'$+50°$', 'autre', 's')
text(ax, *pt(90, r+4.5), r'$90°$', 'resultat', 's')
text(ax, cx, cy+3, r'$40° + 50° = 90°$', 'resultat', 's')
text(ax, cx, cy-4, 'un point = une rotation', 'sujet', 's')
arrow(ax, pt(80), pt(92), 'autre', lw=1.4, curve=0.0)
arrow(ax, pt(-30), pt(-18), 'fixe', lw=1.0)
text(ax, *pt(-24, r+8), 'sens des rotations', 'fixe', 's')
save(fig, '25-148')
