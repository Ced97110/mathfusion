import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pt(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9, dash=False):
    pts = [pt(cx, cy, r, a0 + (a1 - a0) * i / 120) for i in range(121)]
    line(ax, pts, role, lw=lw, dash=dash)
    if head: arrow(ax, pt(cx, cy, r, a1 - (a1 - a0) * 0.05), pts[-1], role, lw=lw)
fig, ax = canvas(62)
O = (18, 24)
line(ax, [O, pt(*O, 20, 0)], 'fixe')
line(ax, [O, pt(*O, 20, 35)], 'sujet')
line(ax, [O, pt(*O, 20, 125)], 'resultat')
arc(ax, *O, 9, 0, 35, 'sujet', head=True)
arc(ax, *O, 13, 35, 125, 'varie', head=True)
text(ax, *pt(*O, 25, 15), r'$a=\theta$', 'sujet', 's')
text(ax, *pt(*O, 20, 85), r'$b=90°$', 'varie', 's')
text(ax, 10, 49, r'$\theta+90°$', 'resultat', 's')
box(ax, 50, 42, 36, 10, 'sujet', label=r'$\cos(a+b)$')
arrow(ax, (60, 42), (60, 33), 'varie')
text(ax, 74, 37.5, r'$a=\theta,\ b=90°$', 'varie', 's')
box(ax, 50, 22, 36, 10, 'autre', label=r'$\cos(\theta+90°)$')
arrow(ax, (68, 22), (68, 13), 'resultat')
box(ax, 50, 3, 36, 10, 'resultat', label=r'$=-\sin\theta$')
save(fig, '28-145')
