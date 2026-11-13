import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 20, 54, 'nombres précis', 'fixe', 'm')
text(ax, 68, 54, 'nombres quelconques', 'sujet', 'm')
for i, s in enumerate(('3 et 4', '4 et 3', '10 et 6')):
    box(ax, 8, 38 - i * 12, 24, 9, 'fixe', label=s)
arrow(ax, (36, 28), (52, 28), 'varie')
disc(ax, 60, 36, 5, 'sujet', label='$x$', size='l')
disc(ax, 60, 20, 5, 'sujet', label='$y$', size='l')
text(ax, 77, 36, 'un nombre', 'sujet', 's')
text(ax, 77, 20, 'un nombre', 'sujet', 's')
text(ax, 44, 5, 'une phrase pour tous les couples', 'encre', 's')
save(fig, '12-020')
