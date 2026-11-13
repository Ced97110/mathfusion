import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
box(ax, 22, 82, 44, 10, 'fixe', label='1  1  5  /  2  1  8', size='m')
text(ax, 44, 96, 'les six nombres', 'fixe', 's')
# élimination (gauche) : deux étapes
text(ax, 20, 74, 'élimination', 'autre', 'm')
box(ax, 3, 56, 34, 12, 'autre', label='1. retirer une commande', size='s')
box(ax, 3, 36, 34, 12, 'autre', label='2. lire le prix', size='s')
arrow(ax, (30, 82), (20, 69), 'autre'); arrow(ax, (20, 56), (20, 49), 'autre')
# formule (droite) : une seule boîte
text(ax, 68, 74, 'règle de Cramer', 'sujet', 'm')
box(ax, 52, 56, 32, 12, 'sujet', label='une formule', size='m')
arrow(ax, (58, 82), (68, 69), 'sujet')
# résultats
box(ax, 8, 8, 24, 10, 'resultat', label='3 euros', size='m'); box(ax, 56, 8, 24, 10, 'resultat', label='3 euros', size='m')
arrow(ax, (20, 36), (20, 19), 'autre'); arrow(ax, (68, 56), (68, 19), 'sujet')
text(ax, 44, 27, 'même résultat', 'resultat', 's')
save(fig, '76-008')
