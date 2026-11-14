import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
box(ax, 3, 20, 24, 20, 'fixe', fill=False, dash=True, label=r'$\varnothing$', size='l')
text(ax, 15, 45, 'ensemble vide', 'fixe', 's'); text(ax, 15, 14, '0 élément', 'fixe', 's')
arrow(ax, (28, 30), (40, 30), 'varie', 1.2); text(ax, 34, 34, 'ses parties', 'varie', 's')
box(ax, 41, 14, 45, 26, 'sujet')
box(ax, 53, 21, 21, 12, 'fixe', fill=False, dash=True, label=r'$\varnothing$', size='l')
text(ax, 63.5, 45, r'$\mathcal{P}(\varnothing)=\{\varnothing\}$', 'sujet', 'm')
text(ax, 63.5, 9, '1 seul sous-ensemble', 'sujet', 's')
text(ax, 44, 2.5, r'$2^0=1$', 'resultat', 'm')
save(fig, '42-288')
