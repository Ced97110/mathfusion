import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(64)
c = (6, 34); s = 36.0
pp = lambda r, t: (c[0] + r * cos(t), c[1] + r * sin(t))
for r in (0.5, 1.0):
    line(ax, [pp(s * r, radians(-40 + 80 * i / 60)) for i in range(61)], 'fixe', lw=0.4)
line(ax, [pp(s * cos(3 * t), t) for t in [radians(-30 + 60 * i / 300) for i in range(301)]], 'sujet', lw=1.3)
# (angle, r, box centre y): each ray is joined to its own box
data = [(30, 0.0, 52), (20, 0.5, 36), (0, 1.0, 20)]
for deg, r, cy in data:
    t = radians(deg)
    tip = pp(s * 1.1, t)
    line(ax, [c, tip], 'fixe', lw=0.5, dash=True)
    line(ax, [tip, (56, cy)], 'fixe', lw=0.5)
    disc(ax, *pp(s * r, t), 1.0, 'resultat')
disc(ax, c[0], c[1], 0.8, 'fixe')
line(ax, [(c[0] + s - 0.7, c[1] - 0.7), (c[0] + s - 4, c[1] - 6)], 'resultat', lw=0.5)
text(ax, c[0] + s - 4.5, c[1] - 8, r'$r=1$', 'resultat', 's', ha='right')
text(ax, 26, 37.5, r'$r=0{,}5$', 'resultat', 's', ha='left')
text(ax, 3, 25, r'$r=0$ en $O$', 'resultat', 's', ha='left')
line(ax, [(c[0], c[1] - 1), (7, 27)], 'resultat', lw=0.5)
rows = [(52, r'$\theta=30^\circ$', r'$\cos 90^\circ=0$'), (36, r'$\theta=20^\circ$', r'$\cos 60^\circ=0{,}5$'),
        (20, r'$\theta=0^\circ$', r'$\cos 0^\circ=1$')]
for cy, a, b in rows:
    box(ax, 56, cy - 5.5, 30, 11, 'fixe', label=a + '\n' + b, size='s')
text(ax, 71, 61, r'$3\theta$, puis $\cos$, puis $r$', 'varie', 's')
save(fig, '40-005')
