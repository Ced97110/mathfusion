import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
fig, ax = canvas(50)
o = (33, 22); L = 21; Hh = 22
F = iso(0, 0, 0, o); Sx = iso(-L, 0, 0, o); Wy = iso(0, -L, 0, o); P = iso(0, 0, Hh, o)
poly(ax, [F, Sx, Wy], 'fixe'); poly(ax, [P, F, Sx], 'sujet'); poly(ax, [P, F, Wy], 'autre')
for a, b in ((P, F), (F, Sx), (F, Wy), (P, Sx), (P, Wy), (Sx, Wy)): line(ax, [a, b], 'encre', lw=0.8)
def vec(p, q): return (q[0] - p[0], q[1] - p[1])
def unit(v): l = math.hypot(*v); return (v[0] / l, v[1] / l)
uS, uW, uP = unit(vec(F, Sx)), unit(vec(F, Wy)), unit(vec(F, P))
square(ax, F, uS, uW, 2.0); square(ax, F, uP, uS, 2.0); square(ax, F, uP, uW, 2.0)
text(ax, P[0], P[1] + 3.5, r'$P$', 'sujet', 'l'); text(ax, F[0] + 4.5, F[1] - 4, r'$F$', 'encre', 'l')
text(ax, Sx[0] - 3, Sx[1] - 1, r'$S$', 'sujet', 'l'); text(ax, Wy[0] + 3, Wy[1] - 1, r'$W$', 'autre', 'l')
box(ax, 60, 36, 4, 4, 'sujet', r=0.3); text(ax, 66, 38, 'PFS : vertical', 'sujet', 's', ha='left')
box(ax, 60, 26, 4, 4, 'autre', r=0.3); text(ax, 66, 28, 'PFW : vertical', 'autre', 's', ha='left')
box(ax, 60, 16, 4, 4, 'fixe', r=0.3); text(ax, 66, 18, 'SFW : horizontal', 'fixe', 's', ha='left')
save(fig, '27-102')
