import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
# départ
box(ax, 14, 66, 60, 16, 'sujet', label=r'$\frac{2}{3}+\frac{4}{5}$', size='l')
# produits en croix
arrow(ax, (30, 66), (24, 54), 'varie')
arrow(ax, (58, 66), (64, 54), 'varie')
text(ax, 14, 59, r'$\times5$', 'varie', 's')
text(ax, 74, 59, r'$\times3$', 'varie', 's')
box(ax, 4, 38, 38, 16, 'fixe', label=r'$\frac{10}{15}$', size='l')
box(ax, 46, 38, 38, 16, 'fixe', label=r'$\frac{12}{15}$', size='l')
text(ax, 44, 46, '+', 'encre', 'l')
text(ax, 23, 34, r'$a\times d=2\times5$', 'varie', 's')
text(ax, 65, 34, r'$b\times c=3\times4$', 'varie', 's')
arrow(ax, (44, 32), (44, 22), 'resultat')
box(ax, 14, 4, 60, 18, 'resultat', label=r'$\frac{22}{15}$', size='l')
text(ax, 44, 28, r'$b\times d=3\times5=15$', 'fixe', 's')
save(fig, '54-043')
