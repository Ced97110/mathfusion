import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 58, r'$\frac{x+1}{x-1}$', 'sujet', 'xl')
box(ax, 4, 6, 38, 30, 'resultat'); box(ax, 46, 6, 38, 30, 'limite')
arrow(ax, (36, 50), (23, 37), 'fixe'); arrow(ax, (52, 50), (65, 37), 'fixe')
text(ax, 23, 31, '$x = 3$', 'resultat', 'm'); text(ax, 23, 21, r'$\frac{4}{2} = 2$', 'resultat', 'm'); text(ax, 23, 11, 'permis', 'resultat', 's')
text(ax, 65, 31, '$x = 1$', 'limite', 'm'); text(ax, 65, 21, r'$\frac{2}{0}$', 'limite', 'm'); text(ax, 65, 11, 'bas = 0 : interdit', 'limite', 's')
save(fig, '09-123')
