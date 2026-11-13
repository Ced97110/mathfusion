import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(66)
cx, cy, R = 24, 40, 17
disc(ax, cx, cy, R, 'fixe', fill=False); axes(ax, cx, cy, R)
line(ax, [(4, cy + R / 2), (44, cy + R / 2)], 'fixe', 0.8, dash=True)
p, q = P(cx, cy, R, 30), P(cx, cy, R, 150)
disc(ax, *p, 1.8, 'sujet'); disc(ax, *q, 1.8, 'autre')
text(ax, p[0] + 3, p[1] + 3.5, 'P', 'sujet', 'm'); text(ax, q[0] - 3, q[1] + 3.5, 'P′', 'autre', 'm')
text(ax, cx, 16, 'sin B = 0,5', 'encre', 'm')
B1, C1 = (54, 50), (84, 50); A1 = (B1[0] + 14 * math.cos(math.radians(30)), B1[1] + 14 * math.sin(math.radians(30)))
poly(ax, [B1, C1, A1], 'sujet'); arc(ax, B1[0], B1[1], 6, 0, 30, 'varie', 1.0)
text(ax, 69, 44, 'B = 30°', 'sujet', 'm')
B2, C2 = (60, 22), (84, 22); A2 = (B2[0] + 14 * math.cos(math.radians(150)), B2[1] + 14 * math.sin(math.radians(150)))
poly(ax, [B2, C2, A2], 'autre'); arc(ax, B2[0], B2[1], 6, 0, 150, 'varie', 1.0)
text(ax, 68, 15, 'B = 150°', 'autre', 'm')
save(fig, '32-155')
