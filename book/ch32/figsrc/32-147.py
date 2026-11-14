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
R = 15
for cx, lx, lab, ang, ttl, tx in ((22, 37, '0°', 0, 'cos θ = 1', 24), (66, 51, '180° = −180°', 180, 'cos θ = −1', 64)):
    cy = 32
    disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
    line(ax, [(lx, 11), (lx, 53)], 'sujet', 1.2)
    disc(ax, lx, cy, 1.7, 'resultat')
    text(ax, tx, 57, ttl, 'sujet', 's'); text(ax, cx, 10, lab, 'resultat', 's')
text(ax, 44, 3.5, 'une solution par tour', 'resultat', 's')
save(fig, '32-147')
