import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
items = [('sujet', 'partir de a = 3'), ('fixe', 'écart voulu par 5 : 1'), ('varie', 'en pas de 4 : 1 × 4 = 4'), ('resultat', 'arrivée : 19')]
for i, (role, lab) in enumerate(items):
    y = 54 - i * 16
    box(ax, 12, y, 64, 10, role, label=lab)
    if i < 3: arrow(ax, (44, y), (44, y - 6), 'varie')
save(fig, '52-191')
