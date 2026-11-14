import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [('Léa', 40, (2, 3, 4), 'sujet'), ('Théo', 10, (4, 2, 3), 'autre')]
for name, y, order, role in rows:
    text(ax, 7, y + 6, name, role, 'm')
    for i, n in enumerate(order):
        box(ax, 15 + 15 * i, y, 13, 12, role, label=rf'$x-{n}$', size='s')
    arrow(ax, (59, y + 6), (66, 31 if y > 20 else 25), 'resultat')
box(ax, 66, 20, 20, 16, 'resultat', label='9, 26, 24', size='s')
text(ax, 76, 15, 'mêmes', 'resultat', 's'); text(ax, 76, 10, 'coefficients', 'resultat', 's')
text(ax, 36, 56, 'ordre différent', 'fixe', 's')
save(fig, '55-072')
