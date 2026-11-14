import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# Ligne 1 : u = -1, une unité : 3 et -3 associés
text(ax, 44, 74, 'b = a × u', 'encre', 'l')
box(ax, 4, 48, 20, 14, 'sujet', label='a = 3', size='m')
box(ax, 64, 48, 20, 14, 'resultat', label='b = −3', size='m')
arrow(ax, (24.8, 55), (63.2, 55), 'varie')
text(ax, 44, 59.5, '× u,  u = −1', 'varie', 's')
text(ax, 44, 50, 'u est une unité', 'resultat', 's')
text(ax, 44, 43, '3 ∼ −3', 'resultat', 'm')
# Ligne 2 : u = 2 n'est pas une unité
box(ax, 4, 18, 20, 14, 'sujet', label='a = 3', size='m')
box(ax, 64, 18, 20, 14, 'fixe', label='b = 6', size='m')
arrow(ax, (24.8, 25), (63.2, 25), 'varie')
text(ax, 44, 29.5, '× u,  u = 2', 'varie', 's')
text(ax, 44, 20, '2 n’est pas une unité', 'limite', 's')
text(ax, 44, 11, '6 ∣ 3 exigerait 3 = 6 × c,', 'limite', 's')
text(ax, 44, 5, 'donc c = 1/2 : non entier', 'limite', 's')
save(fig, '56-037')
