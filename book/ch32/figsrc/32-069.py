import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(80); cx, cy, R = 44, 38, 22
a = 36.87
uc(ax, cx, cy, R)
P = pp(cx, cy, R, a); Q = pp(cx, cy, R, a + 180)
line(ax, [Q, P], 'fixe', lw=0.8, dash=True)
ax.add_patch(Arc((cx, cy), 0.8 * R, 0.8 * R, theta1=0, theta2=a, ec=COL['sujet'], lw=1.8, zorder=3))
ax.add_patch(Arc((cx, cy), 1.4 * R, 1.4 * R, theta1=a, theta2=a + 180, ec=COL['varie'], lw=1.8, zorder=3))
arrow(ax, pp(cx, cy, 0.7 * R, a + 168), pp(cx, cy, 0.7 * R, a + 180), 'varie')
dot(ax, P, 'sujet', 1.6); dot(ax, Q, 'resultat', 1.6)
text(ax, cx + 14, cy + 2.8, '36,87°', 'sujet', 's')
text(ax, cx - 14, cy + 17, '+ 180°', 'varie', 's')
text(ax, P[0] + 2.5, P[1] + 2.5, 'P', 'sujet', 'l', weight='bold')
text(ax, Q[0] - 2.5, Q[1] - 2.5, 'Q : 216,87°', 'resultat', 's', ha='right')
text(ax, W / 2, 7, 'tan = 0,75 en P et en Q', 'encre', 'm')
save(fig, '32-069')
