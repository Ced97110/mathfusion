import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(84)
s = 13.0; c = (36.0, 50.0)
pp = lambda r, t: (c[0] + s * r * cos(t), c[1] + s * r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
for r in (1, 2):
    line(ax, [pp(r, t) for t in T(-pi, pi, 120)], 'fixe', lw=0.3)
line(ax, [pp(1 + cos(t), t) for t in T(0, 2 * pi, 400)], 'sujet', lw=1.3)
for deg in (0, 60, 90, 180):
    t = radians(deg)
    line(ax, [c, pp(2.15, t)], 'fixe', lw=0.4, dash=True)
    disc(ax, *pp(1 + cos(t), t), 1.1, 'varie')
disc(ax, *c, 0.9, 'encre')
text(ax, 58, 72, 'courbe\n$r=1+\\cos\\theta$', 'sujet', 's', ha='left')
for deg in (0, 60, 90, 180):
    text(ax, *pp(2.4, radians(deg)), str(deg) + '°', 'fixe', 's')
text(ax, c[0] + 2 * s + 1, c[1] + 3.5, '$r=2$', 'varie', 's')
labs = [('0°', '1 + 1 = 2'), ('60°', '1 + 0,5 = 1,5'), ('90°', '1 + 0 = 1'), ('180°', '1 − 1 = 0')]
for i, (a, b) in enumerate(labs):
    box(ax, 3 + i * 21.2, 4, 20, 14, 'varie', label=a + '\n' + b, size='s')
save(fig, '40-016')
