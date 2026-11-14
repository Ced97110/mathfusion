import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X = lambda v: 44 + 18 * v
Y = lambda v: 30 + 12 * v
pts = [(X(-2.2 + 0.05 * i), Y((-2.2 + 0.05 * i) ** 2 + (-2.2 + 0.05 * i) - 1)) for i in range(69)]
arrow(ax, (3, 30), (70, 30), 'fixe', lw=0.8)
line(ax, pts, 'sujet', lw=1.3)
r1, r2 = (-1 + 5 ** 0.5) / 2, (-1 - 5 ** 0.5) / 2
disc(ax, X(r1), 30, 1.4, 'resultat')
disc(ax, X(r2), 30, 1.4, 'resultat')
text(ax, X(r1) + 4, 25, '0,618', 'resultat', 's')
text(ax, X(r2) - 3, 25, '−1,618', 'resultat', 's')
text(ax, 74, 30, 'y', 'fixe', 'm')
text(ax, 44, 57, r'$y^2+y-1=0$', 'sujet', 'l')
text(ax, 68, 12, '0,618² + 0,618 − 1 ≈ 0', 'resultat', 's')
text(ax, 38, 4, '(y² − 2) + y + 1 = y² + y − 1', 'encre', 's')
save(fig, '66-093')
