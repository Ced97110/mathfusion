import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
fig, ax = canvas(60)
F = (58, 40); S = (58, 17.5); Wp = (12.7, 40)
poly(ax, [F, S, Wp], 'fixe'); line(ax, [S, Wp], 'resultat', lw=1.8)
square(ax, F, (0, -1), (-1, 0), 2.5)
disc(ax, F[0], F[1], 1.8, 'sujet'); disc(ax, S[0], S[1], 1.5, 'varie'); disc(ax, Wp[0], Wp[1], 1.5, 'varie')
text(ax, 66, 44, 'pied F', 'sujet', 's'); text(ax, 58, 11, r'$S$', 'varie', 'l'); text(ax, 9, 44, r'$W$', 'varie', 'l')
text(ax, 66, 29, '50 m', 'fixe', 'm')
text(ax, 72, 14, 'P vu à 10°', 'varie', 's'); text(ax, 30, 47, 'P vu à 5°', 'varie', 's')
text(ax, 25, 21, r'$SW \approx 112$ m', 'resultat', 'm')
text(ax, 58, 51, 'nord', 'fixe', 's'); text(ax, 58, 55, '', 'fixe', 's')
arrow(ax, (58, 46), (58, 49), 'fixe')
save(fig, '27-101')
