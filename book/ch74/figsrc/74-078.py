import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 28, 50, r'$G/T$ : 2 paquets', 'sujet', 'm'); text(ax, 74, 50, r'$G_0$', 'resultat', 'm')
box(ax, 3, 28, 50, 14, 'sujet'); box(ax, 3, 9, 50, 14, 'varie')
for i in range(4):
    disc(ax, 8 + 4.5*i, 35, 1.1, 'sujet'); disc(ax, 8 + 4.5*i, 16, 1.1, 'varie')
text(ax, 38, 35, 'glissements', 'sujet', 's'); text(ax, 38, 16, 'symétries glissées', 'varie', 's')
box(ax, 62, 28, 24, 14, 'resultat', label='identité', size='s')
box(ax, 62, 9, 24, 14, 'resultat', label='retournement', size='s')
arrow(ax, (54, 35), (61, 35), 'encre'); arrow(ax, (54, 16), (61, 16), 'encre')
save(fig, '74-078')
