import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pt(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9, dash=False):
    pts = [pt(cx, cy, r, a0 + (a1 - a0) * i / 120) for i in range(121)]
    line(ax, pts, role, lw=lw, dash=dash)
    if head: arrow(ax, pt(cx, cy, r, a1 - (a1 - a0) * 0.05), pts[-1], role, lw=lw)
fig, ax = canvas(80)
O = (44, 48); R = 16
arc(ax, *O, R, 0, 360, 'fixe')
line(ax, [(O[0] - 20, O[1]), (O[0] + 20, O[1])], 'fixe'); line(ax, [(O[0], O[1] - 20), (O[0], O[1] + 20)], 'fixe')
pts = [pt(*O, R, a) for a in (0, 120, 240)]
poly(ax, pts, 'sujet')
for p in pts: disc(ax, *p, 1.4, 'sujet')
text(ax, pts[0][0] + 2.5, pts[0][1] + 3, '(1 ; 0)', 'sujet', 's', ha='left')
text(ax, pts[1][0] - 3, pts[1][1] + 4.5, '(−0,5 ; 0,866)', 'sujet', 's')
text(ax, pts[2][0] - 3, pts[2][1] - 4.5, '(−0,5 ; −0,866)', 'sujet', 's')
text(ax, 44, 17, 'x : 1 − 0,5 − 0,5 = 0', 'resultat', 'm')
text(ax, 44, 9, 'y : 0 + 0,866 − 0,866 = 0', 'resultat', 'm')
save(fig, '28-152')
