import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(64)
cx, cy, R = 44, 32, 22
disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
a = math.degrees(math.atan(1000))
line(ax, [P(cx, cy, R * 1.1, a + 180), P(cx, cy, R * 1.1, a)], 'sujet', 1.2)
for t in (a, a + 180): disc(ax, *P(cx, cy, R, t), 1.7, 'resultat')
text(ax, cx + 3, cy + R + 4, 'pente 1 000', 'sujet', 'm', ha='left')
text(ax, cx, 3.5, 'deux points opposés', 'resultat', 'm')
save(fig, '32-148')
