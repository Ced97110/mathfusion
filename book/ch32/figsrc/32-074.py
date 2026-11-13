import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(84); cx, cy, R = 44, 46, 22
uc(ax, cx, cy, R)
a = 40
P = pp(cx, cy, R, a); P2 = pp(cx, cy, R, -a); F = pp(cx, cy, R, a + 180)
arrow(ax, (P[0], P[1] - 1.8), (P2[0], P2[1] + 1.8), 'varie')
arrow(ax, (P2[0] - 1.8, P2[1]), (F[0] + 1.8, F[1]), 'varie')
dot(ax, P, 'sujet', 1.7); dot(ax, P2, 'varie', 1.6); dot(ax, F, 'resultat', 1.7)
text(ax, P[0] + 3, P[1] + 1, 'P : 40°', 'sujet', 's', ha='left')
text(ax, P2[0] + 3, P2[1] - 1, '−40°', 'varie', 's', ha='left')
text(ax, F[0] - 3, F[1] - 1, '220°', 'resultat', 's', ha='right')
text(ax, P[0] - 2.5, cy, 'reflet 1', 'varie', 's', ha='right')
text(ax, cx, P2[1] - 4, 'reflet 2', 'varie', 's')
text(ax, W / 2, 14, '220° = 40° + 180°', 'resultat', 'm')
text(ax, W / 2, 7, 'avec 70° : 250°', 'encre', 's')
text(ax, W / 2, 80, 'deux reflets = un demi-tour', 'encre', 'm')
save(fig, '32-074')
