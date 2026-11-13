import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 8, 50, 72, 9, 'sujet', label=r'$k$ = somme $\div$ permutations', size='l')
rows = [('2 fils', '(16 + 8) / 2', '12', 38), ('3 fils', '480 / 6', '80', 24), ('4 fils', '76 928 / 8', '9 616', 10)]
for lab, expr, k, y in rows:
    box(ax, 3, y, 16, 9, 'varie', label=lab, size='s')
    box(ax, 23, y, 36, 9, 'fixe', label=expr)
    text(ax, 62, y+4.5, '=', 'encre', 'm')
    box(ax, 66, y, 19, 9, 'resultat', label=k, weight='bold')
    arrow(ax, (19.5, y+4.5), (22.5, y+4.5), 'varie')
save(fig, '49-273')
