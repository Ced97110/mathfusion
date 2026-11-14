import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(54); y0 = 28
f = numberline(ax, 8, 76, y0, -180, 540, 180, labels=False)
vals = [(-143.13, 'n = −1', '−143,13°'), (36.87, 'n = 0 (α)', '36,87°'), (216.87, 'n = 1', '216,87°'), (396.87, 'n = 2', '396,87°')]
for i, (v, nl, al) in enumerate(vals):
    role = 'sujet' if i == 1 else 'resultat'
    dot(ax, (f(v), y0), role, 1.5)
    text(ax, f(v), y0 - 7, al, role, 's')
    text(ax, f(v), y0 - 12, nl, 'fixe', 's')
for i in range(3):
    xa, xb = f(vals[i][0]), f(vals[i + 1][0])
    arrow(ax, (xa + 1.5, y0 + 1.5), (xb - 1.5, y0 + 1.5), 'varie', curve=-0.5)
    text(ax, (xa + xb) / 2, y0 + 9, '+ 180°', 'varie', 's')
text(ax, W / 2, 48, r'$\theta=\alpha+180^\circ n$', 'encre', 'l')
save(fig, '32-070')
