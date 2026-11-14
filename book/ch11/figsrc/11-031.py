import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 14, 53, 'on mesure', 'fixe', 's'); text(ax, 44, 53, 'grandeur', 'fixe', 's'); text(ax, 74, 53, 'unité de base', 'sujet', 's')
for k, (a, b, c) in enumerate([('une route', 'longueur', 'mètre'), ('un sac', 'masse', 'gramme'), ('une bouteille', 'capacité', 'litre')]):
    y = 38 - k * 15
    box(ax, 2, y, 24, 9, 'fixe', label=a, size='s'); box(ax, 32, y, 24, 9, 'fixe', label=b, size='s'); box(ax, 62, y, 24, 9, 'sujet', label=c, size='s')
    arrow(ax, (26, y + 4.5), (32, y + 4.5), 'varie'); arrow(ax, (56, y + 4.5), (62, y + 4.5), 'varie')
save(fig, '11-031')
