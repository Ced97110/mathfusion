import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pt(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9, dash=False):
    pts = [pt(cx, cy, r, a0 + (a1 - a0) * i / 120) for i in range(121)]
    line(ax, pts, role, lw=lw, dash=dash)
    if head: arrow(ax, pt(cx, cy, r, a1 - (a1 - a0) * 0.05), pts[-1], role, lw=lw)
fig, ax = canvas(68)
O = (30, 30); R = 24
arc(ax, *O, R, 0, 360, 'fixe')
A = pt(*O, R, 0); P1 = pt(*O, R, 30); P2 = pt(*O, R, 100)
line(ax, [O, A], 'fixe')
arc(ax, *O, 9, 0, 30, 'varie', head=True); arc(ax, *O, 13, 0, 100, 'varie', head=True)
disc(ax, *O, 1.0, 'encre'); disc(ax, *A, 1.5, 'sujet'); disc(ax, *P1, 1.5, 'resultat'); disc(ax, *P2, 1.5, 'resultat')
text(ax, O[0] - 3, O[1] - 3, r'$O$', 'encre', 's')
text(ax, A[0] + 3, A[1] - 3, r'$A$', 'sujet', 'm')
text(ax, P1[0] + 3, P1[1] + 3, 'rotation 30°', 'varie', 's', ha='left')
text(ax, P2[0] + 2, P2[1] + 6.5, 'rotation 100°', 'varie', 's', ha='left')
text(ax, 44, 4, 'chaque rotation = un point du cercle', 'resultat', 's')
save(fig, '28-150')
