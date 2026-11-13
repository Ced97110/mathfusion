import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 14, 52, 60, 14, 'sujet', label=r'$Sp_{2n}(\mathbb{F}_2)$', size='l')
arrow(ax, (44, 51.5), (44, 40.5), 'varie'); text(ax, 62, 46, r'$n=2$', 'varie', 'm')
box(ax, 24, 28, 40, 12, 'resultat', label='720 éléments', size='m')
arrow(ax, (44, 27.5), (44, 16.5), 'varie'); text(ax, 62, 22, 'compte', 'varie', 'm')
box(ax, 6, 3, 76, 13, 'autre', label='circuits quantiques simulables', size='s')
save(fig, '75-185')
