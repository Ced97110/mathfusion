import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def vec(ax, o, v, u, role, lw=1.3):
    arrow(ax, o, (o[0] + u * v[0], o[1] + u * v[1]), role, lw)
def para(ax, o, x, y, u, role='fixe'):
    p = lambda a, b: (o[0] + u * (a[0] * 1 + b[0]), o[1] + u * (a[1] + b[1]))
    poly(ax, [o, (o[0] + u * x[0], o[1] + u * x[1]), (o[0] + u * (x[0] + y[0]), o[1] + u * (x[1] + y[1])), (o[0] + u * y[0], o[1] + u * y[1])], role)
def arc(ax, o, r, a0, a1, role='varie', n=30):
    pts = [(o[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), o[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:n - 2], role, lw=1.0); arrow(ax, pts[n - 3], pts[n], role, lw=1.0)
fig, ax = canvas(46)
u = 5
o = (3, 14)
y = (6, 3)
para(ax, o, (1, 0), y, u, 'varie')
vec(ax, o, (1, 0), u, 'sujet', lw=1.6); vec(ax, o, y, u, 'varie', lw=1.6)
text(ax, o[0] + 2.5, o[1] - 3, '$e_1$', 'sujet', 'm')
text(ax, o[0] + 6 * u - 4, o[1] + 3 * u + 3.5, '$y$', 'varie', 'm')
text(ax, 21, 36, 'essai : aire $k=3$', 'varie', 's')
text(ax, 21, 5, '$B(e_1,\\ y)=3$', 'varie', 'm')
o2 = (62, 14)
f = (2, 1)
para(ax, o2, (1, 0), f, u, 'resultat')
vec(ax, o2, (1, 0), u, 'sujet', lw=1.6); vec(ax, o2, f, u, 'resultat', lw=1.6)
text(ax, o2[0] + 2.5, o2[1] - 3, '$e_1$', 'sujet', 'm')
text(ax, o2[0] + 2 * u - 2, o2[1] + u + 3.5, '$f_1$', 'resultat', 'm')
text(ax, 72, 28, 'aire 1', 'resultat', 's')
text(ax, 72, 5, '$B(e_1,\\ f_1)=1$', 'resultat', 'm')
arrow(ax, (42, 26), (55, 26), 'varie', lw=1.3)
text(ax, 48.5, 31, '$y\\div3$', 'varie', 'm')
save(fig, '75-027')
