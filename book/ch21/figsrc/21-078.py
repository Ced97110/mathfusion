import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 4, 28, 20, 16, 'sujet', label=r'$\frac{1}{6}$'); box(ax, 64, 28, 20, 16, 'resultat', label=r'$\frac{2}{12}$')
arrow(ax, (25, 36), (63, 36), 'varie')
text(ax, 44, 41.5, r'haut et bas $\times2$', 'varie', 's'); text(ax, 44, 31, 'même valeur', 'resultat', 's')
text(ax, 36, 11, r'$\frac{P\times b}{Q\times b}=\frac{P}{Q}$', 'encre', 'm'); text(ax, 74, 11, r'$b\neq0$', 'encre', 'm')
save(fig, '21-078')
