import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def nb(ax, cx, cy, w, h, role, label, size="s", fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size, fill=fill)
def ed(ax, p, q, role="fixe", t=5.0, lw=0.9, head=False):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * t, p[1] + uy * t); b = (q[0] - ux * t, q[1] - uy * t)
    if head: arrow(ax, a, b, role, lw=lw)
    else: line(ax, [a, b], role, lw=lw)
fig, ax = canvas(84)
text(ax, 44, 80, 'en série', 'sujet', 'm', weight='bold')
y = 68
line(ax, [(6, y), (22, y)], 'fixe'); line(ax, [(34, y), (54, y)], 'fixe'); line(ax, [(66, y), (82, y)], 'fixe')
nb(ax, 28, y, 12, 8, 'sujet', 'A', 'm'); nb(ax, 60, y, 12, 8, 'autre', 'B', 'm')
text(ax, 44, 55, 'passe si A et B fermés', 'resultat', 's')
text(ax, 44, 46, 'en parallèle', 'sujet', 'm', weight='bold')
ya, yb = 36, 22
line(ax, [(6, 29), (22, 29), (22, yb), (22, ya), (30, ya)], 'fixe'); line(ax, [(22, yb), (30, yb)], 'fixe')
line(ax, [(58, ya), (66, ya), (66, 29), (82, 29)], 'fixe'); line(ax, [(58, yb), (66, yb), (66, ya)], 'fixe')
nb(ax, 44, ya, 28, 8, 'fixe', ' ', 's', fill=False) if False else None
line(ax, [(30, ya), (58, ya)], 'fixe'); line(ax, [(30, yb), (58, yb)], 'fixe')
nb(ax, 44, ya, 12, 8, 'sujet', 'A', 'm'); nb(ax, 44, yb, 12, 8, 'autre', 'B', 'm')
text(ax, 44, 9, 'passe si A ou B fermé', 'resultat', 's')
save(fig, '79-219')
