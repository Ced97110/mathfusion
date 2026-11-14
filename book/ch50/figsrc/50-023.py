import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
text(ax, 24, 54, r'$\mathbb{Z}/8\mathbb{Z}$ : $8=2^3$', 'sujet', 'm')
for i in range(8):
    a = math.radians(90 - 45 * i)
    disc(ax, 24 + 15 * math.cos(a), 27 + 15 * math.sin(a), 3.2, 'sujet', label=str(i), size='s')
text(ax, 66, 54, r'rotations : $3=3^1$', 'autre', 'm')
def tri(cx, cy, R, th):
    return [(cx + R * math.cos(math.radians(90 + 120 * k + th)), cy + R * math.sin(math.radians(90 + 120 * k + th))) for k in range(3)]
for i, (cx, nm) in enumerate([(53, 'e'), (66, 'r'), (79, r'$r^2$')]):
    poly(ax, tri(cx, 33, 5.8, 0), 'autre')
    mx, my = tri(cx, 33, 5.8, 0)[0]
    p = tri(cx, 33, 5.8, 0)[i]
    disc(ax, p[0], p[1], 1.4, 'varie')
    text(ax, cx, 19, nm, 'autre', 'm')
save(fig, '50-023')
