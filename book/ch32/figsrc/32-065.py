import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(72); cx, cy, R = 32, 32, 26
uc(ax, cx, cy, R)
P = pp(cx, cy, R, 45); Pe = pp(cx, cy, R * 1.18, 45)
line(ax, [(cx, cy), Pe], 'sujet', lw=1.3)
line(ax, [(cx, cy), (P[0], cy)], 'autre', lw=2.0)
line(ax, [(P[0], cy), P], 'varie', lw=2.0)
dot(ax, P, 'sujet')
text(ax, cx - 2.5, cy - 2.8, 'O')
text(ax, P[0] - 2, P[1] + 3.2, 'P', 'sujet', 'l', weight='bold')
text(ax, cx + 6, cy + 17, 'droite OP', 'sujet', 's', ha='right')
text(ax, (cx + P[0]) / 2, cy - 4.2, 'avancée 0,71', 'autre', 's')
text(ax, P[0] + 2, (cy + P[1]) / 2, 'montée 0,71', 'varie', 's', ha='left')
text(ax, W / 2, 67, 'pente de OP = tan 45° = 1', 'resultat', 'm')
save(fig, '32-065')
