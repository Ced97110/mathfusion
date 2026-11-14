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
u = 5.2
def panel(cx, first, title, val, role):
    o = (cx - 11, 14)
    x = (3, 1); y = (1, 2)
    para(ax, o, x, y, u, 'fixe')
    vec(ax, o, x, u, 'sujet'); vec(ax, o, y, u, 'autre')
    text(ax, o[0] + 3 * u + 1, o[1] + 1 * u - 3, '$x$', 'sujet', 'm', ha='left')
    text(ax, o[0] + 1 * u - 2.5, o[1] + 2 * u + 1.5, '$y$', 'autre', 'm', ha='right')
    ax1 = math.degrees(math.atan2(1, 3)); ax2 = math.degrees(math.atan2(2, 1))
    if first == 'x': arc(ax, o, 7.5, ax1 + 3, ax2 - 3, 'varie')
    else: arc(ax, o, 7.5, ax2 - 3, ax1 + 3, 'varie')
    text(ax, cx, 40, title, 'encre', 'm')
    text(ax, cx, 5, val, role, 'l', weight='bold')
panel(22, 'x', '$B(x,\\ y)$', '$5$', 'resultat')
panel(66, 'y', '$B(y,\\ x)$', '$-5$', 'varie')
text(ax, 44, 26, 'ordre échangé', 'varie', 's')
arrow(ax, (36, 21), (52, 21), 'varie', lw=1.0, both=True)
save(fig, '75-023')
