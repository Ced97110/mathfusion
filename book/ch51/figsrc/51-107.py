import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
# départ -> étape décisive (orange) -> arrivée
box(ax, 22, 80, 44, 11, 'sujet', label=r'$ab = ac$', size='l'); text(ax, 74, 85.5, 'départ', 'sujet', 's')
arrow(ax, (44, 79), (44, 64), 'varie', lw=1.8)
text(ax, 46, 71.5, 'distributivité', 'varie', 's', ha='left', weight='bold')
box(ax, 22, 52, 44, 11, 'varie', label=r'$a(b - c) = 0$', size='l'); text(ax, 74, 57.5, 'produit nul', 'varie', 's')
arrow(ax, (44, 51), (44, 36), 'fixe')
text(ax, 46, 43.5, r'$a \neq 0$, pas de', 'fixe', 's', ha='left'); text(ax, 46, 39.5, 'diviseur de zéro', 'fixe', 's', ha='left')
box(ax, 22, 24, 44, 11, 'autre', label=r'$b - c = 0$', size='l')
arrow(ax, (44, 23), (44, 14), 'fixe')
box(ax, 22, 2.5, 44, 11, 'resultat', label=r'$b = c$', size='l'); text(ax, 74, 8, 'arrivée', 'resultat', 's')
save(fig, '51-107')
