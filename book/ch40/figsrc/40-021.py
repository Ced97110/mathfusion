import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin
fig, ax = canvas(84)
s = 14.0; c = (14.0, 42.0)
pp = lambda r, t: (c[0] + s * r * cos(t), c[1] + s * r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
line(ax, [pp(2 * (1 + cos(t)), t) for t in T(0, 2 * pi, 400)], 'autre', lw=1.2)
line(ax, [pp(1 + cos(t), t) for t in T(0, 2 * pi, 400)], 'sujet', lw=1.2)
disc(ax, *c, 1.3, 'encre')
text(ax, c[0] - 1, c[1] + 6, 'pointe en $O$', 'encre', 's', ha='left')
text(ax, 56, 42, 'arrondie\nde ce côté', 'encre', 's')
text(ax, 44, 79, 'cardioïde', 'resultat', 'xl')
text(ax, 62, 66, '$r=2(1+\\cos\\theta)$', 'autre', 's')
text(ax, 34, 52, '$r=1+\\cos\\theta$', 'sujet', 's')
save(fig, '40-021')
