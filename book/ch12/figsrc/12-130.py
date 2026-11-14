import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 8, 50, 10, 9, 'fixe', label='6', size='l'); box(ax, 20, 50, 10, 9, 'varie', label=r'$x$', size='l')
text(ax, 13, 46, 'nombre', 'fixe', 's'); text(ax, 25, 46, 'lettre', 'varie', 's')
arrow(ax, (32, 54.5), (50, 54.5), 'varie'); text(ax, 41, 58, r'$x=3$', 'varie', 's')
box(ax, 52, 50, 14, 9, 'resultat', label='18', size='l')
xs = [4, 16, 28, 40, 52, 64]
specs = [('4', 'fixe'), ('(', 'autre'), ('5', 'fixe'), ('+', 'sujet'), ('2', 'fixe'), (')', 'autre')]
for x, (s, r) in zip(xs, specs): box(ax, x, 20, 10, 9, r, label=s, size='l')
text(ax, 45, 15, 'opération', 'sujet', 's'); text(ax, 21, 15, 'groupement', 'autre', 's', ha='center')
save(fig, '12-130')
