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
S = 4.0; OX = 30; OY = 15
fig, ax = canvas(80)
P = T(-5, 0); N = T(0, 0); R = T(9, 0); Q = T(0, 12)

poly(ax, [P, N, Q], 'sujet')
poly(ax, [N, R, Q], 'varie')
rt(ax, N, (-1, 0), (0, 1))
rt(ax, N, (1, 0), (0, 1))
text(ax, P[0] - 3, P[1] - 1, r'$P$', 'sujet', 'm')
text(ax, N[0], N[1] - 3.5, r'$N$', 'encre', 'm')
text(ax, R[0] + 3, R[1] - 1, r'$R$', 'varie', 'm')
text(ax, Q[0], Q[1] + 3.5, r'$Q$', 'encre', 'm')
text(ax, T(-2.2, 2.2)[0], T(-2.2, 2.2)[1], 'PNQ', 'sujet', 's')
text(ax, T(4.0, 2.4)[0], T(4.0, 2.4)[1], 'triangle RNQ', 'varie', 's', weight='bold')
text(ax, T(-2.5, 0.9)[0], T(-2.5, 0.9)[1], '5', 'sujet', 's')
text(ax, T(-3.3, 7.0)[0], T(-3.3, 7.0)[1], '13', 'sujet', 's')
text(ax, T(4.0, 0.9)[0], T(4.0, 0.9)[1], '9', 'varie', 's')
text(ax, T(5.7, 7.0)[0], T(5.7, 7.0)[1], '15', 'varie', 's')
text(ax, T(0.9, 6.0)[0], T(0.9, 6.0)[1], '12', 'encre', 's')
brace(ax, P[0], R[0], P[1] - 5, 'fixe', label='grand triangle $PQR$')
save(fig, '34-018')
