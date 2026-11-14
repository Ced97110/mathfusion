import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 22, 56, 44, 10, 'fixe', label='celle qui veut recevoir')
arrow(ax, (44, 55.5), (44, 45), 'varie')
text(ax, 58, 50.5, 'un prénom', 'varie', 's')
disc(ax, 44, 36, 8, 'sujet', label='Alice', size='l')
for x, lab in [(2, 'fabrique les clés'), (30.5, 'garde la clé privée'), (59, 'publie la clé publique')]:
    box(ax, x, 6, 27.5, 10, 'resultat', label=lab, size='s')
arrow(ax, (39, 28.7), (17, 16.6), 'varie')
arrow(ax, (44, 27.5), (44.2, 16.6), 'varie')
arrow(ax, (49, 28.7), (71, 16.6), 'varie')
save(fig, '53-084')
