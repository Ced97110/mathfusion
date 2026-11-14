import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(74)
for yc, top, bot, rhs in [(60, r'$P$', r'$Q$', r'$P\div Q$'), (36, r'$3$', r'$8$', r'$3\div 8$'), (12, r'$x+9$', r'$x-7$', r'$(x+9)\div(x-7)$')]:
    text(ax, 16, yc + 5, top, 'encre', 'm'); text(ax, 16, yc - 5, bot, 'encre', 'm')
    line(ax, [(5, yc), (27, yc)], 'varie', lw=1.6)
    arrow(ax, (31, yc), (42, yc), 'varie', both=True)
    text(ax, 64, yc, rhs, 'sujet', 'm')
save(fig, '21-029')
