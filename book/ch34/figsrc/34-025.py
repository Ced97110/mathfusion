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
S = 4.0; OX = 22; OY = 13
fig, ax = canvas(74)
P = T(-5, 0); N = T(0, 0); R = T(9, 0); Q = T(0, 12)

poly(ax, [P, N, Q], 'sujet')
rt(ax, N, (-1, 0), (0, 1))
wedge(ax, Q, 11, aQP, aQN, 'sujet')
line(ax, [P, N], 'varie', lw=2.6)
line(ax, [P, Q], 'fixe', lw=2.0)
text(ax, polar(Q, 16, (aQP + aQN) / 2)[0] - 1, polar(Q, 16, (aQP + aQN) / 2)[1], r'$A$', 'sujet', 'l', weight='bold')
text(ax, Q[0], Q[1] + 3.5, r'$Q$', 'encre', 'm')
text(ax, mid(P, N)[0], N[1] - 3.5, r'$x = 5$', 'varie', 'm')
text(ax, mid(P, Q)[0] - 6, mid(P, Q)[1] + 4, r'$r = 13$', 'fixe', 'm')
text(ax, 64, 54, r'$\sin A = x\,/\,r$', 'encre', 'm')
text(ax, 64, 42, r'$= 5\,/\,13$', 'resultat', 'l')
text(ax, 64, 31, r'$\approx 0{,}3846$', 'resultat', 'm')
save(fig, '34-025')
