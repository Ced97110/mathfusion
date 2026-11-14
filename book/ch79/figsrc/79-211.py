import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def nb(ax, cx, cy, w, h, role, label, size="s", fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size, fill=fill)
def ed(ax, p, q, role="fixe", t=5.0, lw=0.9, head=False):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * t, p[1] + uy * t); b = (q[0] - ux * t, q[1] - uy * t)
    if head: arrow(ax, a, b, role, lw=lw)
    else: line(ax, [a, b], role, lw=lw)

fig, ax = canvas(76)
orders = [1, 2, 4, 12, 60]
pts = [(12 + i * 16, 10 + i * 13) for i in range(5)]
for i, ((x, y), o) in enumerate(zip(pts, orders)):
    nb(ax, x, y, 20, 8, 'sujet', f'ordre {o}')
for i in range(4):
    p, q = pts[i], pts[i + 1]
    arrow(ax, (p[0] + 4, p[1] + 4.5), (q[0] - 4, q[1] - 4.5), 'sujet', lw=1.1)
    text(ax, (p[0] + q[0]) / 2 + 7, (p[1] + q[1]) / 2 - 1.5, f'marche {i + 1}', 'varie', 's')
text(ax, 28, 70, r'sous-groupes de $\mathbb{Z}/60$', 'sujet', 'm')
text(ax, 28, 64, 'chacun dans le suivant,', 'fixe', 's')
text(ax, 28, 59.5, 'rien entre les deux', 'fixe', 's')
save(fig, '79-211')
