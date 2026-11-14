import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(72)
s = 13.0; c = (32.0, 36.0)
pp = lambda r, t: (c[0] + s * r * cos(t), c[1] + s * r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
for r in (0.5, 1, 1.5, 2):
    ax.add_patch(Circle(c, s * r, ec=COL['fixe'], fc='none', lw=0.3, zorder=1))
line(ax, [pp(1 + cos(t), t) for t in T(0, 2 * pi, 400)], 'sujet', lw=1.3)
t = radians(60)
arrow(ax, c, pp(1.5, t), 'varie', lw=1.2)
arrow(ax, c, pp(2, 0), 'varie', lw=1.2)
disc(ax, *pp(1.5, t), 1.2, 'resultat'); disc(ax, *pp(2, 0), 1.2, 'resultat'); disc(ax, *c, 1.2, 'encre')
text(ax, pp(1.5, t)[0] + 3, pp(1.5, t)[1] + 3, '$P$ : $r=1{,}5$', 'varie', 's', ha='left')
text(ax, pp(2, 0)[0] - 4, c[1] - 5, '$r=2$', 'varie', 's')
text(ax, c[0] + 1, c[1] - 5, '$O$', 'encre', 's')
box(ax, 4, 2, 80, 8, 'varie', label='$r$ : la distance de $O$ au point', size='s')
save(fig, '40-026')
