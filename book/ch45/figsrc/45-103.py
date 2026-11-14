import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 4, 56, 80, 16, 'resultat'); text(ax, 44, 67.5, 'Départ', 'resultat', 's', weight='bold'); text(ax, 44, 61.5, r'vrai pour moins de $n$ éléments', 'encre', 's')
arrow(ax, (44, 55.5), (44, 46.5), 'varie')
box(ax, 4, 30, 80, 16, 'varie'); text(ax, 44, 41.5, 'Étape qui porte la preuve', 'varie', 's', weight='bold'); text(ax, 44, 35.5, 'le lemme recolle $u$ et $v$', 'encre', 's')
arrow(ax, (44, 29.5), (44, 20.5), 'varie')
box(ax, 4, 4, 80, 16, 'resultat'); text(ax, 44, 15.5, 'Arrivée', 'resultat', 's', weight='bold'); text(ax, 44, 9.5, r'vrai pour $n$ éléments', 'encre', 's')
save(fig, '45-103')
