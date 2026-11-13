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
cx, cy, R = 44, 34, 22
disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
pts = [P(cx, cy, R, 72 * k) for k in range(5)]
for p in pts: line(ax, [(cx, cy), p], 'fixe', 0.5, dash=True)
poly(ax, pts, 'sujet', fill=False, lw=1.2)
for k, p in enumerate(pts):
    disc(ax, *p, 1.8, 'resultat'); x, y = P(cx, cy, R + 5, 72 * k); text(ax, x, y, f'{72 * k}°', 'resultat', 's')
text(ax, 44, 67, 'cos 5θ = 1 : 5 points, 72° d’écart', 'sujet', 's')
save(fig, '32-159')
