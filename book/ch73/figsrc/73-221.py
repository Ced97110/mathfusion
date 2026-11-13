import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(58)
O = (44, 8); k = 8
t = np.linspace(0, np.pi, 80)
line(ax, [(O[0] + 5 * k * np.cos(a), O[1] + 5 * k * np.sin(a)) for a in t], 'fixe', dash=True)
line(ax, [(4, 8), (84, 8)], 'fixe', lw=0.6)
tx, tA = (O[0] + 3 * k, O[1] + 4 * k), (O[0] - 1.4 * k, O[1] + 4.8 * k)
arrow(ax, O, tx, 'sujet', lw=1.3); arrow(ax, O, tA, 'resultat', lw=1.3)
disc(ax, O[0], O[1], 1.0, 'fixe')
arrow(ax, (tx[0] - 2, tx[1] + 3), (tA[0] + 3, tA[1] + 1.5), 'varie', curve=0.3)
text(ax, 70.5, 41, r'$x=(3,4)$', 'sujet', 's', ha='left')
text(ax, 33, 53.5, r'$Ax=(-7/5,\ 24/5)$', 'resultat', 's')
text(ax, 59, 21, r'$\|x\|=5$', 'sujet', 's', ha='left')
text(ax, 36, 27, r'$\|Ax\|=5$', 'resultat', 's', ha='right')
text(ax, 44, 3.2, 'même cercle, même longueur', 'fixe', 's')
save(fig, '73-221')
