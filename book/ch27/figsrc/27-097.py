import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
poly(ax, [A, V, O], 'sujet'); poly(ax, [V, C, O], 'autre')
line(ax, [V, O], 'varie', lw=1.3)
square(ax, O, (-1, 0), (0, 1), 2.5)
for p, q in ((A, V), (V, C)):
    m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2); d = (q[0] - p[0], q[1] - p[1]); l = math.hypot(*d)
    n = (-d[1] / l, d[0] / l)
    line(ax, [(m[0] - n[0] * 1.2, m[1] - n[1] * 1.2), (m[0] + n[0] * 1.2, m[1] + n[1] * 1.2)], 'encre', lw=0.9)
arc(ax, V, 10, 239.49, 270, 'sujet'); arc(ax, V, 10, 270, 300.51, 'autre'); arc(ax, V, 15, 239.49, 300.51, 'resultat', lw=1.1)
text(ax, 31, b + 47.5, r'$V$', 'sujet', 'l'); text(ax, 3.5, b - 4, r'$A$', 'sujet', 'l'); text(ax, 58, b - 4, r'$C$', 'autre', 'l'); text(ax, 31, b - 4, r'$O$', 'varie', 'l')
text(ax, 20, b + 14, 'VO', 'varie', 's')
text(ax, 73, 52, 'VA = VC', 'fixe', 's')
text(ax, 73, 42, '30,51°', 'sujet', 'l'); arrow(ax, (73, 38), (73, 32), 'varie'); text(ax, 73, 28, '× 2', 'varie', 'l'); arrow(ax, (73, 24), (73, 18), 'varie'); text(ax, 73, 14, '61,02°', 'resultat', 'l')
save(fig, '27-097')
