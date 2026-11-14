import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(60)
box(ax, 4, 38, 24, 10, 'sujet', label=r'$x+9$'); line(ax, [(2, 35), (30, 35)], 'encre'); box(ax, 4, 22, 24, 10, 'autre', label=r'$x-7$')
arrow(ax, (29, 43), (38, 43), 'fixe'); arrow(ax, (29, 27), (38, 27), 'fixe')
box(ax, 39, 38, 46, 10, 'sujet', label=r'$P=x+9$ : polynôme', size='s')
box(ax, 39, 22, 46, 10, 'autre', label=r'$Q=x-7$ : polynôme', size='s')
arrow(ax, (62, 22), (62, 14), 'fixe')
box(ax, 39, 4, 46, 10, 'resultat', label=r'$Q$ n’est pas le polynôme nul', size='s')
save(fig, '21-030')
