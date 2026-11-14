import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

f = lambda x: x ** 3 - 3 * x + 2
assert f(1) == 0 and f(-2) == 0 and (1 - 1) ** 2 * (1 + 2) == 0
X0, X1, Y0, Y1 = -2.5, 2.2, -3.0, 5.0
sx, sy = 74 / (X1 - X0), 4.8
ox = 6
oy = 24
px = lambda x: ox + (x - X0) * sx
py = lambda y: oy + y * sy
fig, ax = canvas(66)
arrow(ax, (px(X0), py(0)), (px(X1) + 3, py(0)), 'fixe', lw=0.8)
n = 120
pts = [(px(X0 + (X1 - X0) * i / n), py(f(X0 + (X1 - X0) * i / n))) for i in range(n + 1)]
pts = [(a, b) for a, b in pts if b > 6]
line(ax, pts, 'sujet', lw=1.6)
disc(ax, px(1), py(0), 1.8, 'varie')
disc(ax, px(-2), py(0), 1.8, 'resultat')
text(ax, px(1), py(0) - 5, '1 : racine double', 'varie', 's')
text(ax, px(-2) + 1, py(0) - 5, '−2', 'resultat', 's')
text(ax, 70, 52, r'$x^3-3x+2$', 'sujet', 'm', weight='bold')
text(ax, 44, 8, r'$=(x-1)^2(x+2)$', 'sujet', 'm')
text(ax, 44, 2.5, 'd = 108 − 108 = 0', 'varie', 'm', weight='bold')
save(fig, '65-056')
