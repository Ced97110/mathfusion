import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = lambda x: 22 + (x - 2) * 8
Y = lambda y: 36 + y * 4
n = 20
text(ax, 22, 74, r'$\frac{1}{x-2}$', 'sujet', 'm'); text(ax, 22, 62, r'haut $=1$', 'sujet', 's')
line(ax, [(X(2), 18), (X(2), 54)], 'limite', dash=True, lw=1.1)
line(ax, [(X(2.25 + i * (2.0 / n)), Y(1 / (0.25 + i * (2.0 / n)))) for i in range(n + 1)], 'sujet', lw=1.2)
line(ax, [(X(0.2 + i * (1.5 / n)), Y(1 / (-1.8 + i * (1.5 / n)))) for i in range(n + 1)], 'sujet', lw=1.2)
text(ax, 22, 11, 'coupure', 'limite', 'm')
G = lambda x: 48 + x * 9.5
H_ = lambda y: 20 + (y - 2) * 8
line(ax, [(G(0), H_(2)), (G(1.8), H_(3.8))], 'autre', lw=1.2); line(ax, [(G(2.2), H_(4.2)), (G(4), H_(6))], 'autre', lw=1.2)
disc(ax, G(2), H_(4), 1.5, 'encre')
text(ax, 67, 74, r'$\frac{x^2-4}{x-2}$', 'autre', 'm'); text(ax, 67, 62, r'haut $=0$ si $x=2$', 'autre', 's')
text(ax, 67, 11, 'point manquant', 'autre', 'm')
save(fig, '21-145')
