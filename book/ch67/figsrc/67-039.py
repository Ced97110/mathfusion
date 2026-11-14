import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 44, 50, r'corps à 6 éléments : $p$ divise 6', 'encre', 's')
for x, d in zip((4, 26, 48, 70), (1, 2, 3, 6)):
    keep = d in (2, 3)
    box(ax, x, 28, 16, 10, 'varie' if keep else 'fixe', label=str(d))
    text(ax, x + 8, 24, 'premier' if keep else 'pas premier', 'varie' if keep else 'fixe', 's')
brace(ax, 26, 64, 19, 'varie', label='deux possibilités : 2 ou 3')
text(ax, 44, 6, 'n’exclut pas encore le cas 6', 'encre', 's')
save(fig, '67-039')
