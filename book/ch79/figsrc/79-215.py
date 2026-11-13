import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def nb(ax, cx, cy, w, h, role, label, size="s", fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size, fill=fill)
def ed(ax, p, q, role="fixe", t=5.0, lw=0.9, head=False):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * t, p[1] + uy * t); b = (q[0] - ux * t, q[1] - uy * t)
    if head: arrow(ax, a, b, role, lw=lw)
    else: line(ax, [a, b], role, lw=lw)
fig, ax = canvas(66)
rows = [(52, 'nombres', 'sup(12 ; 20) = 60'), (34, 'groupes', 'ordre 12 + ordre 20 = ℤ/60'), (16, 'espaces', 'droite + droite = plan')]
for y, dom, calc in rows:
    nb(ax, 14, y, 22, 10, 'fixe', dom)
    nb(ax, 46, y, 38, 10, 'sujet', calc)
    nb(ax, 76, y, 20, 10, 'resultat', r'loi $M$ : vraie')
text(ax, 44, 62.5, 'trois domaines, une seule loi', 'resultat', 'm')
save(fig, '79-215')
