import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

fig, ax = canvas(74)

# Question commune aux deux méthodes
text(ax, 44, 69, '432 ÷ 3 a-t-il un reste 0 ?', 'encre', 'm')

# Méthode 1 : la division (violet, en haut)
text(ax, 3, 60, 'la division : 432 ÷ 3', 'autre', 's', ha='left')
for x0 in (4, 22, 40):
    box(ax, x0, 44, 18, 8, 'autre', label='144', size='m')
arrow(ax, (58, 48), (67, 48), 'fixe', lw=0.9)
box(ax, 67, 42, 19, 12, 'autre', label='144, reste 0', size='s')

# Séparation des deux méthodes
line(ax, [(2, 38), (86, 38)], 'fixe', lw=0.9)

# Méthode 2 : le critère (bleu, en bas)
text(ax, 3, 33, 'le critère : chiffres de 432', 'sujet', 's', ha='left', weight='bold')
for x0, chiffre in ((4, '4'), (12, '3'), (20, '2')):
    box(ax, x0, 20, 7, 8, 'sujet', label=chiffre, size='m')
arrow(ax, (27, 24), (33, 24), 'sujet', lw=1.0)
text(ax, 45, 26.5, '4 + 3 + 2 = 9', 'sujet', 'm')
text(ax, 45, 20.5, '3 divise 9', 'sujet', 's')
arrow(ax, (57, 24), (67, 24), 'fixe', lw=0.9)
box(ax, 67, 18, 19, 12, 'resultat', label='oui', size='l')
text(ax, 76.5, 12, 'pas de quotient', 'resultat', 's')

save(fig, '03-087')
