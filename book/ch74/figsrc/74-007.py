import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def ngon(c, ang0, n, s):
    ext = 360 / n; pts = [c]; p = c; d = ang0
    for _ in range(n - 1):
        p = (p[0] + s * math.cos(math.radians(d)), p[1] + s * math.sin(math.radians(d))); pts.append(p); d += ext
    return pts
def around(ax, c, n, s, copies, alpha, role):
    for k in range(copies): poly(ax, ngon(c, k * alpha, n, s), role)
fig, ax = canvas(60)
c = (28, 30)
around(ax, c, 3, 22, 6, 60, 'sujet')
a0 = [(c[0] + 7 * math.cos(math.radians(t)), c[1] + 7 * math.sin(math.radians(t))) for t in range(0, 61, 5)]
line(ax, a0, 'varie', lw=1.1)
text(ax, c[0] + 12, c[1] + 4, '60°', 'varie', 's')
text(ax, 68, 44, '360 ÷ 60 = 6', 'resultat', 'l')
text(ax, 68, 36, 'nombre entier', 'resultat', 's')
text(ax, 68, 22, '6 triangles', 'sujet', 'm'); text(ax, 68, 16, 'remplissent le tour', 'sujet', 's')
save(fig, '74-007')
