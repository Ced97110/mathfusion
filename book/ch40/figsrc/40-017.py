import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(52)
s = 10.0; c = (24.0, 6.0)
pp = lambda r, t: (c[0] + s * r * cos(t), c[1] + s * r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
for r in (0.5, 1, 1.5, 2):
    line(ax, [pp(r, t) for t in T(0, pi, 90)], 'fixe', lw=0.4)
for k in range(7):
    t = radians(30 * k)
    line(ax, [c, pp(2.1, t)], 'fixe', lw=0.3)
pts = [pp(1 + cos(radians(30 * k)), radians(30 * k)) for k in range(7)]
line(ax, pts, 'sujet', lw=1.0)
for k, p in enumerate(pts):
    disc(ax, *p, 0.9 if k != 2 else 1.3, 'varie' if k != 2 else 'resultat')
disc(ax, *c, 0.8, 'encre')
text(ax, 4, 46, 'sept points, un tous les 30°', 'sujet', 's', ha='left')
box(ax, 54, 34, 32, 12, 'varie', label='1. choisir\n$\\theta=60°$', size='s')
box(ax, 54, 18, 32, 12, 'sujet', label='2. calculer\n$r=1+0{,}5=1{,}5$', size='s')
box(ax, 54, 2, 32, 12, 'resultat', label='3. placer le point\nà 1,5 de $O$', size='s')
arrow(ax, (70, 34), (70, 30.5), 'fixe'); arrow(ax, (70, 18), (70, 14.5), 'fixe')
save(fig, '40-017')
