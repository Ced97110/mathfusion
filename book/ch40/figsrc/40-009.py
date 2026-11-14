import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(64)
pp = lambda c, r, t: (c[0] + r * cos(t), c[1] + r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
cs = [(15, 36), (44, 36), (73, 36)]
# 1. spirale
a = 9.0 / (2 * pi)
line(ax, [pp(cs[0], a * t, t) for t in T(0, 4 * pi, 300)], 'sujet', lw=1.0)
# 2. trois boucles
line(ax, [pp(cs[1], 12 * cos(3 * t), t) for t in T(0, pi, 300)], 'sujet', lw=1.0)
# 3. orbite (cercle presque rond)
line(ax, [pp(cs[2], 12 * 149.6 / 147.1 / (1 + 0.017 * cos(t)) * 147.1 / 149.6, t) for t in T(0, 2 * pi, 300)], 'sujet', lw=1.0)
for c, ang in zip(cs, (50, 60, 50)):
    disc(ax, c[0], c[1], 1.2, 'varie')
    line(ax, [c, pp(c, 13, radians(ang))], 'varie', lw=0.8)
    line(ax, [pp(c, 6, radians(a_)) for a_ in T(0, ang, 20)], 'varie', lw=0.7)
for c, lab in zip(cs, ('l’axe', 'le centre\ndu motif', 'le Soleil')):
    text(ax, c[0], 14, lab, 'varie', 's')
for c, lab in zip(cs, ('rouleau', 'trois boucles', 'orbite')):
    text(ax, c[0], 58, lab, 'sujet', 's')
box(ax, 4, 2, 80, 6, 'resultat', label=r'un centre : on lit une distance $r$ et un angle $\theta$', size='s')
save(fig, '40-009')
