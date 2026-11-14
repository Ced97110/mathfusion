import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(70)
O, u = (22, 32), 7.5
X = lambda a, b: (O[0] + a * u, O[1] + b * u)
line(ax, [(44.5, 3), (44.5, 68)], 'fixe', lw=0.5, dash=True)
text(ax, 22, 66, 'face 1 : le résultant', 'resultat', 's', weight='bold')
text(ax, 66, 66, 'face 2 : Tarski', 'autre', 's', weight='bold')
line(ax, [X(-2.2, 0), X(2.2, 0)], 'fixe', lw=0.6)
t = np.linspace(-1.7, 1.7, 80)
line(ax, [X(a, a * a) for a in t], 'sujet', lw=1.6)
line(ax, [X(-1.9, 1), X(1.9, 1)], 'autre', lw=1.6)
for xv in (-1, 1):
    line(ax, [X(xv, 1), X(xv, 0)], 'resultat', dash=True)
    disc(ax, *X(xv, 1), 1.2, 'resultat'); disc(ax, *X(xv, 0), 1.0, 'resultat')
    text(ax, X(xv, 0)[0], 27.5, str(xv).replace('-', '−'), 'resultat', 's')
text(ax, 13, 59, r'$y=x^2$', 'sujet', 's'); text(ax, 38, 40.5, r'$y=1$', 'autre', 's')
arrow(ax, (22, 24), (22, 16), 'fixe')
box(ax, 4, 4, 36, 11, 'resultat', label=r'$x^2-1$', size='m')
box(ax, 47, 48, 38, 10, 'autre', label=r'$x^2+bx+c=0$', size='m')
arrow(ax, (66, 47), (66, 36), 'fixe')
box(ax, 47, 24, 38, 11, 'autre', label=r'$b^2-4c\geq 0$', size='m')
text(ax, 66, 14, 'toute question bien\nposée : réponse calculable', 'autre', 's')
save(fig, '70-186')
