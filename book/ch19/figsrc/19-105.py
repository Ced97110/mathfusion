import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
# stage 1 : the slope from A and B
text(ax, 4, 96.5, 'étape 1 : la pente', 'fixe', 's', ha='left', weight='bold')
box(ax, 4, 80, 34, 11, 'sujet', label=r'$A(1,\,1)$'); box(ax, 50, 80, 34, 11, 'autre', label=r'$B(4,\,3)$')
box(ax, 4, 62, 38, 12, 'varie', label='montée 3 − 1 = 2', size='s'); box(ax, 46, 62, 38, 12, 'resultat', label='avancée 4 − 1 = 3', size='s')
arrow(ax, (21, 80), (21, 74.5), 'fixe'); arrow(ax, (67, 80), (67, 74.5), 'fixe')
box(ax, 26, 44, 36, 12, 'fixe', label=r'pente $\frac{2}{3}$')
arrow(ax, (23, 62), (35, 56.5), 'fixe'); arrow(ax, (65, 62), (53, 56.5), 'fixe')
# stage 2 : the equation, built from the slope and A
line(ax, [(2, 41), (86, 41)], 'fixe', dash=True)
text(ax, 4, 37, 'étape 2 : l’équation', 'fixe', 's', ha='left', weight='bold')
arrow(ax, (44, 44), (44, 31.5), 'varie'); text(ax, 48, 36, 'pente et point A', 'varie', 's', ha='left')
box(ax, 14, 20, 60, 11, 'fixe', label=r'$y-1=\frac{2}{3}(x-1)$')
arrow(ax, (44, 20), (44, 13.5), 'varie')
box(ax, 14, 2, 60, 11, 'resultat', label=r'$y=\frac{2}{3}x+\frac{1}{3}$')
save(fig, '19-105')
