import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 4, 38, 18, 11, 'sujet', label=r'$5x$'); text(ax, 28, 43.5, 'veut dire', 'fixe', 's', ha='left')
for i in range(5):
    x = 4 + i * 16.5
    box(ax, x, 18, 11, 11, 'sujet', label=r'$x$')
    if i < 4: text(ax, x + 13.75, 23.5, '+', 'varie', 'l')
brace(ax, 4, 4 + 4 * 16.5 + 11, 16, 'resultat', 'cinq fois $x$', size='m')
arrow(ax, (13, 37), (13, 30.5), 'fixe')
save(fig, '15-029')
