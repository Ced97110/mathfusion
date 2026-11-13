import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(84); cx, cy, R = 44, 42, 22
uc(ax, cx, cy, R)
a = 40
P = pp(cx, cy, R, a); P1 = pp(cx, cy, R, 180 - a); P2 = pp(cx, cy, R, -a); P3 = pp(cx, cy, R, a + 180)
line(ax, [P, P1], 'varie', lw=1.1, dash=True)
line(ax, [P, P2], 'varie', lw=1.1, dash=True)
line(ax, [P, P3], 'varie', lw=1.1, dash=True)
dot(ax, P, 'sujet', 1.7)
for q in (P1, P2, P3): dot(ax, q, 'resultat', 1.6)
text(ax, P[0] + 3, P[1] + 1, 'P : 40°', 'sujet', 's', ha='left')
text(ax, P1[0] - 3, P1[1] + 1, '140° (sinus)', 'resultat', 's', ha='right')
text(ax, P2[0] + 3, P2[1] - 1, '−40° (cosinus)', 'resultat', 's', ha='left')
text(ax, P3[0] - 3, P3[1] - 1, '220° (tangente)', 'resultat', 's', ha='right')
text(ax, cx, P[1] + 3.2, 'reflet', 'varie', 's')
text(ax, P[0] - 2, cy + 2.5, 'reflet', 'varie', 's', ha='right')
text(ax, cx - 9, cy - 4.5, 'demi-tour', 'varie', 's')
text(ax, W / 2, 80, 'un seul geste par cas', 'encre', 'm')
save(fig, '32-073')
