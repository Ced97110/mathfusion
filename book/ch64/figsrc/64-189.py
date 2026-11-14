import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 14, 70, 60, 14, 'fixe', label='équation générale, degré $n$\ncoefficients : $t_1,\\ldots,t_n$', size='s')
box(ax, 2, 40, 40, 14, 'sujet', label=r'$G=S_n$ (chapitre 65)', size='s')
box(ax, 46, 40, 40, 14, 'autre', label=r'$S_n$ non résoluble, $n\geq5$', size='s')
arrow(ax, (44, 69), (24, 55), 'varie'); arrow(ax, (44, 69), (66, 55), 'varie')
box(ax, 12, 6, 64, 14, 'resultat', label='aucune formule par radicaux', size='s')
arrow(ax, (22, 39), (34, 21), 'resultat'); arrow(ax, (66, 39), (54, 21), 'resultat')
save(fig, '64-189')
