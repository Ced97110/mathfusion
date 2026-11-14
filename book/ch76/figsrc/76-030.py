import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 12, 53, 'nombres', 'fixe', 's'); text(ax, 56, 53, r'$a\,1$ : $a$ fois l’unité', 'sujet', 's')
A = '3  0\n0  3'; B = '2  0\n0  2'
def row(y, left, mats, op, res):
    text(ax, 12, y + 6, left, 'fixe', 'm')
    arrow(ax, (24, y + 6), (28, y + 6), 'resultat')
    box(ax, 30, y, 15, 12, 'sujet', label=mats[0]); text(ax, 48, y + 6, op, 'encre', 'l')
    box(ax, 51, y, 15, 12, 'sujet', label=mats[1]); arrow(ax, (67.5, y + 6), (71, y + 6), 'resultat')
    box(ax, 72, y, 15, 12, 'resultat', label=res)
row(32, '3 + 2 = 5', (A, B), '+', '5  0\n0  5')
row(10, '3 × 2 = 6', (A, B), r'$\times$', '6  0\n0  6')
save(fig, '76-030')
