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
fig, ax = canvas(78)
P = T(-5, 0); N = T(0, 0); R = T(9, 0); Q = T(0, 12)

u = unit((P[0] - Q[0], P[1] - Q[1]))
t = 7.615 * S
H = (Q[0] + u[0] * t, Q[1] + u[1] * t)
poly(ax, [P, R, Q], 'fixe', fill=False)
poly(ax, [Q, H, R], 'autre')
line(ax, [N, Q], 'fixe', lw=0.7, dash=True)
line(ax, [H, R], 'encre', lw=1.6, dash=True)
rt(ax, H, (Q[0] - H[0], Q[1] - H[1]), (R[0] - H[0], R[1] - H[1]))
text(ax, H[0] - 3.5, H[1] - 1.5, r'$H$', 'autre', 'l', weight='bold')
text(ax, P[0] - 3, P[1] - 1, r'$P$', 'fixe', 'm')
text(ax, N[0] + 1.5, N[1] - 3.2, r'$N$', 'fixe', 's')
text(ax, R[0] + 3, R[1] - 1, r'$R$', 'encre', 'm')
text(ax, Q[0], Q[1] + 3.5, r'$Q$', 'encre', 'm')
text(ax, mid(Q, H)[0] - 8, mid(Q, H)[1] + 2, r'$QH \approx 7{,}62$', 'autre', 's')
text(ax, mid(H, R)[0] + 6, mid(H, R)[1] - 5.5, r'$RH \approx 12{,}92$', 'encre', 's')
save(fig, '34-023')
