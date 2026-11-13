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

fig, ax = canvas(84)
def case(y, a, b, ra, rb, role_s, sumtxt):
    f = numberline(ax, 8, 74, y, 0, 120, step=30, arrow_right=True)
    box(ax, f(0), y + 1.6, f(90) - f(0), 4.2, 'resultat', label=None)
    for v, lab, role in ((a, r'$A$', 'sujet'), (b, r'$B$', 'varie'), (a + b, r'$A + B$', role_s)):
        disc(ax, f(v), y, 1.5, role)
        text(ax, f(v), y + 10.5 if lab != r'$A + B$' else y + 15, lab, role, 'm')
        line(ax, [(f(v), y + 1.5), (f(v), y + (9 if lab != r'$A + B$' else 13.5))], role, lw=0.6)
    text(ax, 44, y - 11, sumtxt, role_s, 's')
case(58, 22.62, 36.87, 0, 0, 'resultat', r'22,62° + 36,87° = 59,49°  < 90°')
case(22, 60, 45, 0, 0, 'limite', r'60° + 45° = 105°  > 90°')
text(ax, 26, 81, 'zone des angles aigus (< 90°)', 'resultat', 's')
save(fig, '34-024')
