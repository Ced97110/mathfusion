import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
fig, ax = canvas(64)
k = 0.5; y0 = 50; F = (31, y0); S = (31 - 50 * k, y0); Wp = (31 + 100.77 * k, y0); P = (31, y0 + 8.816 * k)
poly(ax, [S, F, P], 'sujet'); poly(ax, [F, Wp, P], 'autre')
line(ax, [F, P], 'varie', lw=2.2)
text(ax, 31, y0 + 8.5, r'$P$', 'varie', 'l'); text(ax, 31, y0 - 4, r'$F$', 'encre', 'm'); text(ax, S[0] - 3, y0 - 3, r'$S$', 'sujet', 'm'); text(ax, Wp[0] + 2, y0 - 3, r'$W$', 'autre', 'm')
text(ax, 34.5, y0 + 2.3, 'PF', 'varie', 's', ha='left')
text(ax, 19, y0 - 3.5, '50 m', 'sujet', 's'); text(ax, S[0] + 10, y0 + 5, '10°', 'sujet', 's'); text(ax, Wp[0] - 10, y0 + 5, '5°', 'autre', 's')
box(ax, 8, 25, 44, 9, 'sujet', label=r'PFS : $PF \approx 8{,}816$ m')
box(ax, 8, 7, 44, 9, 'autre', label=r'PFW : $FW \approx 100{,}77$ m')
arrow(ax, (30, 25), (30, 16), 'varie'); text(ax, 56, 20.5, 'PF réutilisé', 'varie', 's', ha='left')
save(fig, '27-103')
