import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(56)
A, B, C = (6, 10), (30, 10), (30, 42)
poly(ax, [A, B, C], 'sujet')
line(ax, [(28, 10), (28, 12), (30, 12)], 'sujet', 0.6)
arc(ax, A[0], A[1], 6, 0, 53.13, 'varie', 1.2)
text(ax, 20, 14.5, '53,13°', 'varie', 's')
text(ax, 18, 5.5, '3', 'sujet', 'm'); text(ax, 33.5, 26, '4', 'sujet', 'm'); text(ax, 15.2, 28, '5', 'resultat', 'm')
text(ax, 64, 49, '3 sin x + 4 cos x = 3', 'encre', 'm')
arrow(ax, (64, 45), (64, 36), 'varie'); text(ax, 72, 40.5, 'réécrite', 'varie', 's', ha='left')
text(ax, 64, 31, '5 sin(x + 53,13°) = 3', 'resultat', 'm')
arrow(ax, (64, 27), (64, 18), 'varie'); text(ax, 72, 22.5, '÷ 5', 'varie', 's', ha='left')
text(ax, 64, 13, 'sin(x + 53,13°) = 0,6', 'resultat', 'm')
save(fig, '32-154')
