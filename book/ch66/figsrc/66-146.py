import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
cx, cy, R = 18, 32, 12
disc(ax, cx, cy, R, 'fixe', fill=False)
for k in range(8):
    a = k * math.pi / 4
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 1.7, 'sujet')
text(ax, cx, 13, 'racines de l’unité', 'sujet', 's')
arrow(ax, (33, 32), (45, 32), 'varie')
box(ax, 46, 25, 40, 16, 'autre')
text(ax, 66, 35, 'transformée de Fourier', 'autre', 's')
text(ax, 66, 30, 'discrète', 'autre', 's')
arrow(ax, (53, 25), (55, 14), 'resultat'); arrow(ax, (79, 25), (77, 14), 'resultat')
text(ax, 66, 20, 'compresser', 'fixe', 's')
box(ax, 46, 3, 18, 10, 'resultat', label='son')
box(ax, 68, 3, 18, 10, 'resultat', label='images')
save(fig, '66-146')
