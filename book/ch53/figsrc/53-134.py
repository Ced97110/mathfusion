import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
rows = [
    (70, ('16', 'resultat'), ('26', 'resultat'), ('31', 'varie'), '16 × 26 = 416 = 7 × 55 + 31'),
    (44, ('31', 'varie'), ('14', 'resultat'), ('49', 'varie'), '31 × 14 = 434 = 7 × 55 + 49'),
    (18, ('49', 'varie'), ('17', 'resultat'), ('8', 'sujet'), '49 × 17 = 833 = 15 × 55 + 8'),
]
for y, a, b, r, calc in rows:
    box(ax, 2, y, 18, 11, a[1], label=a[0])
    cx, cy = 24, y + 5.5
    line(ax, [(cx - 1.3, cy - 1.3), (cx + 1.3, cy + 1.3)], 'fixe'); line(ax, [(cx - 1.3, cy + 1.3), (cx + 1.3, cy - 1.3)], 'fixe')
    box(ax, 28, y, 18, 11, b[1], label=b[0])
    arrow(ax, (47.5, cy), (55.5, cy), 'varie')
    box(ax, 56, y, 22, 11, r[1], label=r[0])
    text(ax, 40, y - 5, calc, 'fixe', 's')
text(ax, 44, 3, 'plus grand produit : 833 < 3 025', 'fixe', 's')
save(fig, '53-134')
