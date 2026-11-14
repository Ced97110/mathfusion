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
u = 8
o = (12, 16)
box(ax, 3, 6, 54, 46, 'sujet', r=1.5)
text(ax, 9, 47, '$P_1$', 'sujet', 'l', weight='bold')
vec(ax, o, (1, 0), u, 'sujet', lw=1.8); vec(ax, o, (0, 1), u, 'autre', lw=1.8)
text(ax, o[0] + u / 2, o[1] - 3, '$e_1$', 'sujet', 'm')
text(ax, o[0] - 3.5, o[1] + u / 2, '$f_1$', 'autre', 'm')
tip = (o[0] + 3 * u, o[1] + 2 * u)
line(ax, [o, (tip[0], o[1]), tip], 'varie', dash=True)
for k in range(1, 4): ax.plot([o[0] + k * u] * 2, [o[1] - 1, o[1] + 1], color=COL['varie'], lw=0.9, zorder=3)
arrow(ax, o, (tip[0] - 0.6, tip[1] - 0.4), 'resultat', lw=1.6)
text(ax, o[0] + 3 * u / 2 + 4, o[1] - 4.5, '3 fois $e_1$', 'varie', 's')
text(ax, tip[0] + 2, o[1] + u, '2 fois $f_1$', 'varie', 's', ha='left')
text(ax, tip[0] - 12, tip[1] + 6, '$3e_1+2f_1$', 'resultat', 's')
text(ax, 72, 32, '$(3,\\ 2,\\ 0,\\ 0)$', 'resultat', 's')
text(ax, 72, 24, 'les deux', 'fixe', 's'); text(ax, 72, 19, 'dernières', 'fixe', 's'); text(ax, 72, 14, 'coordonnées', 'fixe', 's'); text(ax, 72, 9, 'valent 0', 'fixe', 's')
save(fig, '75-028')
