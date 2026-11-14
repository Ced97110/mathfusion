import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
O, u = (8, 8), 16
X = lambda a, b: (O[0] + a * u, O[1] + b * u)
arrow(ax, X(0, 0), X(4.5, 0), 'fixe', lw=0.7); arrow(ax, X(0, 0), X(0, 3), 'fixe', lw=0.7)
t = np.linspace(0.4, 4.2, 120)
line(ax, [X(a, 1 / a) for a in t], 'sujet', lw=1.6)
for r2, role, a0, a1 in ((2, 'resultat', 8, 82), (4.25, 'varie', 3, 70)):
    th = np.radians(np.linspace(a0, a1, 60)); r = r2 ** 0.5
    line(ax, [X(r * np.cos(a), r * np.sin(a)) for a in th], role, lw=1.1, dash=True)
disc(ax, *X(1, 1), 1.4, 'resultat'); disc(ax, *X(2, 0.5), 1.4, 'varie')
text(ax, 5, 4.5, 'O', 'encre', 's')
text(ax, 24, 56, 'courbe x · y = 1', 'sujet', 's')
text(ax, 34, 37, 'distance² = 2', 'resultat', 's'); arrow(ax, (30, 34.5), (25, 25.8), 'resultat', lw=0.7)
text(ax, 62, 24, 'distance² = 4,25', 'varie', 's'); arrow(ax, (54, 21.5), (41.7, 17), 'varie', lw=0.7)
save(fig, '70-179')
