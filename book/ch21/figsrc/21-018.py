import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(66)
gx = lambda v: 12 + v * 16; gy = lambda v: 32 + v * 7.5
line(ax, [(12, 32), (80, 32)], 'fixe'); line(ax, [(12, 8), (12, 56)], 'fixe')
text(ax, 83, 32, r'$x$', 'fixe', 's'); text(ax, 15, 56, r'$y$', 'fixe', 's')
line(ax, [(gx(2), 8), (gx(2), 56)], 'limite', dash=True)
gcurve(ax, gx, gy, 2 + 1 / 3.2, 4, 'sujet'); gcurve(ax, gx, gy, 0, 2 - 1 / 3.2, 'sujet')
text(ax, gx(2), 61.5, r'$x=2$ : aucun point', 'limite', 's')
text(ax, 66, 52, 'morceau de droite', 'sujet', 's'); text(ax, 24, 14, 'morceau de gauche', 'sujet', 's')
save(fig, '21-018')
