import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 23, 56, 'chapitre 3 : ranger', 'autre', 's'); text(ax, 65, 56, 'chapitre 9 : comparer', 'sujet', 's')
box(ax, 3, 38, 40, 12, 'autre', label='50 objets par paquets de 2', size='s')
box(ax, 45, 38, 40, 12, 'sujet', label='50 miles pour 2 gallons', size='s')
box(ax, 24, 4, 40, 14, 'resultat', label=r'$50 \div 2 = 25$', size='l', weight='bold')
arrow(ax, (23, 37), (38, 19), 'fixe'); arrow(ax, (65, 37), (50, 19), 'fixe')
text(ax, 44, 28, 'même calcul', 'fixe', 's')
save(fig, '09-124')
