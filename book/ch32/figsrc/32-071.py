import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(84); cx, cy, R = 44, 40, 20
a = 36.87
uc(ax, cx, cy, R, ext=3)
P = pp(cx, cy, R, a); Q = pp(cx, cy, R, a + 180)
Pa = pp(cx, cy, R + 5, a); Qa = pp(cx, cy, R + 5, a + 180)
arrow(ax, Pa, Qa, 'varie', curve=1.0)
arrow(ax, Qa, Pa, 'varie', curve=1.0)
dot(ax, P, 'sujet', 1.6); dot(ax, Q, 'resultat', 1.6)
text(ax, pp(cx, cy, R + 9.5, a)[0], pp(cx, cy, R + 9.5, a)[1], 'P', 'sujet', 'l', weight='bold')
text(ax, pp(cx, cy, R + 9.5, a + 180)[0], pp(cx, cy, R + 9.5, a + 180)[1], 'Q', 'resultat', 'l', weight='bold')
text(ax, 25.4, 65, 'n = 1 : 216,87° (Q)', 'resultat', 's')
text(ax, 62.6, 15, 'n = 2 : 396,87° (P)', 'sujet', 's')
text(ax, W / 2, 78, r'$\theta=\alpha+180^\circ n$', 'encre', 'l')
text(ax, W / 2, 5, 'une seule famille suffit', 'encre', 'm')
save(fig, '32-071')
