import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# changement de base : le stock reste, les nombres changent ; transporteur : le stock change
text(ax, 22, 57, 'changement de base', 'sujet', 'm', weight='bold')
text(ax, 66, 57, 'transporteur', 'fixe', 'm', weight='bold')
line(ax, [(44, 8), (44, 52)], 'fixe', lw=0.5, dash=True)
# gauche : un seul stock, deux descriptions
box(ax, 5, 34, 34, 11, 'resultat', label='même stock (5, 4)', size='s', weight='bold')
box(ax, 1, 8, 20, 10, 'sujet', label='5 et 4', size='s')
box(ax, 23, 8, 20, 10, 'autre', label='1 et 3', size='s')
arrow(ax, (12, 33.5), (11, 18.5), 'sujet', lw=1.0)
arrow(ax, (32, 33.5), (33, 18.5), 'autre', lw=1.0)
text(ax, 11, 23.5, 'sacs', 'sujet', 's', ha='right')
text(ax, 33, 23.5, 'lots', 'autre', 's', ha='left')
# droite : deux stocks différents
box(ax, 52, 36, 30, 10, 'fixe', label='stock (5, 4)', size='s')
arrow(ax, (67, 35.5), (67, 19.5), 'varie', lw=1.3)
box(ax, 52, 8, 30, 11, 'varie', label='autre stock (14, 17)', size='s', weight='bold')
save(fig, '58-017')
