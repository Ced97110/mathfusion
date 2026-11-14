import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# Gauche : p = 7, produit 3 × 14 = 42
text(ax, 22, 76, 'p = 7', 'sujet', 'l')
box(ax, 4, 54, 36, 12, 'fixe', label='a b = 3 × 14 = 42', size='s')
text(ax, 22, 48, '7 ∣ 42', 'sujet', 's')
arrow(ax, (22, 53), (22, 30), 'resultat')
box(ax, 4, 16, 36, 12, 'resultat', label='7 ∣ 14   ✓', size='m')
text(ax, 22, 8, 'divise un facteur', 'resultat', 's')
# Droite : p = 6, produit 3 × 4 = 12
text(ax, 66, 76, 'p = 6', 'limite', 'l')
box(ax, 48, 54, 36, 12, 'fixe', label='a b = 3 × 4 = 12', size='s')
text(ax, 66, 48, '6 ∣ 12', 'limite', 's')
arrow(ax, (58, 53), (58, 30), 'limite')
arrow(ax, (74, 53), (74, 30), 'limite')
box(ax, 48, 16, 16, 12, 'limite', label='6 ∤ 3', size='m')
box(ax, 68, 16, 16, 12, 'limite', label='6 ∤ 4', size='m')
text(ax, 66, 8, 'ne divise aucun facteur', 'limite', 's')
save(fig, '56-044')
