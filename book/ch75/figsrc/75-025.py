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
# 1. V : l'espace de flèches, sur un corps F
box(ax, 3, 36, 26, 26, 'fixe', r=1.0)
o = (8, 41)
vec(ax, o, (14, 3), 1, 'sujet'); vec(ax, o, (4, 14), 1, 'autre')
text(ax, 24, 42, '$x$', 'sujet', 's'); text(ax, 9, 59, '$y$', 'autre', 's')
text(ax, 3, 32, '$V$ sur un corps $F$', 'fixe', 's', ha='left')
# 2. B : la règle, deux flèches entrent
box(ax, 37, 40, 16, 18, 'sujet', label='$B$', size='l', weight='bold')
arrow(ax, (29.5, 52), (36.5, 52), 'sujet', lw=1.2); arrow(ax, (29.5, 46), (36.5, 46), 'autre', lw=1.2)
text(ax, 45, 62, 'règle $B$', 'sujet', 's')
# 3. un nombre de F sort
box(ax, 62, 42, 22, 14, 'resultat', label='un nombre', size='s')
arrow(ax, (53.5, 49), (61.5, 49), 'resultat', lw=1.2)
text(ax, 73, 61, 'de $F$', 'resultat', 's')
# deux propriétés de B
line(ax, [(45, 39.5), (45, 33), (20, 33)][:2], 'sujet', dash=True)
line(ax, [(45, 33), (34, 33), (34, 25)], 'sujet', dash=True); line(ax, [(45, 33), (66, 33), (66, 25)], 'sujet', dash=True)
box(ax, 4, 4, 40, 20, 'sujet', r=1.0); box(ax, 46, 4, 38, 20, 'sujet', r=1.0)
text(ax, 24, 18, 'alternée', 'sujet', 's', weight='bold'); text(ax, 24, 10, '$B(x,\\ x)=0$', 'sujet', 's')
text(ax, 65, 14, 'non dégénérée', 'sujet', 's', weight='bold')
save(fig, '75-025')
