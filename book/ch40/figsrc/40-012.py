import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(74)
s = 16.0; c = (34, 37)
pp = lambda r, t: (c[0] + s * r * cos(t), c[1] + s * r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
for r in (0.5, 1, 1.5, 2):
    ax.add_patch(Circle(c, s * r, ec=COL['fixe'], fc='none', lw=0.4, zorder=1))
for k in range(12):
    t = radians(30 * k)
    line(ax, [c, pp(2, t)], 'fixe', lw=0.3)
line(ax, [c, pp(2.2, 0)], 'fixe', lw=0.9)
line(ax, [pp(1 + cos(t), t) for t in T(0, 2 * pi, 400)], 'sujet', lw=1.3)
t3 = radians(60)
disc(ax, *pp(1.5, -t3), 1.0, 'varie')
line(ax, [pp(1.5, t3), pp(1.5, -t3)], 'varie', lw=0.6, dash=True)
disc(ax, *pp(2, 0), 1.0, 'varie')
text(ax, pp(2, 0)[0] + 2, pp(2, 0)[1] + 3.5, 'large', 'varie', 's', ha='left')
text(ax, c[0] - 7, c[1] + 6, 'pointe', 'varie', 's', ha='right')
line(ax, [(c[0] - 7, c[1] + 5), (c[0] - 0.8, c[1] + 0.6)], 'varie', lw=0.5)
line(ax, [c, pp(1.5, t3)], 'varie', lw=1.0)
disc(ax, *pp(1.5, t3), 1.2, 'resultat')
disc(ax, c[0], c[1], 1.0, 'encre')
text(ax, c[0] - 3, c[1] - 3, '$O$', 'encre', 's')
text(ax, pp(1.5, t3)[0] + 3, pp(1.5, t3)[1] + 2, '$P$', 'resultat', 'm')
text(ax, c[0] + 9, c[1] + 3.5, r'$\theta=\pi/3$', 'varie', 's', ha='left')
line(ax, [pp(0.45, t) for t in T(0, t3, 20)], 'varie', lw=0.8)
for r, lab in ((0.5, '0,5'), (1, '1'), (1.5, '1,5'), (2, '2')):
    text(ax, c[0] + s * r, c[1] - 3, lab, 'fixe', 's')
text(ax, 72, 8, 'miroir : haut = bas', 'fixe', 's')
save(fig, '40-012')
