import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(64)
P = np.pi
x0, y0, sx, sy = 14, 46, 66 / (1.4 * P), 5.0
X = lambda x: x0 + x * sx
Y = lambda y: y0 + y * sy
arrow(ax, (X(0), Y(0)), (X(1.4 * P) + 3, Y(0)), 'fixe', lw=0.7)
line(ax, [(X(0), Y(-1.6)), (X(0), Y(3.4))], 'fixe', lw=0.7)
t = np.linspace(0, 1.4 * P, 200)
line(ax, list(zip(X(t), Y(2 * np.sin(2 * (t - P / 4)) + 1))), 'sujet', lw=1.3)
line(ax, [(X(0), Y(-1)), (X(0.5), Y(-1))], 'resultat', lw=0.6, dash=True)
disc(ax, X(0), Y(-1), 1.3, 'resultat')
text(ax, x0 - 3, Y(-1), '−1', 'resultat', 's')
text(ax, x0 + 1, Y(-1) - 4, r'$x=0$', 'varie', 's', ha='left')
steps = [r'$2(0-\pi/4)=-\pi/2$', r'$\sin(-\pi/2)=-1$', r'$y=2\times(-1)+1=-1$']
roles = ['varie', 'sujet', 'resultat']
for i, (s, r) in enumerate(zip(steps, roles)):
    y = 28 - i * 11.5
    box(ax, 14, y - 4, 60, 8, r, label=s)
    if i: arrow(ax, (44, y + 7.5), (44, y + 4.2), 'fixe')
save(fig, '30-131')
