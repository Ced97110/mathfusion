import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(72)
x0, x1, y0, hh = 12, 80, 14, 20
d = np.linspace(0, 360, 400); r = np.radians(d)
X = lambda a: x0 + a / 360 * (x1 - x0)
Y = lambda v: y0 + v * hh
for v in (0, 1, 2):
    line(ax, [(x0, Y(v)), (x1, Y(v))], 'fixe', lw=0.5, dash=True)
    text(ax, x0 - 2, Y(v), str(v), 'fixe', 's', ha='right')
for a in (0, 90, 180, 270, 360):
    ax.plot([X(a)] * 2, [y0 - 1, y0 + 1], color=COL['fixe'], lw=0.8)
    text(ax, X(a), y0 - 4, f'{a}°', 'fixe', 's')
ax.plot(X(d), Y(np.cos(r) ** 2), color=COL['sujet'], lw=2.2, zorder=3)
ax.plot(X(d), Y(1 - np.sin(r)), color=COL['varie'], lw=2.2, zorder=3)
for a, v in ((0, 1), (90, 0), (180, 1), (360, 1)):
    disc(ax, X(a), Y(v), 1.5, 'resultat')
arrow(ax, (X(270) + 3, Y(0)), (X(270) + 3, Y(2)), 'limite', both=True)
text(ax, X(270) + 4, Y(2) + 3.5, 'écart 2', 'limite', 's', ha='left')
line(ax, [(14, 66), (22, 66)], 'sujet', lw=2.2); text(ax, 24, 66, r'$\cos^2 x$', 'sujet', 'm', ha='left')
line(ax, [(50, 66), (58, 66)], 'varie', lw=2.2); text(ax, 60, 66, r'$1-\sin x$', 'varie', 'm', ha='left')
text(ax, 28, 58.5, 'accord en 4 points', 'resultat', 's')
save(fig, '31-088')
