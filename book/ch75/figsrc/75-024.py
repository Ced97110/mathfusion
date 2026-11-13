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
fig, ax = canvas(54)
u = 15
text(ax, 22, 49, 'aire orientée', 'sujet', 'm', weight='bold')
text(ax, 66, 49, 'règle voisine', 'autre', 'm', weight='bold')
# gauche : x = (0,1), y = (1,0)
o = (14, 18)
poly(ax, [o, (o[0] + u, o[1]), (o[0] + u, o[1] + u), (o[0], o[1] + u)], 'resultat')
vec(ax, o, (0, 1), u, 'sujet', lw=1.5); vec(ax, o, (1, 0), u, 'autre', lw=1.5)
text(ax, o[0] - 3, o[1] + u / 2, '$x$', 'sujet', 'm')
text(ax, o[0] + u + 2.5, o[1] - 1, '$y$', 'autre', 'm')
text(ax, 22, 9, '$B(x,\\ y)=-1\\neq0$', 'resultat', 's')
text(ax, 22, 3.5, 'une partenaire existe', 'resultat', 's')
# droite : x = (0,1), plusieurs y, toujours 0
o2 = (62, 18)
vec(ax, o2, (0, 1), u, 'sujet', lw=1.5)
for a in (0, 40, 140, 180):
    r = math.radians(a)
    vec(ax, o2, (math.cos(r), math.sin(r)), 12, 'autre', lw=1.0)
    text(ax, o2[0] + 16.5 * math.cos(r), o2[1] + 16 * math.sin(r) + (0 if a in (0, 180) else 0), '$0$', 'limite', 's')
text(ax, o2[0] - 3, o2[1] + u + 2, '$x$', 'sujet', 'm')
text(ax, 66, 9, '$B(x,\\ y)=0$ pour tout $y$', 'limite', 's')
text(ax, 66, 3.5, 'aucune partenaire', 'limite', 's')
line(ax, [(44, 2), (44, 46)], 'fixe', lw=0.6, dash=True)
save(fig, '75-024')
