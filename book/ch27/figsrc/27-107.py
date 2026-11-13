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
s = 3.0; ab = 4.44 * s
A1 = (6, 50); B1 = (6 + ab, 50); C1 = (6 + ab, 50 + s)
poly(ax, [A1, B1, C1], 'sujet')
A2 = (6, 10); B2 = (6 + 3 * ab, 10); C2 = (6 + 3 * ab, 10 + 3 * s)
poly(ax, [A2, B2, C2], 'autre')
square(ax, B1, (-1, 0), (0, 1), 1.6); square(ax, B2, (-1, 0), (0, 1), 2.5)
text(ax, C1[0] + 2, 50 + s / 2, 'hauteur 1', 'sujet', 's', ha='left'); text(ax, 20, 56, 'AC ≈ 4,55', 'sujet', 's')
text(ax, C2[0] + 2, 10 + 1.5 * s, 'hauteur 3', 'autre', 's', ha='left'); text(ax, 22, 19, 'AC ≈ 13,65', 'autre', 's')
text(ax, 66, 54, '0,2198', 'sujet', 'l'); text(ax, 66, 8, '0,2198', 'autre', 'l')
arrow(ax, (66, 48), (66, 36), 'varie'); text(ax, 74, 42, '× 3', 'varie', 'm')
text(ax, 66, 24, 'même angle', 'resultat', 's')
text(ax, 12, 46, r'$\alpha$', 'sujet', 's'); text(ax, 12, 6, r'$\alpha$', 'autre', 's')
save(fig, '27-107')
