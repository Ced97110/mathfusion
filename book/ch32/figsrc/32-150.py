import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(62)
R = 13; cy = 34
c1, c2 = 22, 66
for cx in (c1, c2): disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
line(ax, [(c1 - R - 3, cy + R), (c1 + R + 3, cy + R)], 'sujet', 1.2)
disc(ax, *P(c1, cy, R, 90), 1.7, 'resultat'); text(ax, c1, cy + R + 4.5, '90°', 'resultat', 's')
line(ax, [P(c2, cy, R, 45), P(c2, cy, R, 225)], 'fixe', 0.6, dash=True)
for a in (45, 225):
    disc(ax, *P(c2, cy, R, a), 1.7, 'resultat'); x, y = P(c2, cy, R + 5.5, a); text(ax, x, y, f'{a}°', 'resultat', 's')
arrow(ax, (c1 + R + 2, cy), (c2 - R - 2, cy), 'varie'); text(ax, 44, cy + 3.5, '÷ 2', 'varie', 'm')
text(ax, 44, 59, 'sin 2θ = 1', 'sujet', 'm')
text(ax, c1, 15, 'angle 2θ', 'encre', 's'); text(ax, c2, 15, 'angle θ', 'encre', 's')
text(ax, 44, 5.5, 'deux solutions, pas quatre', 'resultat', 'm')
save(fig, '32-150')
