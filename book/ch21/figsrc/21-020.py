import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(56)
box(ax, 2, 37, 29, 11, 'varie', label='écart 0,0001', size='s'); arrow(ax, (31, 42.5), (37, 42.5), 'fixe')
box(ax, 38, 37, 30, 11, 'resultat', label=r'$y=10\,000$', size='s')
text(ax, 44, 31.5, r'écart $\div 10$ : $y\times 10$', 'fixe', 's')
box(ax, 2, 12, 29, 11, 'varie', label='écart 0,0000001', size='s'); arrow(ax, (31, 17.5), (35, 17.5), 'fixe')
box(ax, 36, 12, 29, 11, 'resultat', label=r'$y=10\,000\,000$', size='s')
text(ax, 68.5, 17.5, r'$>$', 'encre', 'l')
box(ax, 71, 12, 15, 11, 'fixe', label='1 000 000', size='s')
text(ax, 78.5, 27, 'nombre choisi', 'fixe', 's')
text(ax, 44, 5, 'toujours un y plus grand', 'encre', 's')
save(fig, '21-020')
