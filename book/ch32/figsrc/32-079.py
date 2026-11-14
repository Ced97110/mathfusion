import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(78)
rows = [r'$2+2\sin(30t)$', r'$2\sin(30t)$', r'$\sin(30t)$']; rhs = ['3', '1', '0,5']
ys = [62, 38, 14]
for i in range(3):
    box(ax, 3, ys[i], 52, 10, 'sujet', label=rows[i], size='l')
    text(ax, 60.5, ys[i] + 5, '=', 'encre', 'l')
    box(ax, 66, ys[i], 19, 10, 'resultat', label=rhs[i], size='l')
for i, lab in enumerate(['retirer 2 de chaque côté', 'diviser par 2 de chaque côté']):
    arrow(ax, (29, ys[i] - 0.3), (29, ys[i + 1] + 10.3), 'varie')
    arrow(ax, (75.5, ys[i] - 0.3), (75.5, ys[i + 1] + 10.3), 'varie')
    text(ax, 52, ys[i] - 7, lab, 'varie', 's')
text(ax, 29, 8, 'fonction seule', 'sujet', 's')
text(ax, 75.5, 8, 'un nombre', 'resultat', 's')
save(fig, '32-079')
