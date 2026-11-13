import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(52)
x0, x1 = 6.0, 80.0
f = lambda d: x0 + d / 90 * (x1 - x0)
yt, yb = 34, 14
for y in (yt, yb):
    line(ax, [(x0, y), (x1, y)], 'fixe')
    for d in range(0, 100, 10):
        line(ax, [(f(d), y - 1.2), (f(d), y + 1.2)], 'fixe', lw=0.7)
    line(ax, [(x0, y), (f(10), y)], 'sujet', lw=2.6)
text(ax, f(0), yt + 4.5, '0°', 'fixe', 's'); text(ax, f(10), yt + 4.5, '10°', 'sujet', 's'); text(ax, f(90), yt + 4.5, '90°', 'fixe', 's')
text(ax, f(0), yb - 4.5, '0', 'fixe', 's'); text(ax, f(10) + 1, yb - 4.5, '0,1745', 'sujet', 's'); text(ax, f(90), yb - 4.5, '1,571', 'fixe', 's')
line(ax, [(f(90), yt), (f(90), yb)], 'fixe', dash=True)
arrow(ax, (40, yt - 2), (40, yb + 2), 'varie')
text(ax, 53, 24, r'$\times\ \pi$/180', 'varie', 'm')
text(ax, 44, 47, r'$\pi$/180 ≈ 0,01745 radian par degré', 'resultat', 's')
text(ax, 77, yt - 5, 'degrés', 'fixe', 's', ha='right')
text(ax, 77, yb + 5, 'radians', 'fixe', 's', ha='right')
save(fig, '29-056')
