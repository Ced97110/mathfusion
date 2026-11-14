import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pt(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9, dash=False):
    pts = [pt(cx, cy, r, a0 + (a1 - a0) * i / 120) for i in range(121)]
    line(ax, pts, role, lw=lw, dash=dash)
    if head: arrow(ax, pt(cx, cy, r, a1 - (a1 - a0) * 0.05), pts[-1], role, lw=lw)
fig, ax = canvas(63)
for cx, n in [(19, 3), (65, 4)]:
    cy = 34; r = 13
    arc(ax, cx, cy, r, 0, 360, 'fixe')
    pts = [pt(cx, cy, r, k * 360 / n) for k in range(n)]
    poly(ax, pts, 'sujet')
    for k, p in enumerate(pts): disc(ax, *p, 1.3, 'sujet')
    for k in range(n):
        text(ax, *pt(cx, cy, r + 5.5, k * 360 / n), f'{k * 360 // n}°', 'sujet', 's')
    arc(ax, cx, cy, 6, 0, 360 / n, 'varie', head=True)
    text(ax, cx, 9, f'écart 360° ÷ {n}', 'varie', 's')
    text(ax, cx, 60, f'$n={n}$', 'encre', 'l')
save(fig, '28-149')
