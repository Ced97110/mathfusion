import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pt(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9, dash=False):
    pts = [pt(cx, cy, r, a0 + (a1 - a0) * i / 120) for i in range(121)]
    line(ax, pts, role, lw=lw, dash=dash)
    if head: arrow(ax, pt(cx, cy, r, a1 - (a1 - a0) * 0.05), pts[-1], role, lw=lw)
fig, ax = canvas(64)
O = (44, 22); R = 19
arc(ax, *O, R, 0, 360, 'fixe')
line(ax, [(O[0] - 23, O[1]), (O[0] + 23, O[1])], 'fixe'); line(ax, [(O[0], O[1] - 22), (O[0], O[1] + 22)], 'fixe')
P1 = pt(*O, R, 30); P2 = pt(*O, R, 120)
line(ax, [P1, (P1[0], O[1])], 'varie', dash=True); line(ax, [P2, (P2[0], O[1])], 'varie', dash=True)
arc(ax, *O, 11, 30, 120, 'varie', head=True)
disc(ax, *P1, 1.4, 'sujet'); disc(ax, *P2, 1.4, 'resultat')
text(ax, P1[0] + 2.5, P1[1] + 3.5, '(0,866 ; 0,5)', 'sujet', 's', ha='left')
text(ax, P2[0] - 1, P2[1] + 4.5, '(−0,5 ; 0,866)', 'resultat', 's')
text(ax, *pt(*O, 15, 75), '90°', 'varie', 's')
text(ax, P1[0] + 1.5, O[1] + 4, 'y = 0,5', 'varie', 's', ha='left')
text(ax, P2[0] - 1.5, O[1] - 4, 'x = −0,5', 'varie', 's', ha='right')
text(ax, 44, 59, r'$(x,\ y)\mapsto(-y,\ x)$', 'sujet', 'l')
save(fig, '28-151')
