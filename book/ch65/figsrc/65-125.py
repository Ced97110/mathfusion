import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
X = lambda x: 23.5 + x * 9.5
Y = lambda v: 30 + v * 4
xs = np.linspace(-2.1, 2.05, 90)
pts = [(X(x), Y(x ** 3 - 3 * x + 1)) for x in xs]
line(ax, [(3, 30), (44, 30)], 'fixe', lw=0.8)
line(ax, pts, 'sujet', lw=1.3)
for r in np.roots([1, 0, -3, 1]).real:
    disc(ax, X(r), 30, 1.5, 'resultat')
text(ax, 23.5, 52, r'$x^3-3x+1$', 'sujet', 's')
text(ax, 23.5, 12, '3 racines réelles', 'resultat', 's')
box(ax, 50, 44, 36, 11, 'fixe', label=r'$d=81$')
arrow(ax, (68, 44), (68, 39), 'varie')
box(ax, 50, 28, 36, 11, 'fixe', label=r'$-3d=-243$')
arrow(ax, (68, 28), (68, 23), 'varie')
box(ax, 50, 6, 36, 17, 'autre', label=r'$\sqrt{-243}$' + '\npas un nombre réel', size='s')
save(fig, '65-125')
