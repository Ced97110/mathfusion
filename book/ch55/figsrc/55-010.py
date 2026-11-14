import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 65, 'problème 1', 'encre', 'm', weight='bold')
text(ax, 66, 65, 'problème 2', 'encre', 'm', weight='bold')
line(ax, [(44, 6), (44, 62)], 'fixe', dash=True)
# problème 1 : tableau -> liste ?
box(ax, 4, 42, 36, 12, 'sujet', label='liste des coefficients', size='s')
box(ax, 4, 12, 36, 12, 'autre', label='tableau de valeurs', size='s')
arrow(ax, (22, 24.5), (22, 41.5), 'varie')
text(ax, 25, 33, 'retrouver ?', 'varie', 's', ha='left')
# problème 2 : coefficients -> quantités des racines ?
box(ax, 48, 42, 36, 12, 'sujet', label='coefficients', size='s')
box(ax, 48, 12, 36, 12, 'autre', label='somme et produit', size='s')
text(ax, 66, 8, 'des racines', 'autre', 's')
arrow(ax, (66, 41.5), (66, 24.5), 'varie')
text(ax, 69, 33, 'retrouver ?', 'varie', 's', ha='left')
save(fig, '55-010')
