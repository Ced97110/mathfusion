import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 56, 'un énoncé, une lettre', 'sujet', 's')
box(ax, 32, 40, 24, 12, 'sujet', label=r'$p$', size='xl')
xs = [14, 31, 48, 65]
for x, v in zip(xs, ['2', '3', '5', '7']):
    disc(ax, x, 20, 5, 'fixe', label=v, size='l')
    arrow(ax, (44 + (x - 44) * 0.25, 40), (x + (44 - x) * 0.12, 25.6), 'varie')
text(ax, 79, 20, '…', 'fixe', 'l')
text(ax, 44, 8, r'on choisit une valeur de $p$', 'encre', 's')
save(fig, '50-021')
