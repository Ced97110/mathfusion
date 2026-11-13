import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
labs = [(76, r'$2x + 3 = 7$', 'sujet'), (46, r'$2x = 4$', 'fixe'), (16, r'$x = 2$', 'resultat')]
for y, l, r in labs: box(ax, 4, y, 36, 11, r, label=l, size='l')
arrow(ax, (22, 75), (22, 58), 'varie'); arrow(ax, (22, 45), (22, 28), 'varie')
text(ax, 48, 66.5, 'enlève 3 de chaque côté', 'varie', 's', ha='left')
text(ax, 48, 36.5, 'divise chaque côté par 2', 'varie', 's', ha='left')
text(ax, 44, 6, 'chaque pas suit une règle', 'fixe', 'm')
save(fig, '80-486')
