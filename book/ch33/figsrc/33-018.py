import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(64)
X = lambda a: 44 + a * 34 / 90
Y = lambda h: 30 + h * 20
line(ax, [(X(-90), Y(0)), (X(95), Y(0))], 'fixe')
a = np.linspace(-90, 90, 80)
line(ax, [(X(v), Y(np.sin(np.radians(v)))) for v in a], 'sujet', lw=1.8)
for v, hl in ((-30, '−0,5'), (0, '0'), (64.16, '0,9')):
    h = np.sin(np.radians(v)) if v != 0 else 0
    line(ax, [(X(-90), Y(h)), (X(95), Y(h))], 'varie', dash=True)
    line(ax, [(X(v), Y(h)), (X(v), 9)], 'resultat', dash=True)
    disc(ax, X(v), Y(h), 1.6, 'resultat')
    text(ax, 84, Y(h), hl, 'varie', 's')
    text(ax, X(v), 5, '64,16°' if v == 64.16 else f'{v}°'.replace('-', '−'), 'resultat', 's')
text(ax, 44, 58, 'un seul angle par hauteur', 'sujet', 's')
save(fig, '33-018')
