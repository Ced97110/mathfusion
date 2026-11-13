import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
from matplotlib.patches import Rectangle
fig, ax = canvas(64)
text(ax, 47, 59, r'$y=1\div$ écart', 'encre', 'm')
line(ax, [(26, 6), (26, 55)], 'fixe', dash=True); text(ax, 26, 3, r'$2$', 'fixe', 's')
for yc, xs, ec, ys in [(46, '2{,}5', '0,5', '2'), (28, '2{,}1', '0,1', '10'), (10, '2{,}01', '0,01', '100')]:
    L = 60 * float(ec.replace(',', '.'))
    text(ax, 13, yc, r'$x=%s$' % xs, 'varie', 'm')
    ax.add_patch(Rectangle((26, yc - 2), L, 4, fc=FILL['sujet'], ec=COL['sujet'], lw=0.8, zorder=2))
    text(ax, 27, yc + 5.5, 'écart ' + ec, 'sujet', 's', ha='left')
    arrow(ax, (60, yc), (66, yc), 'fixe')
    box(ax, 68, yc - 5, 18, 10, 'resultat', label=r'$y=%s$' % ys)
save(fig, '21-019')
