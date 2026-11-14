import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 19, 38, 11
for k in range(4):
    a = math.radians(90 - 90 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 3.3, 'fixe', label=str(k), size='s')
text(ax, cx, 16, 'définition : on repart de 0', 'fixe', 's')
text(ax, cx, 11, 'rien sur la distributivité', 'fixe', 's')
box(ax, 44, 38, 42, 18, 'resultat')
text(ax, 65, 51, 'constat : les deux', 'resultat', 's', weight='bold')
text(ax, 65, 44, '3×(2+3) = 3×2+3×3', 'resultat', 's')
box(ax, 44, 6, 42, 14, 'varie')
text(ax, 65, 15, 'pourquoi ?', 'varie', 'l', weight='bold')
text(ax, 65, 10, 'à expliquer ensuite', 'varie', 's')
arrow(ax, (33, 38), (44, 44), 'fixe')
arrow(ax, (65, 38), (65, 20), 'varie')
save(fig, '51-003')
