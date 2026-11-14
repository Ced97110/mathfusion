import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(60)
ay = 40
X = lambda t: 8 + 100 * t
ts = np.linspace(0, 0.7, 60)
line(ax, [(6, ay), (80, ay)], 'fixe')
line(ax, [(X(t), ay + 6 * (t ** 3 - 3 * t + 1)) for t in ts], 'sujet', lw=1.4)
line(ax, [(X(t), ay + 6 * (3 * t ** 2 - 3)) for t in ts], 'varie', lw=1.4)
r = 0.3473
line(ax, [(X(r), 18), (X(r), 51)], 'fixe', dash=True, lw=0.6)
text(ax, X(r), 13.5, r'$r_2\approx 0{,}35$', 'encre', 'm')
text(ax, 13, 47, r'$f_0$', 'sujet', 'm')
text(ax, 14, 26.5, r'$f_1$', 'varie', 'm')
text(ax, (8 + X(r)) / 2, 55, r'$+,-$', 'encre', 'm')
text(ax, (X(r) + X(0.7)) / 2, 55, r'$-,-$', 'encre', 'm')
text(ax, (8 + X(r)) / 2, 6, 'un changement', 'varie', 's')
text(ax, (X(r) + X(0.7)) / 2, 6, 'aucun changement', 'fixe', 's')
save(fig, '69-099')
