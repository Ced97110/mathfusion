import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(80)
g = lambda x: x * (x - 3) * (x + 3) * (x ** 2 + 3)
f = lambda x: g(x) - 3
text(ax, 44, 76, r'$f(x)=x(x-3)(x+3)(x^2+3)-3$', 'sujet', 'm')
# vue d'ensemble
sx, sy, x0, y0 = 5.2, 0.16, 23, 38
X = np.linspace(-3.5, 3.5, 300)
line(ax, [(x0 + sx * x, y0 + sy * g(x)) for x in X], 'fixe', lw=1.6)
line(ax, [(x0 + sx * x, y0 + sy * f(x)) for x in X], 'sujet', lw=0.8)
line(ax, [(2, y0), (44, y0)], 'fixe', lw=0.5)
for v in (-3, 0, 3):
    disc(ax, x0 + sx * v, y0, 1.2, 'fixe')
    dxy = {-3: (-4, 3.5), 0: (4, 3.5), 3: (4, -3.5)}[v]
    text(ax, x0 + sx * v + dxy[0], y0 + dxy[1], f'{v}'.replace('-', '−'), 'fixe', 's')
text(ax, 23, 68, "vue d'ensemble", 'encre', 's')
# zoom près de 3
cx, ky, y1 = 67, 1.2 / 1.0, 38
sxz = 34 / 0.14
def P(x, h): return (cx + sxz * (x - 3), y1 + ky * h)
Z = np.linspace(2.93, 3.07, 60)
line(ax, [P(x, g(x)) for x in Z], 'fixe', lw=1.6)
line(ax, [P(x, f(x)) for x in Z], 'sujet', lw=0.9)
line(ax, [(50, y1), (85, y1)], 'fixe', lw=0.5)
r = 3.0
for _ in range(60): r -= f(r) / (216.0)
disc(ax, P(3, 0)[0], y1, 1.2, 'fixe'); disc(ax, P(r, 0)[0], y1, 1.2, 'resultat')
arrow(ax, (P(3.03, g(3.03))[0] - 3, P(3.03, g(3.03))[1]), (P(3.03, g(3.03))[0] - 3, P(3.03, f(3.03))[1]), 'varie')
text(ax, 67, 68, 'zoom près de 3', 'encre', 's')
text(ax, 77, 63, 'produit', 'fixe', 's'); text(ax, 84, 49, '$f$', 'sujet', 's')
text(ax, 66.5, 46, '− 3', 'varie', 's')
save(fig, '64-174')
