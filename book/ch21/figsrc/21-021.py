import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def gcurve(ax, gx, gy, a, b, role, lw=1.4):
    xs = np.linspace(a, b, 80); ys = 1 / (xs - 2)
    ax.plot([gx(v) for v in xs], [gy(v) for v in ys], color=COL[role], lw=lw, zorder=3, solid_capstyle="round")
fig, ax = canvas(62)
gx = lambda v: 4 + v * 8; gy = lambda v: 30 + v * 6
line(ax, [(4, 30), (37, 30)], 'fixe'); line(ax, [(4, 9), (4, 51)], 'fixe')
text(ax, 39, 30, r'$x$', 'fixe', 's'); text(ax, 7, 54, r'$y$', 'fixe', 's')
line(ax, [(gx(2), 9), (gx(2), 51)], 'limite', dash=True)
gcurve(ax, gx, gy, 2 + 1 / 3.5, 4, 'fixe'); gcurve(ax, gx, gy, 0, 2 - 1 / 3.5, 'sujet')
text(ax, gx(2), 57, r'$x=2$', 'limite', 's'); text(ax, gx(1), 14, 'descend', 'varie', 's'); text(ax, 30, 50, 'monte', 'fixe', 's')
for yb, a, b in [(41, r'$x=1{,}9$ : $x-2=-0{,}1$', r'$y=-10$'), (23, r'$x=1{,}99$ : $x-2=-0{,}01$', r'$y=-100$'), (5, r'$x=1{,}999$ : $x-2=-0{,}001$', r'$y=-1000$')]:
    box(ax, 42, yb, 45, 14, 'sujet', label=a + '\n' + b, size='s')
arrow(ax, (64, 41), (64, 37), 'varie'); arrow(ax, (64, 23), (64, 19), 'varie')
save(fig, '21-021')
