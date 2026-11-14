import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(56)
x0, y0, sx, sy = 12, 24, 70 / (1.4 * np.pi), 6.0
X = lambda x: x0 + x * sx
Y = lambda y: y0 + y * sy
arrow(ax, (X(0), Y(0)), (X(1.4 * np.pi) + 3, Y(0)), 'fixe', lw=0.7)
line(ax, [(X(0), Y(-1.4)), (X(0), Y(3.4))], 'fixe', lw=0.7)
line(ax, [(X(0), Y(1)), (X(1.4 * np.pi), Y(1))], 'fixe', dash=True)
t = np.linspace(0, 1.4 * np.pi, 200)
line(ax, list(zip(X(t), Y(2 * np.sin(2 * (t - np.pi / 4)) + 1))), 'sujet', lw=1.3)
pts = [(np.pi / 4, 1), (np.pi / 2, 3), (3 * np.pi / 4, 1), (np.pi, -1), (5 * np.pi / 4, 1)]
labs = [r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$', r'$5\pi/4$']
for (px, py), lb in zip(pts, labs):
    line(ax, [(X(px), Y(py)), (X(px), 14)], 'fixe', lw=0.5, dash=True)
    disc(ax, X(px), Y(py), 1.1, 'varie')
    text(ax, X(px), 11, lb, 'varie', 's')
for v in (-1, 1, 3):
    text(ax, x0 - 3.5, Y(v), f'{v}'.replace('-', '−'), 'fixe', 's')
arrow(ax, (X(np.pi / 2) + 6, Y(1)), (X(np.pi / 2) + 6, Y(3)), 'varie', both=True)
text(ax, X(np.pi / 2) + 8, Y(2), r'$A=2$', 'varie', 's', ha='left')
text(ax, 44, 51, r'$y=2\,\sin(2(x-\pi/4))+1$', 'sujet', 'l')
save(fig, '30-128')
