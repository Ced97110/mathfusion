import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
fig, ax = canvas(52)
k = 5.5; y0 = 28
def tri(A, B, C, role, labs):
    poly(ax, [A, B, C], role); square(ax, B, (-1, 0), (0, 1), 2.0)
tA = (4, y0); tB = (4 + 2.74 * k, y0); tC = (tB[0], y0 + k)
tri(tA, tB, tC, 'fixe', 0)
uA = (33, y0 - 4); uB = (33 + 2.92 * k, y0 - 4); uC = (uB[0], uB[1] + 3.48 * k)
tri(uA, uB, uC, 'fixe', 0)
vA = (60, y0); vB = (60 + 4.44 * k, y0); vC = (vB[0], y0 + k)
tri(vA, vB, vC, 'fixe', 0)
line(ax, [tA, tC], 'varie', lw=1.5); line(ax, [uA, uB], 'varie', lw=1.5); line(ax, [uA, uC], 'autre', lw=1.5); line(ax, [vA, vC], 'autre', lw=1.5)
line(ax, [tB, tC], 'sujet', lw=1.5); line(ax, [vB, vC], 'sujet', lw=1.5)
text(ax, tB[0] + 2.5, y0 + k / 2, '1', 'sujet', 'm'); text(ax, vB[0] + 2.5, y0 + k / 2 + 0.5, '1', 'sujet', 'm')
text(ax, 10, y0 + 6.5, '2,92', 'varie', 's'); text(ax, uA[0] + 7, uA[1] - 3, '2,92', 'varie', 's'); text(ax, 54, y0 + 13, '4,55', 'autre', 's'); text(ax, vA[0] + 9, y0 + 5.5, '4,55', 'autre', 's')
text(ax, 2, y0 + 3.5, '20°', 'sujet', 's', ha='right') if False else None
text(ax, tA[0] + 6, y0 + 2, '20°', 'sujet', 's', ha='left') if False else None
text(ax, 11, y0 - 7, 'ADE : 20°', 'sujet', 's'); text(ax, 41, y0 - 13, 'AEC : 50°', 'autre', 's'); text(ax, 74, y0 - 7, 'ABC : 12,70°', 'resultat', 's')
arrow(ax, (18, 9), (35, 9), 'varie'); text(ax, 26, 13, 'AE', 'varie', 's'); arrow(ax, (47, 9), (65, 9), 'autre'); text(ax, 56, 13, 'AC', 'autre', 's')
save(fig, '27-108')
