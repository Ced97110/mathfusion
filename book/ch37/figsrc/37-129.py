import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
k = 8.0; x0 = 8
box(ax, x0, 44, 8 * k, 7, 'sujet', label='$a$ = 8', size='m')
box(ax, x0, 30, 3 * k, 7, 'varie', label='$b$ = 3', size='m')
box(ax, x0 + 3 * k, 30, 4 * k, 7, 'autre', label='$c$ = 4', size='m')
box(ax, x0 + 7 * k, 30, 1 * k, 7, 'limite', fill=False, dash=True)
text(ax, x0 + 7.5 * k, 26.5, 'manque 1', 'limite', 's')
text(ax, x0 + 3.5 * k, 26.5, '3 + 4 = 7 < 8', 'fixe', 's')
text(ax, 44, 17, r'$s-a$ = 7,5 − 8 = −0,5', 'limite', 'm')
text(ax, 44, 9, 'produit ≈ −59,06 : pas de racine', 'limite', 's')
save(fig, '37-129')
