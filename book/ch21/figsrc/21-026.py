import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(68)
text(ax, 44, 65, 'numérateur : le haut', 'sujet', 'm')
box(ax, 8, 46, 24, 10, 'sujet', label=r'$x+9$'); line(ax, [(6, 43), (34, 43)], 'encre'); box(ax, 8, 30, 24, 10, 'fixe', label=r'$x-7$')
arrow(ax, (33, 51), (46, 51), 'varie'); box(ax, 47, 46, 36, 10, 'sujet', label=r'$P=x+9$')
box(ax, 8, 20, 24, 10, 'sujet', label='3'); line(ax, [(6, 17), (34, 17)], 'encre'); box(ax, 8, 4, 24, 10, 'fixe', label='8')
arrow(ax, (33, 25), (46, 25), 'varie'); box(ax, 47, 20, 36, 10, 'sujet', label=r'$P=3$')
save(fig, '21-026')
