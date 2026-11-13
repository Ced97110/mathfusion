import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
disc(ax, 12, 32, 6, 'fixe', label='7')
text(ax, 12, 22, 'un entier', 'fixe', 's')
box(ax, 40, 14, 46, 36, 'sujet')
text(ax, 63, 44, 'paquet de 7', 'sujet', 's', weight='bold')
for i, v in enumerate(['3', '7', '11']):
    disc(ax, 50 + i * 13, 30, 5, 'sujet', fill=True, label=v, size='s')
arrow(ax, (18.5, 32), (39.5, 32), 'varie')
text(ax, 29, 37, r'$\nu$', 'varie', 'l')
text(ax, 63, 20, 'aucun choix à faire', 'resultat', 's')
text(ax, 44, 6, r'$\nu$ ne dépend que de $G$ et $K$', 'encre', 's')
save(fig, '48-084')
