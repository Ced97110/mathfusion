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
def panel(cx, title, role, calc, val, valrole):
    o = (cx - 10, 16)
    vec(ax, o, (3, 1), u, 'sujet', lw=2.0)
    vec(ax, o, (3, 1), u, 'autre', lw=0.8)
    text(ax, o[0] + 15, o[1] + 7, '$x$ et $x$', 'sujet', 's')
    text(ax, cx, 41, title, role, 'm', weight='bold')
    text(ax, cx, 11, calc, 'encre', 's')
    text(ax, cx, 4, val, valrole, 'l', weight='bold')
panel(22, 'produit scalaire', 'autre', '$3\\times3+1\\times1$', '$10$', 'autre')
panel(66, 'aire orientée', 'sujet', '$3\\times1-1\\times3$', '$0$', 'resultat')
line(ax, [(44, 3), (44, 40)], 'fixe', lw=0.6, dash=True)
save(fig, '75-021')
