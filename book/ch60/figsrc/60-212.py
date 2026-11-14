import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
xs = [3, 33, 63]
box(ax, xs[0], 28, 22, 13, 'sujet', label=r'$A-1\neq0$')
box(ax, xs[1], 28, 22, 13, 'resultat', label=r'$(A-1)^2=0$')
box(ax, xs[2], 28, 22, 13, 'resultat', label=r'$(A-1)^3=0$')
for i in (0, 1):
    arrow(ax, (xs[i] + 22.5, 34.5), (xs[i + 1] - 0.5, 34.5), 'varie')
    text(ax, xs[i] + 26.5, 24, r'$\times(A-1)$', 'varie', 's')
text(ax, xs[1] + 11, 48, 'polynôme minimal', 'resultat', 's')
text(ax, xs[2] + 11, 48, 'Cayley-Hamilton', 'resultat', 's')
text(ax, 44, 10, 'premier exposant nul : 2', 'fixe', 'm')
save(fig, '60-212')
