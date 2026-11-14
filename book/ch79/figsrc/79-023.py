import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 2, 3, 84, 50, 'fixe'); text(ax, 44, 48.5, 'ordre partiel : 3 règles', 'fixe', 's')
box(ax, 6, 7, 46, 36, 'resultat'); text(ax, 29, 38.5, 'chaîne : 3 règles + totalité', 'resultat', 's')
box(ax, 19, 15, 20, 9, 'sujet', label='réels')
box(ax, 57, 17, 27, 9, 'autre', label='diviseurs de 60')
text(ax, 70.5, 12, '12 et 20 sans lien', 'limite', 's')
save(fig, '79-023')
