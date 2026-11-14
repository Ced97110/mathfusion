import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r"$A'=Q\,A\,P^{-1}$", 'encre', 'l')
def mat(x, rows, roles, c=9):
    for i, (vals, role) in enumerate(zip(rows, roles)):
        for j, v in enumerate(vals):
            box(ax, x + j * c, 30 - i * 8, c, 8, role, label=str(v))
# Q à gauche, A, P^-1 à droite, puis le résultat
box(ax, 3, 22, 16, 16, 'varie', label=r'$Q$', size='l')
mat(22, [(4, 6), (6, 4)], ['fixe', 'sujet'])
box(ax, 43, 22, 16, 16, 'autre', label=r'$P^{-1}$', size='l')
text(ax, 63, 30, '=', 'encre', 'l')
mat(67, [(4, 6), (10, 10)], ['fixe', 'varie'])
text(ax, 31, 41.5, r'$A$', 'sujet', 'm'); text(ax, 76, 41.5, r"$A'$", 'varie', 'm')
text(ax, 11, 17, 'les lignes', 'varie', 's'); text(ax, 51, 17, 'les colonnes', 'autre', 's')
arrow(ax, (19.5, 15), (21, 21), 'varie'); arrow(ax, (42.5, 15), (41, 21), 'autre')
text(ax, 44, 9, r'$Q$ : ligne 2 + ligne 1', 'varie', 's')
text(ax, 44, 3.5, r'ici $P^{-1}$ ne change aucun nombre', 'autre', 's')
save(fig, '59-044')
