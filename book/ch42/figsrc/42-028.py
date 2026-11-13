import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 4, 38, 48, 22, 'fixe'); text(ax, 9, 55, r'$S$', 'fixe', 's', ha='left')
disc(ax, 20, 46, 5, 'fixe', label=r'$a$'); disc(ax, 38, 46, 5, 'fixe', label=r'$b$')
disc(ax, 68, 49, 5, 'varie', label=r'$c$'); text(ax, 68, 40, 'c : la lampe', 'varie', 's')
box(ax, 6, 18, 44, 11, 'resultat', label=r'$c\notin S$', size='l'); text(ax, 66, 23.5, 'vrai', 'resultat', 'm')
box(ax, 6, 3, 44, 11, 'limite', label=r'$c\in S$', size='l'); text(ax, 66, 8.5, 'faux', 'limite', 'm')
save(fig, '42-028')
