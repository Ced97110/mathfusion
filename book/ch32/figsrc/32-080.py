import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(78); cx, cy, R = 28, 34, 16
disc(ax, cx, cy, R, 'sujet')
line(ax, [(cx, cy - 2 * R - 3), (cx, cy + 2 * R + 3)], 'fixe', lw=0.5)
for s in (1, -1): line(ax, [(cx - R - 4, cy + s * R), (cx + R + 4, cy + s * R)], 'fixe', lw=0.7, dash=True)
line(ax, [(6, cy + 2 * R), (82, cy + 2 * R)], 'limite', lw=1.6)
text(ax, cx, cy, 'rayon 1', 'sujet', 's')
text(ax, cx + R + 6, cy + R + 2.5, 'hauteur 1', 'fixe', 's', ha='left')
text(ax, cx + R + 6, cy - R - 2.5, 'hauteur −1', 'fixe', 's', ha='left')
text(ax, 44, cy + 2 * R + 4, r'$\sin\theta=2$', 'limite', 'm')
text(ax, cx, cy + 1.5 * R + 0, 'aucun point commun', 'limite', 's')
text(ax, 66, cy + 1.5 * R + 1, 'aucune solution', 'limite', 's')
save(fig, '32-080')
