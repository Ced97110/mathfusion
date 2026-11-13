import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(52); y0 = 24
f = numberline(ax, 8, 74, y0, -1, 3, 1, labels=False)
for v, l in [(0, '0'), (2, r'$2\pi$')]: text(ax, f(v), y0 - 4, l, 'fixe', 's')
t = 1 / 3
items = [(0, -t, r'$-\pi/3$'), (0, t, r'$\pi/3$'), (2, 2 - t, r'$5\pi/3$'), (2, 2 + t, r'$7\pi/3$')]
for c, pt, pl in items:
    arrow(ax, (f(c), y0), (f(pt), y0), 'varie', lw=1.8)
    dot(ax, (f(pt), y0), 'resultat', 1.5)
    text(ax, f(pt), y0 + 5, pl, 'resultat', 's')
text(ax, f(0), y0 - 10, 'n = 0', 'varie', 's')
text(ax, f(2), y0 - 10, 'n = 1', 'varie', 's')
text(ax, W / 2, 46, r'$\theta=2n\pi\pm\alpha$', 'encre', 'l')
text(ax, W / 2, 38, r'$\alpha=\pi/3$', 'sujet', 'm')
save(fig, '32-076')
