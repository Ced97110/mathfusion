import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 58, 'Salle sans élève', 'fixe', 's'); text(ax, 66, 58, 'Partie vide de l’horloge', 'autre', 's')
box(ax, 3, 30, 38, 22, 'fixe', fill=False, dash=True, label='aucun élève', size='s')
box(ax, 47, 30, 38, 22, 'autre', fill=False, dash=True, label='aucun élément', size='s')
for cx in (22, 66):
    arrow(ax, (cx, 30), (cx, 25), 'resultat')
text(ax, 22, 21, '« tous ont plus de 15 ans »', 'resultat', 's'); text(ax, 22, 16.5, 'vrai', 'resultat', 's', weight='bold')
text(ax, 66, 21, '« pour tous les couples… »', 'resultat', 's'); text(ax, 66, 16.5, 'vrai', 'resultat', 's', weight='bold')
box(ax, 14, 2, 60, 9, 'varie', label='à part : H n’est pas vide', size='s')
save(fig, '46-053')
