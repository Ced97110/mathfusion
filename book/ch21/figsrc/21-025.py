import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(80)
box(ax, 12, 62, 24, 10, 'sujet', label='P'); line(ax, [(10, 59), (38, 59)], 'encre'); box(ax, 12, 45, 24, 10, 'autre', label='Q')
text(ax, 42, 67, 'polynôme', 'sujet', 's', ha='left'); text(ax, 42, 50, 'polynôme non nul', 'autre', 's', ha='left')
text(ax, 44, 38, 'exemples', 'fixe', 's')
box(ax, 14, 22, 16, 9, 'sujet', label='3'); line(ax, [(12, 19), (32, 19)], 'encre'); box(ax, 14, 6, 16, 9, 'autre', label='8')
box(ax, 48, 22, 28, 9, 'sujet', label=r'$x+9$'); line(ax, [(46, 19), (78, 19)], 'encre'); box(ax, 48, 6, 28, 9, 'autre', label=r'$x-7$')
save(fig, '21-025')
