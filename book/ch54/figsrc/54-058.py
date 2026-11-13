import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# haut : a -> a/1, deux images différentes
text(ax, 44, 76, r'$a\mapsto a/1$ : images différentes', 'resultat', 's')
box(ax, 2, 44, 12, 10, 'sujet', label='3', size='m')
box(ax, 2, 58, 12, 10, 'sujet', label='4', size='m')
box(ax, 66, 44, 20, 10, 'resultat', label=r'$\frac{3}{1}$', size='m')
box(ax, 66, 58, 20, 10, 'resultat', label=r'$\frac{4}{1}$', size='m')
arrow(ax, (14, 49), (66, 49), 'resultat')
arrow(ax, (14, 63), (66, 63), 'resultat')
# bas : reste modulo 6, deux éléments vers la même image
text(ax, 44, 34, 'reste modulo 6 : même image', 'limite', 's')
box(ax, 2, 12, 12, 10, 'sujet', label='6', size='m')
box(ax, 2, 24, 12, 8, 'sujet', label='0', size='m')
box(ax, 66, 17, 20, 10, 'limite', label='0', size='m')
arrow(ax, (14, 16), (66, 20), 'limite')
arrow(ax, (14, 28), (66, 24), 'limite')
save(fig, '54-058')
