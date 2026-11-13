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
yT, yM, yB = 62, 40, 18
text(ax, 18, 77, r'$\mathbb{Z}/4$', 'sujet', 'm', weight='bold')
text(ax, 62, 77, r'$\mathbb{Z}/2 \times \mathbb{Z}/2$', 'autre', 'm', weight='bold')
ys = [yT, yM, yB]
for y, l in zip(ys, ['ordre 4', 'ordre 2', 'ordre 1']): nb(ax, 18, y, 20, 8, 'sujet', l)
for p, q in [((18, yB), (18, yM)), ((18, yM), (18, yT))]: ed(ax, p, q, 'sujet', 4.5, 1.2)
nb(ax, 62, yT, 20, 8, 'autre', 'ordre 4'); nb(ax, 62, yB, 20, 8, 'autre', 'ordre 1')
for x, l in [(46, r'$D_1$'), (62, r'$D_2$'), (78, r'$D_3$')]:
    nb(ax, x, yM, 12, 8, 'autre', l, 'm')
    ed(ax, (x, yM), (62, yT), 'autre', 4.5, 1.2); ed(ax, (x, yM), (62, yB), 'autre', 4.5, 1.2)
text(ax, 18, 7, 'cyclique : une chaîne', 'sujet', 's')
text(ax, 62, 7, 'pas cyclique : un diamant', 'autre', 's')
save(fig, '79-222')
