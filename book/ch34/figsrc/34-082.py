import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(74)
O = (10, 22); R = 38
for a in (0, 30, 60): line(ax, [O, P(O, R, a)], 'fixe')
arc(ax, O, 13, 0, 30, 'sujet'); arc(ax, O, 13, 30, 60, 'autre')
text(ax, *P(O, 18, 15), 'A', 'sujet', 'm'); text(ax, *P(O, 20, 47), 'B = A', 'autre', 's')
arc(ax, O, 28, 0, 60, 'resultat', 1.2); text(ax, *P(O, 33.5, 18), '2A = 60°', 'resultat', 's')
text(ax, 44, 12, r'$\sin 60° = \sin 30° \cos 30° + \cos 30° \sin 30°$'.replace('60° =', '60°=') if False else 'sin 60° = 0,433 + 0,433', 'encre', 's')
box(ax, 22, 2, 44, 6, 'resultat', label='= 0,866', size='s')
save(fig, '34-082')
