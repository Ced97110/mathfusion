import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(72)
box(ax, 26, 58, 36, 11, 'sujet', label=r'$1/(x-2)$')
arrow(ax, (44, 58), (44, 50), 'fixe')
box(ax, 14, 39, 60, 11, 'varie', label=r'dénominateur $=0$ ?')
arrow(ax, (28, 39), (21, 28), 'fixe'); arrow(ax, (60, 39), (67, 28), 'fixe')
text(ax, 16, 34, 'non', 'resultat', 's'); text(ax, 73, 34, 'oui', 'limite', 's')
box(ax, 2, 8, 38, 20, 'resultat', label=r'$x=5$ : $x-2=3$' + '\n' + 'un tiers', size='s')
box(ax, 48, 8, 38, 20, 'limite', label=r'$x=2$ : $x-2=0$' + '\n' + 'impossible', size='s')
save(fig, '21-024')
