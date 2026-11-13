import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def nb(ax, cx, cy, w, h, role, label, size="s", fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size, fill=fill)
def ed(ax, p, q, role="fixe", t=5.0, lw=0.9, head=False):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * t, p[1] + uy * t); b = (q[0] - ux * t, q[1] - uy * t)
    if head: arrow(ax, a, b, role, lw=lw)
    else: line(ax, [a, b], role, lw=lw)
fig, ax = canvas(80)
text(ax, 44, 75, r'$S$ = {1, 2, 3}', 'encre', 'm')
box(ax, 4, 24, 80, 44, 'fixe', fill=False, dash=True)
box(ax, 8, 28, 46, 30, 'sujet')
box(ax, 60, 28, 20, 30, 'resultat')
for x, n in [(21, '1'), (41, '2')]:
    disc(ax, x, 43, 5, 'sujet', label=n)
disc(ax, 70, 43, 5, 'resultat', label='3')
text(ax, 31, 63, r'$A$ = {1, 2}', 'sujet', 's')
text(ax, 70, 63, 'complément', 'resultat', 's')
text(ax, 44, 15, 'union : $S$ en entier', 'resultat', 's')
text(ax, 44, 8, 'intersection : partie vide', 'resultat', 's')
save(fig, '79-217')
