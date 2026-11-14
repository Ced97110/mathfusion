import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X0, U, Y0, K = 44, 16.0, 30, 6.0   # origine x, mm par unité, axe, mm par unité de valeur
g = lambda x: x ** 3 - 3 * x + 1
px = lambda x: X0 + U * x
py = lambda v: Y0 + K * v
n = 200
xs = [-2.2 + 4.4 * i / n for i in range(n + 1)]
line(ax, [(px(x), py(g(x))) for x in xs], 'sujet', lw=1.3)
line(ax, [(px(-2.4), Y0), (px(2.4), Y0)], 'fixe')
for v in (-2, -1, 0, 1, 2):
    line(ax, [(px(v), Y0 - 1.2), (px(v), Y0 + 1.2)], 'fixe')
for v in (-2, 0, 1, 2):
    text(ax, px(v), Y0 - 2.9, f'{v}'.replace('-', '−'), 'fixe', 's')
vals = {-2: -1, 0: 1, 1: -1, 2: 3}
for x, v in vals.items():
    disc(ax, px(x), py(v), 1.0, 'varie')
    dx, dy = {-2: (-5.5, -1), 0: (4.5, 2), 1: (5.5, -1), 2: (-5.5, 1)}[x]
    text(ax, px(x) + dx, py(v) + dy, f'{v}'.replace('-', '−'), 'varie', 's')
for r, dx in ((-1.88, 0), (0.35, 0), (1.53, 0)):
    disc(ax, px(r), Y0, 1.3, 'resultat')
    text(ax, px(r), Y0 - 9.5, f'{r:g}'.replace('.', ',').replace('-', '−'), 'resultat', 's')
text(ax, 44, 61, r'$x^3-3x+1$', 'sujet', 'l')
disc(ax, 66, 10, 1.2, 'resultat'); text(ax, 69, 10, 'racines', 'resultat', 's', ha='left')
disc(ax, 66, 15, 1.0, 'varie'); text(ax, 69, 15, 'essais', 'varie', 's', ha='left')
save(fig, '65-002')
