import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 59, 'message reçu : 8 bits', 'encre', 'm')
for i in range(8):
    box(ax, 5.8 + i * 9.7, 46, 8.5, 8, 'fixe', label='?')
arrow(ax, (44, 45.5), (44, 41.6), 'varie')
box(ax, 14, 30, 60, 11, 'varie', label='nombre de 1 : impair\n(la règle demande : pair)', size='s')
arrow(ax, (44, 29.5), (44, 26.6), 'varie')
box(ax, 14, 17, 60, 9, 'resultat', label='règle violée : une erreur existe', size='s')
arrow(ax, (44, 16.5), (44, 13.6), 'fixe')
box(ax, 14, 4, 60, 9, 'fixe', label='quel bit est faux ? on ne sait pas', size='s', dash=True)
save(fig, '68-005')
