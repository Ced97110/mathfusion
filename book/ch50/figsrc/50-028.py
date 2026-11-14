import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
cx, cy, R, r = 27, 30, 17, 3.4
pos = {}
for i in range(6):
    a = math.radians(90 - 60 * i); pos[i] = (cx + R * math.cos(a), cy + R * math.sin(a))
for i in range(6):
    disc(ax, *pos[i], r, 'varie' if i in (0, 2, 4) else 'fixe', label=str(i), size='m')
text(ax, cx, cy, r'$\mathbb{Z}/6\mathbb{Z}$', 'encre', 's')
for a, b in [(0, 2), (2, 4), (4, 0)]:
    (x1, y1), (x2, y2) = pos[a], pos[b]
    d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    arrow(ax, (x1 + ux * (r + 0.4), y1 + uy * (r + 0.4)), (x2 - ux * (r + 0.4), y2 - uy * (r + 0.4)), 'varie')
text(ax, 67, 54, 'pas de 2 en 2 :', 'encre', 's')
text(ax, 67, 47, r'$0\to2\to4\to0$', 'varie', 'm')
box(ax, 52, 28, 32, 11, 'limite', label="3 pas : ordre 3", size='s')
text(ax, 68, 20, 'pas une puissance de 2', 'limite', 's')
save(fig, '50-028')
