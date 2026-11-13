import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(80)
O = (8, 22); R = 50
arc(ax, O, R, 0, 90, 'fixe'); line(ax, [O, (O[0] + R, O[1])], 'fixe')
q = P(O, R, 30); p = P(O, R, 60)
line(ax, [O, q], 'sujet'); line(ax, [O, p], 'resultat')
line(ax, [q, (q[0], O[1])], 'sujet', 1.3); line(ax, [O, (q[0], O[1])], 'autre', 1.6)
line(ax, [p, (p[0], O[1])], 'resultat', 1.6)
arc(ax, O, 12, 0, 30, 'sujet'); text(ax, 24, 25, 'A', 'sujet', 's')
arc(ax, O, 17, 0, 60, 'resultat'); text(ax, 22, 37, '2A', 'resultat', 's')
text(ax, q[0] + 5, 33, '0,5', 'sujet', 's'); text(ax, p[0] - 6, 52, '0,866', 'resultat', 's')
text(ax, 33, 17, 'cos A = 0,866', 'autre', 's')
text(ax, 44, 8, r'$\sin 2A = 2 \sin A \cos A$', 'encre', 'm')
text(ax, 44, 2.5, r'$0{,}866 = 2 \times 0{,}5 \times 0{,}866$', 'resultat', 's')
save(fig, '34-083')
