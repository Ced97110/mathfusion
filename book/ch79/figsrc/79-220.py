import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def nb(ax, cx, cy, w, h, role, label, size="s", fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size, fill=fill)
def ed(ax, p, q, role="fixe", t=5.0, lw=0.9, head=False):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * t, p[1] + uy * t); b = (q[0] - ux * t, q[1] - uy * t)
    if head: arrow(ax, a, b, role, lw=lw)
    else: line(ax, [a, b], role, lw=lw)
fig, ax = canvas(78)
T, L, R, Bm = (44, 64), (26, 44), (62, 44), (44, 24)
nb(ax, *T, 22, 11, 'resultat', '6\nsomme 12')
nb(ax, *L, 22, 11, 'varie', '2\nsomme 3')
nb(ax, *R, 22, 11, 'varie', '3\nsomme 4')
nb(ax, *Bm, 22, 11, 'varie', '1\nsomme 1')
for p, q in [(Bm, L), (Bm, R), (L, T), (R, T)]:
    ed(ax, p, q, 'fixe', 7)
text(ax, 80, 44, '− 4', 'varie', 'm')
text(ax, 8, 44, '− 3', 'varie', 'm')
text(ax, 66, 24, '+ 1', 'varie', 'm')
text(ax, 44, 11, '12 − 4 − 3 + 1 = 6', 'resultat', 'l')
save(fig, '79-220')
