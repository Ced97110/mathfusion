import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin
fig, ax = canvas(84)
c = (36, 42); per = 7.0; a = per / (2 * pi)
g = lambda t: a * t * cos(t)
N = 700; T = [i * 8 * pi / N for i in range(N + 1)]
line(ax, [(c[0] + g(t), c[1] + a * t * sin(t)) for t in T], 'sujet', lw=1.1)
disc(ax, c[0], c[1], 0.9, 'fixe')
X = 11.0  # abscisse de la verticale (mm depuis le centre)
line(ax, [(c[0] + X, 6), (c[0] + X, 80)], 'varie', lw=1.0, dash=True)
hits = []
for i in range(N):
    u, v = g(T[i]) - X, g(T[i + 1]) - X
    if u == 0 or u * v < 0:
        lo, hi = T[i], T[i + 1]
        for _ in range(40):
            m = (lo + hi) / 2
            if (g(lo) - X) * (g(m) - X) <= 0: hi = m
            else: lo = m
        hits.append(lo)
for t in hits:
    disc(ax, c[0] + X, c[1] + a * t * sin(t), 1.1, 'varie')
n = len(hits)
text(ax, 72, 70, 'même x', 'varie', 's')
arrow(ax, (63, 70), (c[0] + X + 1.5, 70), 'varie')
text(ax, 72, 46, f'{n} points\npour ce x', 'varie', 'm')
text(ax, 72, 28, '$y=f(x)$ :\n1 seul y\npar x', 'fixe', 's')
save(fig, '40-002')
