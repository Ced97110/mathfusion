import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 3, 24, 20, 10, 'sujet', label='étalon', size='s')
for k, (name, y) in enumerate([('Paris', 40), ('Lyon', 10)]):
    arrow(ax, (23, 29), (33, y + 3.5), 'varie')
    text(ax, 35, y + 10, name, 'fixe', 's', ha='left')
    for i in range(4):
        box(ax, 34 + i * 11, y, 11, 7, 'autre', lw=0.8)
    text(ax, 83, y + 3.5, '4', 'resultat', 'l')
text(ax, 13, 38, 'copie exacte', 'varie', 's')
text(ax, 58, 28, '4 pouces = 4 pouces', 'resultat', 'm')
save(fig, '11-019')
