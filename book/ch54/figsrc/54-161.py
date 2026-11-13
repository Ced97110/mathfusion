import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, 'entiers', 'fixe', 'm')
text(ax, 44, 47, 'polynômes', 'fixe', 'm')
# 12 | 156 : reste nul
box(ax, 4, 62, 38, 20, 'resultat')
text(ax, 23, 76, r'$156=12\times13$', 'resultat', 's')
text(ax, 23, 68, r'$12$ divise $156$ : reste 0', 'resultat', 's')
# 12 ne divise pas 157
box(ax, 46, 62, 38, 20, 'limite')
text(ax, 65, 76, r'$157=12\times13+1$', 'limite', 's')
text(ax, 65, 68, r'$12$ ne divise pas : reste 1', 'limite', 's')
# x-1 | x^2-1
box(ax, 4, 18, 38, 24, 'resultat')
text(ax, 23, 36, r'$x^2-1=(x-1)(x+1)$', 'resultat', 's')
text(ax, 23, 27, r'$x-1$ divise : reste 0', 'resultat', 's')
# x-1 ne divise pas x^3-2x^2+4
box(ax, 46, 18, 38, 24, 'limite')
text(ax, 65, 36, r'$x^3-2x^2+4$', 'limite', 's')
text(ax, 65, 27, r'$x-1$ ne divise pas : reste 3', 'limite', 's')
save(fig, '54-161')
