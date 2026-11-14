import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# crystal
for i in range(3):
    for j in range(3): disc(ax, 7 + i*6, 50 + j*6, 1.8, 'sujet')
text(ax, 13, 36, 'cristal', 'sujet', 's')
# rays
for k in range(3): arrow(ax, (26, 50 + k*6), (47, 50 + k*6), 'varie')
text(ax, 36, 66, 'rayons X', 'varie', 's')
# plate with spots
box(ax, 50, 40, 34, 24, 'fixe', lw=0.8)
for (a, b) in itertools.product(range(-2, 3), range(-1, 2)):
    disc(ax, 67 + a*5.5, 52 + b*5.5, 1.1, 'encre')
text(ax, 67, 36, 'taches du cliché', 'encre', 's')
# group
arrow(ax, (67, 32), (67, 24), 'resultat'); 
box(ax, 44, 8, 40, 14, 'resultat', label='groupe d’espace', size='s')
arrow(ax, (44, 15), (30, 15), 'resultat')
for i in range(2):
    for j in range(2): disc(ax, 12 + i*8, 11 + j*8, 1.8, 'sujet')
text(ax, 20, 4, 'position des atomes', 'sujet', 's')
save(fig, '74-181')
