import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(64)
s = 13.0; c = (6.0, 8.0)
pp = lambda r, t: (c[0] + s * r * cos(t), c[1] + s * r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
for r in (0.5, 1, 1.5, 2):
    hl = r == 1.5
    line(ax, [pp(r, t) for t in T(0, pi / 2, 60)], 'varie' if hl else 'fixe', lw=1.3 if hl else 0.4)
for k in range(4):
    t = radians(30 * k)
    hl = k == 2
    line(ax, [c, pp(2.1, t)], 'sujet' if hl else 'fixe', lw=1.3 if hl else 0.3)
line(ax, [c, pp(1.5, radians(60))], 'encre', lw=0.9)
disc(ax, *pp(1.5, radians(60)), 1.3, 'resultat')
text(ax, pp(1.5, radians(60))[0] + 3, pp(1.5, radians(60))[1] + 2, '$P$', 'resultat', 'm')
disc(ax, *c, 1.0, 'encre')
text(ax, c[0] - 0.5, c[1] - 3, '$O$', 'encre', 's', ha='left')
for r, lab in ((0.5, '0,5'), (1, '1'), (1.5, '1,5'), (2, '2')):
    text(ax, c[0] + s * r, c[1] - 3, lab, 'fixe', 's')
box(ax, 50, 44, 36, 14, 'sujet', label='1. le rayon\n$\\theta=\\pi/3$ (60°)', size='s')
box(ax, 50, 26, 36, 14, 'varie', label='2. le cercle\n3e cercle : $r=1{,}5$', size='s')
box(ax, 50, 6, 36, 16, 'resultat', label='calcul\n$1+\\cos(\\pi/3)=1{,}5$', size='s')
save(fig, '40-015')
