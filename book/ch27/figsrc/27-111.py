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
k = 7; ab = 4.44 * k; A = (5, 22); B = (5 + ab, 22); C = (B[0], 22 + k)
poly(ax, [A, B, C], 'sujet'); square(ax, B, (-1, 0), (0, 1), 2.0)
line(ax, [B, C], 'varie', lw=1.6); line(ax, [A, C], 'autre', lw=1.6)
text(ax, B[0] + 3, 22 + k / 2, '1', 'varie', 'm'); text(ax, 20, 33, 'AC ≈ 4,55', 'autre', 's'); text(ax, 13, 25.5, r'$\alpha$', 'resultat', 's')
arc(ax, A, 10, 0, 12.7, 'resultat'); text(ax, 18, 16, 'A', 'sujet', 's'); text(ax, B[0], 16, 'B', 'sujet', 's'); text(ax, C[0] + 1, C[1] + 4, 'C', 'sujet', 's')
box(ax, 44, 44, 42, 13, 'sujet', label=r'$\sin\alpha = \frac{1}{AC}$')
arrow(ax, (65, 44), (65, 35), 'varie'); text(ax, 78, 39.5, 'remplacer', 'varie', 's')
box(ax, 44, 22, 42, 13, 'varie', label=r'$\sin\alpha = \sin\theta \times \cos\varphi$', size='s')
arrow(ax, (65, 22), (65, 13), 'varie'); text(ax, 78, 17.5, 'calculer', 'varie', 's')
box(ax, 44, 0.5, 42, 12.5, 'resultat', label=r'$0{,}3420 \times 0{,}6428 \approx 0{,}2198$', size='s')
save(fig, '27-111')
