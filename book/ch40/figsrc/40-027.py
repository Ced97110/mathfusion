import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin
fig, ax = canvas(62)
s = 6.5  # même échelle pour les trois courbes : r = 2 vaut 13 mm
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
cs = [(15, 26), (45, 26), (73, 26)]
fs = [lambda t: 2.0, lambda t: 1 + cos(t), lambda t: cos(3 * t)]
rg = [(0, 2 * pi), (0, 2 * pi), (0, pi)]
labs = ['toujours 2', '1 + cos $\\theta$', 'cos 3$\\theta$']
for c, f, (a, b), lab in zip(cs, fs, rg, labs):
    line(ax, [(c[0] + s * f(t) * cos(t), c[1] + s * f(t) * sin(t)) for t in T(a, b, 400)], 'sujet', lw=1.2)
    disc(ax, *c, 0.8, 'encre')
    text(ax, c[0], 5, '$f$ : ' + lab, 'varie', 's')
box(ax, 24, 48, 40, 10, 'sujet', label='$r=f(\\theta)$', size='l')
for c in cs:
    arrow(ax, (44 + (c[0] - 44) * 0.35, 48), (c[0], 43), 'sujet', lw=0.8)
save(fig, '40-027')
