import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(78)
text(ax, 44, 74, r'$Q$ est différent de zéro', 'encre', 'm')
box(ax, 4, 54, 20, 12, 'sujet', label=r'$Q$', size='l'); box(ax, 34, 54, 20, 12, 'varie', label=r'$\neq$', size='l'); box(ax, 64, 54, 20, 12, 'fixe', label=r'$0$', size='l')
text(ax, 14, 49, 'le dénominateur', 'sujet', 's'); text(ax, 44, 49, 'différent de', 'varie', 's'); text(ax, 74, 49, 'le polynôme nul', 'fixe', 's')
text(ax, 44, 38, 'exemple', 'fixe', 's')
box(ax, 3, 8, 38, 20, 'sujet', label=r'$Q=x-7$' + '\n' + 'polynôme non nul', size='s')
arrow(ax, (41, 18), (48, 18), 'fixe')
box(ax, 49, 8, 36, 20, 'limite', label=r'$x=7$ : $Q=0$' + '\n' + 'valeur interdite', size='s')
save(fig, '21-028')
