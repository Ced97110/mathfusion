import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(70)
s = 14.0; c = (30.0, 35.0)
pp = lambda r, t: (c[0] + s * r * cos(t), c[1] + s * r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
for r in (1, 2):
    ax.add_patch(Circle(c, s * r, ec=COL['fixe'], fc='none', lw=0.3, zorder=1))
line(ax, [pp(1 + cos(t), t) for t in T(0, 2 * pi, 400)], 'sujet', lw=1.2)
for deg, r in ((0, 2), (90, 1)):
    t = radians(deg)
    arrow(ax, c, pp(r, t), 'varie', lw=0.9)
disc(ax, *c, 2.0, 'sujet')
text(ax, c[0] - 8, c[1] - 6, '$O$', 'sujet', 'xl')
text(ax, 72, 56, 'le pôle $O$ :\nd’où l’on mesure\nles distances', 'sujet', 's')
text(ax, 72, 40, '$r$ mesuré\ndepuis $O$', 'varie', 's')
text(ax, 72, 16, '$\\theta=\\pi$ :\n$r=0$, la courbe\nest en $O$', 'resultat', 's')
arrow(ax, (58, 18), (c[0] - 2.3, c[1] - 1.2), 'resultat', lw=0.7, curve=-0.2)
save(fig, '40-024')
