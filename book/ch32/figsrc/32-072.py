import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(54); cy, R = 30, 10
cols = [15, 44, 73]
for cx in cols: uc(ax, cx, cy, R, ext=2)
k = 0.5
# sinus : droite horizontale de hauteur 0,5
line(ax, [(cols[0] - R - 2, cy + k * R), (cols[0] + R + 2, cy + k * R)], 'sujet', lw=1.2)
for a in (30, 150): dot(ax, pp(cols[0], cy, R, a), 'resultat', 1.4)
# cosinus : droite verticale d'abscisse 0,5
line(ax, [(cols[1] + k * R, cy - R - 2), (cols[1] + k * R, cy + R + 2)], 'sujet', lw=1.2)
for a in (60, -60): dot(ax, pp(cols[1], cy, R, a), 'resultat', 1.4)
# tangente : droite de pente 1 par le centre
e = (R + 3) * math.cos(math.radians(45))
line(ax, [(cols[2] - e, cy - e), (cols[2] + e, cy + e)], 'sujet', lw=1.2)
for a in (45, 225): dot(ax, pp(cols[2], cy, R, a), 'resultat', 1.4)
for cx, eq, sol in zip(cols, ['sin = 0,5', 'cos = 0,5', 'tan = 1'], ['30° et 150°', '60° et −60°', '45° et 225°']):
    text(ax, cx, cy - R - 6, eq, 'sujet', 's')
    text(ax, cx, cy - R - 11, sol, 'resultat', 's')
text(ax, W / 2, 49, 'deux solutions de base chacune', 'encre', 'm')
save(fig, '32-072')
