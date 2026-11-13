import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 8, 62, 30, 11, 'fixe', label=r'$p$', size='m'); box(ax, 50, 62, 30, 11, 'fixe', label=r'$q$', size='m')
arrow(ax, (40, 67.5), (48, 67.5), 'fixe')
arrow(ax, (30, 61), (58, 41), 'varie'); arrow(ax, (58, 61), (30, 41), 'varie')
text(ax, 18, 51, 'on échange', 'varie', 's'); text(ax, 70, 51, 'et on met « non »', 'varie', 's')
box(ax, 8, 30, 30, 11, 'sujet', label=r'non $q$', size='m'); box(ax, 50, 30, 30, 11, 'sujet', label=r'non $p$', size='m')
arrow(ax, (40, 35.5), (48, 35.5), 'sujet')
text(ax, 44, 24.5, 'contraposée', 'sujet', 's')
box(ax, 4, 6, 38, 10, 'resultat', label='7 : pas pair', size='s'); box(ax, 46, 6, 38, 10, 'resultat', label='7 : pas multiple de 4', size='s')
arrow(ax, (43.2, 11), (44.8, 11), 'resultat') if False else None
save(fig, '42-107')
