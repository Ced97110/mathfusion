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
fig, ax = canvas(60)
u = 17
def square(o, role, fillrole='fixe'):
    poly(ax, [o, (o[0] + u, o[1]), (o[0] + u, o[1] + u), (o[0], o[1] + u)], fillrole)
o1 = (7, 28); o2 = (56, 28)
square(o1, 'fixe'); square(o2, 'fixe')
vec(ax, o1, (u, 0), 1, 'sujet'); vec(ax, o1, (0, u), 1, 'autre')
text(ax, o1[0] + u + 1.5, o1[1] - 2.5, '$e$', 'sujet', 'm'); text(ax, o1[0] - 3, o1[1] + u + 1, '$f$', 'autre', 'm')
arc(ax, o1, 7, 4, 86, 'varie')
# image : l'image de e est vers le haut, l'image de f vers la droite
vec(ax, o2, (0, u), 1, 'sujet'); vec(ax, o2, (u, 0), 1, 'autre')
text(ax, o2[0] - 5.5, o2[1] + u + 1, '$e\\prime$', 'sujet', 'm'); text(ax, o2[0] + u + 2, o2[1] - 2.5, '$f\\prime$', 'autre', 'm')
arc(ax, o2, 7, 86, 4, 'varie')
arrow(ax, (31, 36), (50, 36), 'varie', lw=1.2)
text(ax, 40.5, 40, 'la transformation', 'varie', 's')
text(ax, 15.5, 51, 'départ', 'fixe', 's'); text(ax, 64.5, 51, 'image', 'fixe', 's')
text(ax, 44, 18, 'aire ordinaire : $1\\rightarrow1$', 'resultat', 'm')
text(ax, 44, 9, 'aire orientée : $1\\rightarrow-1$', 'limite', 'm')
text(ax, 44, 1.6, '$ad-bc=0-1\\neq1$', 'limite', 'm')
save(fig, '75-019')
