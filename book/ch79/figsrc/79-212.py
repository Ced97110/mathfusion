import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def nb(ax, cx, cy, w, h, role, label, size="s", fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size, fill=fill)
def ed(ax, p, q, role="fixe", t=5.0, lw=0.9, head=False):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * t, p[1] + uy * t); b = (q[0] - ux * t, q[1] - uy * t)
    if head: arrow(ax, a, b, role, lw=lw)
    else: line(ax, [a, b], role, lw=lw)

fig, ax = canvas(86)
xm = 44
yT, yM, yB = 66, 42, 18
nb(ax, xm, yT, 28, 12, 'sujet', '60\nℤ/60 entier')
nb(ax, 19, yM, 30, 12, 'sujet', '12\nmultiples de 5')
nb(ax, 69, yM, 30, 12, 'autre', '20\nmultiples de 3')
nb(ax, xm, yB, 30, 12, 'resultat', '4\nmultiples de 15')
for x in (19, 69):
    ed(ax, (x, yM), (xm, yT), 'fixe', 8); ed(ax, (x, yM), (xm, yB), 'fixe', 8)
text(ax, 44, 81, 'ordre du sous-groupe', 'sujet', 'm')
text(ax, 44, 76.5, '= diviseur de 60', 'sujet', 'm')
text(ax, 44, 6, 'partie commune : ordre 4', 'resultat', 's')
text(ax, 44, 1.8, '= pgcd de 12 et de 20', 'resultat', 's')
save(fig, '79-212')
