import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def nb(ax, cx, cy, w, h, role, label, size="s", fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size, fill=fill)
def ed(ax, p, q, role="fixe", t=5.0, lw=0.9, head=False):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * t, p[1] + uy * t); b = (q[0] - ux * t, q[1] - uy * t)
    if head: arrow(ax, a, b, role, lw=lw)
    else: line(ax, [a, b], role, lw=lw)

fig, ax = canvas(72)
text(ax, 20, 67, 'sous-groupes', 'sujet', 'm', weight='bold')
text(ax, 68, 67, 'corps fixes', 'autre', 'm', weight='bold')
yt, yb = 50, 20
nb(ax, 20, yt, 30, 10, 'sujet', 'groupe entier')
nb(ax, 20, yb, 30, 10, 'sujet', 'identité seule')
nb(ax, 68, yt, 30, 10, 'autre', 'gros corps')
nb(ax, 68, yb, 30, 10, 'autre', 'corps de base')
ed(ax, (20, yb), (20, yt), 'fixe', 5, head=True)
ed(ax, (68, yb), (68, yt), 'fixe', 5, head=True)
text(ax, 11, 35, 'contient', 'fixe', 's', ha='center')
text(ax, 77, 35, 'contient', 'fixe', 's', ha='center')
arrow(ax, (35, yt - 2), (53, yb + 2), 'resultat', lw=1.1)
arrow(ax, (35, yb + 2), (53, yt - 2), 'resultat', lw=1.1)
text(ax, 44, 8, 'plus le groupe est gros,', 'resultat', 's')
text(ax, 44, 3.5, 'plus le corps est petit', 'resultat', 's')
save(fig, '79-209')
