import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(62)
k = 7.07; O = (6, 10); A = (6 + 25, 10); V = (6, 35)
poly(ax, [O, A, V], 'sujet'); square(ax, O, (1, 0), (0, 1), 2.5)
line(ax, [V, A], 'resultat', lw=1.6)
arc(ax, A, 8, 135, 180, 'resultat', lw=1.1)
text(ax, 6, 41, r'$V$', 'sujet', 'l'); text(ax, 3, 6, r'$O$', 'sujet', 'l'); text(ax, 34, 6, r'$A$', 'sujet', 'l')
text(ax, 17, 6, 'ℎ = OA', 'varie', 's')
text(ax, 22.5, 30, 'VA = 5', 'resultat', 's')
text(ax, 22, 15, '45°', 'resultat', 's')
P = (46, 14); Q = (81, 14); R = (63.5, 14 + 35 * math.sqrt(3) / 2)
poly(ax, [P, Q, R], 'resultat'); line(ax, [P, Q, R, P], 'resultat', lw=1.6)
text(ax, 63.5, 9, '5', 'resultat', 'm'); text(ax, 51, 31, '5', 'resultat', 'm'); text(ax, 76, 31, '5', 'resultat', 'm')
text(ax, 63.5, 29, 'équilatérale', 'resultat', 's')
save(fig, '27-100')
