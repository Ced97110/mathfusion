import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 6, 44, 18, 11, 'limite', label='34', size='l')
text(ax, 54, 49.5, 'un seul nombre : trente-quatre', 'limite', 's', ha='center')
line(ax, [(2, 38), (86, 38)], 'fixe', lw=0.5, dash=True)
box(ax, 6, 16, 18, 11, 'sujet', label='(3)', size='l')
box(ax, 24, 16, 18, 11, 'sujet', label='(4)', size='l')
text(ax, 15, 11, 'deux nombres', 'sujet', 's')
text(ax, 33, 11, 'séparés', 'sujet', 's') if False else None
arrow(ax, (45, 21.5), (56, 21.5), 'varie')
text(ax, 50.5, 33, 'rien entre eux', 'varie', 's', ha='center')
box(ax, 58, 16, 26, 11, 'resultat', label='3 fois 4 = 12')
save(fig, '12-025')
