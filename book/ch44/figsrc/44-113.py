import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# three conditions of the test; the second carries the weight
conds = [('1 inversible', 'fixe'), ('produit inversible', 'varie'), ('inverse inversible', 'fixe')]
for i, (t, r) in enumerate(conds):
    box(ax, 2 + i * 29.5, 46, 27, 9, r, label=t, size='s')
text(ax, 44, 40, 'étape décisive : le produit', 'varie', 's')
# chain of the decisive step
xs = [2, 33, 71]; ws = [27, 28, 15]
box(ax, xs[0], 14, ws[0], 10, 'sujet', label=r'$u_1u_2\,u_2^{-1}u_1^{-1}$', size='s')
box(ax, xs[1], 14, ws[1], 10, 'varie', label=r'$u_1\cdot 1\cdot u_1^{-1}$', size='s')
box(ax, xs[2], 14, ws[2], 10, 'resultat', label=r'$1$')
arrow(ax, (xs[0] + ws[0], 19), (xs[1], 19), 'varie')
arrow(ax, (xs[1] + ws[1], 19), (xs[2], 19), 'varie')
text(ax, 15.5, 8, r'$u_2u_2^{-1}=1$ au milieu', 'varie', 's')
text(ax, 61, 8, r'$u_1u_1^{-1}=1$', 'varie', 's')
save(fig, '44-113')
