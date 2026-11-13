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
L = 12
ang = math.radians(math.degrees(math.atan2(1, 3)))
x = (L * math.cos(ang), L * math.sin(ang))
def panel(cx, ay, title, val, vrole):
    o = (cx - 8, 12)
    ya = math.radians(ay)
    y = (L * math.cos(ya), L * math.sin(ya))
    poly(ax, [o, (o[0] + x[0], o[1] + x[1]), (o[0] + x[0] + y[0], o[1] + x[1] + y[1]), (o[0] + y[0], o[1] + y[1])], 'sujet')
    vec(ax, o, x, 1, 'sujet', lw=1.6)
    vec(ax, o, y, 1, 'varie', lw=1.6)
    text(ax, cx, 40, title, 'encre', 's')
    text(ax, cx, 5, val, vrole, 's')
panel(14, 85, '$y$ loin de $x$', 'aire grande', 'sujet')
panel(42, 48, '$y$ se rapproche', 'aire plus petite', 'sujet')
panel(68, math.degrees(ang), '$y=x$', 'aire 0', 'resultat')
arrow(ax, (21, 22), (30, 22), 'varie', lw=0.9)
arrow(ax, (55, 22), (59, 22), 'varie', lw=0.9)
save(fig, '75-022')
