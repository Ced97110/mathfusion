import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'$\sin^2 A=(\sin A)^2$', 'sujet', 'xl')
box(ax, 4, 24, 28, 11, 'sujet', label=r'$\sin A=\frac{5}{13}$', size='m')
arrow(ax, (34, 29.5), (52, 29.5), 'varie')
text(ax, 43, 34, 'au carré', 'varie', 's')
box(ax, 54, 24, 32, 11, 'resultat', label=r'$\sin^2 A=\frac{25}{169}$', size='m')
text(ax, 44, 8, r'$\sin^2 A$ ne veut pas dire $\sin(A^2)$', 'limite', 's')
save(fig, '34-074')
