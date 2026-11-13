import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(84)
L = 28
V = (10, 46); T = P(V, L, 80); F = (T[0], V[1])
poly(ax, [V, F, T], 'resultat'); line(ax, [V, (V[0] + L, V[1])], 'fixe'); square(ax, F, 180, 90)
arc(ax, V, 9, 0, 80); text(ax, 22, 53, '80°', 'varie', 's')
text(ax, 24, 40, 'angle aigu', 'resultat', 's')
V2 = (58, 46); T2 = P(V2, L, 100); F2 = (T2[0], V2[1])
poly(ax, [V2, F2, T2], 'varie'); line(ax, [V2, (V2[0] + L, V2[1])], 'fixe'); square(ax, F2, 0, 90)
line(ax, [V2, T2], 'varie'); arc(ax, V2, 9, 0, 100, 'encre'); text(ax, 69, 53, '100°', 'encre', 's')
text(ax, 72, 40, 'plus de 90°', 'varie', 's')
box(ax, 5, 24, 78, 8, 'fixe', label='figures : un cas par position', size='s')
box(ax, 5, 4, 38, 8, 'resultat', label='ch. 39 : tous les angles', size='s')
box(ax, 45, 4, 38, 8, 'resultat', label='ch. 41 : tous les angles', size='s')
arrow(ax, (24, 24), (24, 12.8), 'varie'); arrow(ax, (64, 24), (64, 12.8), 'varie')
save(fig, '34-081')
