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
fig, ax = canvas(66)
u = 3.3
text(ax, 44, 62, '$B(x,\\ y)=x_1y_2-x_2y_1$', 'sujet', 'l', weight='bold')
def draw(o, x, y, rx, ry, lx, ly, fill='sujet'):
    para(ax, o, x, y, u, fill)
    vec(ax, o, x, u, 'sujet'); vec(ax, o, y, u, 'autre')
    return o
# A : x=(3,1), y=(1,2)
oA = (6, 30)
draw(oA, (3, 1), (1, 2), 0, 0, 0, 0)
text(ax, oA[0] + 3 * u + 1, oA[1] + 1 * u - 3, '$x$', 'sujet', 'm', ha='left')
text(ax, oA[0] + 1 * u - 2.5, oA[1] + 2 * u + 1.5, '$y$', 'autre', 'm', ha='right')
text(ax, 17, 22, '$3\\times2-1\\times1=5$', 'resultat', 's')
# B : x doublé
oB = (46, 30)
draw(oB, (6, 2), (1, 2), 0, 0, 0, 0)
text(ax, oB[0] + 6 * u + 1.5, oB[1] + 2 * u - 3, '$2x$', 'sujet', 'm', ha='left')
text(ax, oB[0] + 1 * u - 2.5, oB[1] + 2 * u + 1.5, '$y$', 'autre', 'm', ha='right')
text(ax, 64, 22, '$6\\times2-2\\times1=10$', 'resultat', 's')
text(ax, 44, 50, 'flèche doublée : aire doublée', 'varie', 's')
# C : rectangle
oC = (6, 4)
draw(oC, (2, 0), (0, 3), 0, 0, 0, 0)
text(ax, oC[0] + 2 * u + 1.5, oC[1] - 0.2, '$x$', 'sujet', 'm', ha='left')
text(ax, oC[0] - 2.5, oC[1] + 3 * u + 0.5, '$y$', 'autre', 'm', ha='right')
text(ax, 22, 11, '$2\\times3-0\\times0=6$', 'resultat', 's', ha='left')
text(ax, 22, 4, 'rectangle de côtés 2 et 3', 'fixe', 's', ha='left')
save(fig, '75-020')
