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
cx = 44
T, L, R, Bm = (cx, 68), (cx - 22, 42), (cx + 22, 42), (cx, 16)
poly(ax, [T, R, Bm, L], 'fixe', fill=True, lw=0.8)
for p, role, lab in [(T, 'sujet', '8'), (L, 'sujet', '4'), (R, 'autre', '4'), (Bm, 'resultat', '2')]:
    disc(ax, p[0], p[1], 5, role, label=lab, size='m')
text(ax, 52, 68, 'groupe entier', 'sujet', 's', ha='left')
text(ax, 14, 51, 'rotations', 'sujet', 's')
text(ax, 74, 51, r'$K$', 'autre', 'm')
text(ax, 52, 16, 'identité, demi-tour', 'resultat', 's', ha='left')
text(ax, 44, 76.5, 'symétries du carré', 'fixe', 's')
text(ax, 44, 5, 'partie commune de deux éléments', 'resultat', 's')
save(fig, '79-214')
