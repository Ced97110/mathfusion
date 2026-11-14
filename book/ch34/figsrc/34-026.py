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

fig, ax = canvas(74)
def tri(nx, ny, s, hv, rv):
    Pp = (nx - 5 * s, ny); Nn = (nx, ny); Qq = (nx, ny + 12 * s)
    poly(ax, [Pp, Nn, Qq], 'sujet')
    rt(ax, Nn, (-1, 0), (0, 1), s=1.8)
    line(ax, [Nn, Qq], 'varie', lw=2.4)
    line(ax, [Pp, Qq], 'fixe', lw=1.8)
    wedge(ax, Qq, 5, aQP, aQN, 'sujet')
    text(ax, Nn[0] + 3.5 + (2 if s > 2 else 0), ny + 6 * s, hv, 'varie', 'm')
    text(ax, nx - 2.5 * s - 4.5, ny + 6 * s + 2, rv, 'fixe', 'm')
    text(ax, Qq[0] - 2.5 * s * 0.6 - 1, Qq[1] - 6.5 if s < 2 else Qq[1] - 9, r'$A$', 'sujet', 's')
tri(32, 13, 1.7, r'12', r'13')
tri(74, 13, 3.4, r'24', r'26')
text(ax, 44, 64, r'$12\,/\,13 = 24\,/\,26$', 'resultat', 'l')
save(fig, '34-026')
