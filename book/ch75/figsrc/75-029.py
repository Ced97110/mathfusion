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
fig, ax = canvas(62)
u = 4
def frame(x0, title, role):
    box(ax, x0, 12, 40, 38, role, r=1.5)
    text(ax, x0 + 20, 54, title, role, 'm', weight='bold')
frame(3, '$P_1$', 'sujet'); frame(45, '$P_1^\\perp$', 'autre')
o = (9, 20)
vec(ax, o, (1, 0), 6, 'sujet', lw=1.6); vec(ax, o, (0, 1), 6, 'autre', lw=1.6)
text(ax, o[0] + 6, o[1] - 3, '$e_1$', 'sujet', 's'); text(ax, o[0] - 3, o[1] + 7, '$f_1$', 'autre', 's')
text(ax, 23, 44, 'plan des 2 premières', 'fixe', 's')
text(ax, 23, 40, 'coordonnées', 'fixe', 's')
o2 = (53, 20)
vec(ax, o2, (5, 2), u, 'limite' if False else 'varie', lw=1.6)
text(ax, o2[0] + 22, o2[1] + 10.5, '$z$', 'varie', 'm')
text(ax, 65, 44, 'plan des 2 dernières', 'fixe', 's')
text(ax, 65, 40, 'coordonnées', 'fixe', 's')
text(ax, 65, 33, '$z=(0,\\ 0,\\ 5,\\ 2)$', 'varie', 's')
text(ax, 65, 7, '$B(z,\\ e_1)=0$', 'resultat', 's')
text(ax, 65, 1.5, '$B(z,\\ f_1)=0$', 'resultat', 's')
text(ax, 23, 7, 'combinaisons de $e_1$, $f_1$', 'sujet', 's')
save(fig, '75-029')
