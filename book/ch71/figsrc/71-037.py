import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 4, 48, 'règle (€ par kilo)', 'fixe', 's', ha='left')
text(ax, 84, 48, 'panier de 1 kg ; 2 kg', 'fixe', 's', ha='right')
box(ax, 4, 30, 34, 10, 'sujet', label=r'$f$ : 2 ; 1'); arrow(ax, (40, 35), (58, 35), 'fixe'); box(ax, 60, 30, 22, 10, 'resultat', label='4 €')
box(ax, 4, 4, 34, 10, 'varie', label=r'$2f$ : 4 ; 2'); arrow(ax, (40, 9), (58, 9), 'fixe'); box(ax, 60, 4, 22, 10, 'resultat', label='8 €')
arrow(ax, (21, 29), (21, 15), 'varie'); text(ax, 28, 22, r'$\times 2$', 'varie')
arrow(ax, (71, 29), (71, 15), 'varie'); text(ax, 78, 22, r'$\times 2$', 'varie')
save(fig, '71-037')
