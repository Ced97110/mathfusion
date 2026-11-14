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
S = 4.0; OX = 30; OY = 17
fig, ax = canvas(80)
P = T(-5, 0); N = T(0, 0); R = T(9, 0); Q = T(0, 12)

poly(ax, [P, R, Q], 'resultat')
line(ax, [N, Q], 'fixe', lw=0.8, dash=True)
wedge(ax, Q, 9, aQP, aQN, 'sujet')
wedge(ax, Q, 9, aQN, aQR, 'varie')
arcl(ax, Q, 15, aQP, aQR, 'resultat', lw=1.4)
text(ax, polar(Q, 12, (aQP + aQN) / 2)[0] - 2, polar(Q, 12, (aQP + aQN) / 2)[1] - 1, r'$A$', 'sujet', 's', weight='bold')
text(ax, polar(Q, 12, (aQN + aQR) / 2)[0] + 2, polar(Q, 12, (aQN + aQR) / 2)[1] - 1, r'$B$', 'varie', 's', weight='bold')
text(ax, Q[0], Q[1] - 21, r'$A + B$', 'resultat', 'm', weight='bold')
text(ax, Q[0], Q[1] + 3.5, r'$Q$', 'encre', 'm')
text(ax, P[0] - 3, P[1] - 1, r'$P$', 'encre', 'm')
text(ax, R[0] + 3, R[1] - 1, r'$R$', 'encre', 'm')
brace(ax, P[0], R[0], N[1] - 2.5, 'resultat', label=r'$x + y = 14$', size='m')
text(ax, 44, 3.5, r'22,62° + 36,87° = 59,49°', 'resultat', 's')
save(fig, '34-022')
