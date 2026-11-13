import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# les couples d'entiers : deux opérations, le résultat reste dans l'ensemble
box(ax, 2, 12, 84, 56, 'sujet', fill=False, lw=1.0)
text(ax, 6, 63, r'$\mathbb{Z}^{(2)}$ : tous les couples d’entiers', 'sujet', 'm', ha='left', weight='bold')
def row(y, left, op, res):
    box(ax, 7, y, 34, 10, 'sujet', label=left, size='m')
    arrow(ax, (42, y + 5), (53, y + 5), 'varie', lw=1.2)
    text(ax, 47.5, y + 8.5, op, 'varie', 's')
    box(ax, 55, y, 26, 10, 'resultat', label=res, size='m', weight='bold')
row(40, '(2, 1) + (5, 4)', 'addition', '(7, 5)')
row(22, r'$3\ \times\ (2,\ 1)$', 'fois 3', '(6, 3)')
text(ax, 44, 5.5, r'scalaires : les entiers $\mathbb{Z}$', 'fixe', 's')
text(ax, 68, 37, 'encore un couple', 'resultat', 's')
text(ax, 68, 19, 'encore un couple', 'resultat', 's')
save(fig, '58-005')
