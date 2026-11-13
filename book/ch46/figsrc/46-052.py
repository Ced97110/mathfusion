import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
bw, y = 20, 28
xs = [2, 34, 66]
box(ax, xs[0], y, bw, 12, 'sujet', label='h = 8', size='s')
box(ax, xs[1], y, bw, 12, 'varie', label='h⁻¹ = 4', size='s')
box(ax, xs[2], y, bw, 12, 'resultat', label='gh⁻¹ = 8', size='s')
box(ax, xs[2], 4, bw, 12, 'sujet', label='g = 4', size='s')
arrow(ax, (xs[0] + bw, y + 6), (xs[1], y + 6), 'fixe'); arrow(ax, (xs[1] + bw, y + 6), (xs[2], y + 6), 'fixe')
arrow(ax, (xs[2] + bw / 2, 16), (xs[2] + bw / 2, y), 'fixe')
text(ax, 28, y + 9.5, 'inverse', 'fixe', 's'); text(ax, 60, y + 9.5, 'produit', 'fixe', 's')
text(ax, 24, 46, 'H = {0, 4, 8}, un sous-groupe', 'sujet', 's', ha='center')
text(ax, 34, 10, '1. inverse dans H', 'fixe', 's', ha='right'); text(ax, 34, 4, '2. produit dans H', 'fixe', 's', ha='right')
save(fig, '46-052')
