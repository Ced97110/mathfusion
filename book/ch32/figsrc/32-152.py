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
cx, cy, R = 44, 32, 22
disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
line(ax, [(14, cy + R / 2), (74, cy + R / 2)], 'fixe', 0.8, dash=True)
arc(ax, cx, cy, R, -90, 90, 'sujet', 2.4)
disc(ax, *P(cx, cy, R, 30), 1.9, 'resultat'); disc(ax, *P(cx, cy, R, 150), 1.9, 'autre')
text(ax, 76, 49, '30° affiché', 'resultat', 's'); text(ax, 11, 49, '150°', 'autre', 'm'); text(ax, 11, 44.5, 'jamais donné', 'autre', 's')
text(ax, 72, 14, 'moitié choisie', 'sujet', 's')
text(ax, 44, 58, 'sin θ = 0,5', 'encre', 'm')
save(fig, '32-152')
