import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# gauche : la torsion de l'horloge à deux heures
text(ax, 20, 56, 'Torsion', 'sujet', 'l', weight='bold')
disc(ax, 9, 32, 5, 'fixe', label='0', size='l')
disc(ax, 31, 32, 5, 'sujet', label='1', size='l')
arrow(ax, (30, 37.5), (10, 37.5), 'varie', lw=1.2, curve=0.45)
text(ax, 20, 46, r'$\times\,2$', 'varie', 'm')
text(ax, 20, 8, 'horloge à 2 heures', 'fixe', 's')
text(ax, 20, 19, r'$2 \times 1 = 0$', 'resultat', 'l', weight='bold')
# droite : le changement de base
text(ax, 64, 56, 'Changement de base', 'sujet', 'l', weight='bold')
text(ax, 64, 44, r"$A' = P^{-1}\,A\,P$", 'encre', 'xl')
for i, (s, r) in enumerate([(r"$A'$ : matrice, autre base", 'resultat'),
                            (r'$A$ : matrice, première base', 'sujet'),
                            (r'$P$ : changement de base', 'varie'),
                            (r'$P^{-1}$ : inverse de $P$', 'varie')]):
    text(ax, 47, 33 - 6 * i, s, r, 's', ha='left')
save(fig, '58-332')
