import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(72)
cx, cy, R = 30, 38, 24
disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
line(ax, [(cx, cy - R), (cx, cy + R)], 'sujet', 1.4)
arc(ax, cx, cy, R, -90, 90, 'resultat', 2.2)
for y in (cy + R, cy - R): disc(ax, cx, y, 1.9, 'limite')
text(ax, cx, cy + R + 4, '90°', 'limite', 'm'); text(ax, cx, cy - R - 4, '−90°', 'limite', 'm')
text(ax, 72, 49, 'α entre', 'resultat', 'm'); text(ax, 72, 44, '−90° et 90°', 'resultat', 'm')
text(ax, 72, 31, '90° exclu', 'limite', 'm')
text(ax, 72, 24, 'droite verticale', 'sujet', 's'); text(ax, 72, 19.5, '= pas de pente', 'sujet', 's')
save(fig, '32-149')
