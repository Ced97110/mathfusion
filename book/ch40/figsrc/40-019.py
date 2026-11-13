import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(70)
s = 11.0; c = (28.0, 24.0)
pp = lambda r, t: (c[0] + s * r * cos(t), c[1] + s * r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
for r in (1, 2):
    line(ax, [pp(r, t) for t in T(0, pi, 90)], 'fixe', lw=0.3)
line(ax, [pp(1 + cos(t), t) for t in T(0, pi, 300)], 'sujet', lw=1.3)
pts = [pp(1 + cos(radians(30 * k)), radians(30 * k)) for k in range(7)]
for k in range(6):
    arrow(ax, pts[k], pts[k + 1], 'varie', lw=0.8, curve=0.0)
for p in pts:
    disc(ax, *p, 0.9, 'varie')
disc(ax, *c, 1.1, 'encre')
text(ax, c[0] + 22 + 2, c[1] - 4, '$r=2$', 'varie', 's')
text(ax, c[0] - 2, c[1] - 4, '$O$ : $r=0$', 'encre', 's', ha='right')
text(ax, 70, 55, 'angle ↑ de 0 à $\\pi$', 'varie', 'm')
box(ax, 56, 36, 30, 11, 'varie', label='$\\cos\\theta$ : $1\\to0\\to-1$', size='s')
box(ax, 56, 21, 30, 11, 'resultat', label='$r$ : $2\\to1\\to0$', size='s')
arrow(ax, (71, 52), (71, 47.5), 'fixe'); arrow(ax, (71, 36), (71, 32.5), 'fixe')
text(ax, 44, 4, 'la courbe arrive en $O$ pour $\\theta=\\pi$', 'encre', 's')
save(fig, '40-019')
