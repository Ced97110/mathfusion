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
u = 0.62
A = (22, 8); Bv = (8, 20)   # generic arrows (a,b) and (c,d), directions only
def panel(cx, first, second, rf, rs, ccw, title, formula, role_val):
    o = (cx - 14, 14)
    para(ax, o, A if first == 'a' else Bv, Bv if first == 'a' else A, 1.0, 'fixe')
    v1, v2 = (A, Bv) if first == 'a' else (Bv, A)
    vec(ax, o, v1, 1.0, 'sujet'); vec(ax, o, v2, 1.0, 'autre')
    text(ax, o[0] + v1[0] + 1, o[1] + v1[1] - 3.2 if first == 'a' else o[1] + v1[1] + 2.6, rf, 'sujet', 's', ha='left' if first == 'a' else 'center')
    text(ax, o[0] + v2[0] - 1, o[1] + v2[1] + 2.8 if first == 'a' else o[1] + v2[1] - 3.2, rs, 'autre', 's', ha='right' if first == 'a' else 'left')
    a1, a2 = math.degrees(math.atan2(v1[1], v1[0])), math.degrees(math.atan2(v2[1], v2[0]))
    arc(ax, o, 7, a1 + 2, a2 - 2, 'varie')
    text(ax, cx, 5, formula, role_val, 'm', weight='bold')
    text(ax, cx, 49, title, 'varie', 's')
panel(22, 'a', 'c', '1re : $(a,\\ b)$', '2e : $(c,\\ d)$', True, 'sens inverse des aiguilles', '$ad-bc$ positif', 'resultat')
panel(66, 'c', 'a', '1re : $(c,\\ d)$', '2e : $(a,\\ b)$', False, 'sens des aiguilles', '$cb-da$ négatif', 'varie')
save(fig, '75-017')
