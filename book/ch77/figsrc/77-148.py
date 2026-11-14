import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def row(y, a, b, lab, role):
    box(ax, 2, y, 26, 10, role, label=a, size='s'); arrow(ax, (29, y + 5), (41, y + 5), 'varie')
    box(ax, 42, y, 26, 10, role, label=b, size='s'); text(ax, 78, y + 5, lab, 'varie', 's')
row(74, 'groupe', 'permutations', 'Cayley', 'sujet')
row(60, 'algèbre', 'matrices', 'ce chapitre', 'sujet')
row(46, 'matrice', 'trace, norme', 'résumé', 'sujet')
text(ax, 44, 34, 'tour K ⊆ E ⊆ L, norme de u', 'encre', 's')
box(ax, 2, 14, 22, 12, 'autre', label=r'$u$ dans $L$', size='s'); box(ax, 33, 14, 22, 12, 'varie', label=r'$2\sqrt{2}$ dans $E$', size='s'); box(ax, 64, 14, 22, 12, 'resultat', label=r'$-8$ dans $K$', size='s')
arrow(ax, (25, 20), (32, 20), 'varie'); arrow(ax, (56, 20), (63, 20), 'varie')
save(fig, '77-148')
