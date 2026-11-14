import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def T(a, b): return (OX + a * S, OY + b * S)
def unit(v):
    n = math.hypot(*v); return (v[0] / n, v[1] / n)
def rt(ax, at, d1, d2, s=2.4, role='fixe'):
    u, v = unit(d1), unit(d2)
    line(ax, [(at[0] + s * u[0], at[1] + s * u[1]), (at[0] + s * (u[0] + v[0]), at[1] + s * (u[1] + v[1])), (at[0] + s * v[0], at[1] + s * v[1])], role, lw=0.7)
def arcpts(c, r, a0, a1, n=24):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
def wedge(ax, c, r, a0, a1, role):
    poly(ax, [c] + arcpts(c, r, a0, a1), role)
def arcl(ax, c, r, a0, a1, role, lw=1.0):
    line(ax, arcpts(c, r, a0, a1), role, lw=lw)
def polar(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def mid(p, q, t=0.5): return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
aA = math.degrees(math.atan2(5, 12)); aB = math.degrees(math.atan2(9, 12))
aQN = 270.0; aQP = aQN - aA; aQR = aQN + aB
S = 4.0; OX = 30; OY = 19
fig, ax = canvas(78)
P = T(-5, 0); N = T(0, 0); R = T(9, 0); Q = T(0, 12)

poly(ax, [P, N, Q], 'sujet')
poly(ax, [N, R, Q], 'varie')
rt(ax, N, (-1, 0), (0, 1))
rt(ax, N, (1, 0), (0, 1))
line(ax, [N, Q], 'resultat', lw=3.0)
text(ax, N[0] + 7, mid(N, Q)[1], r'$h = 12$', 'resultat', 'm', weight='bold')
text(ax, Q[0], Q[1] + 3.5, r'$Q$', 'encre', 'm')
text(ax, T(-2.6, 5)[0] - 1, T(-2.6, 5)[1], r'$r = 13$', 'sujet', 's')
text(ax, T(5, 6)[0] + 4, T(5, 6)[1] + 2, r'$p = 15$', 'varie', 's')
text(ax, 20, 9, r'$13 \times 12/13 = 12$', 'sujet', 's')
text(ax, 68, 9, r'$15 \times 4/5 = 12$', 'varie', 's')
text(ax, 44, 2.5, r'$r\,\cos A = p\,\cos B$', 'resultat', 'm')
save(fig, '34-029')
