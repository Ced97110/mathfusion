import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
box(ax, 2, 54, 40, 12, 'sujet', label='10 = 2 × 5')
box(ax, 46, 54, 40, 12, 'sujet', label='10⁸¹ multiple de 5', size='s')
cx, cy, R = 44, 24, 14
for i in range(5):
    th = math.radians(90 - 72 * i)
    disc(ax, cx + R * math.cos(th), cy + R * math.sin(th), 4.5, 'resultat' if i == 0 else 'fixe', label=str(i))
text(ax, cx, cy, 'même\nreste 0', 'resultat', 's')
arrow(ax, (22, 53.5), (40.5, 41.5), 'varie')
arrow(ax, (66, 53.5), (47.5, 41.5), 'varie')
text(ax, 44, 3.5, 'horloge à 5 cases', 'fixe', 's')
save(fig, '53-140')
