import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def table(x0, first, role):
    for j, b in enumerate((r'$-1$', r'$-2$')):
        yy = 28 - 12 * j
        box(ax, x0, yy, 14, 9, role, label=first)
        box(ax, x0 + 14, yy, 14, 9, 'fixe', label=b)
table(6, r'$x$', 'varie')
table(54, r'$0$', 'varie')
text(ax, 13, 45, 'têtes', 'varie', 's')
text(ax, 61, 45, 'têtes', 'varie', 's')
arrow(ax, (37, 28), (49, 28), 'varie', lw=1.0)
text(ax, 43, 32, r'$x=0$', 'varie', 's')
box(ax, 50, 3, 36, 9, 'resultat', label='colonne de 0 : déterminant 0', size='s')
save(fig, '70-124')
