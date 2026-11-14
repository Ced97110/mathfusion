import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 22, 68, 'externe', 'encre', 'm', weight='bold')
text(ax, 66, 68, 'interne', 'encre', 'm', weight='bold')
# externe : on construit une liste de modules donnés
box(ax, 3, 46, 17, 10, 'sujet', label=r'$M_1$')
box(ax, 24, 46, 17, 10, 'autre', label=r'$M_2$')
arrow(ax, (11, 45), (17, 30), 'varie')
arrow(ax, (32, 45), (27, 30), 'varie')
box(ax, 4, 19, 36, 10, 'resultat', label=r'$M_1\oplus M_2$')
text(ax, 22, 10, 'on construit', 'varie', 's', weight='bold')
# interne : le module existe déjà
box(ax, 47, 17, 38, 43, 'fixe', label=None)
text(ax, 66, 54.5, r'$M=\mathbb{Z}^2$', 'fixe', 'm', weight='bold')
box(ax, 52, 31, 28, 10, 'sujet', label='riz pur', size='s')
box(ax, 52, 19.5, 28, 10, 'autre', label='lentilles pur', size='s')
text(ax, 66, 10, 'on constate', 'varie', 's', weight='bold')
save(fig, '58-251')
