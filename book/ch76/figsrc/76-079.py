import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 17, 52, 'exemples', 'autre', 's'); text(ax, 72, 52, 'sur $A$ on peut', 'resultat', 's')
for k, lab in enumerate(['tableaux', 'nombres complexes', 'polynômes']):
    box(ax, 2, 36 - k * 14, 30, 9, 'autre', label=lab, size='s')
    arrow(ax, (33, 40.5 - k * 14), (40, 28 + 3 * (1 - k)), 'fixe', lw=0.8)
box(ax, 40, 18, 16, 20, 'sujet', label='$A$', size='xl')
for k, lab in enumerate(['additionner', 'multiplier', 'nombre fois élément']):
    box(ax, 60, 36 - k * 14, 26, 9, 'resultat', label=lab, size='s')
    arrow(ax, (57, 28 + 3 * (1 - k)), (59.5, 40.5 - k * 14), 'fixe', lw=0.8)
text(ax, 28, 4, 'une algèbre quelconque', 'sujet', 's')
save(fig, '76-079')
