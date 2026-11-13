import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(54)
text(ax, 44, 51, 'deux nombres, aucune lettre', 'fixe', 's')
box(ax, 6, 31, 24, 12, 'sujet', label='3'); line(ax, [(4, 28), (32, 28)], 'encre'); box(ax, 6, 13, 24, 12, 'autre', label='8')
text(ax, 36, 37, r'$P=3$', 'sujet', 'm', ha='left'); text(ax, 36, 19, r'$Q=8$', 'autre', 'm', ha='left')
arrow(ax, (34, 28), (56, 28), 'fixe')
box(ax, 57, 22, 29, 12, 'resultat', label=r'$3\div 8=0{,}375$', size='s')
save(fig, '21-031')
