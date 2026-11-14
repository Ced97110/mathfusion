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
o = (44, 40); u = 14
def P(x, y, z): return iso(x, y, z, o, u)
A = [P(-1, -1, 0), P(1, -1, 0), P(1, 1, 0), P(-1, 1, 0)]
B = [P(0, -1, -1), P(0, 1, -1), P(0, 1, 1), P(0, -1, 1)]
ax.add_patch(Polygon(A, closed=True, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, alpha=0.85, zorder=2))
ax.add_patch(Polygon(B, closed=True, ec=COL['autre'], fc=FILL['autre'], lw=0.8, alpha=0.75, zorder=2.2))
line(ax, [P(0, -1, 0), P(0, 1, 0)], 'varie', lw=1.8)
text(ax, 77, 40, 'plan 1', 'sujet', 'm')
text(ax, 32, 66, 'plan 2', 'autre', 'm')
text(ax, 72, 22, 'droite commune', 'varie', 's')
arrow(ax, (65, 24), (P(0, -1, 0)[0] - 1, P(0, -1, 0)[1] - 0.5), 'varie', lw=0.8)
text(ax, 44, 8, 'dimensions : 2 + 2 = 3 + 1', 'resultat', 'm')
save(fig, '79-216')
