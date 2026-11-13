import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x, s in [(31.5, 'millions'), (53, 'mille'), (74.5, 'unités')]:
    text(ax, x, 62, s, 'fixe', 's')
# ligne du haut : écriture juste
box(ax, 22, 48, 19, 8, 'fixe', label='10', size='l')
box(ax, 43.5, 48, 19, 8, 'sujet', label='000', size='l')
box(ax, 65, 48, 19, 8, 'fixe', label='512', size='l')
text(ax, 3, 52, '10 000 512', 'resultat', 'm', ha='left')
text(ax, 31.5, 44.6, '10 000 000', 'resultat', 's')
# ligne du bas : écriture fausse, sans les 0
box(ax, 22, 20, 19, 8, 'limite', fill=False, dash=True)
box(ax, 43.5, 20, 19, 8, 'limite', label='10', size='l')
box(ax, 65, 20, 19, 8, 'fixe', label='512', size='l')
text(ax, 3, 24, '10 512', 'limite', 'm', ha='left')
text(ax, 53, 31.8, '10 000', 'limite', 's')
arrow(ax, (33, 42.0), (50.5, 35.3), 'limite')
text(ax, 72, 39.5, '1 000 fois plus petit', 'limite', 's')
text(ax, 53, 12, 'les 0 gardent la place', 'resultat', 's')
save(fig, '01-090')
