import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pt(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9, dash=False):
    pts = [pt(cx, cy, r, a0 + (a1 - a0) * i / 120) for i in range(121)]
    line(ax, pts, role, lw=lw, dash=dash)
    if head: arrow(ax, pt(cx, cy, r, a1 - (a1 - a0) * 0.05), pts[-1], role, lw=lw)
fig, ax = canvas(52)
P = (24, 38); A = pt(*P, 22, 210); B = pt(*P, 22, 330)
poly(ax, [P, A, B], 'sujet')
arc(ax, *P, 6, 210, 330, 'varie')
text(ax, 24, 29, '120°', 'varie', 's')
text(ax, 24, 20, 'côté cherché', 'sujet', 's')
line(ax, [(A[0], A[1] - 3), (B[0], B[1] - 3)], 'sujet', lw=1.4)
y = 26; f = numberline(ax, 52, 84, y, -1, 1, step=0.5, labels=False, arrow_right=False)
for v, s in [(-1, '−1'), (0, '0'), (1, '1')]: text(ax, f(v), y - 4, s, 'fixe', 's')
line(ax, [(f(-1), y), (f(0), y)], 'varie', lw=2.2)
disc(ax, f(-0.5), y, 1.5, 'sujet')
text(ax, f(-0.5), y + 9, r'$\cos 120°$', 'sujet', 's')
text(ax, f(-0.5), y + 5, '−0,5', 'sujet', 's')
text(ax, f(-0.5), y - 11, 'négatif', 'varie', 's')
save(fig, '28-146')
