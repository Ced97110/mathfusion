import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(74)
R = 14; cy = 38
c1, c2 = 22, 66
for cx in (c1, c2): disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
p = P(c1, cy, R, 60); line(ax, [(c1, cy), p], 'fixe', 0.6); line(ax, [p, (p[0], cy)], 'fixe', 0.6, dash=True)
line(ax, [(c1, cy), (p[0], cy)], 'sujet', 2.2); disc(ax, *p, 1.6, 'sujet')
q = P(c2, cy, R, 30); line(ax, [(c2, cy), q], 'fixe', 0.6); line(ax, [q, (c2, q[1])], 'fixe', 0.6, dash=True)
line(ax, [(c2, cy), (c2, q[1])], 'varie', 2.2); disc(ax, *q, 1.6, 'varie')
x, y = P(c1, cy, R + 5, 60); text(ax, x, y, '60°', 'sujet', 's')
x, y = P(c2, cy, R + 5, 30); text(ax, x, y, '30°', 'varie', 's')
text(ax, c1, 16, 'cos 60° = 0,5', 'sujet', 's'); text(ax, c2, 16, 'sin 30° = 0,5', 'varie', 's')
text(ax, 44, 6, 'pour θ = 30° : cos 2θ = 1 − 2 × 0,25 = 0,5', 'resultat', 's')
text(ax, 44, 70, 'cos 2θ = 1 − 2 sin² θ', 'encre', 'm')
text(ax, 44, 64, 'vrai pour tout θ', 'resultat', 'm')
save(fig, '32-153')
