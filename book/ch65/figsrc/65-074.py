import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(80)
X = lambda x: 52 + x * 14.0
Y = lambda y: 46 + y * 1.8
f = lambda x: x**3 - 3 * x + 3
xs = [-3.2 + i * 0.05 for i in range(111)]
line(ax, [(X(-3.4), 46), (X(2.4), 46)], 'fixe')
line(ax, [(X(x), Y(f(x))) for x in xs], 'autre', lw=1.3)
for x in (-3, -2, 0, 2):
    ax.plot([X(x), X(x)], [45, 47], color=COL['fixe'], lw=0.8)
    text(ax, X(x), 42.5, f'{x}'.replace('-', '−'), 'fixe', 's')
    disc(ax, X(x), Y(f(x)), 1.0, 'autre')
text(ax, X(-3) + 6, Y(-15) - 0.5, '−15', 'autre', 's')
text(ax, X(-2) - 3, Y(1) + 3, '1', 'autre', 's')
text(ax, X(0) + 3, Y(3) + 3, '3', 'autre', 's')
text(ax, X(2) + 3, Y(5) + 1, '5', 'autre', 's')
r = [z.real for z in np.roots([1, 0, -3, 3]) if abs(z.imag) < 1e-9][0]
disc(ax, X(r), 46, 1.5, 'resultat')
box(ax, 12, 66, 64, 9, 'fixe', label=r'$d = 108 - 27\times 9 = -135$', size='s')
disc(ax, 46, 22, 1.5, 'resultat')
text(ax, 49, 22, 'une seule racine réelle', 'resultat', 's', ha='left')
save(fig, '65-074')
