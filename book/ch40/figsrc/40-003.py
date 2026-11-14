import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(80)
c = (32, 40); s = 24.0
pp = lambda r, t: (c[0] + r * cos(t), c[1] + r * sin(t))
for k in range(3):
    t = radians(120 * k)
    line(ax, [c, pp(1.18 * s, t)], 'fixe', lw=0.5, dash=True)
line(ax, [pp(s * cos(3 * t), t) for t in [i * pi / 600 for i in range(601)]], 'sujet', lw=1.2)
disc(ax, c[0], c[1], 0.9, 'fixe')
for k in range(3):
    a0 = radians(120 * k)
    line(ax, [pp(0.3 * s, a0 + radians(120) * j / 30) for j in range(31)], 'varie', lw=0.8)
text(ax, 58, 52, '$120^\\circ$', 'varie', 's')
text(ax, 15, 61, '$120^\\circ$', 'varie', 's')
text(ax, 15, 20, '$120^\\circ$', 'varie', 's')
box(ax, 4, 70, 40, 8, 'sujet', label=r'$(x^2+y^2)^2=x^3-3xy^2$', size='s')
box(ax, 50, 70, 34, 8, 'autre', label=r'$r=\cos\,3\theta$', size='m')
text(ax, 66, 8, 'même courbe,\ndeux équations', 'encre', 's')
save(fig, '40-003')
