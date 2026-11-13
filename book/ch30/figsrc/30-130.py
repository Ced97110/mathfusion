import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(66)
x0, y0, sx, sy = 10, 36, 70 / (1.4 * np.pi), 6.0
X = lambda x: x0 + x * sx
Y = lambda y: y0 + y * sy
P = np.pi
arrow(ax, (X(0), Y(0)), (X(1.4 * P) + 3, Y(0)), 'fixe', lw=0.7)
line(ax, [(X(0), Y(-1.5)), (X(0), Y(3.5))], 'fixe', lw=0.7)
line(ax, [(X(0), Y(1)), (X(1.4 * P), Y(1))], 'resultat', lw=0.9)
t = np.linspace(0, 1.4 * P, 200)
line(ax, list(zip(X(t), Y(np.sin(t)))), 'fixe', dash=True, lw=1.0)
line(ax, list(zip(X(t), Y(2 * np.sin(2 * (t - P / 4)) + 1))), 'sujet', lw=1.3)
disc(ax, X(0), Y(0), 0.9, 'fixe')
disc(ax, X(P / 4), Y(1), 1.2, 'autre')
text(ax, X(P / 4) - 1.5, Y(1) + 3, r'$S$', 'autre', 'm')
arrow(ax, (X(0), Y(-0.5)), (X(P / 4), Y(-0.5)), 'varie')
text(ax, X(P / 8), Y(-0.5) - 2.6, r'$C$', 'varie', 's')
line(ax, [(X(P / 4), Y(0)), (X(P / 4), Y(-0.5))], 'fixe', lw=0.5, dash=True)
arrow(ax, (X(P / 2) + 5, Y(1)), (X(P / 2) + 5, Y(3)), 'varie')
text(ax, X(P / 2) + 7, Y(2), r'$A$', 'varie', 's', ha='left')
arrow(ax, (X(P / 4), 18), (X(5 * P / 4), 18), 'varie', both=True)
for xv in (P / 4, 5 * P / 4):
    line(ax, [(X(xv), Y(1)), (X(xv), 19.5)], 'fixe', lw=0.5, dash=True)
text(ax, X(3 * P / 4), 14, 'une période', 'varie', 's')
text(ax, X(P), Y(1) + 2.4, 'ligne médiane', 'resultat', 's')
text(ax, 24, 62, r'$\sin x$', 'fixe', 'm')
text(ax, 60, 62, r'$y=2\,\sin(2(x-\pi/4))+1$', 'sujet', 's')
save(fig, '30-130')
