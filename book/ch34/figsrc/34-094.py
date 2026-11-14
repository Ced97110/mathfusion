import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(84)
fig, ax = canvas(66)
s = 10; M = (44, 10); K = (M[0] - 3 * s, 10); Pp = (M[0] + 3 * s, 10); Ot = (44, 10 + 4 * s)
poly(ax, [K, M, Ot], 'sujet'); poly(ax, [M, Pp, Ot], 'autre')
line(ax, [Ot, M], 'fixe', dash=True); square(ax, M, 180, 90, 2.4); square(ax, M, 0, 90, 2.4)
arc(ax, K, 11, 0, 53.13, 'resultat', 1.2); arc(ax, Pp, 11, 126.87, 180, 'resultat', 1.2)
text(ax, K[0] + 15.5, 17.5, 'égal', 'resultat', 's'); text(ax, Pp[0] - 15.5, 17.5, 'égal', 'resultat', 's')
text(ax, 25, 36, '5', 'sujet', 's'); text(ax, 63, 36, '5', 'autre', 's')
text(ax, 29, 5, '3', 'sujet', 's'); text(ax, 59, 5, '3', 'autre', 's'); text(ax, 47, 28, '4', 'fixe', 's')
text(ax, K[0] - 2, K[1] + 3, 'K', 'encre', 's'); text(ax, Pp[0] + 2, Pp[1] + 3, 'P', 'encre', 's')
text(ax, Ot[0], Ot[1] + 4, 'O', 'encre', 's'); text(ax, M[0] + 3, M[1] - 3.5, 'M', 'encre', 's')
save(fig, '34-094')
