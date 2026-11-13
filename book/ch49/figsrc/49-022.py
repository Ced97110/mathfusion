import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
words = [(40, [r'$x$', r'$y$']), (26, [r'$y$', r'$x$']), (12, [r'$x$', r'$x$'])]
rl = {r'$x$': 'sujet', r'$y$': 'autre'}
for y, ls in words:
    for i, l in enumerate(ls): box(ax, 4 + i * 9, y, 8.5, 9, rl[l], label=l)
text(ax, 4, 51.5, 'trois mots', 'encre', 's', ha='left')
text(ax, 4, 4.5, 'l’ordre compte', 'encre', 's', ha='left')
line(ax, [(24, 44.5), (28, 44.5), (28, 30.5), (24, 30.5)], 'fixe')
arrow(ax, (28, 37.5), (33, 37.5), 'fixe')
box(ax, 34, 30, 50, 15, 'fixe', label=r'un seul ensemble $\{x,y\}$', size='s')
text(ax, 59, 22, 'mêmes lettres,', 'encre', 's')
text(ax, 59, 18, 'deux ordres : deux mots', 'encre', 's')
save(fig, '49-022')
