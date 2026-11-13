import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 3, 50, 39, 11, 'sujet', label=r'$\det P=2\times1-1\times1=1$', size='s')
box(ax, 46, 50, 39, 11, 'autre', label=r'$\det Q=1\times2-(-1)^2=1$', size='s')
arrow(ax, (22.5, 49.5), (33, 40.5), 'fixe')
arrow(ax, (65.5, 49.5), (55, 40.5), 'fixe')
text(ax, 44, 45, 'étape clé', 'varie', 's', weight='bold')
box(ax, 3, 29, 82, 11, 'varie', label=r'$\det P\times\det Q=\det(PQ)=1$', size='s')
arrow(ax, (44, 28.5), (44, 23.5), 'fixe')
box(ax, 3, 6, 82, 17, 'resultat', size='s',
    label='deux entiers de produit 1 :\n(1, 1) ou (−1, −1),\ndonc 1 ou $-1$')
save(fig, '58-230')
