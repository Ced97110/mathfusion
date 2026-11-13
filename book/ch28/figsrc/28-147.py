import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pt(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9, dash=False):
    pts = [pt(cx, cy, r, a0 + (a1 - a0) * i / 120) for i in range(121)]
    line(ax, pts, role, lw=lw, dash=dash)
    if head: arrow(ax, pt(cx, cy, r, a1 - (a1 - a0) * 0.05), pts[-1], role, lw=lw)
fig, ax = canvas(52)
O = (44, 8); R = 34
arc(ax, *O, R, 0, 180, 'fixe')
line(ax, [(8, O[1]), (80, O[1])], 'fixe')
P1 = pt(*O, R, 30); P2 = pt(*O, R, 150)
line(ax, [O, P1], 'sujet'); line(ax, [O, P2], 'autre')
line(ax, [P2, P1], 'fixe', dash=True)
line(ax, [P1, (P1[0], O[1])], 'resultat', lw=1.3); line(ax, [P2, (P2[0], O[1])], 'resultat', lw=1.3)
disc(ax, *P1, 1.3, 'sujet'); disc(ax, *P2, 1.3, 'autre')
text(ax, P1[0] - 1, P1[1] + 5, '30°', 'sujet', 'm')
text(ax, P2[0] - 1, P2[1] + 5, '150°', 'autre', 'm')
text(ax, 44, P1[1] + 4, 'sin = 0,5', 'resultat', 'm')
text(ax, 44, 3, 'même hauteur, même sinus', 'resultat', 's')
save(fig, '28-147')
