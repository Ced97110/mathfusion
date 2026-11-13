import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(52)
X = lambda d: 10 + d * 70 / 360
y0, k = 12, 10
d = np.linspace(0, 360, 300); s = np.sin(np.radians(d)); c2 = np.cos(np.radians(d)) ** 2
line(ax, [(10, y0), (80, y0)], 'fixe')
line(ax, list(zip(X(d), y0 + k * c2)), 'sujet', lw=1.3)
line(ax, list(zip(X(d), y0 + k * (1 - s))), 'varie', lw=1.3)
for a in (0, 90, 180, 270, 360):
    line(ax, [(X(a), y0 - 1), (X(a), y0 + 1)], 'fixe'); text(ax, X(a), 7.5, f'{a}°', 'encre', 's')
for a, v in ((0, 1), (90, 0), (180, 1), (360, 1)):
    disc(ax, X(a), y0 + k * v, 1.0, 'resultat')
line(ax, [(X(270), y0), (X(270), y0 + 2 * k)], 'limite', dash=True)
disc(ax, X(270), y0, 1.2, 'sujet'); disc(ax, X(270), y0 + 2 * k, 1.2, 'varie')
text(ax, X(270) + 3.5, y0 + 2.5, '0', 'sujet', 's'); text(ax, X(270) + 3.5, y0 + 2 * k, '2', 'varie', 's')
text(ax, 24, 44, 'cos² x', 'sujet', 's'); text(ax, 62, 44, '1 − sin x', 'varie', 's')
save(fig, '31-110')
