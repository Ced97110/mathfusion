import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$|G|=12=4\times3$', 'sujet', 'l')
for b in range(3):
    x0 = 12 + b * 24
    for i in range(2):
        for j in range(2):
            box(ax, x0 + i * 8, 24 + j * 8, 8, 8, 'sujet')
    text(ax, x0 + 8, 46, '4 éléments', 'limite', 's')
brace(ax, 12, 12 + 2 * 24 + 16, 24, 'resultat', label='3 blocs')
text(ax, 44, 38 + 12, r'3 ne divise pas 4', 'limite', 's')
text(ax, 44, 5, "3 divise l'indice 3", 'resultat', 's')
save(fig, '50-136')
