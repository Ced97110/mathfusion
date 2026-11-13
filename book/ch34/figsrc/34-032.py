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

fig, ax = canvas(64)
K = 34.0; X0 = 14.0; Y0 = 8.0
cy = lambda v: Y0 + v * K
line(ax, [(X0, cy(0)), (X0, cy(1.5))], 'fixe', lw=0.9)
for v in (0.5, 1, 1.5):
    line(ax, [(X0 - 1.2, cy(v)), (X0 + 1.2, cy(v))], 'fixe', lw=0.8)
    text(ax, X0 - 5.5, cy(v), f'{v:g}'.replace('.', ','), 'limite' if v == 1 else 'fixe', 's')
arcl(ax, (X0, Y0), K, 0, 90, 'fixe', lw=1.0)
line(ax, [(X0, cy(1)), (74, cy(1))], 'limite', lw=1.2)
bx = 60; bw = 9
box(ax, bx, cy(0), bw, 0.5 * K, 'sujet', label=r'$0{,}5$', size='s')
box(ax, bx, cy(0.5), bw, 0.71 * K, 'autre', label=r'$0{,}71$', size='s')
text(ax, bx + bw / 2, cy(1.21) + 3, r'$1{,}21$', 'varie', 'm', weight='bold')
for a, v, role, lab, dx, dy in ((30, 0.5, 'sujet', '30°', 3, -3), (45, 0.7071, 'autre', '45°', 5, 1), (75, 0.9659, 'resultat', '75°', 3, 4.5)):
    px, py = X0 + K * math.cos(math.radians(a)), Y0 + K * math.sin(math.radians(a))
    disc(ax, px, py, 1.4, role)
    text(ax, px + dx + 2, py + dy, lab, role, 's')
line(ax, [(X0 + K * math.cos(math.radians(75)), cy(0.9659)), (bx, cy(0.9659))], 'resultat', lw=0.8, dash=True)
line(ax, [(X0 + K * math.cos(math.radians(30)), cy(0.5)), (bx, cy(0.5))], 'sujet', lw=0.8, dash=True)
text(ax, 46, cy(0.9659) - 3.2, r'$0{,}97$', 'resultat', 's')
text(ax, 38, cy(1) + 3.5, 'ligne 1', 'limite', 's')
save(fig, '34-032')
