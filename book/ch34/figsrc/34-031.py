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

fig, ax = canvas(80)
S = 2.4; OX = 30; OY = 66
Q = (OX, OY); R = (OX + 9 * S, OY - 12 * S)
u = unit((-5, -12))
def tri(k, role, lw, rv, hv, fill):
    Hh = (Q[0] + u[0] * 7.615 * S * k, Q[1] + u[1] * 7.615 * S * k)
    Rr = (Q[0] + 9 * S * k, Q[1] - 12 * S * k)
    poly(ax, [Q, Hh, Rr], role, fill=fill)
    rt(ax, Hh, (Q[0] - Hh[0], Q[1] - Hh[1]), (Rr[0] - Hh[0], Rr[1] - Hh[1]), s=2.0)
    line(ax, [Q, Hh], 'varie', lw=lw)
    return Hh, Rr
H1, R1 = tri(1, 'autre', 2.6, 0, 0, True)
H2, R2 = tri(2, 'fixe', 1.8, 0, 0, False)
arcl(ax, Q, 8, aQP, aQR, 'resultat', lw=1.6)
text(ax, Q[0], Q[1] + 3.5, r'$Q$', 'encre', 'm')
text(ax, mid(Q, H1)[0] - 6.5, mid(Q, H1)[1] + 1, r'$7{,}62$', 'varie', 's')
text(ax, mid(Q, H2)[0] - 6.5, mid(Q, H2)[1] + 1, r'$15{,}23$', 'varie', 's')
text(ax, mid(Q, R1)[0] + 6, mid(Q, R1)[1] + 4, r'$15$', 'autre', 's')
text(ax, mid(Q, R2)[0] + 6, mid(Q, R2)[1] + 4, r'$30$', 'fixe', 's')
text(ax, Q[0] + 2, Q[1] - 13, r'$A + B$', 'resultat', 's')
text(ax, 30, 13, r'$QH\,/\,p \approx 0{,}5077$', 'resultat', 's')
text(ax, 30, 6, 'dans les deux triangles', 'resultat', 's')
save(fig, '34-031')
