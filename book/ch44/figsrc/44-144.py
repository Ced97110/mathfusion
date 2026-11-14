import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
y, h = 18, 12
text(ax, 44, 40, 'additionner modulo 5', 'encre', 'l')
xs = [3, 33, 63]
box(ax, xs[0], y, 22, h, 'sujet', label='7 + 4', size='l')
box(ax, xs[1], y, 22, h, 'varie', label='11', size='l')
box(ax, xs[2], y, 22, h, 'resultat', label='1', size='l')
arrow(ax, (25.5, y + h / 2), (32.5, y + h / 2), 'varie')
arrow(ax, (55.5, y + h / 2), (62.5, y + h / 2), 'varie')
text(ax, 14, y - 4, 'un entier par classe', 'sujet', 's')
text(ax, 44, y - 4, 'somme ordinaire', 'varie', 's')
text(ax, 74, y - 4, 'reste de ÷ 5', 'resultat', 's')
text(ax, 44, 5, '11 = 2 × 5 + 1', 'encre', 'm')
save(fig, '44-144')
