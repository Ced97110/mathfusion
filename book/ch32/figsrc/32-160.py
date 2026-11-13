import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(70)
cx, cy, R = 30, 36, 22
disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
angs = [18 + 36 * k for k in range(10)]
poly(ax, [P(cx, cy, R, a) for a in angs], 'sujet', fill=False, lw=1.0)
for k, a in enumerate(angs):
    disc(ax, *P(cx, cy, R, a), 1.8, 'resultat' if k % 2 == 0 else 'varie')
for a in (18, 54, 90):
    x, y = P(cx, cy, R + 5, a); text(ax, x, y, f'{a}°', 'encre', 's')
arc(ax, cx, cy, 10, 18, 54, 'encre', 1.0); text(ax, cx + 13, cy + 11, '36°', 'encre', 's')
text(ax, 72, 40, '10 sommets', 'sujet', 'm')
disc(ax, 60, 13, 1.8, 'resultat'); text(ax, 64, 13, '5θ = 90°', 'resultat', 's', ha='left')
disc(ax, 60, 7, 1.8, 'varie'); text(ax, 64, 7, '5θ = 270°', 'varie', 's', ha='left')
save(fig, '32-160')
