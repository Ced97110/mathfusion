import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
text(ax, 44, 45, r'$f : V \to F$', 'encre', 'xl')
box(ax, 3, 12, 22, 22, 'sujet', label=r'$V$', size='xl')
box(ax, 33, 12, 22, 22, 'varie', label=r'$f$', size='xl')
box(ax, 63, 12, 22, 22, 'resultat', label=r'$F$', size='xl')
arrow(ax, (25, 23), (33, 23), 'fixe'); arrow(ax, (55, 23), (63, 23), 'fixe')
text(ax, 14, 8, 'vecteurs', 'sujet', 's'); text(ax, 44, 8, 'la règle', 'varie', 's'); text(ax, 74, 8, 'nombres', 'resultat', 's')
text(ax, 14, 37.5, 'départ', 'sujet', 's'); text(ax, 74, 37.5, 'arrivée', 'resultat', 's')
save(fig, '71-130')
