import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 2, 72, 'Chemin 1 : la descente', 'sujet', 's', ha='left')
labs = [r'$2^1=2$', r'$2^0=1$', r'$2^{-1}$']
for k, x in enumerate((2, 32, 62)):
    box(ax, x, 50, 24, 14, ('sujet', 'sujet', 'resultat')[k], label=labs[k], size='m')
    if k < 2: arrow(ax, (x + 25, 57), (x + 29, 57), 'varie')
text(ax, 29, 67, '÷ 2', 'varie', 's'); text(ax, 59, 67, '÷ 2', 'varie', 's')
text(ax, 2, 40, 'Chemin 2 : règle du quotient', 'autre', 's', ha='left')
box(ax, 2, 22, 50, 14, 'autre', label=r'$2^{-1}=\frac{1}{2^1}$', size='m')
arrow(ax, (53, 29), (62, 40), 'autre') if False else None
box(ax, 62, 22, 24, 14, 'resultat', label=r'$\frac{1}{2}$', size='l')
arrow(ax, (53, 29), (61, 29), 'autre')
arrow(ax, (74, 49), (74, 37), 'resultat')
box(ax, 14, 2, 60, 12, 'resultat', label=r'$2\times\frac{1}{2}=1$', size='m')
save(fig, '14-062')
