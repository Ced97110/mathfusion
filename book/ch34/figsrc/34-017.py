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
S = 4.0; OX = 30; OY = 13
fig, ax = canvas(76)
P = T(-5, 0); N = T(0, 0); R = T(9, 0); Q = T(0, 12)

poly(ax, [P, N, Q], 'sujet')
rt(ax, N, (-1, 0), (0, 1))
line(ax, [P, N], 'varie', lw=2.4)
line(ax, [N, Q], 'fixe', lw=1.4)
text(ax, P[0] - 3, P[1] - 1, r'$P$', 'sujet', 'm')
text(ax, N[0] + 3, N[1] - 1, r'$N$', 'sujet', 'm')
text(ax, Q[0], Q[1] + 3.5, r'$Q$', 'sujet', 'm')
text(ax, mid(P, N)[0], P[1] - 5, r'$x$', 'varie', 'l', weight='bold')
text(ax, N[0] + 3.5, mid(N, Q)[1], r'$h$', 'fixe', 'm')
text(ax, 60, 56, r'$x = 5$ ici', 'varie', 'm')
text(ax, 60, 46, r'$x = 3$ ou $7$', 'varie', 'm')
text(ax, 60, 36, 'ailleurs', 'varie', 'm')
text(ax, 44, 5, r'$x$ est la longueur de $PN$', 'encre', 's')
save(fig, '34-017')
