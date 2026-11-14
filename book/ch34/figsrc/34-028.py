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
S = 4.5; OX = 16; OY = 13
fig, ax = canvas(76)
P = T(-5, 0); N = T(0, 0); R = T(9, 0); Q = T(0, 12)

poly(ax, [N, R, Q], 'varie')
n2 = T(0, 8); r2 = T(3, 8)
poly(ax, [n2, r2, Q], 'autre')
rt(ax, N, (1, 0), (0, 1))
rt(ax, n2, (1, 0), (0, 1), s=1.6)
wedge(ax, Q, 12, aQN, aQR, 'varie')
line(ax, [N, Q], 'fixe', lw=2.0)
line(ax, [Q, R], 'varie', lw=1.8)
text(ax, polar(Q, 17, (aQN + aQR) / 2)[0] + 0.5, polar(Q, 17, (aQN + aQR) / 2)[1], r'$B$', 'varie', 'l', weight='bold')
text(ax, Q[0], Q[1] + 3.5, r'$Q$', 'encre', 'm')
text(ax, N[0] - 4, mid(N, Q)[1] - 12, r'$12$', 'fixe', 'm')
text(ax, mid(Q, R)[0] + 7, mid(Q, R)[1] + 3, r'$15$', 'varie', 'm')
text(ax, N[0] - 4, mid(n2, Q)[1] + 1, r'$4$', 'autre', 'm')
text(ax, mid(Q, r2)[0] + 4.5, mid(Q, r2)[1] + 4.5, r'$5$', 'autre', 'm')
text(ax, 70, 52, r'$\cos B = h\,/\,p$', 'encre', 's')
text(ax, 70, 43, r'$12\,/\,15$', 'varie', 'm')
text(ax, 70, 35, r'$4\,/\,5$', 'autre', 'm')
text(ax, 70, 27, 'même angle', 'resultat', 's')
save(fig, '34-028')
