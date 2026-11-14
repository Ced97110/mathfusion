import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
fig, ax = canvas(62)
k = 9; A = (5, 22); D = (5 + 2.74 * k, 22); E = (D[0], 22 + k)
poly(ax, [A, D, E], 'sujet'); square(ax, D, (-1, 0), (0, 1), 2.2)
line(ax, [D, E], 'varie', lw=1.6)
arc(ax, A, 10, 0, 20, 'resultat')
text(ax, D[0] + 3, 22 + k / 2, '1', 'varie', 'm'); text(ax, 15, 33, 'AE', 'sujet', 'm'); text(ax, 17, 24.5, r'$\theta$', 'resultat', 's')
text(ax, 11, 16, 'A', 'sujet', 's'); text(ax, D[0], 16, 'D', 'sujet', 's'); text(ax, E[0] + 1, E[1] + 4, 'E', 'sujet', 's')
box(ax, 44, 44, 40, 13, 'sujet', label=r'$\sin\theta = \frac{1}{AE}$')
arrow(ax, (64, 44), (64, 35), 'varie'); text(ax, 76, 39.5, 'échanger', 'varie', 's')
box(ax, 44, 22, 40, 13, 'varie', label=r'$AE = \frac{1}{\sin\theta}$')
arrow(ax, (64, 22), (64, 13), 'varie'); text(ax, 76, 17.5, 'calculer', 'varie', 's')
box(ax, 44, 0.5, 40, 12.5, 'resultat', label=r'$\approx 1 / 0{,}3420 \approx 2{,}92$', size='s')
save(fig, '27-109')
