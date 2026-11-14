import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(64)
X = lambda d: 6 + d * 76 / 360
y0, k = 30, 3.6
Y = lambda v: y0 + v * k
line(ax, [(6, y0), (82, y0)], 'fixe')
for d in (0, 180, 360):
    line(ax, [(X(d), 5), (X(d), 54)], 'limite', dash=True)
    text(ax, X(d), 58, f'{d}°', 'limite', 's')
for a, b in ((9.4, 170.6), (189.4, 350.6)):
    d = np.linspace(a, b, 200); v = 1 / np.tan(np.radians(d))
    line(ax, list(zip(X(d), Y(v))), 'sujet', lw=1.3)
for d, v, lab, dx, dy in ((10, 5.67, '5,67', 5.5, 0), (45, 1, '1', 2.5, 3), (100, -0.1763, '−0,1763', -3.5, -5), (170, -5.67, '−5,67', 6.5, 0)):
    disc(ax, X(d), Y(v), 0.9, 'varie'); text(ax, X(d) + dx, Y(v) + dy, lab, 'varie', 's')
text(ax, 44, 1.5, 'verticales : angles interdits', 'limite', 's')
save(fig, '31-107')
