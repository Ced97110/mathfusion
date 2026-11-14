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
fig, ax = canvas(78)
box(ax, 14, 66, 60, 10, 'sujet', label='$z=(3,\\ 2,\\ 5,\\ 2)$', size='m')
arrow(ax, (30, 65.5), (24, 55), 'varie', lw=1.2); arrow(ax, (58, 65.5), (64, 55), 'varie', lw=1.2)
box(ax, 3, 30, 36, 24, 'sujet', r=1.5); box(ax, 49, 30, 36, 24, 'autre', r=1.5)
text(ax, 21, 49, '$P_1$', 'sujet', 'm', weight='bold'); text(ax, 67, 49, '$P_1^\\perp$', 'autre', 'm', weight='bold')
vec(ax, (8, 33), (3, 0.5), 5, 'sujet', lw=1.7); vec(ax, (54, 33), (5, 0.5), 4.4, 'autre', lw=1.7)
text(ax, 21, 40, '$(3,\\ 2,\\ 0,\\ 0)$', 'sujet', 's'); text(ax, 67, 40, '$(0,\\ 0,\\ 5,\\ 2)$', 'autre', 's')
text(ax, 44, 42, '+', 'varie', 'xl', weight='bold')
box(ax, 3, 4, 36, 20, 'resultat', r=1.5)
text(ax, 21, 17, '$z$ = somme', 'resultat', 's', weight='bold'); text(ax, 21, 10, 'des deux morceaux', 'resultat', 's')
line(ax, [(67, 29.5), (67, 24.5)], 'autre', dash=True)
box(ax, 49, 4, 36, 20, 'autre', r=1.5)
text(ax, 67, 17, '$B$ reste', 'autre', 's', weight='bold'); text(ax, 67, 10, 'non dégénérée', 'autre', 's')
save(fig, '75-030')
