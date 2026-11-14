import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(64)
ox, oy, r = 26, 30, 22
disc(ax, ox, oy, r, 'fixe', fill=False)
u1 = np.array([0.6, 0.8]); u2 = np.array([-0.8, 0.6]); O = np.array([ox, oy])
arrow(ax, tuple(O), tuple(O + r * u1), 'sujet', lw=1.3)
arrow(ax, tuple(O), tuple(O + r * u2), 'autre', lw=1.3)
line(ax, [tuple(O + 3 * u1), tuple(O + 3 * u1 + 3 * u2), tuple(O + 3 * u2)], 'fixe')
text(ax, 43, 53, 'colonne 1', 'sujet', 's'); text(ax, 11, 50, 'colonne 2', 'autre', 's')
text(ax, 72, 50, r'$\frac{9}{25}+\frac{16}{25}=1$', 'sujet', 's')
text(ax, 72, 36, r'$\frac{16}{25}+\frac{9}{25}=1$', 'autre', 's')
text(ax, 72, 24, 'produit scalaire', 'resultat', 's')
text(ax, 72, 16, r'$-\frac{12}{25}+\frac{12}{25}=0$', 'resultat', 's')
save(fig, '73-220')
