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
R = 34; O = (44, 14)
K = (O[0] - R, O[1]); Pp = P(O, R, 60); F = (Pp[0], O[1])
arc(ax, O, R, 0, 180, 'fixe'); line(ax, [K, (O[0] + R, O[1])], 'fixe')
disc(ax, K[0], K[1], 1.3, 'sujet'); disc(ax, Pp[0], Pp[1], 1.3, 'varie'); disc(ax, F[0], F[1], 1.3, 'resultat')
line(ax, [O, Pp], 'varie'); line(ax, [Pp, F], 'autre', 2.0, dash=True); line(ax, [O, F], 'resultat', 2.0)
arc(ax, O, 9, 0, 60, 'varie'); text(ax, O[0] + 14, O[1] + 6, '2A', 'varie', 's')
text(ax, K[0] + 2, K[1] - 4, 'K : −1', 'sujet', 's')
text(ax, O[0] - 3, O[1] - 4, 'O', 'encre', 's'); text(ax, F[0] + 1, F[1] - 4, 'F', 'resultat', 's')
text(ax, Pp[0] + 3, Pp[1] + 3, 'P', 'varie', 's')
text(ax, 22, 52, 'P : sur le cercle', 'varie', 's')
text(ax, 65, 24, r'$FP = \sin 2A$', 'autre', 's', rot=90)
text(ax, 64, 4, r'$OF = \cos 2A$', 'resultat', 's')
save(fig, '34-092')
