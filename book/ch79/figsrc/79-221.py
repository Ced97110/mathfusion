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
B, T = (44, 14), (44, 70)
left = [('2', (22, 30)), ('4', (22, 54))]; right = [('3', (66, 30)), ('6', (66, 54))]
nb(ax, *B, 12, 8, 'fixe', '1', 'm'); nb(ax, *T, 12, 8, 'fixe', '12', 'm')
chain = lambda lst, role: [B] + [p for _, p in lst] + [T]
for lst, role in [(left, 'sujet'), (right, 'autre')]:
    pts = chain(lst, role)
    for (l, p) in lst: nb(ax, *p, 12, 8, role, l, 'm')
    for p, q in zip(pts, pts[1:]): ed(ax, p, q, role, 5.5, 1.2)
text(ax, 10, 42, '3 marches', 'sujet', 's')
text(ax, 78, 42, '3 marches', 'autre', 's')
text(ax, 44, 4, r'ordres des sous-modules de $\mathbb{Z}/12$', 'fixe', 's')
save(fig, '79-221')
