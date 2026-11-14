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
R = 40; O = (44, 8)
K = (O[0] - R, O[1]); Pp = P(O, R, 60)
poly(ax, [O, K, Pp], 'sujet')
def tick(a, b, role='encre'):
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2); dx, dy = b[0] - a[0], b[1] - a[1]; n = math.hypot(dx, dy)
    nx, ny = -dy / n * 1.6, dx / n * 1.6; line(ax, [(m[0] - nx, m[1] - ny), (m[0] + nx, m[1] + ny)], role, 1.0)
tick(O, K); tick(O, Pp)
text(ax, 24, 3, '1', 'encre', 's'); text(ax, 58, 28, '1', 'encre', 's')
arc(ax, O, 10, 60, 180, 'varie'); text(ax, 36, 22, '120°', 'varie', 's')
arc(ax, K, 12, 0, 30, 'resultat'); text(ax, K[0] + 18, K[1] + 3.2, '30° = A', 'resultat', 's')
arc(ax, Pp, 10, 210, 240, 'resultat'); text(ax, Pp[0] + 7, Pp[1] - 4, '30°', 'resultat', 's')
text(ax, K[0] - 1, K[1] - 4, 'K', 'encre', 's'); text(ax, O[0] + 1, O[1] - 4, 'O', 'encre', 's'); text(ax, Pp[0] + 3, Pp[1] + 3, 'P', 'encre', 's')
text(ax, 62, 10, 'deux côtés égaux', 'sujet', 's', ha='left') if False else None
save(fig, '34-093')
