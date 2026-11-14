import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(52)
x0, x1, y = 6, 78, 24
f = numberline(ax, x0, x1, y, 0, 40, 8, arrow_right=False)
for i in range(4):
    brace(ax, f(8 * i) + 0.4, f(8 * i + 8) - 0.4, y + 3, 'sujet', '8 min', False, depth=1.6)
brace(ax, f(32) + 0.4, f(37), y + 3, 'varie', '5 min', False, depth=1.6)
dot(ax, f(37), y, 'varie', 1.3)
text(ax, f(37), y - 9.5, '37 min', 'varie', 's')
text(ax, 44, 46, '4 périodes entières, puis 5 min', 'encre', 's')
text(ax, 44, 8, '37 − 32 = 5 : même hauteur qu’à 5 min', 'resultat', 's')
save(fig, '30-006')
