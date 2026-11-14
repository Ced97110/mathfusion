import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(60)
X = lambda a: 8 + (a + 270) / 720 * 72
Y = lambda h: 30 + h * 18
line(ax, [(8, Y(0)), (80, Y(0))], 'fixe')
a = np.linspace(-270, 450, 200)
line(ax, [(X(v), Y(np.sin(np.radians(v)))) for v in a], 'sujet', lw=1.6)
line(ax, [(8, Y(0.5)), (80, Y(0.5))], 'varie', dash=True)
text(ax, 84, Y(0.5), '0,5', 'varie', 's')
for v in (-210, 30, 150, 390):
    line(ax, [(X(v), Y(0.5)), (X(v), 10)], 'varie', dash=True)
    disc(ax, X(v), Y(0.5), 1.6, 'varie')
    text(ax, X(v), 6, f'{v}°'.replace('-', '−'), 'varie', 's')
text(ax, 44, 55, 'infinité d’angles pour 0,5', 'encre', 's')
save(fig, '33-022')
