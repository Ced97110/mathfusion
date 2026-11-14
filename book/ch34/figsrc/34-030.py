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
S = 5.0; OX = 22; OY = 13
fig, ax = canvas(82)
P = T(-5, 0); N = T(0, 0); R = T(9, 0); Q = T(0, 12)

u = unit((P[0] - Q[0], P[1] - Q[1]))
H = (Q[0] + u[0] * 7.615 * S, Q[1] + u[1] * 7.615 * S)

poly(ax, [Q, H, R], 'autre')
rt(ax, H, (Q[0] - H[0], Q[1] - H[1]), (R[0] - H[0], R[1] - H[1]), s=2.6)
line(ax, [H, R], 'varie', lw=2.8)
line(ax, [Q, R], 'fixe', lw=1.8)
arcl(ax, Q, 13, aQP, aQR, 'resultat', lw=1.6)
text(ax, Q[0], Q[1] - 18, r'$A + B$', 'resultat', 'm', weight='bold')
text(ax, Q[0], Q[1] + 3.5, r'$Q$', 'encre', 'm')
text(ax, H[0] - 3.5, H[1] - 1, r'$H$', 'autre', 'm')
text(ax, R[0] + 3, R[1] - 1, r'$R$', 'encre', 'm')
text(ax, mid(H, R)[0] - 6, mid(H, R)[1] - 6, r'$RH \approx 12{,}92$', 'varie', 's')
text(ax, mid(Q, R)[0] + 6, mid(Q, R)[1] + 5, r'$p = 15$', 'fixe', 'm')
text(ax, 44, 4, r'$RH = 15 \times 0{,}8615$', 'encre', 's')
save(fig, '34-030')
