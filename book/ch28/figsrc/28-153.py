import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pt(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9, dash=False):
    pts = [pt(cx, cy, r, a0 + (a1 - a0) * i / 120) for i in range(121)]
    line(ax, pts, role, lw=lw, dash=dash)
    if head: arrow(ax, pt(cx, cy, r, a1 - (a1 - a0) * 0.05), pts[-1], role, lw=lw)
fig, ax = canvas(84)
O = (44, 50); R = 16
arc(ax, *O, R, 0, 360, 'fixe')
line(ax, [(O[0] - 20, O[1]), (O[0] + 20, O[1])], 'fixe'); line(ax, [(O[0], O[1] - 20), (O[0], O[1] + 20)], 'fixe')
p0 = [pt(*O, R, a) for a in (0, 120, 240)]
p1 = [pt(*O, R, a) for a in (90, 210, 330)]
line(ax, p0 + [p0[0]], 'fixe', dash=True)
poly(ax, p1, 'sujet')
for p in p1: disc(ax, *p, 1.4, 'sujet')
arc(ax, *O, 8, 0, 90, 'varie', head=True)
text(ax, *pt(*O, 12, 40), '90°', 'varie', 's')
text(ax, p0[0][0] + 2.5, p0[0][1] + 3, 'départ', 'fixe', 's', ha='left')
text(ax, p1[0][0], p1[0][1] + 5.5, '(0 ; 1)', 'sujet', 's')
text(ax, p1[1][0] - 2, p1[1][1] - 7, '(−0,866 ; −0,5)', 'sujet', 's')
text(ax, p1[2][0] + 2, p1[2][1] - 7, '(0,866 ; −0,5)', 'sujet', 's')
text(ax, 44, 18, 'x : 0 − 0,866 + 0,866 = 0', 'resultat', 'm')
text(ax, 44, 9, r'pour tout angle $\theta$ ?', 'varie', 'm')
save(fig, '28-153')
