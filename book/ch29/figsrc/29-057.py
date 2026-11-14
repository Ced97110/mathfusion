import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(52)
x0 = 8.0; u = 34.0
f = lambda r: x0 + r * u
yt, yb = 34, 14
for y in (yt, yb):
    line(ax, [(x0, y), (f(2), y)], 'fixe')
    for r in (0, 0.5, 1, 1.5, 2):
        line(ax, [(f(r), y - 1.2), (f(r), y + 1.2)], 'fixe', lw=0.7)
    line(ax, [(f(0), y), (f(1), y)], 'sujet', lw=2.6)
text(ax, f(0), yt + 4.5, '0', 'fixe', 's'); text(ax, f(1), yt + 4.5, '1 radian', 'sujet', 's'); text(ax, f(2), yt + 4.5, '2', 'fixe', 's')
text(ax, f(0), yb - 4.5, '0°', 'fixe', 's'); text(ax, f(1), yb - 4.5, '57,3°', 'sujet', 's'); text(ax, f(2), yb - 4.5, '114,6°', 'fixe', 's')
line(ax, [(f(2), yt), (f(2), yb)], 'fixe', dash=True)
arrow(ax, (20, yt - 2), (20, yb + 2), 'varie')
text(ax, 31, 24, r'$\times\ 180/\pi$', 'varie', 'm')
text(ax, 44, 47, r'180/$\pi$ ≈ 57,3 degrés par radian', 'resultat', 's')
save(fig, '29-057')
