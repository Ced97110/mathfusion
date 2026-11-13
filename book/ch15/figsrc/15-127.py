import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 34, 50, 20, 11, 'resultat', label='0', size='l')
box(ax, 4, 28, 36, 11, 'sujet', label=r'$0x^5$', size='m'); box(ax, 48, 28, 36, 11, 'autre', label=r'$0x^{100}$', size='m')
arrow(ax, (38, 50), (24, 39.5), 'fixe'); arrow(ax, (50, 50), (64, 39.5), 'fixe')
text(ax, 22, 23, 'degré 5 ?', 'sujet', 's'); text(ax, 66, 23, 'degré 100 ?', 'autre', 's')
text(ax, 44, 14, 'deux degrés : impossible', 'limite', 's')
text(ax, 44, 6, 'le polynôme nul : aucun degré', 'resultat', 's')
save(fig, '15-127')
