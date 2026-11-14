import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 74, r'$x^2+1$ dans les restes par 3', 'sujet', 'm')
for i in range(3):
    x = 20 + i * 22
    box(ax, x, 50, 12, 9, 'fixe', label=str(i), size='l')
    arrow(ax, (x + 6, 49.5), (x + 6, 41), 'varie')
    box(ax, x, 31, 12, 9, 'limite', label=str([1, 2, 2][i]), size='l')
text(ax, 10, 54.5, r'$x$', 'fixe', 's')
text(ax, 10, 35.5, 'valeur', 'limite', 's')
text(ax, 44, 25, 'jamais 0 : aucune racine', 'limite', 's')
arrow(ax, (44, 22), (44, 16), 'varie')
box(ax, 8, 2, 72, 13, 'resultat', dash=True)
text(ax, 44, 11, 'corps plus grand :', 'resultat', 's')
text(ax, 44, 6, r'$x^2+1=0$ y a une racine', 'resultat', 's')
save(fig, '52-289')
