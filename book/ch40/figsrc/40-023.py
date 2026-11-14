import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(66)
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
# gauche : graphe de y = f(x)
O = (6.0, 14.0)
arrow(ax, O, (O[0] + 32, O[1]), 'fixe', lw=0.9); arrow(ax, O, (O[0], O[1] + 34), 'fixe', lw=0.9)
text(ax, O[0] + 33, O[1] - 3.5, '$x$', 'fixe', 's'); text(ax, O[0] - 3.5, O[1] + 34, '$y$', 'fixe', 's')
line(ax, [(O[0] + 3 + t * 1.0, O[1] + 4 + 10 * sin(t / 30 * pi) + 8 * t / 30) for t in T(0, 27, 80)], 'sujet', lw=1.2)
text(ax, 22, 56, 'graphe de\n$y=f(x)$', 'encre', 's')
text(ax, 22, 6, 'règle sur $x$ et $y$', 'fixe', 's')
# droite : courbe polaire r = 2
c = (64.0, 32.0); s = 10.0
line(ax, [(c[0] + 2 * s * cos(t), c[1] + 2 * s * sin(t)) for t in T(0, 2 * pi, 200)], 'sujet', lw=1.2)
line(ax, [c, (c[0] + 2.4 * s, c[1])], 'fixe', lw=0.9)
disc(ax, *c, 0.9, 'encre')
disc(ax, c[0] + 2 * s, c[1], 1.3, 'resultat')
disc(ax, c[0] + 1 * s, c[1], 1.3, 'limite')
text(ax, c[0] + 8, c[1] + 11, 'sur la courbe', 'resultat', 's')
arrow(ax, (c[0] + 13, c[1] + 8.5), (c[0] + 2 * s - 0.5, c[1] + 1.8), 'resultat', lw=0.6)
text(ax, c[0] + s, c[1] - 5, 'hors courbe', 'limite', 's')
text(ax, 64, 56, 'courbe polaire\n$r=2$', 'encre', 's')
text(ax, 64, 6, 'règle sur $r$ et $\\theta$', 'fixe', 's')
save(fig, '40-023')
