import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(60)
R = 10.0
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
cs = [(15, 32), (44, 32), (73, 32)]
for c in cs:
    line(ax, [(c[0] + R * cos(t), c[1] + R * sin(t)) for t in T(0, 2 * pi, 200)], 'sujet', lw=1.2)
    disc(ax, *c, 0.8, 'encre')
# 1. y = f(x) : une verticale coupe le cercle deux fois
c = cs[0]; X = 5.0
line(ax, [(c[0] + X, c[1] - 13), (c[0] + X, c[1] + 13)], 'varie', dash=True)
h = (R * R - X * X) ** 0.5
disc(ax, c[0] + X, c[1] + h, 1.0, 'limite'); disc(ax, c[0] + X, c[1] - h, 1.0, 'limite')
text(ax, c[0], 14, '$y=f(x)$', 'encre', 's')
text(ax, c[0], 8, 'deux $y$\npour un $x$', 'limite', 's')
# 2. relation en x et y
c = cs[1]; a = radians(40)
P = (c[0] + R * cos(a), c[1] + R * sin(a))
line(ax, [P, (P[0], c[1])], 'varie', lw=1.0); line(ax, [(P[0], c[1]), c], 'varie', lw=1.0)
disc(ax, *P, 1.0, 'resultat')
text(ax, c[0], 14, '$x^2+y^2=4$', 'encre', 's')
text(ax, c[0], 8, '$x$ et $y$ liés,\nsans sens', 'fixe', 's')
# 3. r = f(theta)
c = cs[2]; a = radians(40)
P = (c[0] + R * cos(a), c[1] + R * sin(a))
line(ax, [c, (c[0] + R + 2, c[1])], 'fixe', lw=0.9)
line(ax, [c, P], 'resultat', lw=1.2)
disc(ax, *P, 1.0, 'resultat')
line(ax, [(c[0] + 4 * cos(t), c[1] + 4 * sin(t)) for t in T(0, a, 20)], 'varie', lw=0.9)
text(ax, c[0] + 7, c[1] + 2.5, '$\\theta$', 'varie', 's')
text(ax, c[0], 14, '$r=f(\\theta)$', 'sujet', 's')
text(ax, c[0], 8, 'entrée $\\theta$ →\nsortie $r=2$', 'sujet', 's')
text(ax, 44, 55, 'cercle de rayon 2, trois écritures', 'encre', 's')
save(fig, '40-022')
