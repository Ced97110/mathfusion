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
fig, ax = canvas(52)
u = 20
def panel(cx, first, title, val, role):
    o = (cx - 10, 17)
    poly(ax, [o, (o[0] + u, o[1]), (o[0] + u, o[1] + u), (o[0], o[1] + u)], 'fixe')
    e = (u, 0); f = (0, u)
    vec(ax, o, e, 1, 'sujet'); vec(ax, o, f, 1, 'autre')
    text(ax, o[0] + u + 2, o[1] - 0.5, '$e$', 'sujet', 'm', ha='left')
    text(ax, o[0] - 2.5, o[1] + u + 1, '$f$', 'autre', 'm', ha='right')
    if first == 'e':
        arc(ax, o, 8, 4, 86, 'varie')
    else:
        arc(ax, o, 8, 86, 4, 'varie')
    text(ax, cx, 46, title, 'varie', 's')
    text(ax, cx, 6, val, role, 'l', weight='bold')
panel(22, 'e', '1re $e$, puis $f$', 'aire orientée $+1$', 'resultat')
panel(66, 'f', '1re $f$, puis $e$', 'aire orientée $-1$', 'varie')
text(ax, 44, 27, 'même carré', 'fixe', 's')
save(fig, '75-018')
