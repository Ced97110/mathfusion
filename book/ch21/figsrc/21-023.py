import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(68)
gx = lambda v: 12 + v * 16; gy = lambda v: 34 + v * 7.5
line(ax, [(12, 34), (80, 34)], 'fixe'); line(ax, [(12, 10), (12, 58)], 'fixe')
text(ax, 83, 34, r'$x$', 'fixe', 's'); text(ax, 15, 58, r'$y$', 'fixe', 's')
line(ax, [(gx(2), 10), (gx(2), 58)], 'limite', dash=True)
gcurve(ax, gx, gy, 2 + 1 / 3.2, 4, 'sujet'); gcurve(ax, gx, gy, 0, 2 - 1 / 3.2, 'sujet')
gcurve(ax, gx, gy, 2.45, 3, 'varie', lw=2.0)
disc(ax, gx(3), gy(1), 1.6, 'varie'); text(ax, gx(3) + 3, gy(1) - 5, r'départ $x=3$', 'varie', 's', ha='left')
arrow(ax, (gx(2.45), gy(1 / 0.45)), (gx(2.4), gy(1 / 0.4)), 'varie')
arrow(ax, (gx(2.32), gy(3.0)), (gx(1.68), gy(-3.0)), 'varie', curve=-0.25)
text(ax, gx(2), 63.5, r'$x=2$', 'limite', 's'); text(ax, 62, 18, 'lever le crayon', 'varie', 's')
save(fig, '21-023')
