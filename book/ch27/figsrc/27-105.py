import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
fig, ax = canvas(56)
k = 8; A = (5, 12)
E = (A[0] + 2.92 * k * math.cos(math.radians(20)), A[1] + 8); C = (A[0] + 4.55 * k * math.cos(math.radians(12.7)), A[1] + 8)
line(ax, [(A[0], A[1] + 8), (C[0] + 4, A[1] + 8)], 'fixe', dash=True)
line(ax, [A, (C[0] + 4, A[1])], 'fixe')
line(ax, [A, E], 'sujet', lw=1.4); line(ax, [A, C], 'varie', lw=1.4)
arc(ax, A, 13, 0, 20, 'sujet'); arc(ax, A, 20, 0, 12.7, 'varie')
text(ax, 27, 14.5, '20°', 'sujet', 's'); text(ax, 31.5, 9, '12,7°', 'varie', 's')
text(ax, 22, 34, 'de profil', 'fixe', 's'); text(ax, 22, 28, 'même hauteur', 'fixe', 's')
O = (60, 12); T1 = (60, 44); T2 = (60 + 30 * math.cos(math.radians(40)), 12 + 30 * math.sin(math.radians(40)))
line(ax, [O, T1], 'sujet', lw=1.4); line(ax, [O, T2], 'varie', lw=1.4)
arc(ax, O, 11, 40, 90, 'encre')
text(ax, 61, 29, '50°', 'encre', 's', ha='left'); text(ax, 70, 7, 'de dessus', 'fixe', 's')
text(ax, 72, 48, 'plus grande pente', 'sujet', 's'); text(ax, 79, 18, 'chemin', 'varie', 's')
save(fig, '27-105')
