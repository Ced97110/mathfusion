import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(74)
R = 34; O = (44, 24)
K = (O[0] - R, O[1]); Pp = P(O, R, 60); F = (Pp[0], O[1])
arc(ax, O, R, 0, 180, 'fixe'); line(ax, [K, (O[0] + R, O[1])], 'fixe')
line(ax, [O, Pp], 'fixe'); line(ax, [Pp, F], 'fixe')
line(ax, [K, F], 'resultat', 2.0); line(ax, [K, Pp], 'sujet', 1.4)
square(ax, F, 180, 90, 2.0)
arc(ax, K, 11, 0, 30, 'varie'); text(ax, K[0] + 15, K[1] + 3, 'A', 'varie', 's')
arc(ax, O, 8, 0, 60, 'varie'); text(ax, O[0] + 13, O[1] + 5, '2A', 'varie', 's')
text(ax, K[0] - 1, K[1] + 3.5, 'K', 'encre', 's'); text(ax, O[0] - 3, O[1] + 3, 'O', 'encre', 's')
text(ax, F[0] + 1.5, F[1] - 3.5, 'F', 'encre', 's'); text(ax, Pp[0] + 3, Pp[1] + 3, 'P', 'encre', 's')
text(ax, 24, 64, r'$KP = 2\cos A = 1{,}732$', 'sujet', 's')
brace(ax, K[0], O[0], O[1] - 1.5, 'resultat', label=r'$KO = 1$')
brace(ax, O[0], F[0], O[1] - 1.5, 'resultat', label=r'$\cos 2A$')
text(ax, 38, 9, r'$KF = 1 + \cos 2A = 1{,}5$', 'resultat', 's')
text(ax, 38, 3.5, r'$= 2\cos^2 A$', 'resultat', 's')
save(fig, '34-090')
