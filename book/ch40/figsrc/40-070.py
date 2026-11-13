import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np

a, b = 3, 2
fig, ax = canvas(76)
X = lambda c: 12 + (c + 1)/0.5*64
Y = lambda x: 60 + (x + 1)*130
c = np.linspace(-1, -0.5, 200)
ax.plot(X(c), Y(a*c + b*c**2), color=COL['sujet'], lw=1.5, zorder=3)
line(ax, [(8, Y(-1)), (82, Y(-1))], 'fixe', dash=True)
arrow(ax, (8, 40), (82, 40), 'fixe', lw=0.8)
text(ax, 84.5, 40, 'c', 'fixe', 's')
for cv, lab in ((-1, '−1'), (-0.9, '−0,9')):
    line(ax, [(X(cv), 38.8), (X(cv), 41.2)], 'fixe')
    text(ax, X(cv), 35.5, lab, 'fixe', 's')
P = (X(-1), Y(-1)); Q = (X(-0.9), Y(a*(-0.9) + b*0.81))
line(ax, [P, (P[0], 40)], 'fixe', dash=True); line(ax, [Q, (Q[0], 40)], 'fixe', dash=True)
disc(ax, P[0], P[1], 0.9, 'sujet'); disc(ax, Q[0], Q[1], 0.9, 'varie')
arrow(ax, (Q[0], P[1] - 0.6), (Q[0], Q[1] + 0.8), 'varie', lw=0.9)
text(ax, Q[0] - 2.5, (P[1] + Q[1])/2 + 1, '−0,08', 'varie', 's', ha='right')
text(ax, P[0] + 1, P[1] + 4, 'x = −1', 'sujet', 's')
text(ax, Q[0] + 3, Q[1] + 5, 'x = −1,08', 'varie', 's', ha='left')
text(ax, 44, 72, 'x = 3c + 2c²   avec c = cos θ', 'sujet', 'm')
text(ax, 44, 29, 'x = ac + bc²', 'encre', 's')
text(ax, 44, 22, 'x(−1+h) − x(−1) = h(a − 2b + bh)', 'encre', 's')
text(ax, 44, 15, '3 et 2 : 0,1 (3 − 4 + 0,2) = −0,08', 'varie', 's')
text(ax, 44, 7, 'a − 2b < 0 : creux', 'resultat', 'm')
save(fig, '40-070')
