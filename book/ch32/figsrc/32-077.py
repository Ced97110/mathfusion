import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(82); cx, cy, R = 44, 40, 20
a = 45
uc(ax, cx, cy, R, ext=3)
P = pp(cx, cy, R, a); Q = pp(cx, cy, R, a + 180)
line(ax, [Q, P], 'fixe', lw=0.8, dash=True)
arrow(ax, pp(cx, cy, R + 5, a), pp(cx, cy, R + 5, a + 180), 'varie', curve=1.0)
arrow(ax, pp(cx, cy, R + 5, a), pp(cx, cy, R + 5, a + 180), 'varie', curve=-1.0)
dot(ax, P, 'sujet', 1.6); dot(ax, Q, 'resultat', 1.6)
text(ax, pp(cx, cy, R + 10, a)[0] + 1, pp(cx, cy, R + 10, a)[1], r'P : $\pi/4$', 'sujet', 's', ha='left')
text(ax, pp(cx, cy, R + 9.5, a + 180)[0], pp(cx, cy, R + 9.5, a + 180)[1], 'Q', 'resultat', 'l', weight='bold')
text(ax, 24, 64, r'n = 1 : $5\pi/4$', 'resultat', 's')
text(ax, 64, 16, r'n = −1 : $-3\pi/4$', 'resultat', 's')
text(ax, W / 2, 77, r'$\theta=n\pi+\alpha$', 'encre', 'l')
text(ax, W / 2, 5, 'un demi-tour vaut π', 'encre', 'm')
save(fig, '32-077')
