import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# trois outils reliés à leur sens : coordonnées, système, anneau de tableaux
rows = [
    ('coordonnées de (14, 17)', r'$14\,e_1 + 17\,e_2$', 'sujet'),
    ('système linéaire', r'$A\,x = y$', 'varie'),
    ('produit de tableaux', 'composition', 'autre'),
]
text(ax, 20, 64, 'outil', 'fixe', 's')
text(ax, 68, 64, 'sens', 'fixe', 's')
for i, (a, b, role) in enumerate(rows):
    y = 46 - i * 20
    box(ax, 3, y, 36, 12, role, label=a, size='s')
    box(ax, 52, y, 34, 12, role, label=b, size='m')
    arrow(ax, (40, y + 6), (51, y + 6), role, lw=1.2)
save(fig, '58-340')
