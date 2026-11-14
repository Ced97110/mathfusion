import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(76); cx, cy, R = 44, 36, 22
a = 36.87
uc(ax, cx, cy, R)
P = pp(cx, cy, R, a); Q = pp(cx, cy, R, a + 180)
line(ax, [Q, P], 'sujet', lw=1.3)
dot(ax, P, 'sujet', 1.6); dot(ax, Q, 'resultat', 1.6); dot(ax, (cx, cy), 'fixe', 1.1)
arrow(ax, pp(cx, cy, 0.5 * R, a), pp(cx, cy, 0.5 * R, a + 180), 'varie', curve=1.0)
text(ax, cx + 3, cy - 3.2, 'O')
text(ax, cx + 11.5, cy + 3, 'OP = 1', 'sujet', 's')
text(ax, cx - 6.1, cy - 10.2, 'OQ = 1', 'resultat', 's')
text(ax, P[0] + 2.5, P[1] + 2.5, 'P : 36,87°', 'sujet', 's', ha='left')
text(ax, Q[0] - 2.5, Q[1] - 2.5, 'Q : 216,87°', 'resultat', 's', ha='right')
text(ax, cx - 8, cy + 16, 'demi-tour 180°', 'varie', 's')
text(ax, W / 2, 71, 'Q est l’opposé de P', 'encre', 'm')
save(fig, '32-068')
