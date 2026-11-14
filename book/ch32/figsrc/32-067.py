import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(80); cx, cy, R = 28, 36, 24
uc(ax, cx, cy, R)
xv = cx + R; T = (xv, cy + 0.75 * R)
line(ax, [(xv, cy - 8), (xv, cy + 32)], 'fixe', lw=1.3)
line(ax, [(cx, cy), T], 'sujet', lw=1.3)
line(ax, [(cx, cy), (xv, cy)], 'autre', lw=2.0)
line(ax, [(xv, cy), T], 'varie', lw=2.0)
dot(ax, T, 'resultat', 1.7)
text(ax, xv, cy + 36, 'verticale x = 1', 'fixe', 's')
text(ax, xv - 3, T[1] + 3.2, 'T', 'resultat', 'l', weight='bold')
text(ax, xv + 2.5, cy + 9, 'hauteur 0,75', 'varie', 's', ha='left')
text(ax, cx + R / 2, cy - 3.5, 'avancée 1', 'autre', 's')
text(ax, cx - 3, cy - 3, 'O')
text(ax, W / 2, 5, 'T est à la hauteur k = 0,75', 'resultat', 'm')
save(fig, '32-067')
