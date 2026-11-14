import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(66)
text(ax, 58, 62, 'diviser par 1 ne change rien', 'varie', 's')
box(ax, 4, 37, 24, 12, 'sujet', label=r'$4x-5$'); text(ax, 36, 43, r'$=$', 'encre', 'l')
box(ax, 46, 46, 24, 10, 'sujet', label=r'$4x-5$'); line(ax, [(44, 43), (72, 43)], 'varie', lw=1.6); box(ax, 46, 30, 24, 10, 'autre', label=r'$1$')
arrow(ax, (16, 37), (16, 16), 'fixe'); arrow(ax, (58, 30), (58, 16), 'fixe')
box(ax, 4, 6, 24, 10, 'resultat', label=r'$x=2$ : 3', size='s'); text(ax, 36, 11, r'$=$', 'encre', 'l')
box(ax, 46, 6, 24, 10, 'resultat', label=r'$3\div 1=3$', size='s')
save(fig, '21-032')
