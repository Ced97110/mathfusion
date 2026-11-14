import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(78)
text(ax, 14, 72, 'Entiers', 'sujet', 'm', weight='bold')
text(ax, 62, 72, 'Rotations', 'autre', 'm', weight='bold')
s = 10
ys = [58, 44, 30, 16]
for k, y in enumerate(ys):
    cx, cy = 62, y
    poly(ax, [(cx - s/2, cy - s/2), (cx + s/2, cy - s/2), (cx + s/2, cy + s/2), (cx - s/2, cy + s/2)], 'autre')
    a = math.radians(90 * k); px, py = -s/2 + 2, s/2 - 2
    disc(ax, cx + px*math.cos(a) - py*math.sin(a), cy + px*math.sin(a) + py*math.cos(a), 1.4, 'varie')
    text(ax, 79, y, f'{90*k}°', 'autre', 's')
box(ax, 4, 50, 20, 9, 'sujet', label='1')
box(ax, 4, 22, 20, 9, 'sujet', label='5')
arrow(ax, (24.5, 54.5), (56, 45), 'varie')
arrow(ax, (24.5, 26.5), (56, 43), 'varie')
text(ax, 14, 8, 'les deux : 90°', 'resultat', 's', weight='bold')
text(ax, 14, 41, '× 90°', 'varie', 's')
save(fig, '48-083')
