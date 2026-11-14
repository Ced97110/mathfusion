import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(84)
fig, ax = canvas(50)
u = 36; M = (44, 8); K = (M[0] - 0.866 * u, 8); Pp = (M[0] + 0.866 * u, 8); O = (44, 8 + 0.5 * u)
poly(ax, [K, Pp, O], 'sujet')
line(ax, [O, M], 'resultat', 1.6); square(ax, M, 180, 90, 3.0, 'resultat'); square(ax, M, 0, 90, 3.0, 'resultat')
def tick(a, b, n=1):
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2); dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy)
    nx, ny = -dy / L * 1.6, dx / L * 1.6
    for k in range(n):
        o = (k - (n - 1) / 2) * 1.8; c = (m[0] + dx / L * o, m[1] + dy / L * o)
        line(ax, [(c[0] - nx, c[1] - ny), (c[0] + nx, c[1] + ny)], 'encre', 1.0)
tick(O, K, 1); tick(O, Pp, 1); tick(K, M, 2); tick(M, Pp, 2)
text(ax, 26, 28, 'OK = 1', 'sujet', 's'); text(ax, 62, 28, 'OP = 1', 'sujet', 's')
text(ax, 50, 17, '90°', 'resultat', 's', ha='left')
text(ax, 28, 4, 'KM', 'encre', 's') if False else None
text(ax, K[0] - 3, K[1] - 1, 'K', 'encre', 's'); text(ax, Pp[0] + 3, Pp[1] - 1, 'P', 'encre', 's')
text(ax, O[0], O[1] + 4, 'O', 'encre', 's'); text(ax, M[0] + 3, M[1] - 4, 'M', 'encre', 's')
text(ax, 44, 45, 'KM = MP : milieu de la base', 'encre', 's') if False else None
save(fig, '34-096')
