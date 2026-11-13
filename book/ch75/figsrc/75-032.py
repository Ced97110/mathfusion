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
fig, ax = canvas(44)
text(ax, 44, 40, 'dimension de l\'espace $V$', 'sujet', 'm', weight='bold')
xs = [9 + i * 10 for i in range(8)]
line(ax, [(xs[0], 26), (xs[-1], 26)], 'fixe', lw=0.9)
for d in range(1, 9):
    x = xs[d - 1]
    if d % 2 == 0:
        disc(ax, x, 26, 4.0, 'resultat', label=str(d), size='m')
    else:
        disc(ax, x, 26, 4.0, 'limite')
        line(ax, [(x - 2.2, 23.8), (x + 2.2, 28.2)], 'limite', lw=1.1)
        line(ax, [(x - 2.2, 28.2), (x + 2.2, 23.8)], 'limite', lw=1.1)
text(ax, 44, 14, 'dimension paire : $2n$', 'resultat', 'm', weight='bold')
text(ax, 44, 6, 'dimension impaire : impossible', 'limite', 'm', weight='bold')
save(fig, '75-032')
