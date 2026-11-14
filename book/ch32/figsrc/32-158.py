import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(66)
cx, cy, R = 44, 34, 22
disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
p1, p2, p3 = P(cx, cy, R, 40), P(cx, cy, R, -40), P(cx, cy, R, 220)
line(ax, [p1, p3], 'resultat', 1.0, dash=True)
arrow(ax, (p1[0], p1[1] - 2), (p2[0], p2[1] + 2), 'varie')
arrow(ax, (p2[0] - 3, p2[1]), (p3[0] + 3, p3[1]), 'varie')
disc(ax, *p1, 1.9, 'sujet'); disc(ax, *p2, 1.9, 'varie'); disc(ax, *p3, 1.9, 'resultat')
text(ax, 65, 52, '40°', 'sujet', 'm'); text(ax, 65, 16.5, '−40°', 'varie', 'm'); text(ax, 23, 16.5, '220°', 'resultat', 'm')
text(ax, 77, 34, 'reflet 1', 'varie', 's'); text(ax, 44, 15.5, 'reflet 2', 'varie', 's')
text(ax, 18, 50, 'demi-tour', 'resultat', 's')
save(fig, '32-158')
