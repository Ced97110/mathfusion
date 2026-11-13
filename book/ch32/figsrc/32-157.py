import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(70)
f = numberline(ax, 8, 80, 56, -330, 750, 360, labels=False, arrow_right=True)
cx, cy, R = 44, 20, 14
disc(ax, cx, cy, R, 'fixe', fill=False)
p = P(cx, cy, R, 30)
for v in (-330, 30, 390, 750):
    text(ax, f(v), 52.6, f'{v}°'.replace('-', '−'), 'sujet', 's')
    line(ax, [(f(v), 49.5), p], 'fixe', 0.6, dash=True)
for v in (-330, 30, 390):
    arrow(ax, (f(v), 58), (f(v + 360), 58), 'varie', curve=-0.5)
    text(ax, (f(v) + f(v + 360)) / 2, 66.5, '+360°', 'varie', 's')
disc(ax, *p, 1.9, 'resultat'); text(ax, 74, 22, 'même point', 'resultat', 's')
text(ax, 44, 4, 'une classe : α + 360° n', 'sujet', 'm')
save(fig, '32-157')
