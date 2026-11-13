import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for y, a, b, c in [(60, 17, 5, 1), (22, 26, 2, 2)]:
    box(ax, 2, y - 4.5, 14, 9, 'fixe', label=str(a)); box(ax, 38, y - 4.5, 14, 9, 'sujet', label=str(b))
    box(ax, 72, y - 4.5, 14, 9, 'resultat', label=str(c))
    arrow(ax, (16, y), (38, y), 'varie'); text(ax, 27, y + 3.5, 'par 12', 'varie', 's')
    arrow(ax, (52, y), (72, y), 'varie'); text(ax, 62, y + 3.5, 'par 4', 'varie', 's')
    arrow(ax, (9, y - 5), (79, y - 5), 'resultat', curve=0.1)
    text(ax, 44, y - 13, 'direct : par 4', 'resultat', 's')
save(fig, '52-269')
