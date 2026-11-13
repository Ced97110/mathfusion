import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
# Haut : la phrase longue est remplacée par la lettre
box(ax, 3, 36, 52, 14, 'fixe', label='vers l’est, 180 km/h')
arrow(ax, (56, 43), (66, 43), 'varie')
box(ax, 67, 36, 18, 14, 'sujet', label=r'$a$', size='xl')
text(ax, 29, 53.5, 'sans la lettre : une phrase', 'fixe', 's')
text(ax, 76, 53.5, 'avec', 'sujet', 's')
# Bas : la flèche de l'avion
O = (10, 14)
k = 3.6
E = (O[0] + 180 / k, O[1])
arrow(ax, O, E, 'sujet', lw=1.6)
disc(ax, O[0], O[1], 1.5, 'encre')
text(ax, 5, 9.5, r'$O$', 'encre', 'm')
text(ax, 35, 19, r'$a$', 'sujet', 'l')
brace(ax, O[0], E[0], 10, 'sujet', label='180 km/h')
text(ax, 72, 14, 'est', 'fixe', 's')
save(fig, '41-010')
