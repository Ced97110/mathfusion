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
cx, cy, R = 30, 36, 24
disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
line(ax, [(4, cy - R), (84, cy - R)], 'sujet', 1.2)
text(ax, 72, cy - R + 3.5, 'y = −1', 'sujet', 's')
line(ax, [(cx, cy), (cx, cy - R)], 'fixe', 0.6, dash=True)
arc(ax, cx, cy, 10, 0, -90, 'sujet', 1.2)
arc(ax, cx, cy, 16, 0, 270, 'varie', 1.2)
disc(ax, cx, cy - R, 1.7, 'resultat')
text(ax, 60, 52, '−90°', 'sujet', 'm', ha='left')
text(ax, 60, 44, '270°', 'varie', 'm', ha='left')
text(ax, 60, 36, 'même point', 'resultat', 'm', ha='left')
text(ax, cx, 6, 'un seul point par tour', 'resultat', 's')
save(fig, '32-145')
