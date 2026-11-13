import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# avant : une infinité de couples sans lien ; après : deux objets, un couple de nombres de sacs
text(ax, 20, 54, 'avant', 'fixe', 'm', weight='bold')
text(ax, 66, 54, 'après : deux sacs types', 'sujet', 'm', weight='bold')
for i in range(6):
    for j in range(5):
        disc(ax, 5 + i * 6.2, 12 + j * 6.2, 1.1, 'fixe')
text(ax, 20, 5, 'une infinité de ventes', 'fixe', 's')
arrow(ax, (40, 30), (47, 30), 'varie', lw=1.3)
# après
box(ax, 50, 36, 15, 9, 'sujet', label=r'$e_1$', size='l', weight='bold')
box(ax, 68, 36, 15, 9, 'autre', label=r'$e_2$', size='l', weight='bold')
text(ax, 66.5, 29, r'$(5,\ 4) = 5\,e_1 + 4\,e_2$', 'encre', 's')
box(ax, 50, 14, 15, 9, 'sujet', label='5', size='l', weight='bold')
box(ax, 68, 14, 15, 9, 'autre', label='4', size='l', weight='bold')
arrow(ax, (57.5, 35.5), (57.5, 24), 'varie', lw=0.9)
arrow(ax, (75.5, 35.5), (75.5, 24), 'varie', lw=0.9)
text(ax, 66.5, 8, 'une seule écriture possible', 'resultat', 's', weight='bold')
save(fig, '58-009')
