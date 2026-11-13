import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(84)
fig, ax = canvas(64)
R = 34; O = (40, 12)
K = (O[0] - R, O[1]); Pp = P(O, R, 60); M = ((K[0] + Pp[0]) / 2, (K[1] + Pp[1]) / 2)
arc(ax, O, R, 0, 180, 'fixe'); line(ax, [K, (O[0] + R, O[1])], 'fixe'); line(ax, [O, Pp], 'fixe')
line(ax, [O, M], 'fixe', dash=True); square(ax, M, 120 + 180 - 180 + 0, -30, 2.4) if False else None
line(ax, [K, Pp], 'sujet', 1.4); line(ax, [K, M], 'resultat', 2.4)
arc(ax, K, 12, 0, 30, 'varie'); text(ax, K[0] + 17, K[1] + 3, 'A', 'varie', 's')
text(ax, K[0] - 1, K[1] - 4, 'K', 'encre', 's'); text(ax, O[0] + 1, O[1] - 4, 'O', 'encre', 's')
text(ax, Pp[0] + 3, Pp[1] + 3, 'P', 'encre', 's'); text(ax, M[0] - 3, M[1] + 3.5, 'M', 'encre', 's')
text(ax, 23, 8, '1', 'encre', 's')
text(ax, 24, 53, r'$KM = \cos A = 0{,}866$', 'resultat', 's')
text(ax, 60, 24, r'$KP = 1{,}732$', 'sujet', 's')
save(fig, '34-095')
