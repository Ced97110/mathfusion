import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(42)
box(ax, 3, 16, 22, 16, 'limite', label='3', size='xl')
text(ax, 14, 10, 'nombre seul', 'limite', 's')
arrow(ax, (25, 24), (32, 24), 'varie')
box(ax, 32, 16, 53, 16, 'resultat', label='La largeur du jardin est 3 m\net sa longueur est 7 m', size='s')
text(ax, 58, 10, 'phrase qui répond + unité', 'resultat', 's')
save(fig, '16-111')
