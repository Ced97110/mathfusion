import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def nb(ax, cx, cy, w, h, role, label, size="s", fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size, fill=fill)
def ed(ax, p, q, role="fixe", t=5.0, lw=0.9, head=False):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * t, p[1] + uy * t); b = (q[0] - ux * t, q[1] - uy * t)
    if head: arrow(ax, a, b, role, lw=lw)
    else: line(ax, [a, b], role, lw=lw)
fig, ax = canvas(74)
B, H_, K_, T = (44, 18), (22, 40), (66, 40), (44, 62)
nb(ax, *B, 24, 8, 'resultat', r'$H\cap K$ : ordre 4')
nb(ax, *H_, 22, 8, 'sujet', r'$H$ : ordre 12')
nb(ax, *K_, 22, 8, 'autre', r'$K$ : ordre 20')
nb(ax, *T, 24, 8, 'resultat', r'$HK$ : ordre 60')
ed(ax, B, H_, 'varie', 6.5, 1.6); ed(ax, K_, T, 'varie', 6.5, 1.6)
ed(ax, B, K_, 'fixe', 6.5); ed(ax, H_, T, 'fixe', 6.5)
text(ax, 14, 26, r'$H/(H\cap K)$' + '\n3 éléments', 'varie', 's')
text(ax, 76, 54, r'$HK/K$' + '\n3 éléments', 'varie', 's')
text(ax, 44, 6, r'$HK/K\ \cong\ H/(H\cap K)$' + '\nisomorphes', 'resultat', 's')
save(fig, '79-213')
