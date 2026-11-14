import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(64)
X = lambda x: 8 + (x - 1.1) * 280
Y = lambda v: 16 + (v - 1.74) * 300
d = lambda x: x ** 4 - 3 * x ** 2 + 4
t = np.linspace(1.1, 1.35, 100)
line(ax, [(X(a), Y(d(a))) for a in t], 'sujet', lw=1.6)
line(ax, [(8, Y(1.75)), (80, Y(1.75))], 'fixe', dash=True)
text(ax, 85, Y(1.75), '1,75', 'fixe', 's', ha='right')
line(ax, [(8, 12), (80, 12)], 'fixe', lw=0.7)
for v in (1.2, 1.3):
    line(ax, [(X(v), 11), (X(v), 13)], 'fixe'); text(ax, X(v), 8.5, f'{v}'.replace('.', ','), 'fixe', 's')
r = 1.5 ** 0.5
disc(ax, X(1.2), Y(d(1.2)), 1.0, 'sujet'); disc(ax, X(1.22), Y(d(1.22)), 1.0, 'sujet')
ax.add_patch(Circle((X(r), Y(1.75)), 1.1, fill=False, ec=COL['limite'], lw=1.0, zorder=4))
text(ax, 24, 33, '6/5 → 1,7536', 'sujet', 's'); arrow(ax, (28, 31), (35, 21), 'fixe', lw=0.7)
text(ax, 24, 14.8, '1,22 → 1,7501', 'sujet', 's'); arrow(ax, (31, 16), (40.4, 18.6), 'fixe', lw=0.7)
text(ax, 66, 14.8, 'minimum en x² = 3/2', 'limite', 's'); arrow(ax, (56, 16.3), (44.2, 18.8), 'limite', lw=0.7)
text(ax, 6, 58, 'carré de la distance', 'encre', 's', ha='left')
save(fig, '70-178')
