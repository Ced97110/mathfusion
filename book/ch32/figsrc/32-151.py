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
R = 11; cy = 32
specs = [(15, 'sinus', 30, 'arcsin 0,5', '= 30°'), (44, 'cosinus', 60, 'arccos 0,5', '= 60°'), (73, 'tangente', 45, 'arctan 1', '= 45°')]
for cx, ttl, ang, nm, val in specs:
    disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
    if ttl == 'sinus': line(ax, [(cx - R - 2, cy + R / 2), (cx + R + 2, cy + R / 2)], 'sujet', 1.2)
    elif ttl == 'cosinus': line(ax, [(cx + R / 2, cy - R - 2), (cx + R / 2, cy + R + 2)], 'sujet', 1.2)
    else: line(ax, [P(cx, cy, R * 1.25, 225), P(cx, cy, R * 1.25, 45)], 'sujet', 1.2)
    line(ax, [(cx, cy), P(cx, cy, R, ang)], 'fixe', 0.6, dash=True)
    arc(ax, cx, cy, R * 0.45, 0, ang, 'varie', 1.2)
    disc(ax, *P(cx, cy, R, ang), 1.6, 'resultat')
    text(ax, cx, cy + R + 6.5, ttl, 'encre', 's')
    text(ax, cx, 17, nm, 'sujet', 's'); text(ax, cx, 11.5, val, 'resultat', 's')
save(fig, '32-151')
