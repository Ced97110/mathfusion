import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 3, 72, r'éléments de $\mathbb{Z}/8\mathbb{Z}$', 'sujet', 'm', ha='left')
text(ax, 3, 28, r'éléments de $\mathbb{Z}/6\mathbb{Z}$', 'autre', 'm', ha='left')
rows = [(62, '1', 'ordre 8 = 2³', 'sujet', 'resultat'), (50, '2', 'ordre 4 = 2²', 'sujet', 'resultat'),
        (38, '4', 'ordre 2 = 2¹', 'sujet', 'resultat'), (15, '2', 'ordre 3, pas une puissance de 2', 'autre', 'limite')]
for y, e, o, r1, r2 in rows:
    disc(ax, 12, y, 4.2, r1, label=e, size='l')
    arrow(ax, (17.5, y), (30.5, y), 'varie')
    box(ax, 32, y - 5, 52, 10, r2, label=o, size='s')
save(fig, '50-026')
