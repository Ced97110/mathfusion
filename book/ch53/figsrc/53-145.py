import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def row(y, first, second, mid):
    box(ax, 2, y, 14, 9, 'sujet', label=r'$8$')
    box(ax, 37, y, 16, 9, 'fixe', label=mid)
    box(ax, 72, y, 14, 9, 'resultat', label=r'$8^{81}$')
    arrow(ax, (17, y + 4.5), (36, y + 4.5), first[1])
    arrow(ax, (54, y + 4.5), (71, y + 4.5), second[1])
    text(ax, 26.5, y + 8, first[0], first[1], 's')
    text(ax, 62.5, y + 8, second[0], second[1], 's')
row(38, ('puissance 3', 'varie'), ('puissance 27', 'autre'), r'$8^{3}$')
row(20, ('puissance 27', 'autre'), ('puissance 3', 'varie'), r'$8^{27}$')
text(ax, 44, 7, r'$3 \times 27 = 81 = 27 \times 3$', 'encre', 'l')
save(fig, '53-145')
