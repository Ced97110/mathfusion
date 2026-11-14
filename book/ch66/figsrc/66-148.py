import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
import numpy as np
fig, ax = canvas(100)
ay = 52
X = lambda v: 10 + (v - 1.5) * 22
P = lambda v: ay + 14 * (v * v - 5.860 * v + 8.540)
vs = np.linspace(1.5, 4.5, 80)
line(ax, [(6, ay), (82, ay)], 'fixe')
line(ax, [(X(v), P(v)) for v in vs], 'fixe', lw=1.2)
disc(ax, X(math.e), ay, 1.5, 'sujet'); text(ax, X(math.e), ay - 4, r'$e$', 'sujet', 'm')
disc(ax, X(math.pi), ay, 1.5, 'autre'); text(ax, X(math.pi), ay - 4, r'$\pi$', 'autre', 'm')
text(ax, 44, 96, r'$x^{2}-5{,}860\,x+8{,}540$', 'encre', 'm')
text(ax, 44, 73, r'somme $\approx5{,}860$', 'fixe', 's')
text(ax, 44, 67, r'produit $\approx8{,}540$', 'fixe', 's')
box(ax, 14, 30, 60, 8, 'varie', label='somme, produit algébriques', size='s')
arrow(ax, (44, 30), (44, 24), 'fixe')
box(ax, 14, 16, 60, 8, 'fixe', label=r'racines $e$, $\pi$ algébriques', size='s')
arrow(ax, (44, 16), (44, 10), 'fixe')
box(ax, 14, 2, 60, 8, 'limite', label=r'$e$ algébrique : faux', size='s')
save(fig, '66-148')
