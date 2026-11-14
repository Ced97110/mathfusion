import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 3, 40, 14, 9, 'fixe', label='17'); box(ax, 31, 40, 14, 9, 'sujet', label='5')
box(ax, 66, 40, 14, 9, 'resultat', label='1'); box(ax, 31, 16, 14, 9, 'sujet', label='9')
arrow(ax, (17, 44.5), (31, 44.5), 'varie'); text(ax, 24, 48.5, 'par 12', 'varie', 's')
arrow(ax, (45, 44.5), (66, 44.5), 'varie'); text(ax, 55.5, 48.5, 'par 4', 'varie', 's')
arrow(ax, (45, 22), (70, 39.5), 'varie')
text(ax, 44, 8, '5 et 9 : même reste par 4', 'encre', 's')
save(fig, '52-267')
