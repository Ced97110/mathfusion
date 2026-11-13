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
k = 8; A = (8, 14)
E1 = (A[0] + 2.92 * k, 14); C1 = (E1[0], 14 + 3.48 * k); E2 = (A[0] + 2 * k, 14); C2 = (E2[0], 14 + 2 * math.tan(math.radians(50)) * k)
poly(ax, [A, E1, C1], 'sujet'); poly(ax, [A, E2, C2], 'autre')
line(ax, [A, E1, C1, A], 'sujet', lw=1.1); line(ax, [A, E2, C2, A], 'autre', lw=1.1)
square(ax, E1, (-1, 0), (0, 1), 2.2)
arc(ax, A, 9, 0, 50, 'encre')
text(ax, 20, 19, r'$\varphi = 50°$', 'encre', 's')
text(ax, 15, 10, 'AE = 2', 'autre', 's'); text(ax, 21, 5, 'AE = 2,92', 'sujet', 's')
text(ax, C1[0] + 1, C1[1] + 4, 'AC ≈ 4,55', 'sujet', 's', ha='right'); text(ax, C2[0] - 2, C2[1] + 4, 'AC ≈ 3,11', 'autre', 's', ha='right')
box(ax, 44, 33, 42, 9, 'sujet', label=r'$\theta=20°$ : 4,55 / 2,92', size='s')
box(ax, 44, 20, 42, 9, 'autre', label=r'$\theta=30°$ : 3,11 / 2', size='s')
arrow(ax, (65, 33), (65, 29.8), 'varie'); arrow(ax, (65, 20), (65, 15.5), 'varie')
box(ax, 44, 5, 42, 10, 'resultat', label=r'même rapport ≈ 1,56', size='s')
save(fig, '27-110')
