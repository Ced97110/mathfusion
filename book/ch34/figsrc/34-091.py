import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(84)
fig, ax = canvas(100)
R = 17; O = (26, 72)
K = (O[0] - R, O[1]); Pp = P(O, R, 60); F = (Pp[0], O[1])
arc(ax, O, R, 0, 180, 'fixe'); line(ax, [K, (O[0] + R, O[1])], 'fixe'); line(ax, [Pp, F], 'fixe')
line(ax, [O, Pp], 'fixe'); poly(ax, [K, F, Pp], 'sujet')
for t, p, d in (('K', K, (-3, -3)), ('O', O, (0, -3.5)), ('F', F, (2, -3.5)), ('P', Pp, (3, 3))):
    text(ax, p[0] + d[0], p[1] + d[1], t, 'encre', 's')
text(ax, 66, 82, 'départ', 'sujet', 's'); text(ax, 66, 77, 'demi-cercle', 'sujet', 's')
box(ax, 6, 40, 76, 11, 'varie', label=r'étape clé : $KP = 2\cos A$', size='s')
arrow(ax, (44, 63), (44, 52.2), 'varie')
box(ax, 6, 14, 76, 9, 'resultat', label=r'$\sin 2A = 2\sin A\cos A$', size='s')
box(ax, 6, 2, 76, 9, 'resultat', label=r'$\cos 2A = 2\cos^2 A - 1$', size='s')
text(ax, 44, 30, 'arrivée', 'resultat', 's')
arrow(ax, (44, 39), (44, 33), 'varie')
save(fig, '34-091')
