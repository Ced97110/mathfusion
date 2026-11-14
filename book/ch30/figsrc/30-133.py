import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(58)
x0, y0, sx, sy = 10, 12, 70 / 18, 0.8
X = lambda t: x0 + t * sx
Y = lambda h: y0 + h * sy
arrow(ax, (X(0), Y(0)), (X(18) + 4, Y(0)), 'fixe', lw=0.7)
line(ax, [(X(0), Y(0)), (X(0), Y(46))], 'fixe', lw=0.7)
line(ax, [(X(0), Y(22)), (X(18), Y(22))], 'fixe', dash=True)
t = np.linspace(0, 18, 300)
line(ax, list(zip(X(t), Y(20 * np.sin(np.pi / 4 * (t - 2)) + 22))), 'sujet', lw=1.3)
disc(ax, X(0), Y(2), 1.3, 'fixe')
text(ax, X(0) + 2.5, Y(2) - 0.2, 'départ : en bas', 'fixe', 's', ha='left')
disc(ax, X(2), Y(22), 1.6, 'varie')
text(ax, X(2) - 0.5, Y(22) + 6.5, r'$C=2$', 'varie', 'm', ha='right')
for tv in (10, 18):
    disc(ax, X(tv), Y(22), 1.2, 'varie')
for tv in (2, 10, 18):
    text(ax, X(tv), y0 - 3.2, f'{tv}', 'varie', 's')
text(ax, X(18) + 1, Y(22) + 3.5, 'ligne médiane', 'fixe', 's', ha='right')
text(ax, 46, 55, 'sur la ligne médiane, en montant', 'varie', 's')
save(fig, '30-133')
