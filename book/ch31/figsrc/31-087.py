import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(64)
x0, x1, y0, hh = 12, 80, 14, 34
d = np.linspace(0, 360, 400); r = np.radians(d)
X = lambda a: x0 + a / 360 * (x1 - x0)
Y = lambda v: y0 + v * hh
for v in (0, 1):
    line(ax, [(x0, Y(v)), (x1, Y(v))], 'fixe', lw=0.5, dash=True)
    text(ax, x0 - 2, Y(v), str(v), 'fixe', 's', ha='right')
for a in (0, 90, 180, 270, 360):
    ax.plot([X(a)] * 2, [y0 - 1, y0 + 1], color=COL['fixe'], lw=0.8)
    text(ax, X(a), y0 - 4, f'{a}°', 'fixe', 's')
line(ax, [(x0, y0), (x1, y0)], 'fixe', lw=0.9)
ax.plot(X(d), Y(np.cos(r) ** 2), color=COL['sujet'], lw=3.0, zorder=3)
ax.plot(X(d), Y(1 - np.sin(r) ** 2), color=COL['encre'], lw=1.0, ls=(0, (2, 2)), zorder=4)
for a in (60, 120):
    line(ax, [(X(a), y0), (X(a), Y(0.25))], 'resultat', lw=0.7, dash=True)
    disc(ax, X(a), Y(0.25), 1.3, 'resultat')
line(ax, [(X(60), Y(0.25)), (X(120), Y(0.25))], 'resultat', lw=0.7, dash=True)
text(ax, X(90), Y(0.25) + 3.2, '0,25', 'resultat', 's')
line(ax, [(14, 58), (22, 58)], 'sujet', lw=3.0); text(ax, 24, 58, r'$\cos^2 x$', 'sujet', 'm', ha='left')
line(ax, [(50, 58), (58, 58)], 'encre', lw=1.0, dash=True); text(ax, 60, 58, r'$1-\sin^2 x$', 'encre', 'm', ha='left')
save(fig, '31-087')
