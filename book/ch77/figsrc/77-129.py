import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def panel(x, titre, tr, base, tab, coef, role):
    text(ax, x + 18, 66, titre, role, 'm', weight='bold')
    box(ax, x, 50, 36, 9, 'fixe', label=base, size='s')
    box(ax, x, 38, 36, 9, 'fixe', label=tab, size='s')
    box(ax, x, 26, 36, 9, 'varie', label=coef, size='s')
    box(ax, x, 14, 36, 9, 'fixe', label='dimension 2', size='s')
panel(2, r'$A$', 0, r'base $1,\ i$', r'$i\cdot i=-1$', 'coefficients réels', 'sujet')
panel(50, r'$A_K=K\otimes A$', 0, r'base $1,\ j$', r'$j\cdot j=-1$', 'coefficients complexes', 'autre')
arrow(ax, (39, 66), (49, 66), 'varie'); text(ax, 44, 70, r'$\otimes$', 'varie', 'l')
for y in (54.5, 42.5, 18.5): text(ax, 44, y, '=', 'resultat', 'l')
text(ax, 44, 30.5, '≠', 'varie', 'l')
save(fig, '77-129')
