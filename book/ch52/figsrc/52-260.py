import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
specs = [(62, 'sujet', '3 267 154', 'départ : les 4 restes'),
         (36, 'varie', 'comparer à 89 403 930', 'étape qui porte le poids'),
         (10, 'resultat', r'$2134\times1531$', 'arrivée : le produit')]
for y, role, s, cap in specs:
    box(ax, 3, y, 44, 9, role, label=s)
    text(ax, 3, y + 12.5, cap, 'fixe', 's', ha='left')
arrow(ax, (42, 62), (42, 45.5), 'fixe'); arrow(ax, (42, 36), (42, 19.5), 'fixe')
box(ax, 54, 36, 31, 9, 'limite', label='92 671 084', size='s')
text(ax, 69.5, 31, 'mêmes restes', 'limite', 's')
text(ax, 69.5, 27.5, 'pas le produit', 'limite', 's')
text(ax, 3, 30, 'tous deux < 89 403 930', 'resultat', 's', ha='left')
text(ax, 3, 25.5, 'et mêmes restes : égaux', 'resultat', 's', ha='left')
save(fig, '52-260')
