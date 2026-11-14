import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, r'$c=3$ hors des images du cycle $(2\ 3)$', 'encre', 's')
xs = [14, 44, 74]
disc(ax, xs[0], 30, 4.2, 'sujet', label='3', size='m')
disc(ax, xs[1], 30, 4.2, 'fixe', label='1', size='m')
disc(ax, xs[2], 30, 4.2, 'resultat', label='3', size='m')
arrow(ax, (xs[0] + 4.8, 30), (xs[1] - 4.8, 30), 'varie'); arrow(ax, (xs[1] + 4.8, 30), (xs[2] - 4.8, 30), 'varie')
text(ax, 29, 36, r'$\sigma^{-1}$', 'varie', 'm'); text(ax, 59, 36, r'$\sigma$', 'varie', 'm')
text(ax, 14, 21, r'$c$', 'sujet', 's'); text(ax, 74, 21, r'$c$ reste fixe', 'resultat', 's')
text(ax, 44, 21, 'hors du cycle', 'fixe', 's')
text(ax, 44, 12, r'$\tau$ ne le bouge pas', 'fixe', 's')
save(fig, '47-171')
