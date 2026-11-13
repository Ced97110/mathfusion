import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 59, 'livre français', 'sujet', 's'); text(ax, 66, 59, 'livre anglais', 'autre', 's')
box(ax, 4, 40, 36, 14, 'sujet', label='cosec 30°'); box(ax, 48, 40, 36, 14, 'autre', label='csc 30°')
box(ax, 24, 4, 40, 14, 'resultat', label='1 / 0,5 = 2')
arrow(ax, (22, 40), (36, 18), 'varie'); arrow(ax, (66, 40), (52, 18), 'varie')
text(ax, 44, 29, 'même fonction', 'varie', 's')
save(fig, '30-074')
