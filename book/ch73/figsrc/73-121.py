import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
u = 9
box(ax, 14, 10, 2 * u, 3 * u, 'sujet', r=0.2); box(ax, 14, 10, u, u, 'fixe', r=0.2)
text(ax, 18.5, 14.5, '1', 'fixe', 's'); text(ax, 23, 28, 'aire 6', 'sujet', 'm')
text(ax, 23, 6, '2', 'sujet', 's'); text(ax, 9, 23.5, '3', 'sujet', 's')
arrow(ax, (34, 24), (49, 24), 'varie')
box(ax, 51, 18, 35, 12, 'resultat', label=r'$\det A = 6$', size='l')
text(ax, 68.5, 35, "aire de l'image du carré", 'resultat', 's'); text(ax, 68.5, 11, r'$A$ : (2, 0) et (0, 3)', 'varie', 's')
save(fig, '73-121')
