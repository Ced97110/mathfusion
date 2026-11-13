import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# colonne : départ, étape clé, arrivée
box(ax, 2, 58, 50, 18, 'sujet', label=r'départ : $\alpha\,v + \beta\,u = 0$'+'\n'+r'$v=(0,\ 1)$ et $u=(1,\ 0)$', size='m')
arrow(ax, (27, 58), (27, 50), 'varie')
box(ax, 2, 36, 50, 13, 'varie', label=r'étape clé : diviser par $\alpha$', size='m', weight='bold')
arrow(ax, (27, 36), (27, 24), 'varie')
box(ax, 2, 10, 50, 13, 'resultat', label=r'$\alpha = 0$, puis $\beta = 0$', size='m')
text(ax, 27, 5, 'arrivée : tous les coefficients nuls', 'resultat', 's')
# branche exclue
arrow(ax, (52, 42), (60, 42), 'limite')
box(ax, 60, 30, 26, 24, 'limite', label='si α ≠ 0 :\nv s’écrit avec u\n= exclu', size='s')
save(fig, '58-302')
