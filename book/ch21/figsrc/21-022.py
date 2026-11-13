import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(62)
text(ax, 44, 57, 'la division est bloquée', 'encre', 'm')
text(ax, 16, 42, r'$120/v$', 'sujet', 'l')
f = numberline(ax, 34, 78, 42, -2, 2, labels=False, arrow_right=False)
disc(ax, f(0), 42, 2.2, 'limite'); text(ax, f(0), 33.5, r'$v=0$ interdite', 'limite', 's')
line(ax, [(4, 27), (84, 27)], 'fixe', dash=True)
text(ax, 16, 18, r'$1/(x-2)$', 'sujet', 'l')
g = numberline(ax, 34, 78, 18, 0, 4, labels=False, arrow_right=False)
disc(ax, g(2), 18, 2.2, 'limite'); text(ax, g(2), 9.5, r'$x=2$ interdite', 'limite', 's')
save(fig, '21-022')
