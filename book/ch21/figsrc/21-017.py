import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(64)
gx = lambda v: 6 + v * 9; gy = lambda v: 30 + v * 7
line(ax, [(6, 30), (44, 30)], 'fixe'); line(ax, [(6, 8), (6, 52)], 'fixe')
text(ax, 46, 27, r'$x$', 'fixe', 's'); text(ax, 9, 55, r'$y$', 'fixe', 's')
line(ax, [(gx(2), 9), (gx(2), 52)], 'limite', dash=True)
gcurve(ax, gx, gy, 2 + 1 / 3.0, 4, 'sujet'); gcurve(ax, gx, gy, 0, 2 - 1 / 3.0, 'sujet')
text(ax, gx(2), 58, r'$x=2$', 'limite', 's')
box(ax, 52, 42, 34, 11, 'sujet', label=r'$x=2$')
box(ax, 52, 26, 34, 11, 'fixe', label=r'$x-2=0$')
box(ax, 52, 8, 34, 11, 'limite', label=r'$1\div 0$')
arrow(ax, (69, 42), (69, 37), 'fixe'); arrow(ax, (69, 26), (69, 19), 'fixe')
text(ax, 69, 3.5, 'aucun résultat', 'limite', 's')
save(fig, '21-017')
