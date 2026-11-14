import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(80)
cx, cy, R = 44, 58, 17
disc(ax, cx, cy, R, 'fixe', fill=False)
line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)
line(ax, [(cx - R - 6, cy), (cx + R + 6, cy)], 'sujet', 1.2)
for a, lab, x in ((0, '0°', cx + R + 3), (180, '180°', cx - R - 3)):
    disc(ax, *P(cx, cy, R, a), 1.7, 'resultat'); text(ax, x, cy + 3.2, lab, 'resultat', 's')
text(ax, cx, cy - R - 4, 'axe horizontal (y = 0)', 'sujet', 's')
f = numberline(ax, 10, 70, 14, 0, 540, 180, labels=False, arrow_right=True)
for v in (0, 180, 360, 540):
    text(ax, f(v), 10.6, f'{v}°', 'encre', 's')
for v in (0, 180, 360):
    arrow(ax, (f(v), 15.5), (f(v + 180), 15.5), 'varie', curve=-0.5)
    text(ax, (f(v) + f(v + 180)) / 2, 23.5, '+180°', 'varie', 's')
text(ax, 44, 3.5, 'θ = 180° n', 'resultat', 'm')
save(fig, '32-146')
