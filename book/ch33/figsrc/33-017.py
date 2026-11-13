import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
X = lambda a: 16 + a / 100 * 60
Y = lambda h: 10 + h * 34
line(ax, [(X(0), Y(0)), (X(104), Y(0))], 'fixe')
line(ax, [(X(0), Y(0)), (X(0), Y(1.15))], 'fixe')
text(ax, 8, Y(1.1), 'hauteur', 'fixe', 's')
text(ax, 78, Y(0) - 6, 'angle', 'fixe', 's')
a = np.linspace(6, 100, 60)
line(ax, [(X(v), Y(0.5 * (v / 30) ** 0.7)) for v in a], 'sujet', lw=1.6)
line(ax, [(X(0), Y(0.5)), (X(104), Y(0.5))], 'fixe', dash=True)
text(ax, 9, Y(0.5), '0,5', 'fixe', 's')
for v, r in ((30, 'varie'), (40, 'resultat'), (100, 'resultat')):
    h = 0.5 * (v / 30) ** 0.7
    line(ax, [(X(v), Y(0)), (X(v), Y(h))], r, dash=True)
    disc(ax, X(v), Y(h), 1.6, r)
    text(ax, X(v), Y(0) - 3, f'{v}°', r, 's')
text(ax, 50, 56, 'ne revient pas à 0,5', 'resultat', 's')
save(fig, '33-017')
