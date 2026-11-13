import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
import numpy as np
fig, ax = canvas(58)
x0, x1, yb, k = 10, 78, 8, 14.0
f = numberline(ax, x0, x1, yb, 0, 360, 90, arrow_right=False)
t = np.linspace(0, 360, 200); X = f(t); r = np.radians(t)
ax.plot(X, yb + k * np.cos(r) ** 2, color=COL['sujet'], lw=1.2, zorder=3); ax.plot(X, yb + k * (1 - np.sin(r)), color=COL['varie'], lw=1.2, zorder=3)
for v, y in ((0, 1), (90, 0), (180, 1), (360, 1)): disc(ax, f(v), yb + k * y, 1.6, 'resultat')
text(ax, 18, 50, r'$\cos^2 x$', 'sujet', 's'); text(ax, 58, 50, r'$1-\sin x$', 'varie', 's')
text(ax, 44, 38, 'quatre croisements = solutions', 'resultat', 's')
save(fig, '31-140')
